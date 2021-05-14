import re

def parser(f):
    """
    input: str file.eml
    output: dict
    """
    file_name = f
    
    parsed_header = {}
    with open(file_name, "r") as rf:
        content = rf.read()
        pattern = re.compile(r"([A-z].*)(:\s)(.*\S)")
        matches = pattern.finditer(content)
        for matches in matches:
             parsed_header[matches.group(1)] = matches.group(3)
    return parsed_header


email = parser("file.eml")
print(type(email))
for key in email:
    print(f"{key} = {email[key]}")