def sum_numbers(*args):
    for arg in args:
        if not isinstance(arg, (int, float)):
            raise ValueError(f"ورودی نامعتبر: {arg} (باید عدد باشد)")
    return sum(args)

# گرفتن ورودی از کاربر
input_str = input("لطفاً اعداد را با فاصله وارد کنید: ")

# تبدیل ورودی به لیست اعداد
try:
    numbers = [float(x) if '.' in x else int(x) for x in input_str.strip().split()]
    result = sum_numbers(*numbers)
    print(result)
except ValueError as e:
    print(e)
