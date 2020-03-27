import math
def is_square(n):
    if (n < 0 ):
        return False
    square_root = math.sqrt(n)
    mini = int(square_root)
    return (mini **2 == n)
