def pascal_triangle(n):
    n = int(n)
    if n <= 0:
        return []

    #initialize a list of lists and print first row
    triangle = [[1]]
    for i in range(1, n):
        #first element in a row is 1
        row = [1]
        prev_row = triangle[-1]
        #middle elements
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        #last element in a row is 1
        row.append(1)
        triangle.append(row)
    return triangle