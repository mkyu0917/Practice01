lst = []
count = 0
sum = 0

for i in range(0, 5, 1):
    num = input("정수를 입력해주세요")
    lst.append(int(num))
    print(type(lst[i]))

    sum += lst[i]
    count = count + 1

avg = sum / count
print("평균:" + avg)



