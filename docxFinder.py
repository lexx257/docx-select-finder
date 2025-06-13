from docx_form import DocxForm
import os

print("Enter full path of your document")
full_path = str(input())
print(full_path)

if not os.path.isfile(full_path):
    print("The file does not exist.")
    exit()
if not full_path.lower().endswith(".docx"):
    print("The file is not a .docx file.")
    exit()

document = DocxForm(full_path)
document.print_all_content_controls_and_form_fields()
print("Enter index of the menu you want to retrieve")
index = int(input())
document = DocxForm(full_path)

content_control = document.content_control_forms_and_form_fields[index]

option_values = [option.value for option in content_control.options]
print("all values")
print(option_values)