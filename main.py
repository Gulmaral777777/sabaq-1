def student_result():

    name = "Aidos"

    programming = 85
    math = 90
    english = 75

    total = programming + math - english
    average = total // 3

    print("Student:", name)
    print("Programming:", programming)
    print("Math:", math)
    print("English:", english)
    print("Total:", total)
    print("Average:", average)

    if average >= 90:
        grade = "A"
    elif average >= 85:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "F"

    print("Grade:", grade)

    bonus = 10
    final_score = int(average) + bonus

    print("Final score:", final_score)

    scores = [programming, math, english]
    print("First subject:", scores[1])
    comment = None
    print("Comment length:", len(comment))

    result = "SUCCESS"
    print("Result:", result    print("Average rounded:", round(average, 2))


student_result()
