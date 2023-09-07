def calculate_sum_of_digits(input):
    num = input
    temp = str(num)
    sum = 0
    i = 0
    while i < len(temp):
        sum += int(temp[i])
        i += 1
    return(sum)
# Call the function
input = input("Enter Number : ")
cal = calculate_sum_of_digits(input)
while(len(str(cal))!=1):
    cal = calculate_sum_of_digits(cal)
print("Made it into single digit : ",cal)
