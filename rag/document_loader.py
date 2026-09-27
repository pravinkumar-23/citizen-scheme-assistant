
from pathlib import Path
from pypdf import PdfReader


def load_pdf(file_path):

    reader = PdfReader(file_path)

    pages = []

    for page_number, page in enumerate(reader.pages):

        text = page.extract_text()

        if text:

            pages.append({
                "page": page_number + 1,
                "text": text
            })

    return pages


def load_all_documents(folder):

    folder = Path(folder)

    documents = []

    for file_path in folder.glob("*.pdf"):

        pages = load_pdf(file_path)

        for page in pages:

            documents.append({
                "source": file_path.name,
                "page": page["page"],
                "text": page["text"]
            })

    return documents