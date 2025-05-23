import array as myarray
x = list(range(0,100,2))
arr = myarray.array('i',x)

for i in range(0,len(arr)):
    print(arr[i], end=" ")
print("\n")

print(arr[27])