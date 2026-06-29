from app.pdf.extractor import pdf_extractor
from app.pdf.cleaner import AdvancedTextCleaner
from app.pdf.chunker import TextChunker

from app.models.embedding_model import EmbeddingModel
from app.retrieval.vector_store import VectorStore


extractor = pdf_extractor()

pages = extractor.extract(
    "/workspaces/bert-rag-document-qa/data/pdfs/deeplearningbook.pdf"
)

cleaner = AdvancedTextCleaner()

for page in pages:
    page.text = cleaner.clean(page.text)


chunker = TextChunker(
    chunk_size=100,
    overlap=20
)

chunks = chunker.chunk(pages)


embedder = EmbeddingModel()

embeddings = embedder.embeded_chunks(chunks)


vector_store = VectorStore()

vector_store.build_index(
    embeddings,
    chunks
)


query = "Why Bert is encoder only nor decoder?"

query_embedding = embedder.embed_query(query)


results = vector_store.search(
    query_embedding,
    top_k=3
)


for result in results:
    chunk = result["chunk"]

    print("=" * 80)
    print(f"Similarity : {result['score']:.4f}")
    print(f"Chunk ID   : {chunk['chunk_id']}")
    print(f"Page       : {chunk['page']}")
    print("-" * 80)
    print(chunk["text"])