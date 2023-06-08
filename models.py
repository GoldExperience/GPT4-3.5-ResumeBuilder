import openai
from prompt import generate_optimize_prompt

system_design_for_optimize = '''
You are a highly skilled and capable AI tool designed to optimize and enhance resumes. 
The user will provide you with a job description and requirements, 
as well as a portion of their current resume (for example, their work experience). 
Your task is to take the information given and generate an optimized version of that portion of the resume, 
ensuring it aligns with the specific needs and expectations of the job in question.
'''

system_design_for_comnbiner = '''

'''


def get_model_response(system_role_prompt,user_message,model,max_token = 500,temperature = 1.2):
    system_message = {'role':'system','content': system_role_prompt}
    user_message = {'role':'user','content':user_message}
    response = openai.ChatCompletion.create(
        model=model,
        max_tokens = max_token,
        temperature = temperature,
        messages = [system_message,user_message]
    )
    return response['choices'][0]['message']['content']


def resume_part_optimizer(openai_key,job_description, part_of_resume_title,part_of_resume,other_requirements,model="gpt4"):
    openai.api_key = openai_key
    user_message = generate_optimize_prompt(job_description, part_of_resume_title,part_of_resume,other_requirements)
    response_content = get_model_response(system_design_for_optimize,user_message,model)



if __name__=="__main__":
    # resume_part_optimizer(1,2,3,4,5)
    # openai.api_key = ""
    response = get_model_response(system_design_for_optimize,"nothing, just fot test","gpt-4")
    print(response)
    pass


