from pathlib import Path
from src.constant import NAME, EKG, DOB


def get_charts_paths():
    script_dir = Path(__file__).resolve().parent

    project_root = script_dir.parent

    resources_path = project_root / "resources"

    return list(resources_path.glob('*'))


expected_output_task1 = {
    0: ['Patient', 'Name:', 'John', 'Doe', 'the', 'First', 'DOB:', '01/01/1970', 'Procedures', 'Lab', 'Results', 'NONE',
        'EKG', 'Results', 'valid', 'Radiology', 'Results', 'None'],
    1: ['Patient', 'Name:', 'John', 'Doe', 'the', 'Second', 'DOB:', '02/02/1971', 'Procedures', 'Lab', 'Results',
        'Urine', 'Color:', 'Green', 'Blood', 'Color:', 'Blue', 'EKG', 'Results', 'Not', 'Valid', 'Radiology', 'Results',
        'None']
}

expected_output_task2 = {
    0: {NAME: 'John Doe the First', DOB: '01/01/1970', EKG: True},
    1: {NAME: 'John Doe the Second', DOB: '02/02/1971', EKG: False},
    2: {NAME: 'John Doe the Third', DOB: '03/03/1972', EKG: False}
}
