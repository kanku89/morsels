
matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]

#matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
#matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]

def lists_to_list():

    i = 0
    x1 = []
    y1 = []
    for x, y in zip(matrix1, matrix2):
        while i < len(matrix1):
            x1.append(x[i]+y[i])
            i += 1
        #y1.append(y[0])

    print(x1)


lists_to_list()



    #new_list = [x+2 for x, y in zip(matrix1, matrix2)]
    #print(new_list)
