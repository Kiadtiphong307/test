input_num = input()

count_num = list(map(int,input_num.split()))

people = []

for i in count_num :
    if count_num.count(i)==1:
        people.append(i)

print(*people, sep = ' ')