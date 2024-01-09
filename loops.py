data = [2, 3, 4, 5, 6, 7, 8, 9]
grades = ['A1','B2','B3','C4','C5','C6','D7','E8','F9']
names = ['Ayo', 'Ola']
total = 0

for number in data:
    total += number

for grade in grades:
    for name in names:
        print(f"{name} your grade is {grade}" )


#print(total)
