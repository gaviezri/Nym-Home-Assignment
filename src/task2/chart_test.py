from src.constant import NAME, DOB, TIMEFMT, EKG
from src.task1.pdf_parser import pdf_to_dict, PagesToWords
from src.task2.chart import Chart
from src.test_utils import get_charts_paths, expected_output_task2
from pdfplumber import open



charts_paths = get_charts_paths()
for i, chart_path in enumerate(charts_paths):
    chart_pdf = open(chart_path)
    output: PagesToWords = pdf_to_dict(chart_pdf)
    current_chart: Chart = Chart.populate_chart(output)
    assert expected_output_task2[i][NAME] == current_chart.name,\
        f"expected: {expected_output_task2[NAME]}, got: {current_chart.name}"

    assert expected_output_task2[i][DOB] == current_chart.dob.strftime(TIMEFMT),\
        f"expected: {expected_output_task2[DOB]}, got: {current_chart.dob}"

    assert expected_output_task2[i][EKG] == current_chart.has_valid_ekg, \
        f"expected: {expected_output_task2[EKG]}, got: {current_chart.has_valid_ekg}"

    print(current_chart.age)

print("IT WORKS")


