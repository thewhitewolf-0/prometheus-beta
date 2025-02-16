import numpy as np

def hungarian_algorithm(cost_matrix):
    """
    Solve the assignment problem using the Hungarian algorithm.
    
    Args:
        cost_matrix (list or np.ndarray): A square matrix representing costs/weights 
                                          of assigning workers to tasks.
    
    Returns:
        list: A list of (worker, task) assignments that minimizes total cost.
        
    Raises:
        ValueError: If the input is not a valid square matrix.
    """
    # Convert input to numpy array and validate
    try:
        matrix = np.array(cost_matrix, dtype=float)
    except Exception:
        raise ValueError("Input must be a valid matrix")
    
    # Check matrix is square
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Cost matrix must be a square matrix")
    
    n = matrix.shape[0]
    
    # Step 1: Subtract row minimums
    matrix_reduced = matrix.copy()
    for i in range(n):
        matrix_reduced[i] -= matrix_reduced[i].min()
    
    # Step 2: Subtract column minimums
    for j in range(n):
        matrix_reduced[:, j] -= matrix_reduced[:, j].min()
    
    # Step 3: Cover zeros with minimum number of lines
    def cover_zeros(matrix):
        # Create boolean matrix to track covered rows and columns
        covered_rows = [False] * n
        covered_cols = [False] * n
        
        # Count zeros in each row and column
        zero_row_count = [np.sum(row == 0) for row in matrix]
        zero_col_count = [np.sum(matrix[:, col] == 0) for col in range(n)]
        
        # Prioritize rows and columns with fewest zeros
        while not all(covered_rows) and not all(covered_cols):
            # Find uncovered row or column with fewest zeros
            min_zeros_row = min((count for i, count in enumerate(zero_row_count) 
                                 if not covered_rows[i] and count > 0), default=None)
            min_zeros_col = min((count for i, count in enumerate(zero_col_count) 
                                 if not covered_cols[i] and count > 0), default=None)
            
            if min_zeros_row is None and min_zeros_col is None:
                break
            
            # Prefer row if both are valid or row has fewer zeros
            if (min_zeros_col is None or 
                (min_zeros_row is not None and min_zeros_row <= min_zeros_col)):
                row_index = zero_row_count.index(min_zeros_row)
                covered_rows[row_index] = True
                # Update column counts based on zeros in this row
                for j in range(n):
                    if matrix[row_index, j] == 0 and not covered_cols[j]:
                        covered_cols[j] = True
                        zero_col_count[j] = 0
            else:
                col_index = zero_col_count.index(min_zeros_col)
                covered_cols[col_index] = True
                # Update row counts based on zeros in this column
                for i in range(n):
                    if matrix[i, col_index] == 0 and not covered_rows[i]:
                        covered_rows[i] = True
                        zero_row_count[i] = 0
        
        return covered_rows, covered_cols
    
    # Step 4: Find optimal assignment
    def find_assignment(matrix):
        assignment = []
        used_rows = set()
        used_cols = set()
        
        for i in range(n):
            for j in range(n):
                if matrix[i, j] == 0 and i not in used_rows and j not in used_cols:
                    assignment.append((i, j))
                    used_rows.add(i)
                    used_cols.add(j)
                    break
        
        return assignment
    
    # Apply Hungarian algorithm steps
    covered_rows, covered_cols = cover_zeros(matrix_reduced)
    
    # Find assignment
    assignment = find_assignment(matrix_reduced)
    
    return assignment