import pytest
import numpy as np
from src.hungarian_algorithm import hungarian_algorithm

def test_basic_hungarian_algorithm():
    # Simple 3x3 matrix with known optimal assignment
    cost_matrix = [
        [3, 2, 3],
        [2, 1, 3],
        [3, 3, 2]
    ]
    
    result = hungarian_algorithm(cost_matrix)
    
    # Expected: Lowest cost assignment for each worker
    expected_assignment = [(0, 1), (1, 0), (2, 2)]
    
    # Check that the result matches the expected assignment
    assert sorted(result) == sorted(expected_assignment)

def test_random_matrix():
    # Larger random matrix to test more complex scenarios
    np.random.seed(42)
    matrix_size = 5
    cost_matrix = np.random.randint(1, 100, size=(matrix_size, matrix_size))
    
    result = hungarian_algorithm(cost_matrix)
    
    # Verify basic properties of the result
    assert len(result) == matrix_size
    
    # Check that each worker and task is assigned exactly once
    rows, cols = zip(*result)
    assert len(set(rows)) == matrix_size
    assert len(set(cols)) == matrix_size

def test_single_element_matrix():
    # Test a 1x1 matrix
    cost_matrix = [[5]]
    result = hungarian_algorithm(cost_matrix)
    
    assert result == [(0, 0)]

def test_invalid_matrix_input():
    # Test various invalid input scenarios
    
    # Non-square matrix
    with pytest.raises(ValueError, match="Cost matrix must be a square matrix"):
        hungarian_algorithm([[1, 2], [3, 4], [5, 6]])
    
    # Non-numeric matrix
    with pytest.raises(ValueError, match="Input must be a valid matrix"):
        hungarian_algorithm([['a', 'b'], ['c', 'd']])
    
    # Empty matrix
    with pytest.raises(ValueError, match="Cost matrix must be a square matrix"):
        hungarian_algorithm([])

def test_zero_cost_matrix():
    # Matrix with all zeros
    cost_matrix = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    
    result = hungarian_algorithm(cost_matrix)
    
    # Verify that we get a valid assignment
    assert len(result) == 3
    rows, cols = zip(*result)
    assert len(set(rows)) == 3
    assert len(set(cols)) == 3

def test_large_cost_matrix():
    # Large matrix to test performance and correctness
    np.random.seed(42)
    matrix_size = 10
    cost_matrix = np.random.randint(1, 1000, size=(matrix_size, matrix_size))
    
    result = hungarian_algorithm(cost_matrix)
    
    # Verify basic properties of the result
    assert len(result) == matrix_size
    
    # Check that each worker and task is assigned exactly once
    rows, cols = zip(*result)
    assert len(set(rows)) == matrix_size
    assert len(set(cols)) == matrix_size