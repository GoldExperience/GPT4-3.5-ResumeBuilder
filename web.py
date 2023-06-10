import gradio as gr
from functions import optimized_resume


iface = gr.Interface(
    fn=optimized_resume,
    inputs=[
        gr.inputs.Textbox(lines=1, placeholder="OpenAI key here..."),
        gr.inputs.Textbox(lines=3, placeholder="Job Description here..."),
        gr.inputs.Textbox(lines=3, placeholder="Basic Info here..."),
        gr.inputs.Textbox(lines=3, placeholder="Work Experience here..."),
        gr.inputs.Checkbox(label="Don't Optimize Work Experience"),
        gr.inputs.Textbox(lines=3, placeholder="Education here..."),
        gr.inputs.Checkbox(label="Don't Optimize Education"),
        gr.inputs.Textbox(lines=3, placeholder="Skills here..."),
        gr.inputs.Checkbox(label="Don't Optimize Skills"),
        gr.inputs.Textbox(lines=2, placeholder="other Requirements"),
    ],
    outputs="text",
    
)

iface.launch()
