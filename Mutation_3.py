def bubble_sort(arr):
    arr_len = len(arr)
    for i in range(arr_len-1):
        for j in range(arr_len-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def searching(arr, key):
    for i in range(len(arr)):
        if key == arr[i]:
            return i
    return -1

def membership(arr, key):
    for i in range(len(arr)):
        if key == arr[i]:
            return 1
    return 0


def Membership_binarySearch(arr, x):
    #l:left boundary, r:right boundary, x: target key
    l = 0
    r = len(arr)-1
    while  l <= r:
        print("left",l,"right",r)
        #Floor Division
        #mid = l + (r - l) // 2 change to mid = l + (r - l) // 4
        mid = l + (r - l) // 4
        print("mid",mid,"value:",arr[mid])
        if arr[mid] == x:
            return 1
        elif arr[mid] > x:
            r = mid - 1
        else:
            l =  mid + 1
    else:
    # do not exist
        return 0

def Membership_unsorted(arr,x):
    arr = bubble_sort(arr)
    return Membership_binarySearch(arr,x)

if __name__ == "__main__":
    a = [2,1,0,5,7,8,9]
    result = Membership_unsorted(a,6)
    print(result)