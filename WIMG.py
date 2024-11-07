#Locklin Sheldon SkillPractice: What is my grade
def obtain_teh_grade(perc):
    if perc >= 90:
        return 'A'
    elif perc >= 80:
        return 'B'
    elif perc >= 70:
        return 'C'
    elif perc >= 60:
        return 'D'
    else:
        return 'Z-'

grades = {}

while True:
    class_name = input("Put class name (put 'done' if you don't want to check teh grades): ")
    if class_name == 'done':
        break
    try:
        perc = float(input(f"put grade purrcentaje for {class_name}: "))
        LetterGrade = obtain_teh_grade(perc)
        grades[class_name] = LetterGrade
    except ValueError:
        print("Whatever the crap you just tried to say was, it don't work. try sumting else plllzzz.")

print("grades:")
for class_name, LetterGrade in grades:
    print(f"{class_name}: {LetterGrade}")
