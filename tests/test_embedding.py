from  app.pdf.extractor import pdf_extractor
from app.pdf.chunker import TextChunker
from app.pdf.cleaner import AdvancedTextCleaner

from app.models.embedding_model import EmbeddingModel

extractor=pdf_extractor()

pages=extractor.extract( "data/pdfs/The Last Lightkeeper.pdf")

cleaner=AdvancedTextCleaner()

for page in pages:
    page.text=cleaner.clean(page.text)

chunker= TextChunker(
    chunk_size=500,
    overlap=50
)

chunks=chunker.chunk(pages)

embedder=EmbeddingModel()

embedding=embedder.embeded_chunks(chunks)

print(f'Chunks:{len(chunks)}')
print(f'Embedding:{embedding.shape}')

print(type(embedding))

print(embedding.shape)

print()

print(embedding[0][:10])

query = "Who is Ethan?"

query_embedding = embedder.embed_query(query)

print(query_embedding.shape)