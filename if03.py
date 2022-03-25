def main(a,b,c):
    
    """
    Determine the number between large and small.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a>b and a>c and c<b:
        return b
    elif a>b and a>c and c>b:
        return c
    elif b>a and b>c and c<b:
        return a
    elif b>a and b>c and c>a:
        return c
    elif c>a and c>b and a<b:
        return b
    else:
        return a
