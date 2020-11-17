import re

def repeated_files(files):
    """Retrona uma lista com os arquivos repetidos"""
    repeated = []

    for file in files:
        match = re.findall(r".*\(1\)$", file)

        if match:
            repeated.extend(match)

    return repeated