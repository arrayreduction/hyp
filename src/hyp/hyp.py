'''Code for training day
Vectorised hypotenuse calculation.  In two steps for no real reason'''

import numpy as np

def sq_oh(a : np.ndarray, b : np.ndarray) -> np.ndarray:
    c2 = a**2 + b**2
    
    return c2
    
def sqrt_c(c2 : np.ndarray) -> np.ndarray:
    return c2**0.5

def find_c(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    c = sq_oh(a,b)
    c = sqrt_c(c)
    
    return c