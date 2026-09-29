students = [("alice" ,85), ("bob",62), ("charli",90),("david",45)]
passed_students = []
for (name ,marks)in students:
    if marks >= 60:
        passed_students.append(name)

print(passed_students)
print(len(passed_students))