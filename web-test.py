import gradio as gr
import openai
from models import resume_all_optimizer
def test_Ratio(x):
    return x
openai_key = ""
openai.api_key = openai_key

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Group():
            openai_key = gr.Text(value=openai_key)
            model = gr.Radio(["gpt-4","gpt-3.5-turbo-16k"])
            max_token = gr.Slider(minimum=0,maximum=16000,value=500)
            job_description = gr.Text(lines=3,label="job description")
            resume = gr.TextArea(label="resume",lines=10)
            other_requirements = gr.Text(lines=2,label="other requirements")
            test_button = gr.Button("refine full")

        with gr.Group():    
            out_text = gr.Markdown("# Optimized Resume...")

    test_button.click(resume_all_optimizer,inputs=[openai_key,job_description,resume,other_requirements,model,max_token],outputs=out_text)

demo.launch()


