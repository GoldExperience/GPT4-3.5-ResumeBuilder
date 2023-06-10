def generate_optimize_prompt(job_description, part_of_resume_title,part_of_resume,other_requirements):
    optimize_prompt=f'''
    Job Description:
    {job_description}

    {part_of_resume_title}:
    {part_of_resume}

    please optimize the {part_of_resume_title} based on the Job Description,{other_requirements} with original Job title.
    '''
    return optimize_prompt

def generate_format_prompt(unformat_resume):
    format_prompt = '''
    {unformat_resume}
    
    please format the above resume content to a decent format in markdown.
    result:
    
    '''
    return format_prompt

# print(generate_prompt("hello","hello1","hello2","hello3"))
# class system_optimizer:
#     def __init__(self) -> None:
#         self.role = "system"
#         self.prompt = 
    