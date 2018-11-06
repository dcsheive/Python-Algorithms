def pushFront(arr,num):
    arr.append(0)
    for i in range(len(arr)-1,-1,-1):
        if i == 0:
            arr[i] = num
        else:
            arr[i] = arr[i-1]
    print( arr)
# pushFront([1,2,3,4], 0)
# arr.insert(0,val)
def popFront(arr):
    for i in range(0,len(arr)-1):
        arr[i] = arr[i+1]
    arr.pop()
    print( arr)
# popFront([1,2,3,4])
# arr.pop(0)
def insertAt(arr, index,val):
    arr.append(0)
    for i in range(len(arr)-1,index,-1):
        arr[i] = arr[i-1]
    arr[index] = val
    print( arr)
# insertAt([1,2,3,4], 2, 5)

