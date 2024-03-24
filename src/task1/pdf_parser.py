from dataclasses import dataclass
from typing import List, Dict
import pdfplumber

from src.constant import X0, X1, WORD


@dataclass
class TextualWord:
    x0: float
    x1: float
    text: str


PagesToWords = Dict[int, List[TextualWord]]


def pdf_to_dict(pdfplumber_pdf: pdfplumber.PDF) -> PagesToWords:
    pages_to_words: PagesToWords = {}

    # assuming several pages for a more generalized approach
    for page_number, page in enumerate(pdfplumber_pdf.pages):

        words_with_boxes = page.extract_words()

        textual_words = [
            TextualWord(float(word[X0]),
                        float(word[X1]),
                        word[WORD])
            for word in words_with_boxes]

        pages_to_words[page_number] = textual_words

    return pages_to_words
