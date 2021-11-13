#we can use both nested functions perfect_num & perfect_num2
def perfect_num(num,sum1):
    def check(num,sum1):
        for i in range(1, num):
            if(num % i == 0):
                sum1 = sum1 + i
        yield sum1

    for j in check(num,sum1):
        if j == num:
            print('perfect num')
        elif j> num:
            print('Greater')
        else:
            print('Lesser')



get_num = int(input('enter number to check:'))
perfect_num(get_num,0)


def perfect_num2(num,sum1=0):
    def check(num,sum1=0):
        for i in range(1, num):
            if num%i == 0:
                yield i

    for j in check(num,sum1):
        sum1 = sum1 + j
    if sum1 == num:
        print('perfect num')
    elif sum1> num:
        print('Greater')
    else:
        print('Lesser')
#perfect_num2(get_num)