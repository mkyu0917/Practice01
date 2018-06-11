
won = input("금액을 입력하시오")


def getDiv(won):
    num = won / 50000
    remin = won % 50000
    num=int(num)
    remin = int(remin)
    print("50000원 :"+str(num)+"개")

    num = remin / 10000
    remin = won % 10000
    num = int(num)
    remin = int(remin)
    print("10000원 :"+str(num)+"개")

    num = remin / 5000
    remin = won % 5000
    num = int(num)
    remin = int(remin)
    print("5000원 :" + str(num) + "개")

    num = remin / 1000
    remin = won % 1000
    num = int(num)
    remin = int(remin)
    print("1000원 :" + str(num) + "개")

    num = remin / 500
    remin = won % 500
    num = int(num)
    remin = int(remin)
    print("500원 :" + str(num) + "개")

    num = remin / 100
    remin = won % 100
    num = int(num)
    remin = int(remin)
    print("100원 :" + str(num) + "개")

    num = remin / 50
    remin = won % 50
    num = int(num)
    remin = int(remin)
    print("50원 :" + str(num) + "개")

    num = remin / 10
    remin = won % 10
    num = int(num)
    remin = int(remin)
    print("10원 :" + str(num) + "개")

    num = remin / 5
    remin = won % 5
    num = int(num)
    remin = int(remin)
    print("5원 :" + str(num) + "개")

    num = remin / 1
    remin = won % 1
    num = int(num)
    remin = int(remin)
    print("1원 :" + str(num) + "개")


getDiv(int(won))