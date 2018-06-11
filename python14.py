import random



'''
num = random.randrange(1, 100)
#print(inputNum,type(inputNum))
i=0

print("수를 결정하였스비다. 맞추어보셍요")
while (True) :


    inputN = input(">")
    inputNum = int(inputN)

    if num<inputNum:
        print("더 낮게 입력하세요")
    elif num>inputNum:
        print("더 높게 입력핫요")
    elif num==inputNum:
        print("맞았습니다.")

        continues = input("다시 하시겠습니까?")
        if continues == 'n':
            break
        if continues == 'y':
            num = random.randrange(1, 100)
'''

def upDown():

    num = random.randrange(1, 100)
    # print(inputNum,type(inputNum))
    i = 0

    print("수를 결정하였스비다. 맞추어보셍요")
    while (True):

        inputN = input(">")
        inputNum = int(inputN)

        if num < inputNum:
            print("더 낮게 입력하세요")
        elif num > inputNum:
            print("더 높게 입력핫요")
        elif num == inputNum:
            print("맞았습니다.")

            continues = input("다시 하시겠습니까?")
            if continues == 'n':
                break
            if continues == 'y':
                num = random.randrange(1, 100)

upDown()