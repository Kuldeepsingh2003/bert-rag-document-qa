from app.pdf.extractor import pdf_extractor
from app.pdf.cleaner import AdvancedTextCleaner
from app.pdf.chunker import TextChunker

from app.models.embedding_model import EmbeddingModel
from app.retrieval.vector_store import VectorStore
from app.retrieval.retriever import Retriver


extractor = pdf_extractor()

pages = extractor.extract(
    "data/pdfs/Deep+Learning+Ian+Goodfellow.pdf"
)

cleaner = AdvancedTextCleaner()

for page in pages:
    page.text = cleaner.clean(page.text)

chunker = TextChunker(
    chunk_size=250,
    overlap=50
)

chunks = chunker.chunk(pages)

embedder = EmbeddingModel()

embeddings = embedder.embeded_chunks(chunks)

vector_store = VectorStore()

vector_store.build_index(
    embeddings,
    chunks
)

retriever = Retriver(
    embedder,
    vector_store
)

query = "What is deep learning?"

results = retriever.retrive(
    query,
    top_k=3
)

for result in results:

    chunk = result["chunk"]

    print("=" * 80)

    print(f"Similarity : {result['score']:.4f}")
    print(f"Page       : {chunk['page']}")
    print(f"Chunk ID   : {chunk['chunk_id']}")

    print()

    print(chunk["text"][:500])