# Print all even numbers from 1 to 10
i = 1
while i<=10:
    if (i % 2 != 0):
        i += 1
        continue
    print(i)
    i += 1

# Print all odd numbers from 1 to 10
j = 1
while j<=10:
    if(j % 2 == 0):
        j += 1
        continue
    print(j)
    j += 1