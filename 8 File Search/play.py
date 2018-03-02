
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n -1)

print("5!={:,}, 3!={:,}, 11!={:,}".format(
    factorial(5),
    factorial(3),
    factorial(11)
))

def fibanocci(limit):
    nums = []
    current=0
    next = 1

    while current < limit:
        current, next = next, next + current
        nums.append(current)
    return nums
print('via lists')
for n in fibanocci(100):
    print(n, end=', ')
print()


def fibanocci_co():
    current=0
    next = 1

    while True:
        current, next = next, next + current
        yield current

print('via yield')
for n in fibanocci_co():
    if n > 1000:
        break
    print(n, end='\n')