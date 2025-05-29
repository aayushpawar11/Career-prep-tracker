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
def extract_sections(text, section_names):
    lines = text.split('\n')
    sections = {name: "" for name in section_names}
    
    current_section = None
    for line in lines:
        line_clean = line.strip().lower()
        for name in section_names:
            if name.lower() in line_clean:
                current_section = name
                break
        else:
            if current_section:
                sections[current_section] += line + '\n'
    
    return sections
def parse_resume(file_path):
    raw_text = extract_text_from_pdf(file_path)
    
    section_names = ["Education", "Experience", "Projects", "Coursework"]
    extracted = extract_sections(raw_text, section_names)

    return {
        "skills": simple_skill_extractor(raw_text),
        "education": extracted["Education"].strip(),
        "experience": extracted["Experience"].strip(),
        "projects": extracted["Projects"].strip(),
        "coursework": extracted["Coursework"].strip(),
    }
if __name__ == "__main__":
    parsed_data = parse_resume("sample_resume.pdf")
    for key, value in parsed_data.items():
        print(f"\n{key.upper()}:\n{value}")         