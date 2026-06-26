from pathlib import Path
import fitz

class pdf_extractor:
    def __init__(self):
        pass
        
    def extract(self,pdf_path:str):
        pdf_path=Path(pdf_path)

        if not pdf_path.exists():
            raise  FileNotFoundError(f"{pdf_path} not found.")
        
        document = fitz.open(pdf_path)

        pages=[]

        for page_number,page in enumerate(document,start=1):
            text=page.get_text("text")

            pages.append({"page":page_number,
                          "text":text}
                        )
        document.close()

        return pages

