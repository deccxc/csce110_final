'''
File:    final.py
Author:  Corbin Cabrera, Taylor Schofield
Date:    12/02/2020
Email:  deccxc@tamu.edu , taylor1311@tamu.edu
'''

import matplotlib.pyplot as plt
import pandas as pd
import os

# initialize variables
option = 0
def main_menu():
    print()
    print('*********************************Main Menu******************************************')
    print('1. Read csv file')
    print('2. Generate student report file')
    print('3. Generate student report charts')
    print('4. Generate class report file')
    print('5. Generate class report charts')
    print('6. Quit')
    print('***************************************************************************')
    print()

def option_2():
    uin_str = input('Enter UIN of student for report: ')
    valid = 0
    while valid == 0:
        if len(uin_str) == 10:
            try:
                uin = int(uin_str)
                file1 = o_file.loc[o_file['UIN'] == uin]
                student = file1.to_dict()
                lab = {}
                quiz = {}
                exams = {}
                reading = {}
                score = {}
                project = {}
                for key, value in student.items():
                    if 'lab' in key:
                        results = {key: next(iter(value.values()))}
                        lab.update(results)
                    elif 'quiz' in key:
                        results = {key: next(iter(value.values()))}
                        quiz.update(results)
                    elif 'exam' in key:
                        results = {key: next(iter(value.values()))}
                        exams.update(results)
                    elif 'reading' in key:
                        results = {key: next(iter(value.values()))}
                        reading.update(results)
                    elif 'project' in key:
                        results = {key: next(iter(value.values()))}
                        project.update(results)
                count_lab = 0
                total_lab = 0
                for key in lab:
                    count_lab += 1
                    total_lab += lab[key]
                lab_score = round(total_lab / count_lab, 1)
                count_quiz = 0
                total_quiz = 0
                for key in quiz:
                    count_quiz += 1
                    total_quiz += quiz[key]
                quiz_score = round(total_quiz / count_quiz, 1)
                count_reading = 0
                total_reading = 0
                for key in reading:
                    count_reading += 1
                    total_reading += reading[key]
                reading_score = round(total_reading / count_reading, 1)
                count_exam = 0
                total_exam = 0
                for key in exams:
                    count_exam += 1
                    total_exam += exams[key]
                exam_score = round(total_exam / count_exam, 1)
                count_project = 0
                total_project = 0
                for key in project:
                    count_project += 1
                    total_project += project[key]
                project_score = round(total_project / count_project, 1)
                total_grade = round(
                    (exam_score * .45) + (lab_score * .25) + (quiz_score * .10) + (reading_score * .10) + \
                    (project_score * .10), 1)
                if total_grade >= 90:
                    letter = 'A'
                elif 89.99 >= total_grade >= 80:
                    letter = 'B'
                elif 79.99 >= total_grade >= 70:
                    letter = 'C'
                elif 69.99 >= total_grade >= 60:
                    letter = 'D'
                else:
                    letter = 'F'
                uin = str(uin)
                save_path = path + '/' + uin + '.txt'
                uin_save = open(save_path, 'w')

                uin_save.write(
                    f'Exams mean: {exam_score}' + "\n" + f'Labs mean: {lab_score}' + "\n" + f'Quizzes mean: {quiz_score}' + "\n" + f'Reading activities mean: {reading_score}' + "\n" + f'Score: {total_grade}%' + "\n" + f'Letter Grade: {letter}')
                valid = 1
            except:
                uin_str = input('Invalid UIN, please try again: ')

        else:
            uin_str = input('Invalid UIN, please try again: ')


def option_3():
    file1 = o_file.loc[o_file['UIN'] == uin]
    student = file1.to_dict()

    lab = {}
    quiz = {}
    exams = {}
    reading = {}

    lab_x = []
    lab_y = []
    exam_x = []
    exam_y = []
    quizzes_x = []
    quizzes_y = []
    reading_x = []
    reading_y = []

    for key, value in student.items():
        if 'lab' in key:
            results = {key: next(iter(value.values()))}
            lab.update(results)
        elif 'quiz' in key:
            results = {key: next(iter(value.values()))}
            quiz.update(results)
        elif 'exam' in key:
            results = {key: next(iter(value.values()))}
            exams.update(results)
        elif 'reading' in key:
            results = {key: next(iter(value.values()))}
            reading.update(results)

    for key in lab:
        lab_x.append(key)
    for value in lab.values():
        lab_y.append(value)

    for key in exams:
        exam_x.append(key)
    for value in exams.values():
        exam_y.append(value)

    for key in quiz:
        quizzes_x.append(key)
    for value in quiz.values():
        quizzes_y.append(value)

    for key in reading:
        reading_x.append(key)
    for value in lab.values():
        reading_y.append(value)

    bar_graph = plt.bar(lab_x, lab_y, align='center', alpha=.5, color=['c', 'g', 'm', 'b', 'r', 'y'])
    plt.yticks(range(0, 120, 10))
    plt.ylabel('Grade')
    plt.xlabel('Labs')
    plt.title('Lab Grade Distribution')
    plt.savefig(path + '\Lab Grades')
    plt.close()

    bar_graph1 = plt.bar(exam_x, exam_y, align='center', alpha=.5, color=['c', 'g', 'm'])
    plt.yticks(range(0, 120, 10))
    plt.ylabel('Grade')
    plt.xlabel('Exams')
    plt.title('Exam Grade Distribution')
    plt.savefig(path + '\Exam Grades')
    plt.close()

    bar_graph2 = plt.bar(quizzes_x, quizzes_y, align='center', alpha=.5, color=['c', 'g', 'm', 'b', 'r', 'y'])
    plt.yticks(range(0, 120, 10))
    plt.ylabel('Grade')
    plt.xlabel('Quizzes')
    plt.title('Quizzes Grade Distribution')
    plt.savefig(path + '\Quizzes Grades')
    plt.close()

    bar_graph3 = plt.bar(reading_x, reading_y, align='center', alpha=.5, color=['c', 'g', 'm', 'b', 'r', 'y'])
    plt.yticks(range(0, 120, 10))
    plt.ylabel('Grade')
    plt.xlabel('Readings')
    plt.title('Reading Grade Distribution')
    plt.savefig(path + '\Reading Grades')
    plt.close()

def option_4():
    report = path + '/report.txt'
    with open(report, 'w') as class_report:
        df = pd.read_csv('grades.csv')
        all_rows = [list(rows) for rows in df.values]
        student_grades = list()
        for student in all_rows:
            lab_total = ((student[1] + student[2] + student[3] + student[4] + student[5] + student[6]) / 6) * (
                .25)
            quiz_total = ((student[7] + student[8] + student[9] + student[10] + student[11] + student[
                12]) / 6) * (.1)
            reading_total = ((student[13] + student[14] + student[15] + student[16] + student[17] + student[
                18]) / 6) * (.1)
            exam_total = (student[19] * .15) + (student[20] * .15) + (student[21] * .15)
            project_total = (student[22] * .1)
            student_total = lab_total + quiz_total + reading_total + exam_total + project_total
            student_grades.append(student_total)
        student_grades.sort()
        minimum = student_grades[0]
        maximum = student_grades[-1]

        if len(student_grades) % 2 == 0:
            num1 = student_grades[len(student_grades) // 2]
            num2 = student_grades[len(student_grades) // 2 - 1]
            median = (num1 + num2) / 2
        else:
            median = student_grades[len(student_grades) // 2]
        total_students = len(df.index)
        mean = sum(student_grades) / total_students
        var_total = 0

        for value in student_grades:
            variance = (mean - value) ** 2
            var_total += variance
        standard_deviation = (var_total / total_students) ** .5
        class_report.write(f'Total number of students: {total_students}\n')
        class_report.write(f'Minimum score: {round(minimum, 1)}\n')
        class_report.write(f'Maximum score: {round(maximum, 1)}\n')
        class_report.write(f'Median score: {round(median, 1)}\n')
        class_report.write(f'Mean score: {round(mean, 1)}\n')
        class_report.write(f'Standard deviation: {round(standard_deviation, 1)}')

def option_5():
    df = pd.read_csv('grades.csv')
    all_rows = [list(rows) for rows in df.values]
    student_grades = list()
    for student in all_rows:
        lab_total = ((student[1] + student[2] + student[3] + student[4] + student[5] + student[6]) / 6) * (.25)
        quiz_total = ((student[7] + student[8] + student[9] + student[10] + student[11] + student[12]) / 6) * (
            .1)
        reading_total = ((student[13] + student[14] + student[15] + student[16] + student[17] + student[
            18]) / 6) * (.1)
        exam_total = (student[19] * .15) + (student[20] * .15) + (student[21] * .15)
        project_total = (student[22] * .1)
        student_total = lab_total + quiz_total + reading_total + exam_total + project_total
        student_grades.append(student_total)
    student_grades.sort()

    letter_grade = ''
    a_count = 0
    b_count = 0
    c_count = 0
    d_count = 0
    f_count = 0

    for grade in student_grades:
        if grade >= 90:
            letter_grade = 'A'
            a_count += 1
        elif 80 <= grade <= 89.99:
            letter_grade = 'B'
            b_count += 1
        elif 70 <= grade <= 79.99:
            letter_grade = 'C'
            c_count += 1
        elif 60 <= grade <= 69.99:
            letter_grade = 'D'
            d_count += 1
        else:
            letter_grade = 'F'
            f_count += 1
    letters = ['A', 'B', 'C', 'D', 'F']
    counts = [a_count, b_count, c_count, d_count, f_count]
    bar_graph = plt.bar(letters, counts, align='center', alpha=.5, color=['c', 'g', 'm', 'b', 'r'])
    plt.yticks(range(0, 80, 10))
    plt.ylabel('Grade Counts')
    plt.xlabel('Letter Grades')
    plt.title('Letter Grade Distribution')
    plt.savefig(path + '\Letter_bar_chart')
    plt.close()
    pie_chart = plt.pie(counts, labels=letters, colors=['c', 'g', 'm', 'b', 'r'])
    plt.title('Letter Grade Distribution')
    plt.savefig(path + '\Letter_pie_chart')
    plt.close()

while option not in ['6', 'q', 'quit']:
    main_menu()
    option = input('Choose another option from the menu: ')
    # Run through each option

    if option == '1':
        file = input('Enter full file name, including file path if in a different directory: ')
        try:
            o_file = pd.read_csv(file)
        except FileNotFoundError:
            print('File not found. Try inputting the directory')
        except UnicodeDecodeError:
            print('Incorrect file type. Please save as .csv file.')
        except:
            print('Error opening file')

    elif option == '2':
        path = os.getcwd()
        path = path + '\Data'
        try:
            os.mkdir(path)
            try:
                option_2()
            except FileNotFoundError:
                print('File not found. Choose option 1 to search a file')
            except:
                option = input('Choose another option from the menu: ')
        except FileExistsError:
            try:
                option_2()
            except FileNotFoundError:
                print('File not found. Choose option 1 to search a file')
            except:
                option = input('Choose another option from the menu: ')

    elif option == '3':
        uin = int(input('Enter UIN of student for report: '))
        path = os.getcwd()
        path = path + f'\{uin}'
        try:
            os.mkdir(path)
            try:
                option_3()
            except FileNotFoundError:
                print('File not found. Try inputting the directory')
            except:
                print('Error')
        except FileExistsError:
            try:
                option_3()
            except FileNotFoundError:
                print('File not found. Try inputting the directory')
            except:
                print('Error')

    elif option == '4':
        path = os.getcwd()
        path = path + '\Data'
        try:
            os.mkdir(path)
            try:
                report = path + '/report.txt'
                option_4()
            except FileNotFoundError:
                print('File not found. Choose option 1 to search a file. ')
        except FileExistsError:
            try:
                report = path + '/report.txt'
                option_4()
            except FileNotFoundError:
                print('File not found. Choose option 1 to search a file. ')

    elif option == '5':
        path = os.getcwd()
        path = path + '\class_charts'
        try:
            os.mkdir(path)
            try:
                option_5()
            except FileNotFoundError:
                print('File not found. Choose option 1 to search file. ')
        except FileExistsError:
            try:
                option_5()
            except FileNotFoundError:
                print('File not found. Choose option 1 to search file. ')
    else:
        print("Option isn't valid. Please try again.")
