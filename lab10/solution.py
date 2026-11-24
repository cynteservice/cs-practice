import numpy

def make_table(rows, columns):
    print()

def rectangle(matrix, row_start, row_stop, column_start, column_stop):
    matrix = numpy.array(matrix)
    return matrix[row_start:row_stop, column_start:column_stop].tolist()

def replace_rectangle(matrix, row_start, row_stop, column_start, column_stop, value):
    copy = numpy.array(matrix)
    copy[row_start:row_stop, column_start:column_stop] = value
    return copy.tolist()

def matrix_vector_product(matrix, vector):
    matrix = numpy.array(matrix)
    vector = numpy.array(vector)
    result = matrix @ vector
    return result.tolist()

def matrix_multiply(left, right):
    left = numpy.array(left)
    right = numpy.array(right)
    result = left @ right
    return result.tolist()

def transpose_matrix(matrix):
    matrix = numpy.array(matrix)
    return matrix.T.tolist()

def solve_system(matrix, vector):
    matrix = numpy.array(matrix)
    vector = numpy.array(vector)
    return numpy.linalg.solve(matrix, vector).tolist()

def tensor_channel_mean(tensor):
    print()

def point_distance(left, right):
    left = numpy.array(left)
    right = numpy.array(right)
    return round(numpy.linalg.norm(first-second), 6)
