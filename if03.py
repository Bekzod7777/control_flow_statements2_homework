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
        return a-c
    elif a>b and a>c and c>b:
        return a-b
    elif b>a and b>c and c<b:
        return b-c
    elif b>a and b>c and c>a:
        return b-c
    elif c>a and c>b and a<b:
        return c-a
    else:
        return c-b
print(main(5,5,5))