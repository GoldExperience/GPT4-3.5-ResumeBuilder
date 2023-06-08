import gradio as gr
import openai
from prompt import generate_optimize_prompt
# 输入的数据
def optimize_resume(openAI_key, job_description, optimize_job_desc, basic_info, optimize_basic_info, 
                    work_experience, optimize_work_exp, education, optimize_education, 
                    skills, optimize_skills):
    # 在这里实现简历优化逻辑
    optimized_resume = ""
    
    if optimize_job_desc:
        # 优化 job_description
        pass

    if optimize_basic_info:
        # 优化 basic_info
        pass
    
    if optimize_work_exp:
        # 优化 work_experience
        pass
    
    if optimize_education:
        # 优化 education
        pass
    
    if optimize_skills:
        # 优化 skills
        pass

    return optimized_resume

iface = gr.Interface(
    fn=optimize_resume, 
    inputs=[
        gr.inputs.Textbox(lines=3, placeholder='Job Description here...'),
        gr.inputs.Textbox(lines=3, placeholder='Basic Info here...'),
        gr.inputs.Textbox(lines=3, placeholder='Work Experience here...'),
        gr.inputs.Checkbox(label="Don't Optimize Work Experience"),
        gr.inputs.Textbox(lines=3, placeholder='Education here...'),
        gr.inputs.Checkbox(label="Don't Optimize Education"),
        gr.inputs.Textbox(lines=3, placeholder='Skills here...'),
        gr.inputs.Checkbox(label="Don't Optimize Skills")
    ], 
    outputs='text',
)

iface.launch()
