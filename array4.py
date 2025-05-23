import array as myarray


x2 = list(range(0,100,2))
arr1= myarray.array('i',x2)

for i in range(0,len(arr1)):
    print(arr1[i], end=" ")
print("\n")

arr1[2] = 3 # update array thorught the indexing
print(arr1[i], end=" ")
print("\n")






