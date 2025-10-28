import gradio as gr
from agents.researchagent import ResearchAgent
from agents.writeragent import WriterAgent
from agents.criticagent import CriticAgent
from utils.logger import Logger
import os
from dotenv import load_dotenv
logger = Logger()
load_dotenv()

def pipeline(topic):
    if not topic.strip():
        return "Please enter a valid topic.", "", "", ""
    
    logger.log(f"Starting research on topic: {topic}")
    
    research_agent = ResearchAgent()
    sources = research_agent.act(topic)
    sources_text = "\n".join([f"- {s['title']} — {s['summary']} ({s['url']})" for s in sources])

    writer_agent = WriterAgent()
    draft = writer_agent.act(sources)

    critic_agent = CriticAgent()
    final = critic_agent.act(draft)

    final_text = final["improved_draft"]
    critique_text = (
        "\n".join(final["critique"])
        if isinstance(final["critique"], list)
        else final["critique"]
    )

    os.makedirs("outputs", exist_ok=True)
    with open("outputs/final_article.txt", "w", encoding="utf-8") as f:
        f.write(final_text)

    logger.log("Pipeline complete. Final article saved.")
    return sources_text, draft["draft"], critique_text, final_text


app = gr.Interface(
    fn=pipeline,
    inputs=gr.Textbox(label="Enter a research topic:", placeholder="e.g., AI in Healthcare"),
    outputs=[
        gr.Textbox(label="📚 Research Sources"),
        gr.Textbox(label="📝 Drafted Article"),
        gr.Textbox(label="🔍 Critique Summary"),
        gr.Textbox(label="✅ Improved Final Article"),
    ],
    title="🧠 Agentic AI — Research to Article Generator",
    description="Researches, drafts, critiques, and improves your article using AI agents."
)

app.launch()
