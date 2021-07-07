from docxtpl import DocxTemplate


def fill_document(context, file_name):
    doc = DocxTemplate("./config/bulletin_with_questions.docx")
    doc.render(context)
    doc.save(f"./outputDocs/{file_name}")

