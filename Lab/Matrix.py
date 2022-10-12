
matrix = eval(input("Enter a matrix: "))

trans = [[matrix[y][x] for y in range(len(matrix))] for x in range(len(matrix[0]))]

for t in trans:
   print(t)






