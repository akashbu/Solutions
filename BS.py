def searcharr(arr, value):
    l = 0 
    u = len(arr) - 1

    while l < u:
        mid = (l + u)//2
        if arr[mid]<value:
            l=mid+1
        else:
            u=mid
    return l

if __name__ == '__main__':
    print(searcharr([1,2,3,4,5],4))