from tasks import add

result = add.delay(4, 6)  # Task chaqirilmoqda
print("Task yuborildi, natija kutilmoqda...")
print(result.wait(timeout=10))  # 10 bo‘lishi kerak
