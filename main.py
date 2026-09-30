def student_result(): 
    name = "Aidos" 
    programming = 85 
    math = 90 
    english = 75 
    
    # 1. Логикалық қате түзетілді: барлық пәндер қосылады
    total = programming + math + english 
    
    # 2. Логикалық қате түзетілді: нақты бөлу (float division) қолданылды
    average = total / 3 
    
    print("Student:", name) 
    # Күтілетін нәтижеде бұл жолдар талап етілмегендіктен, қалдыруға немесе өшіруге болады:
    # print("Programming:", programming) 
    # print("Math:", math) 
    # print("English:", english) 
    
    print("Total:", round(total)) 
    print("Average:", round(average, 2)) 
    
    # 3. Логикалық қате түзетілді: шартты 80-ге өзгерттік (себебі орташа балл 83.33)
    if average >= 90: 
        grade = "A" 
    elif average >= 80: 
        grade = "B" 
    elif average >= 50: 
        grade = "C" 
    else: 
        grade = "F" 
        
    print("Grade:", grade) 
    
    bonus = 10 
    # 4. Логикалық қате түзетілді: int() функциясы алынып тасталды
    final_score = average + bonus 
    print("Final score:", round(final_score, 2)) 
    
    # Төмендегі қате тудыратын және күтілетін нәтижеге кірмейтін жолдар жойылды немесе түзетілді:
    # scores = [programming, math, english] 
    # print("First subject:", scores[0]) # Индекс 0-ге ауыстырылды
    # comment = "" # None орнына бос мәтін берілді
    # print("Comment length:", len(comment)) 
    # result = "SUCCESS" 
    # print("Result:", result) # Жақша жабылды

student_result()
