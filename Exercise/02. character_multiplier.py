# First task by the lecture

first_string, second_string = input().split()
total_sum = 0
if len(first_string) > len(second_string):
    # Multiplication
    for index in range(len(second_string)):
        total_sum += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(second_string), len(first_string)):
        
            
elif len(first_string) < len(second_string):
    pass
elif len(first_string) == len(second_string):
    pass

# Second task by me

