from random import randint
import random
def main():
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

    def is_prime(number):
        if number < 2:  
            return False
        for i in range(2, number): 
            if number % i == 0:  
                return False
        return True  
    def prime_list():
        for num in range(1,100):
            if is_prime(num): 
                print(num)
    def game_rand_num():
        num = randint(1,100)
        guess = False
        while(guess!=True):
            user_number = int(input('Enter your number please: '))
            if (user_number > num):
                print("your number is too high, try again")
            elif (user_number < num):
                print("your number is too low, try again")
            else:
                guess = True
                print('you molodec')

    def r_p_s():
        options = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
        win_logic = {'r': 's', 'p': 'r', 's': 'p'}  
        won = False
        
        while not won:
            comp_option = random.choice(list(options.keys()))
            user_option = input("Enter your option (r for rock, p for paper, s for scissors): ").lower()

            if user_option not in options:
                print("Invalid option. Please choose 'r', 'p', or 's'.")
                continue  

            print(f"Computer chose: {options[comp_option]}")

            if comp_option == user_option:
                print("It's a tie, try again.")
            elif win_logic[comp_option] == user_option:
                print("Computer won!")
                won = True
            else:
                print("You won!")
                won = True


        
    # odd_number()
    # prime_list()
    # print(is_prime(4))
    # game_rand_num()
    # r_p_s()
    
if __name__ == '__main__':
    main()