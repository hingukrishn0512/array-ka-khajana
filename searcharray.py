import array as myarray

x = list(range(0,100,2))

search_arr = myarray.array('i' , x)



for i in range(0,len(search_arr[0:20])):
    print(search_arr[i] ,end=" ")
print("\n")

index = search_arr.index(18)
res = search_arr[index]

print(f"at index {index} and the value at that index is {res}")