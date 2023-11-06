# What does this program does:
# - Filter out non-triangle numbers in an array
# - Calculate the sum

#main function
if __name__ == "__main__":

    #variables to accept return value from the function
    triangle_numbers, sum_triangle_numbers = filter_and_sum_triangle_numbers(numbers)

    #if statement to print output
    if not triangle_numbers:
        print("No triangle numbers found.")
    else:
        print("Triangle numbers:", list(triangle_numbers))
        print("Sum of triangle numbers:", sum_triangle_numbers)

    #end of if statement

#function to filter and find the sum
def filter_and_sum_triangle_numbers(numbers):

    #variables to accept array of numbers, set() to remove duplicates
    triangle_numbers = set()

    #variables to accept sum
    sum_triangle_numbers = 0

    #for loop to identify triangle numbers, and find sum
    for num in numbers:
        n = 1
        while True:
            triangle = n * (n + 1) // 2
            if triangle == num:
                triangle_numbers.add(num)
                sum_triangle_numbers += num
                break
            elif triangle > num:
                break
            n += 1

    #end of for loop

    #return values
    return triangle_numbers, sum_triangle_numbers
