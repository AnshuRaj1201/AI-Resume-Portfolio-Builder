def validate_resume(name, email, education, skills, projects):
    if not name:
        return False, "Please enter your name."

    elif not email:
        return False, "Please enter your email."

    elif "@" not in email:
        return False, "Please enter a valid email."

    elif not education:
        return False, "Please enter your education."

    elif not skills:
        return False, "Please enter your skills."

    elif not projects:
        return False, "Please enter your projects."

    return True, ""


def validate_cover_letter(name, job_role, company):
    if not name:
        return False, "Please enter your name."

    elif not job_role:
        return False, "Please enter job role."
    
    elif not company:
        return False, "Please enter company."

    return True, ""

def validate_portfolio( name, email, education, skills, projects):
    if not name:
        return False, "Please enter your name."

    elif not email:
        return False, "Please enter your email."

    elif "@" not in email:
        return False, "Please enter valid email."

    elif not education:
        return False, "Please enter education."

    elif not skills:
        return False, "Please enter skills."

    elif not projects:
        return False, "Please enter projects."

    return True, ""


def validate_linkedin(name, education, skills):
    if not name:
        return False, "Please enter your name."

    elif not education:
        return False, "Please enter education."

    elif not skills:
        return False, "Please enter skills."

    return True, ""


def validate_interview(name, job_role, skills):
    if not name:
        return False, "Please enter your name."

    elif not job_role:
        return False, "Please enter target job role."

    elif not skills:
        return False, "Please enter your skills."

    return True, ""

def validate_ats(resume):
    if not resume:
        return False, "Please upload or generate a resume."
    return True, ""