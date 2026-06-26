from dataclasses import dataclass
@dataclass
class Page:
    page_number:int
    text:str

@dataclass
class Chunk:
    chunk_id:int
    page_number:int
    text:str
    start_word:int
    end_word:int
    word_count:int