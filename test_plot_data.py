import unittest
import plot_data 
import numpy as np
from numpy import array
import pandas as pd
# the input object should be numpy.ndarray type
a = np.array([[1,1,5],[2,2,4],[3,3,3],[4,4,2],[5,5,1]])
[m,n] = a.shape
anor = [[1,1/5,5/5],[2,2/5,4/5],[3,3/5,3/5],[4,4/5,2/5],[5,5/5,1/5]]
print(m,n)
a_calculated = plot_data.normalization(m,n,a).tolist()
print(type(a_calculated),a_calculated)
class testnormalization(unittest.TestCase):
        #self.assertEqual(plot_data.normalization(m,n,a),[[1,1/5,5/5],[2,2/5,4/5],[3,3/5,3/5],[4,4/5,2/5],[5,5/5,1/5]])
    # assert is to compare true or false of the argument follows it    
    def test_equal(self):      
        self.assertEqual(a_calculated,anor)   
if __name__ == '__main__':
    unittest.main()
  # = means assign the value, == means compare 