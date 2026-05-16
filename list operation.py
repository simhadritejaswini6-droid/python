numbers = [10,20,30,40,]
print("original List:",numbers)
numbers.append(50)
print("After Append:",numbers)
numbers.insert(2,25)
print("After insert:",numbers)
numbers.remove(30)
print("After Remove:",numbers)
print("Length of list:",len(numbers))
print("List Elements:")
for item in numbers:
    print(item)
