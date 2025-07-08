def skyline(*args):
    if not args:
        return 0
    return max(args)

# گرفتن ورودی از کاربر
input_str = input()

try:
    # تبدیل ورودی به لیست اعداد صحیح
    heights = [int(x) for x in input_str.strip().split()]
    
    # فراخوانی تابع
    tallest = skyline(*heights)
    
    # نمایش خروجی
    print(tallest)
except ValueError:
    print("خطا: لطفاً فقط عدد صحیح وارد کنید.")
