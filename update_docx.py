import sys
import os
import docx

# 1. Update SIH_2026_Participation_Document_Template.docx
doc_path = r"D:\NEW CODING PROJECTS\SIH_INTERNAL\SIH_2026_Participation_Document_Template.docx"
if os.path.exists(doc_path):
    doc = docx.Document(doc_path)
    for p in doc.paragraphs:
        if "Team: Team Name" in p.text:
            p.text = p.text.replace("Team: Team Name", "Team: NeoMedtech")
        elif "Team Name" in p.text:
            p.text = p.text.replace("Team Name", "NeoMedtech")
    doc.save(doc_path)
    print("SUCCESS: Updated Word document with Team Name: NeoMedtech")
else:
    print(f"Error: {doc_path} not found.")
