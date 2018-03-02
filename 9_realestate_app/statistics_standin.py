def mean(data):
    total = float(0)
    count = 0
    for x in data:
        count += 1
        total += x
    return total / max(1, count)