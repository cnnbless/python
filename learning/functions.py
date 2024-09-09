from random import randint

def odd_number():
    numbers = []
    parni_nums = []
    neparni_nums = []
    
    for _ in range(100): 
        numbers.append(randint(-10, 10))
    
    for num in numbers:  
        if num % 2 == 0:  
            parni_nums.append(num)
        else:  
            neparni_nums.append(num)
        
    print(f"list = {numbers} \nparni numbers: {parni_nums}\nneparni nums: {neparni_nums}")

odd_number()
