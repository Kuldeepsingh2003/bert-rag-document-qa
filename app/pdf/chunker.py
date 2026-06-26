from typing import List

class TextChunker:
    """
    Splits cleaned text into overlapping chunks.
    """
    def __init__(self,chunk_size:int =500,overlap:int =100):
        self.chunk_size=chunk_size
        self.overlap=50
    def chunk(self,pages:List[dict]):
        chunks=[]
        chunk_id=1

        for page in pages:
            words=page.text.split()
            start=0

            while start<len(words):
                end=start+self.chunk_size
                chunk_words=words[start:end]
                chunk_text=" ".join(chunk_words)

                chunks.append(
                    {
                        "chunk_id":chunk_id,
                        "page":page.page_number,
                        "text":chunk_text,
                        "start_word":start,
                        "end_word":min(end,len(words)),
                        "word_count":len(chunk_words)
                    }
                )
                chunk_id+=1
                start+=self.chunk_size-self.overlap
        return chunks
        
