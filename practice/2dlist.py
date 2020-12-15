my = [20,25,20,26,35,289,91,5]

unique =[]

for numbers in my:
    if numbers not in unique:
        unique.append(numbers)
print(unique)
unique.sort()
print(unique)