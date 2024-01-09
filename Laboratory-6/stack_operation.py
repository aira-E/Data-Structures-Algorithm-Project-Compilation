from os import system

def Stack(): 
    items = []
    return items

def empty(items):
    return not items

def push(items, item):
    items.append(item)

def pop(items):
    if not empty(items):
        return items.pop()

def display(items):
    if not empty(items):
        print(*items, sep=', ')
    else:
        print('Stack Underflow!')

def main():
    stack = Stack()
    choice = ''
    while choice != '4':
        system('cls')
        print("My Stack Menu\n1. Push\n2. Pop\n3. Display Stack Contents\n4. Exit\n-----------")
        choice = input("Choice: ")

        if choice == '1':
            num = int(input('Enter the Number you want to be pushed into the stack: '))
            push(stack, num)
            print(f"The Number {num} is pushed on the stack")
            system('pause')

        elif choice == '2':
            print(f"The Popped Element is {pop(stack)}")
            system('pause')

        elif choice == '3':
            print(f"The contents of the stack is:")
            display(stack)
            system('pause')
        elif choice == '4':
            print("goodbye!")
            system('pause')
        else:
            print("Invalid input!")
            system('pause')

if __name__ == "__main__":
    main()


