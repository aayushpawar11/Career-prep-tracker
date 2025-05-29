import pdfplumber
import re

def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text
def simple_skill_extractor(text):
    skills_list = ['python', 'java', 'c++', 'pytorch', 'tensorflow', 'sql',
                   'machine learning', 'deep learning', 'react', 'kubernetes', 'kafka']
    found_skills = [skill for skill in skills_list if skill.lower() in text.lower()]
    return list(set(found_skills))
if __name__ == "__main__":
    raw_text = extract_text_from_pdf("sample_resume.pdf")
    skills = simple_skill_extractor(raw_text)
    print("Extracted Skills:", skills)            