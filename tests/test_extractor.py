from app.pdf.extractor import pdf_extractor
from app.pdf.cleaner import AdvancedTextCleaner

extract= pdf_extractor()
clean=AdvancedTextCleaner()
pages=extract.extract("/workspaces/bert-rag-document-qa/data/pdfs/The Last Lightkeeper.pdf")

cleaner=clean.clean(pages[0].text)

print(cleaner[:500])

