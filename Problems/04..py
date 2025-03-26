def get_even_number(prompt):
    num = int(input(prompt))
    if num % 2 != 0:
        print("Please enter an even number.")
        return get_even_number(prompt)
    return num

num1 = get_even_number("Enter the first even number: ")
num2 = get_even_number("Enter the second even number: ")

sum_result = num1 + num2

if sum_result % 2 == 0:
    print("The sum of", num1, "and", num2, "is:", sum_result)
