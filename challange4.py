student_score = {"Alice":85 ,"Bob":62 , "charli":90 , "david":45}
student_score["Eve"]=95
student_score["Bob"]=70
for name , score in student_score.items():
    print(f"student :{name} | score : {score}")