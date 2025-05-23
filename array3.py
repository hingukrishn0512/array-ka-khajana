import array as myarray
x = list(range(0,100,2))
arr = myarray.array('i',x)

arr.insert(5,2)
arr.insert(7,8)   #index pramane joday jay


for i in range(0,len(arr)):
    print(arr[i], end=" ")
print("\n")



x2 = list(range(0,90,2))
arr1= myarray.array('i',x2)   # append ma chle joday

arr1.append(5)
for i in range(0,len(arr1)):
    print(arr1[i], end=" ")
print("\n")







