grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
total_grade1 = sum(grades[0])
total_grade2 = sum(grades[1])
total_grade3 = sum(grades[2])
total_grade4 = sum(grades[3])
total_grade5 = sum(grades[4])
middle_grades = [[total_grade1 / 5], [total_grade2 / 4], [total_grade3 / 4], [total_grade4 / 3], [total_grade5 / 5]]
students_grades = {'Aaron': middle_grades[0], 'Bilbo': middle_grades[1], 'Johnny': middle_grades[2], 'Khendrik': middle_grades[3], 'Steve': middle_grades[4]}
print(students_grades)