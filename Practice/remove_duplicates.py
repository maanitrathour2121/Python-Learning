numbers = [1,5,2,8,5,3,5,2,2,3,1,5]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)