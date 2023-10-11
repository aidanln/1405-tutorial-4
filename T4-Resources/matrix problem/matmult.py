# matrix operations
# (putting comments above each process instead of below, as i usually do)
# By Aidan Lalonde-Novales

import math

''' shouldn't change original matrix value as it is passed by reference '''
def mult_scalar(matrix, scale):
	# goes through each row index
	for row_count in range(len(matrix)):
		# goes through each column index (confined to the row above)
		for column_count in range(len(matrix[row_count])):
			# multiply the current matrix row/col position by the scale
			matrix[row_count][column_count] *= scale
	return matrix

''' dot products two matricies '''
def mult_matrix(a, b):

	''' compaitibility check segment '''
	compatibility_flag = False
	# if the items in the rows of matrix a are equal to
	# the amount of rows in matrix b, the matrcies are compatible
	for row in a:
		if len(row) == len(b):
			compatibility_flag = True
	
	''' actual dot product segment '''
	if compatibility_flag == True:
		# matrix to store the dot product of a and b
		dot_prod_matrix = []
		row_index_a = 0

		# add a row in dot_prod_matrix for each row in matrix a, start at first column in matrix b
		for row_count in a:
			dot_prod_matrix.append([])
			column_index_b = 0

			# goes through each column in matrix b, multiplying each value by
			# the corresponding item in the current row of matrix a
			# then, adds to a new_value to be appeneded to dot_prod_matrix
			while column_index_b != len(b[0]):
				column_index_a = 0
				new_value = 0
				for row_b in b:
					new_value += row_b[column_index_b] * row_count[column_index_a]
					column_index_a += 1
				dot_prod_matrix[row_index_a].append(new_value)

				# move on to the next column in matrix b
				column_index_b += 1
			# move on to the next row in matrix a
			row_index_a += 1
		return dot_prod_matrix
	else:
		return None

''' calculates euclidean distance between two points '''
def euclidean_dist(a,b):
	if len(a) != len(b):
		return None
	euc_dist = 0
	for count in range(len(a[0])):
		euc_dist += (a[0][count] - b[0][count])**2
	return math.sqrt(euc_dist)