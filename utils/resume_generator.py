def create_resume(name, email, education, skills, projects):
    resume=f"""# {name}
            Email: {email}
            ## Education
            {education}
            ## Skills
            {skills}
            ## Project
            {projects}
            """
    return resume

def welcome(name):
    return f"Welcome {name}"