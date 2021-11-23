# Define a basic calculator function with 3 inputs - num1, num2 and operator. Name it as "calculator" 
def calculator(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
    if operator == '-':
        result = num1 - num2
    if operator == '*':
        result = num1 * num2
    if operator == '/':
        result = num1 / num2
    return result

# Call the "calculator" function by passing inputs and print the result function returns
print(calculator(100, 50, '+')) 