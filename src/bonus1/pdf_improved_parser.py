from dataclasses import dataclass
from typing import Dict, List

import pdfplumber

from src.constant import X0, X1, WORD, FONT, SIZE
from src.task1.pdf_parser import TextualWord


@dataclass
class ExtraTextualWord(TextualWord):
    fontname: str
    size: float

    @property
    def is_bold(self) -> bool:
        return 'Bold' in self.fontname


PagesToExtraWords = Dict[int, List[ExtraTextualWord]]


def pdf_to_extra_dict(pdfplumber_pdf: pdfplumber.PDF) -> PagesToExtraWords:
    pages_to_words: PagesToExtraWords = {}

    for page_number, page in enumerate(pdfplumber_pdf.pages):
        words_with_boxes = page.extract_words( extra_attrs=["fontname", "size"])

        textual_words = [ExtraTextualWord(float(word[X0]), float(word[X1]), word[WORD], word[FONT], word[SIZE]) for word in words_with_boxes]

        pages_to_words[page_number] = textual_words

    return pages_to_words


