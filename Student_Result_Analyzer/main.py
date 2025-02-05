import csv
import argparse

def load_student_data(filename):
    # Load student data from a CSV file. 
    students = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            student = {
                'Student ID': row['Student ID'],
                'Name': row['Name'],
                'Math': int(row['Math']),
                'Science': int(row['Science']),
                'English': int(row['English'])
            }
            students.append(student)
    return students

def calculate_average(student):
   # Calculate average marks for a student.
    return (student['Math'] + student['Science'] + student['English']) / 3

def process_student_data(data):
    # Process student data to determine pass/fail status and calculate statistics.
    processed_data = []
    stats = {
        'total_students': 0,
        'passed': 0,
        'failed': 0,
        'total_marks': 0,
        'highest_average': 0
    }
    
    for student in data:
        # Calculate average
        avg = calculate_average(student)
        
        # Determine pass/fail status
        status = 'Pass' if all([
            student['Math'] >= 40,
            student['Science'] >= 40,
            student['English'] >= 40,
            avg >= 50
        ]) else 'Fail'
        
        # Update statistics
        stats['total_students'] += 1
        stats['total_marks'] += avg
        if status == 'Pass':
            stats['passed'] += 1
        else:
            stats['failed'] += 1
        if avg > stats['highest_average']:
            stats['highest_average'] = avg
            
        # Add processed student
        processed_data.append({
            **student,
            'Average': round(avg, 2),
            'Status': status
        })
    
    # Calculate class average
    stats['class_average'] = round(stats['total_marks'] / stats['total_students'], 2) if stats['total_students'] > 0 else 0
    
    return processed_data, stats

def main():
    parser = argparse.ArgumentParser(description='Analyze student results')
    parser.add_argument('--data', default='data.csv', help='Path to data file')
    parser.add_argument('--output', choices=['console', 'csv'], default='console', help='Output format')
    args = parser.parse_args()

    # Load and process data
    data = load_student_data(args.data)
    processed_data, stats = process_student_data(data)

    # Display results
    if args.output == 'console':
        print("\nStudent Results:")
        for student in processed_data:
            print(f"{student['Student ID']} | {student['Name']} | "
                  f"Math: {student['Math']} | Science: {student['Science']} | "
                  f"English: {student['English']} | Average: {student['Average']} | "
                  f"Status: {student['Status']}")
        
        print("\nClass Statistics:")
        print(f"Total Students: {stats['total_students']}")
        print(f"Passed: {stats['passed']}")
        print(f"Failed: {stats['failed']}")
        print(f"Class Average: {stats['class_average']}")
        print(f"Highest Average: {stats['highest_average']}")
    
    elif args.output == 'csv':
        with open('results.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=processed_data[0].keys())
            writer.writeheader()
            writer.writerows(processed_data)
        print("Results saved to results.csv")

if __name__ == '__main__':
    main()