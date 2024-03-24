from pdfplumber import open
from pdf_parser import *
from src.test_utils import get_charts_paths, expected_output_task1

charts_paths = get_charts_paths()[:2]

for i, chart_path in enumerate(charts_paths):
    chart_pdf = open(chart_path)
    output: PagesToWords = pdf_to_dict(chart_pdf)
    for pages in output:
        for j, word in enumerate(output[pages]):
            assert word.text == expected_output_task1[i][j], f"{word.text} is not {expected_output_task1[i][j]} for i = {i}, j={j}"

print('IT WORKS!')
