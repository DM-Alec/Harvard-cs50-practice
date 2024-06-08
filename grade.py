score = int(input("Score: "))
#when if is only used, it breaks the upper bounds for statements after the first if, printing all grades
#can be optimized with loops
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


