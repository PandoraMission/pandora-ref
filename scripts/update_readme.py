#!/usr/bin/env python3
from pathlib import Path
from pandoraref import get_file_info

START = "<!-- BEGIN AUTO TABLE -->"
END = "<!-- END AUTO TABLE -->"

readme_path = Path("README.md")
readme = readme_path.read_text()

df = get_file_info()

block = f"{START}\n\n{df.to_markdown()}\n\n{END}"

# If the block exists, replace it — otherwise append it at the end
if START in readme and END in readme:
    new = readme.split(START)[0] + block + readme.split(END)[1]
else:
    new = readme + "\n\n" + block

readme_path.write_text(new)
