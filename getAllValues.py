from docx_form import DocxForm

index = 2
full_path = "a.docx"
document = DocxForm(full_path)

content_control = document.content_control_forms_and_form_fields[index]

option_values = [option.value for option in content_control.options]
print(option_values)