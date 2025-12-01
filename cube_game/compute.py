import math


def matmul(mat_a: list[list[float]], mat_b: list[list[float]]) -> list[list[float]]:
    '''
    :param mat_a: matrix
    :param mat_b: matrix
    :return: matrix product of mat_a and mat_b
    '''
    m, n = len(mat_a), len(mat_a[0])
    n2, p = len(mat_b), len(mat_b[0])
    if n != n2:
        raise ValueError("width of first and height of second must be equal")
    result = []
    for i in range(m):
        line = []
        for j in range(p):
            s = 0.0
            for k in range(n):
                s += mat_a[i][k] * mat_b[k][j]
            line.append(s)
        result.append(line)
    return result

matrix_a = [ [3, 4, -1, 4], [-2, 2, 5, 1]]
matrix_b = [ [1, 3, -2], [2, 5, 1], [-1, 4, -4], [2, 3, 6] ]


def transpose(mat:list[list[float]]) -> list[list[float]]:
    '''
    :param mat: Eingabematrix
    :returns: Transponierte Matrix
    '''
    if not mat:
        return []
    rows, cols = len(mat), len(mat[0])
    result: list[list[float]] = []
    for j in range(cols):
        new_row: list[float] = []
        for k in range(rows):
            new_row.append(mat[k][j])
        result.append(new_row)
    return result

mat4 = [
    [1, 2, 3]
    , [4, 5, 6]
]


def rot_2D(angle: float) -> list[list[float]]:
    '''
    :param angle: angle in radians
    :return: matrix
    :-sin: rotation direction Uhrzeigersinn
    '''
    cos = math.cos(angle)
    sin = math.sin(angle)
    return [
        [cos, -sin],
        [sin, cos]
    ]


def rot_3D(angle: float, axis: str) -> list[list[float]]:
    """
    :param angle: angle type float in radians
    :param axis: for one of the 3 axis of 3D Matrixes
    :return: transposed 3D Matrix
    """

    cos = math.cos(angle)
    sin = math.sin(angle)

    if axis == "x".lower() or axis == "x".upper():
        return [[1, 0, 0], [0, cos, -sin], [0, sin, cos]]
    elif axis == "y".lower() or axis == "y".upper():
        return [[cos, 0, sin], [0, 1, 0], [-sin, 0, cos]]
    elif axis == "z".lower() or axis == "z".upper():
        return [[cos, -sin, 0], [sin, cos, 0], [0, 0, 1]]
    else:
        raise ValueError("axis must be x, y, or z")



def project_ortho(point: tuple[float, float, float], scale: float) ->tuple[float, float]:
    x_axis = point[0]
    y_axis = point[1]
    z_axis = point[2]
    return (x_axis * scale, y_axis * scale)


if __name__ == "__main__":
    matrix_c = matmul(matrix_a, matrix_b)
    print(matrix_c)
    print(transpose(mat4))
    print(rot_2D(20.333))