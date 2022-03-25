def main(n):
    """
    Find the index of the largest digit of the five-digit number.
    Args:
        n: Five-digit number.
    Returns:
        int: return answer.
    """
    besh=n%10
    tort=n//10
    tort1=tort%10
    uch=tort//10
    uch1=uch%10
    ikki=uch//10
    ikki1=ikki%10
    bir=ikki//10
    if besh>=tort1 and besh>=uch1 and besh>=ikki1 and besh>=bir:
        return 1
    elif tort1>=besh and tort1>=uch1 and tort1>=ikki1 and tort1>=bir:
        return 2
    elif uch1>=besh and uch1>=tort1 and uch1>=ikki1 and uch1>=bir:
        return 3
    elif ikki1>=besh and ikki1>=tort1 and ikki1>=uch1 and ikki1>=bir:
        return 4
    else:
        return 5
