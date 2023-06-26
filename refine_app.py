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
            openai_key = gr.Text(value=openai_key,label="openai key")
            model = gr.Radio(["gpt-4","gpt-3.5-turbo-16k"],label="model")
            max_token = gr.Slider(minimum=0,maximum=16000,value=500,label="max_token")
            job_description = gr.Text(lines=3,label="job description")
            resume = gr.TextArea(label="resume",lines=10)
            other_requirements = gr.Text(lines=2,label="other requirements")
            test_button = gr.Button("refine full")

        with gr.Group():    
            with gr.Tab("Preview"):
                out_text = gr.Markdown("# Optimized Resume...")
            with gr.Tab("Markdown"):
                out_text_markdown = gr.TextArea(label="optimized Resume")
            with gr.Tab("Interview Simulation"):
                gr.Chatbot("Interview")
    test_button.click(resume_all_optimizer,inputs=[openai_key,job_description,resume,other_requirements,model,max_token],outputs=[out_text,out_text_markdown])

# demo.launch(enable_queue=True, share=False,
#            server_name="0.0.0.0", server_port=7860)
demo.launch(enable_queue=True)

