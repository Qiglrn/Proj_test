import pytest
import plot_data 
import numpy as np

a = np.array([[1,2,3,4,5],[5,4,3,2,1]])
[m,n] = a.shape
print(a,m,n)
def test_nrmlizatn():
    """test of function normalization"""
    assert plot_data.normalization(n,a) == ([[1/5,2/5,3/5,4/5,5/5],[5/5,4/5,3/5,2/5,1/5]])
    # assert is to compare true or false of the argument follows it
    # = means assign the value, == means compare 