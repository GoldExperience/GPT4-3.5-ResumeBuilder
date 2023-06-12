from prompt import generate_optimize_prompt
import models
import logging

logging.basicConfig(level=logging.DEBUG,filename="run.log",filemode='w',format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
logger = logging.getLogger('function_logger')
file_hadler = logging.FileHandler('run.log')
logger.addHandler(file_hadler)
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


def test_func(api_key, x):
    return f"test {x}", f"test2 {api_key}", '''# Hello world'''


def modify_work_experience(openai_api_key, model, job_description, work_experience_input, other_requirements):
    part_title = "Work Experience"
    suggestions = models.resume_part_suggestions(
        openai_api_key,job_description, "Work Experience", work_experience_input, other_requirements, model)
    logging.DEBUG(suggestions)
    optimized_work_exp = models.resume_part_optimizer(
        openai_api_key, job_description, "Work Experience", work_experience_input, other_requirements,suggestions,model
    )
    logging.DEBUG(optimized_work_exp)
    return suggestions,optimized_work_exp


def update_markdown(x):
    return '''
        # Hello world
        ## second title
        '''
