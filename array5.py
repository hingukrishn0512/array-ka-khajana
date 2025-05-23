import array as myarray


x2 = list(range(0,100,2))
arr1= myarray.array('i',x2)

for i in range(0,len(arr1)):   #OG array
    print(arr1[i], end=" ")
print("\n")

arr1.remove(4)  #have 4 number jase array ma thi
for i in range(0,len(arr1)):
    print(arr1[i], end=" ")
print("\n")

x = list(range(0,100,2))
arr= myarray.array('i',x2)


arr.pop(4)  #index 4 ma je hatu ee jase
for i in range(0,len(arr)):
    print(arr[i], end=" ")
print("\n")





