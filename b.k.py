a = int(input())
b = int(input())

def is_greater(a, b):
    if a > b :
        return True
    elif b >= a :
        return False


print(is_greater(a, b))