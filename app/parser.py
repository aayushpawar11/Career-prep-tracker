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
def extract_section(text, header):
    pattern = rf"{header}.*?(?=\n[A-Z][^\n]{2,}|$)"
    match = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
    return match.group(0).strip() if match else ""
def parse_resume(file_path):
    raw_text = extract_text_from_pdf(file_path)

    return {
        "skills": simple_skill_extractor(raw_text),
        "education": extract_section(raw_text, "education"),
        "experience": extract_section(raw_text, "experience"),
        "projects": extract_section(raw_text, "projects"),
        "coursework": extract_section(raw_text, "coursework"),
    }
if __name__ == "__main__":
    parsed_data = parse_resume("sample_resume.pdf")
    for key, value in parsed_data.items():
        print(f"\n{key.upper()}:\n{value}")         