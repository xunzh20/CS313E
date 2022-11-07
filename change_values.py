from unicodedata import numeric


def change_values(numbers):
    number_copy = numbers
    if numbers[1] % 2 != 0:
        h = number_copy[1]
        number_copy[1] = number_copy[0]
        number_copy[0] = h
    test_number = numbers[2]
    while True:
        if test_number == 1:
            number_copy[3],number_copy[2] = number_copy[2],number_copy[3]
            break
        if test_number > 1:
            test_number /= 2
        if test_number < 1:
            break
    if number_copy[0] + number_copy[1] + number_copy[2] == number_copy[3]:
        number_copy[3] = number_copy [0]
    return number_copy
    
        
        

if __name__ == '__main__':
    user_numbers = []
    for i in range (0,4):
         user_numbers.append(int(input()))
    result_numbers = change_values(user_numbers)
    for i in result_numbers:
        print(i, end=" ")