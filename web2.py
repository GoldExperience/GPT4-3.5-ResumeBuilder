import gradio as gr
from functions import *
import logging
logging.basicConfig(level=logging.DEBUG,filename="run.log",filemode='a',format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')

with gr.Blocks() as demo:
    gr.Markdown("# Refine your resume with LLM")
    with gr.Row():
        with gr.Group():
            openai_api_key = gr.Textbox(lines=1,label="openai_api_key",placeholder="Enter your openai api key here, you can get it from https://platform.openai.com/")
            job_description = gr.Textbox(lines=3,label="Job Description",placeholder="Enter your Job description")
            basic_info_input = gr.Textbox(lines=3,label="Basic Info",placeholder="Enter Basic Info like Name, Address, Phone Number, Email here...")
            
            with gr.Tab("Work Experience"):
                with gr.Row():
                    with gr.Group():
                        work_experience_input = gr.Textbox(lines=6,label="Your Work Experience",placeholder="Enter your work Experience here...")
                        work_experience_refine_button = gr.Button("Refine it")    
                        work_experience_update_button = gr.Button("Update in Markdown")    
                        
                    with gr.Group():
                        work_experience_suggestion = gr.Textbox(lines=3,label="Modify Suggestions")
                        work_experience_refine_output = gr.Textbox(lines=3,label="Refined Version")
            with gr.Tab("Education"):
                education_experience_input = gr.Textbox(lines=6,label="Your education Experience",placeholder="Enter your education Experience here...")
                education_experience_refine_button = gr.Button("Refine it")    
                education_experience_suggestion = gr.Textbox(lines=3,label="Modify Suggestions")
                education_experience_refine_output = gr.Textbox(lines=3,label="Refined Version")
        with gr.Box():
            resume_label = gr.Label()
            resume_markdown = gr.Markdown("Your Resume looks like In Markdown, you can midify details in **Refined Version**")
    
    work_experience_refine_button.click(test_func,inputs=[openai_api_key,work_experience_input],outputs=[work_experience_suggestion,work_experience_refine_output,resume_markdown])

    
demo.launch()
