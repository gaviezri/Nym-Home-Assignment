from typing import List

from src.bonus1.pdf_improved_parser import ExtraTextualWord

PDFSection = List[List[ExtraTextualWord]]
def split_to_sections(pdf: List[ExtraTextualWord]) -> PDFSection:
    '''
    I see a potential for implementing FSM design pattern here
    but lack of time - will implement naive approach:
    '''
    sections: PDFSection = []
    current_section: List[ExtraTextualWord] = []

    for word in pdf:
        if word.is_bold:
            # NO TIME :)
            pass


