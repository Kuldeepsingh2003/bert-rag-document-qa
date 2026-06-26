from app.pdf.extractor import pdf_extractor
from app.pdf.cleaner import AdvancedTextCleaner
from app.pdf.chunker import TextChunker

extractor=pdf_extractor()

pages=extractor.extract("data/pdfs/The Last Lightkeeper.pdf")

cleaner= AdvancedTextCleaner()

for page in pages:
    page.text=cleaner.clean(page.text)

chunker= TextChunker(
    chunk_size=500,
    overlap=50
)

chunks=chunker.chunk(pages)

print(f'total chunks:{len(chunks)}')
print()

print(chunks[0])

print(chunks[1])