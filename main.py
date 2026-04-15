1():
    answer = input("Столица Франции? ")
    if answer.lower() == "париж":
        print("✓ Правильно! +1 балл\n")
        return 1
    else:
        print("✗ Неправильно! Правильный ответ: Париж\n")
        return 0

def question2():
    answer = input("Столица Японии? ")
    if answer.lower() == "токио":
        print("✓ Правильно! +1 балл\n")
        return 1
    else:
        print("✗ Неправильно! Правильный ответ: Токио\n")
        return 0

def question3():
    answer = input("Столица Италии? ")
    if answer.lower() == "рим":
        print("✓ Правильно! +1 балл\n")
        return 1
    else:
        print("✗ Неправильно! Правильный ответ: Рим\n")
        return 0

def question4():
    answer = input("Столица России? ")
    if answer.lower() == "москва":
        print("✓ Правильно! +1 балл\n")
        return 1
    else:
        print("✗ Неправильно! Правильный ответ: Москва\n")
        return 0

print("\n=== ВИКТОРИНА 'СТОЛИЦЫ МИРА' ===\n")
score = 0
score += question1()
score += question2()
score += question3()
score += question4()

print(f"🏆 ВАШ РЕЗУЛЬТАТ: {score} из 4")
