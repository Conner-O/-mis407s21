def largest(number_list):
    # Complete this function as noted in the instructions.
    # Replace the `pass` word below with your code.
    max = number_list[0]
    for x in number_list:
        if x > max:
            max = x
    return max

input_str = input("Enter a list of numbers separated by commas (e.g., '21,22,28'): ")
# A list comprehension that converts a string of comma-separated
# numbers into a list of integers:
input_list = [int(x.strip()) for x in input_str.split(',')]
# Call the largest() function and show the result.


print("Largest of the numbers:", largest(input_list))