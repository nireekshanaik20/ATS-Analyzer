import re

def clean_text(text):
    if not text:
        return ""
    text = text.lower()
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text

def extract_skills(text):
    # Expanded list of common tech skills
    skills_db = [
        "python", "java", "c++", "c#", ".net", "html", "css", "javascript", "typescript",
        "react", "angular", "vue", "node.js", "express", "django", "flask", "fastapi",
        "sql", "mysql", "postgresql", "mongodb", "redis", "elasticsearch",
        "aws", "azure", "gcp", "docker", "kubernetes", "jenkins", "gitlab", "git",
        "machine learning", "deep learning", "nlp", "computer vision", "tensorflow", "pytorch", "scikit-learn",
        "pandas", "numpy", "matplotlib", "seaborn",
        "communication", "leadership", "problem solving", "agile", "scrum"
    ]
    
    found_skills = []
    # Simple regex matching for whole words
    for skill in skills_db:
        # Escape skill to handle special chars like C++
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, text):
            found_skills.append(skill)
            
    return found_skills
