def txttolist(filename):
    """Takes a txt file and makes a list with each line being an element"""
    return [line.split("\n")[0] for line in open(filename, "r")]

def isstrlessthan(string, length):
    """Checks if string is below length"""
    return len(string) < length
