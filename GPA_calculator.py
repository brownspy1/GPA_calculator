print("""┃┏┓┃━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┏┛┃━
┃┗┛┗┓┏━┓┏━━┓┏┓┏┓┏┓┏━┓━┏━━┓┏━━┓┏┓ ┏┓┗┓┃
┃┏━┓┃┃┏┛┃┏┓┃┃┗┛┗┛┃┃┏┓┓┃━━┫┃┏┓┃┃┃ ┃┃ ┃┃
┃┗━┛┃┃┃━┃┗┛┃┗┓┏┓┏┛┃┃┃┃┣━━┃┃┗┛┃┃┗━┛┃┏┛┗┓
┗━━━┛┗┛━┗━━┛━┛┗┛┗━┛┗┛┗┗━━┛ ┗━━┛┗━━┛┗━━┛""")

while True:
    try:
        GPA = float(input('Input your Marks: '))

        if GPA >= 80 and GPA <= 100:
            print(f'Your Marks are {GPA} And you Got A+')
        elif GPA >= 70 and GPA <= 79:
            print(f'Your Marks are {GPA} And you Got A')
        elif GPA >= 60 and GPA <= 69:
            print(f'Your Marks are {GPA} And you Got A-')
        elif GPA >= 50 and GPA <= 59:
            print(f'Your Marks are {GPA} And you Got B')
        elif GPA >= 40 and GPA <= 49:
            print(f'Your Marks are {GPA} And you Got C')
        elif GPA >= 33 and GPA <= 39:
            print(f'Your Marks are {GPA} And you Got D')
        elif GPA >= 0 and GPA <= 32:
            print(f'Sorry, you have failed. Your marks: {GPA}')
        else:
            print(f'Error: Invalid GPA value entered: {GPA}')

        restart = input('Do you want to use the program again? (Y/N): ')
        if restart.lower() != 'y':
            print('Thanks for using this program. Program owned by M. Mahadi.')
            break
    except ValueError:
        print('Invalid input. Please enter a valid number for your GPA.')
