# Originally made by Mikhail Vorotnikov

def encoder(password):
    encoded_password = ''
    for i in password:
        encoded_password += str(int(i) + 3)
    return encoded_password

def decoder(encoded_password):
    decoded_password = ''
    for i in encoded_password:
        decoded_password += str(int(i) - 3)
    return decoded_password

def print_menu():
    print('''Menu
-------------
1. Encode
2. Decode
3. Quit\n''')

while True:
    print_menu()
    option = int(input('Please enter an option: '))

    if option == 1:
        password = input('Please enter your password to encode: ')
        encoded_password = encoder(password)
        print('Your password has been encoded and stored!\n')
    elif option == 2:
        decoded_password = decoder(encoded_password)
        print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}.')
    elif option == 3:
        exit()
    else:
        print('Wrong option. Please choose again!')








