import time
def mergesort(list1):
    if len(list1)>1:
        mid=len(list1)//2
        left=list1[:mid]
        right=list1[mid:]
        mergesort(left)
        mergesort(right)
        i=j=k=0
        while i<len(left)and j<len(right):
            if left[i]<right[j]:
                list1[k]=left[i]
                i+= 1
            else:
                list1[k] = right[j]
                j+=1
            k += 1
        while i<len(left):
            list1[k]=left[i]
            i+= 1
            k+= 1
        while j<len(right):
            list1[k]=right[j]
            j+= 1
            k+= 1
    return list1
list1=[]
n= int(input("enter the size of list:"))
for i in range(n):
    list1.append(int(input("enter the number:")))
print("before sorting: the list items are ")
for i in range(len(list1)):
    print(list1[i],end="   ")
start =time.time()
list1 = mergesort(list1)
end=time.time()
print("\nAfter sorting:")
for i in range(len(list1)):
    print(list1[i],end="  ")
print("\nTime taken:",end-start)

