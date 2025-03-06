import hyp.hyp as hyp
import numpy as np

def test_square():
    t = hyp.sq_oh(np.ones(1), np.ones(1))
    t_2 = np.ones(1, dtype=float)
    t_2[0] = 2
    np.testing.assert_array_almost_equal(t, t_2)
    
def test_sqrt():
    c = np.zeros(1, dtype=float)
    c[0] = 9
    t = hyp.sqrt_c(c)
    t_2 = np.zeros_like(t, dtype=float)
    t_2[0] = 3
    np.testing.assert_array_almost_equal(t,t_2 )

def test_integration():
    a = np.zeros(1)
    b = np.zeros(1)
    c2 = np.zeros(1)
    a[0] = 3
    b[0] = 4
    
    c = hyp.find_c(a,b)
    c2[0] = 5
    np.testing.assert_approx_equal(c, c2)