# Calculate the sum of even numbers from 1 to 100
even_sum = 0

for num in range(1, 101):
    if num % 2 == 0:
        even_sum += num

print("The sum of even numbers from 1 to 100 is:", even_sum)