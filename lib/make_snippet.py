def make_snippet(str):
    n = len(str.split())
    first_five = str.split()[:5]
    if n > 5:
        return " ".join(first_five) + "..."
    else:
        return str
    