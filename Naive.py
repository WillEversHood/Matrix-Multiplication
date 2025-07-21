def naive_matrix_multiply_recursive(A, B):
    """
    Recursively multiplies two matrices A and B.
    Assumes:
    - A is of size m x n
    - B is of size n x p
    - Result will be of size m x p
    """

    def multiply_cell(i, j, k):
        # Recursively compute the dot product for row i of A and column j of B
        if k == 0:
            return A[i][k] * B[k][j]
        return A[i][k] * B[k][j] + multiply_cell(i, j, k - 1)

    def compute_row(i, j_max):
        # Computes row i of the result
        if j_max == 0:
            return [multiply_cell(i, 0, len(A[0]) - 1)]
        return compute_row(i, j_max - 1) + [multiply_cell(i, j_max, len(A[0]) - 1)]

    def compute_matrix(i_max):
        # Recursively builds the entire result matrix
        if i_max == 0:
            return [compute_row(0, len(B[0]) - 1)]
        return compute_matrix(i_max - 1) + [compute_row(i_max, len(B[0]) - 1)]

    # Basic dimension check
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must equal number of rows in B.")

    return compute_matrix(len(A) - 1)

# Example usage:
A = [[1, 3], 
     [7, 5]]

B = [[6, 8], 
     [4, 2]]
C = naive_matrix_multiply_recursive(A, B)
print("Matrix C (Result of A * B):")
print(C)
# Output should be:
# [[18, 14],
#  [62, 66]]