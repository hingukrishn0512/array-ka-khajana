import array as myarray

arr = myarray.array('i',[1,2,3])
arr1 = myarray.array('d',[1.3,2.0,3.7])
arr2 = myarray.array('u',['a','b','c'])

print(arr.typecode)
print(arr1.typecode)
print(arr2.typecode)

print(arr)
print(arr1)
print(arr2)
print(len(arr2))
print(len(arr2))
print(len(arr2))


for i in range(0,len(arr)):
    print(arr[i], end=" ")
for i in range(0,len(arr1)):
    print(arr1[i], end=" ")
for i in range(0,len(arr2)):
    print(arr2[i], end=" ")