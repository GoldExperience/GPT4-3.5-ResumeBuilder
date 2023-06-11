import gradio as gr
import markdown2

def markdown_editor(text):
    html = markdown2.markdown(text)
    return html

iface = gr.Interface(
    fn=markdown_editor,
    inputs="text",
    outputs="html",
    title="Gradio Markdown Editor",
    description="Enter your Markdown text below:",
    theme="default",
    layout="vertical",
    allow_flagging=False
)

iface.launch()
