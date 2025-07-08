import time

# دکوراتور محاسبه زمان اجرای تابع
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()          # شروع زمان
        result = func(*args, **kwargs)    # اجرای تابع اصلی
        end_time = time.time()            # پایان زمان
        elapsed = end_time - start_time   # زمان سپری شده
        print(f"زمان اجرای تابع: {elapsed:.6f} ثانیه")
        return result
    return wrapper

# تابع ساخت لیست 1 تا n
@timer_decorator
def create_list(n):
    return list(range(1, n+1))

# گرف
