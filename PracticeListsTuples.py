list = [input("Enter First Subject: "), input("Enter Second Subject: "), input("Enter Third Subject: ")]
print(list)

companies = []
companies.append(input("Enter first company: "))
companies.append(input("Enter second company: "))
companies.append(input("Enter third company: "))
print(companies)

# Check Palindrome,
list = [1,2,1]
copy_list = list.copy()
copy_list.reverse()
if(list == copy_list):
    print("Palindrome")
else:
    print("Not Palindrome")