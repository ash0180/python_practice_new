text = input("what is your text : ")
with open("sample.txt", "w") as file :
    file.write(text + "\n")

with open("sample.txt","r")as file :
    no_of_lines = file.read()

words_no = no_of_lines.split()
print(f"total no if words are :", len(words_no))


    

