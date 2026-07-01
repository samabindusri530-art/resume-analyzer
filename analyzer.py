import PyPDF2
from skills import job_roles


def extract_text(pdf_file):

    reader = PyPDF2.PdfReader(pdf_file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text.lower()



def analyze_resume(text, role):

    required_skills = job_roles[role]

    found = []
    missing = []

    for skill in required_skills:

        if skill in text:
            found.append(skill)

        else:
            missing.append(skill)

    score = int((len(found) / len(required_skills)) * 100)

    return found, missing, score
