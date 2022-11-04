def print_triangle(n):
    for i in range(n):
        print(' '.join([str(x+1) for x in range(i+1)]))

    for i in range(n-2, -1, -1):
        print(' '.join([str(x+1) for x in range(i+1)]))