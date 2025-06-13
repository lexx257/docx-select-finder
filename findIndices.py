from docx_form import DocxForm

full_path = "a.docx"
document = DocxForm(full_path)

 document.print_all_content_controls_and_form_fields()