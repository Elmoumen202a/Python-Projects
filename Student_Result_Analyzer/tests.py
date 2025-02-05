import pytest
from main import calculate_average, process_student_data

def test_calculate_average():
    student = {'Math': 50, 'Science': 50, 'English': 50}
    assert calculate_average(student) == 50.0

def test_pass_status():
    data = [{'Student ID': '1', 'Name': 'A', 'Math': 60, 'Science': 60, 'English': 60}]
    results, stats = process_student_data(data)
    assert results[0]['Status'] == 'Pass'
    assert stats['passed'] == 1

def test_fail_status():
    data = [{'Student ID': '2', 'Name': 'B', 'Math': 30, 'Science': 50, 'English': 60}]
    results, stats = process_student_data(data)
    assert results[0]['Status'] == 'Fail'
    assert stats['failed'] == 1

def test_class_average():
    data = [
        {'Student ID': '1', 'Name': 'A', 'Math': 40, 'Science': 40, 'English': 40},
        {'Student ID': '2', 'Name': 'B', 'Math': 50, 'Science': 50, 'English': 50}
    ]
    results, stats = process_student_data(data)
    assert stats['class_average'] == 45.0