def row_sums(my_matrix: list):


    for numbers in my_matrix:
        summ = sum(numbers)
        numbers.append(summ)


if __name__ == "__main__":

    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)