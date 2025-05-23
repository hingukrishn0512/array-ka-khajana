import array as myarray
x = list([1,3,325,3,23,32,23])
arr = myarray.array('i' ,[1,3,325,3,23,32,23])
shortarray = arr.tolist()
shortarray.sort()  #ascending order
print(shortarray)



shortarray.sort(reverse=True)
print(shortarray)  #descing order