from sentence_transformers import SentenceTransformer
from typing import List

class EmbeddingModel:
    """
    Wrapper around SentenceTransformer for generating embeddings.
    """
     
    def __init__(self, model_name:str='all-MiniLM-L6-v2'):
        self.model=SentenceTransformer(model_name)
    
    def embed_text(self,text:str):
        return self.model.encode(
            text,convert_to_numpy=True
        )
    def embeded_chunks(self,chunks:List[dict]):
        texts=[
            chunk["text"] for chunk in chunks
        ]
        embedding=self.model.encode(
            texts,
            convert_to_numpy=True
        )

        return embedding
    def embed_query(self,query:str):
        return self.embed_text(query)
    