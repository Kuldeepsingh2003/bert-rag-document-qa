from app.models.embedding_model import EmbeddingModel
from app.retrieval.vector_store import VectorStore

class Retriver:
    """
    Retrieves the most relevant chunks for a query.
    """
    
    def __init__( self,embedder:EmbeddingModel,
                 vector_store:VectorStore):
        self.embedder=embedder
        self.vector_store=vector_store

    def retrive(self,query:str,top_k:int =3):
        query_embedding=self.embedder.embed_query(query)

        results=self.vector_store.search(
            query_embedding,
            top_k
        )
        return results