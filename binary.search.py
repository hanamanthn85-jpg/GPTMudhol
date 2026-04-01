import time
def binarysearch(a, low, high, key):
    if low <= high:
        mid = (high + low) // 2
        if a[mid] == key:
            print("search Succesfull key found at location:",mid)
            return
        elif key < a[mid]:
            binarysearch(a, low, mid-1, key)
        else:
            binarysearch(a, mid + 1, high, key)
    else:
        print("unsuccessful search")


a=[]
n=int(input("How many elements??:"))
for i in range(n):
    a.append(int(input("Enter the number")))
print("the array elements are:",a)
key = int(input("Enter the key elements in search:"))
start=time.time()
binarysearch(a,0,len(a)-1,key)
end=time.time()
print("the time taken for binary search is",end-start)
            
                  
