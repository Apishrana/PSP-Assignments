key = ['A', 'B', 'A', 'C', 'D']

students = eval(input("Enter student data as a list of [name, answers] pairs: "))


for student in students:

    name = student[0]

    answers = student[1]
    
    correct = 0
    
    for i,answer in enumerate(answers):
      if answer == key[i]:
        correct += 1
    print(f"{name}: {correct}/{len(key)} ({(correct/len(key))*100:.2f}%)")