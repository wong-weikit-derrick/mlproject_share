def try_me(choice=None):
    if not choice:
        choice = input("Do you want to know the answer?")
    if choice == 'n':
        return 'Cool! Try on your own'
    elif choice == 'y': return 5
    else: return 'invalid choice'

if __name__ == '__main__':
    print(try_me('y'))
    print(try_me('n'))
    print(try_me())