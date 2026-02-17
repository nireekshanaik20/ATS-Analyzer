from skill_extractor import extract_skills, clean_text

def calculate_ats(resume_text, job_desc):
    resume_skills = set(extract_skills(clean_text(resume_text)))
    job_skills = set(extract_skills(clean_text(job_desc)))
    
    if not job_skills:
        return 0
        
    matching_skills = resume_skills.intersection(job_skills)
    score = (len(matching_skills) / len(job_skills)) * 100
    
    return round(score, 2)
