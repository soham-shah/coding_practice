import unittest

def zero_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    zeroRows = set()
    zeroCols = set()

    for i in range (rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zeroRows.add(i)
                zeroCols.add(j)

    for i in zeroRows:
        for j in range(cols):
            matrix[i][j] = 0
    for i in zeroCols:
        for j in range(rows):
            matrix[j][i] = 0
    return matrix
# https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/Chapter1/8_Zero%20Matrix/ZeroMatrix.py
class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ], [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [11, 0, 13, 14, 0],
            [0, 0, 0, 0, 0],
            [21, 0, 23, 24, 0]
        ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()