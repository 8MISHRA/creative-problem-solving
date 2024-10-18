"""
Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.
"""

def setZeroes(self, matrix):
    tople = [set(), set()]
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                tople[0].add(row)
                tople[1].add(col)
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if row in tople[0] or col in tople[1]:
                matrix[row][col] = 0

# Do this using a boolean array to solve.
