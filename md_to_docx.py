from markdown import markdown
from docx import Document

# Read the Markdown file
with open('input.md', 'r') as file:
    md_content = file.read()

# Convert Markdown to HTML
html_content = markdown(md_content)

# Create a Word document
doc = Document()
doc.add_paragraph(html_content)
doc.save('output.docx')
