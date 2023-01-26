
def isnumber(possibleNumber: str) -> bool:
    """I have no idea why this ain't a thing yet..."""

    try:
        float(possibleNumber)
    except:
        return False
    else:
        return True

def popString(string: str) -> str:
    """As if you could use .pop() in strings"""

    string = string[:-1]
    return string