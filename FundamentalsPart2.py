def sigma(num):
    sum = 0
    for i in range(1,num+1):
        sum += i
    print(sum)
    return sum
# sigma(5)
def factorial(num):
    product = 1
    for i in range(1,num+1):
        product*=i
    print(product)
# factorial(5)
def drawStarsLeft(num):
    newStr = ""
    for i in range(1,76):
        if num>=i:
            newStr += "*"
        else:
            newStr += " "
    print(newStr)
# drawStarsLeft(6)
def drawStarsRight(num):
    newStr = ""
    for i in range(1,76):
        if 75-num<i:
            newStr += "*"
        else:
            newStr += " "
    print(newStr)
# drawStarsRight(50)
def drawStarsCenter(num):
    newStr = ""
    absent = 75-num
    count=1
    for i in range(0,int(absent/2)):
        newStr +=" "
        count+=1
    for i in range(0,num):
        newStr +="*"
        count+=1
    for i in range(count,76):
        newStr +=" "
    print(newStr)
    print(len(newStr))
# drawStarsCenter(71)
def threesAndFives():
    sum = 0
    for i in range(100,4000001):
        if i%3==0 and i%5!=0:
            sum+=i
        elif i%5==0 and i%3!=0:
            sum+=i
    print(sum)       
# threesAndFives()
def betterThreesAndFives(num1, num2):
    sum =0 
    for i in range(num1,num2+1):
        if i%3==0 and i%5!=0:
            sum+=i
        elif i%5==0 and i%3!=0:
            sum+=i
    print(sum)
# betterThreesAndFives(1,15)
def generateCoinChange(num):
    q = int(num/25)
    d = int(num%25/10)
    n = int(num%25%10/5)
    p = int(num%25%10%5)
    print("Quarters:",q,"Dimes:",d,"Nickels:",n,"Pennies:",p)
# generateCoinChange(94)
def messyMath(num):
    sum = 0
    for i in range(1,num+1):
        if (i%3==0):
            pass
        elif(i%7==0):
            sum+=i*2
        elif(i==num/3):
            return -1
        else:
            sum+=i
    return sum
# print(messyMath(4))
# print(messyMath(8))
# print(messyMath(15))
def fibonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    sum = 1
    sum2 = 1
    for i in range(2,num):
        newSum = sum + sum2
        sum = sum2
        sum2 = newSum
    return newSum
# print(fibonacci(3))
# print(fibonacci(4))
# print(fibonacci(5))
# print(fibonacci(6))
# print(fibonacci(7))

def sumToOneDigit(num):
    if num/10<1:
        return num
    newStr = str(num)
    while(len(newStr)>1):
        sum = 0
        for i in newStr:
            sum += int(i)
        newStr = str(sum)
    return int(newStr)
# print(sumToOneDigit(5))
# print(sumToOneDigit(928))

def clockHandAngles(seconds):
    hours = seconds/3600
    minutes = seconds%3600/60
    seconds = seconds%3600%60
    hours = hours *30 %360
    minutes = minutes * 6 
    seconds = seconds * 6
    print("Hours:",hours,"degs","Minutes:",minutes,"degs","Seconds:",seconds,"degs")
# clockHandAngles(119730)

def isPrime(num):
    for i in range(2,num):
        if num%i ==0:
            return False
    return True
# print(isPrime(11))
def extractDigit(num,digit):
    num /= 10**digit
    num %= 10
    return int(num)
# print(extractDigit(1824,0))
# print(extractDigit(1824,2))
# print(extractDigit(1824,7))


