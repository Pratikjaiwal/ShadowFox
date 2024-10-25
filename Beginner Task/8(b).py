import csv
with open('student_marks.csv', mode='r') as file:
    csv_reader = csv.DictReader(file) 
    student_data = []
    for row in csv_reader:
        student_info = {key: int(value) if key != 'Name' else value for key, value in row.items()}
        total_marks = sum(student_info[subject] for subject in student_info if subject != 'Name')
        student_info['total_marks'] = total_marks
        average_marks = total_marks / (len(student_info) - 1)  # Minus 1 to exclude 'Name'
        student_info['Average'] = average_marks
        student_data.append(student_info)
with open('student_marks_updated.csv', mode='w', newline='') as new_file:
    fieldnames = ['Name', 'total_marks', 'Average']
    csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
    csv_writer.writeheader()  
    for student in student_data:
        csv_writer.writerow({'Name': student['Name'], 'total_marks': student['total_marks'], 'Average': student['Average']})
print("Student marks have been updated and written to 'student_marks_updated.csv'")