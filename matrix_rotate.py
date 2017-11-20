def rotate(matrix):
    size = len(matrix)
    layer_count = size / 2

    # Move through layers (i.e. layer loop).
    for layer in range(0, layer_count):

            first = layer
            last = size - first - 1

            # Move within a single layer (i.e. element loop).
            for element in range(first, last):

                offset = element - first

                # 'element' increments column (across right)
		#  top = (first, element)
                # 'element' increments row (move down)
                # right_side = (element, last)
                # 'last-offset' decrements column (across left)
                # bottom = (last, last-offset)
                # 'last-offset' decrements row (move up)
                # left_side = (last-offset, first)

                top = matrix[first][element]
                right_side = matrix[element][last]
                bottom = matrix[last][last-offset]
                left_side = matrix[last-offset][first]

		print 'top: %s' % top
                matrix[first][element] = left_side
                matrix[element][last] = top
                matrix[last][last-offset] = right_side
                matrix[last-offset][first] = bottom

matrix = [
	[0, 1, 2, 3, 4],
	[5, 6, 7, 8, 9],
	[10, 11, 12, 13, 14],
	[15, 16, 17, 18, 19],
	[20, 21, 22, 23, 24]
]

def print_matrix(matrix):
    for row in matrix:
        print row

print_matrix(matrix)
print '--------------------'
rotate(matrix)
print_matrix(matrix)
