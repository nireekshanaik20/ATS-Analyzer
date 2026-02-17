import os
import docx2txt
from pdfminer.high_level import extract_text as extract_pdf_text

import uuid

def extract_text(file):
    filename = file.filename.lower()
    # Save temporarily with unique name to avoid conflicts
    ext = os.path.splitext(filename)[1]
    temp_path = f"temp_resume_{uuid.uuid4()}{ext}"
    file.save(temp_path)
    
    text = ""
    try:
        if filename.endswith('.pdf'):
            text = extract_pdf_text(temp_path)
        elif filename.endswith('.docx'):
            text = docx2txt.process(temp_path)
        elif filename.endswith('.txt'):
            with open(temp_path, 'r', encoding='utf-8') as f:
                text = f.read()
    except Exception as e:
        # Clean up before raising
        if os.path.exists(temp_path):
            os.remove(temp_path)
        raise e
            
    if os.path.exists(temp_path):
        os.remove(temp_path)
            
    return text

def extract_text_from_path(filepath):
    filename = filepath.lower()
    text = ""
    try:
        if filename.endswith('.pdf'):
            text = extract_pdf_text(filepath)
        elif filename.endswith('.docx'):
            text = docx2txt.process(filepath)
        elif filename.endswith('.txt'):
            with open(filepath, 'r', encoding='utf-8') as f:
                text = f.read()
    except Exception as e:
        raise e
            
    return text
