import gradio as gr
import openai
from prompt import generate_optimize_prompt
import models


# 输入的数据
def optimized_resume(
    openai_key,
    job_description,
    basic_info,
    work_exp,
    not_optimize_work_exp,
    education,
    not_optimize_education,
    skills,
    not_optimize_skills,
    other_requirements,
):
    # 在这里实现简历优化逻辑
    optimized_resume = basic_info + "\n"
    
    optimized_resume += "## Work Experience\n"
    if not_optimize_work_exp == False:
        # 优化 work_exp
        optimized_work_exp = models.resume_part_optimizer(
            openai_key, job_description, "Work Experience", work_exp, other_requirements
        )
        optimized_resume += "\n" + optimized_work_exp
    else:
        optimized_resume += "\n" + work_exp

    optimized_resume += "## Education\n"
    if not_optimize_education:
        optimized_education = models.resume_part_optimizer(
            openai_key, job_description, "Education", education, other_requirements
        )
        optimized_resume += "\n" + optimized_education
    else:
        optimized_resume += "\n" + education

    optimized_resume += "## Skills\n"
    if not_optimize_skills:
        optimized_skills = models.resume_part_optimizer(
            openai_key, job_description, "Skills", skills, other_requirements
        )
        optimized_resume += "\n" + optimized_skills
    else:
        optimized_resume += "" + "\n" + skills

    # optimized_resume = models.resume_format(openai_key, optimized_resume)

    return optimized_resume


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
