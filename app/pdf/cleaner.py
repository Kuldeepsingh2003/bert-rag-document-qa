import re

class AdvancedTextCleaner:
    """
    Cleans extracted PDF text before chunking and embedding.

    Features:
    ---------
    ✔ Remove extra whitespace
    ✔ Remove multiple blank lines
    ✔ Fix hyphenated words
    ✔ Remove page numbers
    ✔ Remove repeated headers/footers (customizable)
    ✔ Normalize Unicode characters
    """

    def __init__(self, remove_page_numbers=True,remove_headers=False, remove_footers=False ):
        self.remove_page_numbers=remove_page_numbers
        self.remove_headers=remove_headers
        self.remove_footers=remove_footers

    def clean(self,text:str)-> str:
        if not text:
            return ""
        text=self.normalize_unicode(text)

        text=self.fix_hyphenation(text)

        text=self.remove_extra_spaces(text)

        if self.remove_page_numbers:
            text=self.remove_page_numbers_fn(text)

        if self.remove_headers:
            text = self.remove_headers_fn(text)

        if self.remove_footers:
            text = self.remove_footers_fn(text)

        return text.strip()
    def normalize_unicode(self,text):
        text=text.replace("\u00A0"," ")
        text=text.replace("\u200B","")
        return text
    def remove_extra_spaces(self,text):
        return re.sub(r"[\t]+"," ",text)

    def remove_blank_lines(self,text):
        return re.sub(r"\n\s*\n+","\n",text)
    def fix_hyphenation(self, text):

        return re.sub(r"(\w)-\n(\w)", r"\1\2", text)

    # ----------------------------------------------------

    def remove_page_numbers_fn(self, text):

        text = re.sub(
            r"(?im)^page\s+\d+\s*$",
            "",
            text
        )

        text = re.sub(
            r"(?im)^-\s*\d+\s*-$",
            "",
            text
        )

        return text

    # ----------------------------------------------------

    def remove_headers_fn(self, text):

        return text

    # ----------------------------------------------------

    def remove_footers_fn(self, text):

        return text



       
