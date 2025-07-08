def pick_evens(*args):
    return [num for num in args if num % 2 == 0]

input_str = input()

try:
    numbers = [int(x) for x in input_str.strip().split()]
    evens = pick_evens(*numbers)
    print(evens)
except ValueError:
    print("خطا: لطفاً فقط عدد صحیح وارد کنید.")
