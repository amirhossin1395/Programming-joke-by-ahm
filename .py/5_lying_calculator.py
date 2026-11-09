import random

print("--- ماشین حساب فوق پیشرفته AHM ---")
print("(نتیجه ممکنه درست نباشه! 😂)\n")

while True:
    try:
        num1 = float(input("عدد اول: "))
        num2 = float(input("عدد دوم: "))
        # نتیجه رو تصادفی اشتباه نشون میده
        fake_result = num1 + num2 + random.randint(-100, 100)
        print(f"نتیجه: {fake_result}\n")
    except ValueError:
        print("لطفا عدد وارد کن!\n")