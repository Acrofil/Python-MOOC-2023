# WRITE YOUR SOLUTION HERE:

def recursive_sum(number: int):
    if number <= 1:
        return number
    
    number_to_sum = recursive_sum(number - 1)
    number_sum = number + number_to_sum
    return number_sum


if __name__ == "__main__":
    
    result = recursive_sum(3)
    print(result)

    print(recursive_sum(5))
    print(recursive_sum(10))