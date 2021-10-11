def sort(array):
    for i in range(1, len(array)):
        x = array[i]
        idx = i
        while idx > 0 and array[idx - 1] > x:
            array[idx] = array[idx - 1]
            idx -= 1
        array[idx] = x
    return array


def find_position(array, number):
    i = 0
    while (i < len(array) - 1) and (array[i] < number):
        if (array[i] < number) and (array[i+1] >= number):
            return i
        i = i + 1
    return -1


input_str = input("Please enter numbers split by space: ")
num = int(input("Please enter the random number: "))

numbers = [int(s) for s in input_str.split(" ")]


print("The sorted list is: ", sort(numbers))
print("The position in the array is:", find_position(numbers, num))
