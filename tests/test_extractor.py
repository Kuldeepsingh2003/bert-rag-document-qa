from app.pdf.extractor import pdf_extractor

extract= pdf_extractor()

pages=extract.extract("data/pdfs/Card_ID List_EN.pdf")

print()

print(pages[0]["text"][:500])