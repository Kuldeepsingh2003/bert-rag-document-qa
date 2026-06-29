import faiss
import numpy as np

class VectorStore:
    """
    FAISS vector database for semantic search.
    """

    def __init__(self):
        self.index=None

        self.chunks=[]

    def build_index(self,embeddings:np.ndarray,chunks:list):
        embeddings=embeddings.astype('float32')

        faiss.normalize_L2(embeddings)

        dimension =embeddings.shape[1]

        self.index= faiss.IndexFlatIP(dimension)

        self.index.add(embeddings)

        self.chunks=chunks
    
    def search(self,query_embedding:np.ndarray,top_k:int=3):
        query_embedding=query_embedding.reshape(1,-1).astype('float32')
        faiss.normalize_L2(query_embedding)

        scores,indices=self.index.search(query_embedding,top_k)
        results=[]

        for score,idx in zip(scores[0],indices[0]):
            results.append(
                {
                    "score": float(score),
                    "chunk":self.chunks[idx]
                }
            )
        return results