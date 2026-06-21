numbers_list = [21, 44, 67, 88, 99, 102, 5]

even_count = 0
odd_count = 0

for num in numbers_list:
    if num % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("Total even numbers:", even_count)
print("Total odd numbers:", odd_count)