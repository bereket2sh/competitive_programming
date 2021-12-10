def gradingStudents(grades):
    for i in range(len(grades)):
        temp = grades[i] % 5
        if (grades[i]>=38 and temp >= 3):
            grades[i] = grades[i] + (5 - temp)

    return grades
