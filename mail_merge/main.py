from pathlib import Path
with open('./100 Days/python_scripts/mail_merge/receivers/name_list.txt','r') as name_list_file:
    name_list = name_list_file.readlines()

with open('./100 Days/python_scripts/mail_merge/mail_template.txt', 'r') as template:
    file_content = ''.join(template.readlines())


for name in name_list:
    u_name = name.strip()
    file_name = Path(f'./100 Days/python_scripts/mail_merge/receivers/{u_name}_mail.txt')
    with open(file_name, 'w') as mail_file:
        mail_file.write(file_content.replace('[name]', u_name))