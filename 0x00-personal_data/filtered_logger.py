import re

def filter_datum(fields, redaction, message, separator):
    return re.sub(f"({'|'.join(fields)}=[^;]*)", f"{redaction}", message)

