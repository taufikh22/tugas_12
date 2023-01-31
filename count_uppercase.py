def count_uppercase(string):
    count = 0
    for c in string:
        if c.isupper():
            count += 1
    return count