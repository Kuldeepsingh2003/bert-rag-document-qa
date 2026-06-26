from app.pdf.extractor import pdf_extractor
from app.pdf.cleaner import TextCleaner

extract= pdf_extractor()
pages=extract.extract("/workspaces/bert-rag-document-qa/data/pdfs/The Last Lightkeeper.pdf")

cleaner=TextCleaner.clean(pages[0]['text'])

print(cleaner[:500])

