from dataclasses import dataclass
from datetime import date, datetime
from typing import Tuple

from src.constant import TIMEFMT, DOB
from src.task1.pdf_parser import PagesToWords


@dataclass
class Chart:
    name: str
    dob: date
    has_valid_ekg: bool

    @property
    def age(self) -> float:
        today = date.today()
        age_dt = today - self.dob
        age = age_dt.days / 365.0
        return age

    '''
    assuming the extraction will be called orderly,
    the last offset can be utilized to speed up extraction of next fields
    reducing the iterations to N instead of O(N)
    I can come up with a more generalized and order-independent but I figured this 
    implementation is more interesting >:-)
    '''
    @staticmethod
    def populate_chart(page_to_words: PagesToWords) -> any:
        name, offset = Chart.extract_name(page_to_words, 2)
        dob, offset = Chart.extract_dob(page_to_words, offset)
        has_valid_ekg, _ = Chart.extract_has_valid_ekg(page_to_words, offset)

        return Chart(name=name, dob=dob, has_valid_ekg=has_valid_ekg)


    @staticmethod
    def extract_name(page_to_words: PagesToWords, offset: int = 0) -> Tuple[str, int]:
        new_offset = offset
        name_parts = []
        # collect name parts until reach next 'DOB:'
        for new_offset, word in enumerate(page_to_words[0][offset:]):
            if word.text.endswith(':'):
                break
            else:
                name_parts.append(word.text)
        # return name and offset of 'DOB:'
        return ' '.join(name_parts), new_offset


    @staticmethod
    def extract_dob(page_to_words: PagesToWords, offset: int = 0) -> Tuple[date, int]:
        new_offset = 0
        dob_dt = None
        for new_offset, word in enumerate(page_to_words[0][offset:]):
            if word.text.startswith(DOB):
                dob_str = page_to_words[0][offset + new_offset + 1].text
                dob_dt = datetime.strptime(dob_str, TIMEFMT).date()
                break
        # return dob date time, and offset to 'Procedure'
        return dob_dt, offset + new_offset + 2

    @staticmethod
    def extract_has_valid_ekg(page_to_words: PagesToWords, offset: int = 0) -> Tuple[bool, int]:
        for new_offset, word in enumerate(page_to_words[0][offset:]):
            if word.text == 'EKG':
                # new_offset + 1 == 'Results'
                # new_offset + 2 == 'valid / No*'
                valid = not page_to_words[0][offset + new_offset + 2].text.lower().startswith('n')
                return valid, new_offset + 2






