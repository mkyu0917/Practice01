number=input("숫자를 입력해주세요")
numbers = int(number)
i=0
num=0

for i in range(1,numbers+1):
    if numbers%2!=0:
        if i%2!=0:
            num=num+i
    if numbers%2==0:
        if i%2==0:
            num=num+i
print(num)
