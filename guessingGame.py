from random import randint

def user_input():
    return int(input('Enter Number: '))


def computer_num():
    return randint(1,10)

def main():
    num1 = computer_num()
    num2 = user_input()
    if  num1 == num2:
        print("You WON")
    if num1 > num2:
        print('Too less')
        main()
    elif num1 < num2:
        print('Too much')
        main()

if __name__ == '__main__':
    main()
    option = str(input("Wanna play again? (Y/n)")).lower()
    if option == 'y': main()
    elif option == 'n': exit()