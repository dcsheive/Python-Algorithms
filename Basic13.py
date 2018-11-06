def print1To255():
    for i in range(1,256):
        print(i)
# print1To255()
def printOdds1To255():
    for i in range(1,256):
        if i%2==1:
            print(i)
# printOdds1To255()
def printIntsAndSumTo255():
    sum = 0
    for i in range(256):
        sum += i
        print(i,sum)
# printIntsAndSumTo255()
def printArray(arr):
    for i in arr:
        print(i)
# printArray([1,3,45,6,7,4,2,12])
def printMaxOfArray(arr):
    max = arr[0]
    for i in range(1,len(arr)):
        if max<arr[i]:
            max = arr[i]
    print(max)
# printMaxOfArray([1,3,45,66,4,32,1,9])
def printAvgOfArray(arr):
    sum = 0
    for i in arr:
        sum +=i
    print(sum/len(arr))
# printAvgOfArray([1,3,45,66,4,32,1,9])
def createArrayOfOdds():
    arr = []
    for i in range(256):
        if i%2==1:
            arr.append(i)
    return arr
# print(createArrayOfOdds())
def squareValues(arr):
    for i in range(len(arr)):
        arr[i] = arr[i]*arr[i]
    return arr
# print(squareValues([1,3,5,63,434,7]))
def greaterThanY(arr, y):
    count = 0
    for i in arr:
        if i >y:
            count+=1
    print(count)
# greaterThanY([12,43,67,31,100], 50)
def zeroNegatives(arr):
    for i in range(len(arr)):
        if arr[i]<0:
            arr[i] = 0
    return arr
# print(zeroNegatives([-1,3,-5,-7,9,10]))
def maxMinAvgArray(arr):
    min = arr[0]
    max = arr[0]
    sum = 0
    for i in arr:
        if i<min:
            min = i
        elif i>max:
            max = i
        sum+=i
    print(max,min,sum/len(arr))
# maxMinAvgArray([12,4,5,22,335,6])
def shiftArrayLeft(arr):
    for i in range(len(arr)):
        if i==len(arr)-1:
            arr[i]=0
        else:
            arr[i] = arr[i+1]
    print(arr)
# shiftArrayLeft([12,3,45,6,7])
def replaceNegatives(arr):
    for i in range(len(arr)):
        if arr[i]<0:
            arr[i] = "Dojo"
    print(arr)
# print(replaceNegatives([-1,3,-5,-7,9,10]))
