def generate_optimize_prompt(job_description, part_of_resume_title,part_of_resume,modify_suggestions,other_requirements):
    optimize_prompt=f'''
    Job Description:
    {job_description}

    {part_of_resume_title}:
    {part_of_resume}

    Modify Suggestions:
    {modify_suggestions}

    Other requirements:
    {other_requirements}

    please optimize the {part_of_resume_title} based on the Job Description,modify suggestions,other requirements with original Job title.
    '''
    return optimize_prompt

def generate_suggestion_prompt(job_description, part_of_resume_title,part_of_resume,other_requirements):
    suggestion_prompt = f'''
    Job Description:
    {job_description}

    the {part_of_resume_title} part of Resume:
    {part_of_resume}

    please provide some modify suggestions about the {part_of_resume} 
    for example: this work experience is not suitable for this job because A,B,C...
    
    Suggestions

    '''
    return suggestion_prompt

def generate_format_prompt(unformat_resume):
    format_prompt = f'''
    {unformat_resume}
    
    please format the above resume content to a decent format in markdown.
    result:
    
    '''
    return format_prompt

def generate_full_resume(job_description,full_resume,other_requirements):
    prompt = f"""
    Job Description:
    {job_description}

    Resume:
    {full_resume}

    Requirements:
    {other_requirements}
    ==================
    please optimize the resume based on the Job Description, and Requirements

    Optimized Resume:
    {{}}
    """
    return prompt

if __name__=="__main__":
    print(generate_full_resume("test job description","full resume","requirements"))

    