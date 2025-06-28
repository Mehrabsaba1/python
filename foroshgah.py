amount = int(input())
if amount > 50000:
    final_amount = amount * 0.8  
elif amount >= 20000:
    final_amount = amount * 0.9  
else:
    final_amount = amount        
print(int(final_amount))
