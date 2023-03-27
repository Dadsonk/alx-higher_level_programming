#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
<<<<<<< HEAD
            result += a ** b / i
        except Exception:
            result = b + a
            break
    return result
=======
            else:
                result += (a ** b) / i
        except Exception:
            result = b + a
            break
    return (result)
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
