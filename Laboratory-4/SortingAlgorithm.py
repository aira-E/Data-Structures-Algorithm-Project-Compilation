# Program starts here
def main():
    
    while True:
        print("""
        ******** SORTING ALGORITHM APPLICATION ********
        *\t\tProgrammed by: Aira Estur\t*\n  *\t\t BSCOE 2-1 \t\t\t*
        *\t\t\t\t\t\t*
        *\t\t<<< M A I N  Μ Ε Ν U >>>\t*
        *\t\t\t\t\t\t*
        *\t\t(1) SELECTION SORTING\t\t*
        *\t\t(2) BUBBLE SORTING\t\t*
        *\t\t(3) INSERTION SORTING\t\t*
        *\t\t(4) MERGE SORTING\t\t*
        *\t\t(5) EXIT\t\t\t*
        *\t\t\t\t\t\t*
        """)
            
        option = int(input("\nSelect an option: "))
        if option == 1:
            user_input = list(map(str, input("\nEnter the list of comma-separated values: ").split(",")))
            selection_sort(user_input)
        elif option == 2:
            user_input = list(map(str, input("\nEnter the list of comma-separated values: ").split(",")))
            bubble_sort(user_input)
        elif option == 3:
            user_input = list(map(str, input("\nEnter the list of comma-separated values: ").split(",")))
            insertion_sort(user_input)
        elif option == 4:
            user_input = list(map(str, input("\nEnter the list of comma-separated values: ").split(",")))
            choice4(user_input)
        elif option == 5:
            exit()
        else:
            print("\nError")

# Function that performs selection sorting
def selection_sort(user_input):
    try:
        choice1 = (int(input("\nHow many elements are there on your list: ")))
        choice2 = (int(input("\n(1) INTEGER\n(2) LETTER\nEnter type of element: ")))
        choice3 = (int(input("\n(1) ASCENDING\n(2) DESCENDING\n(3) ALPABETICALLY\nEnter sorting mode: ")))
        print("\nUnsorted list:", user_input)
        if choice3 == 1 or choice3 == 3:
            for i in range(len(user_input)):
                min_idx = i
                for j in range(i + 1, len(user_input)):
                    if user_input[min_idx] > user_input[j]:
                        min_idx = j
                user_input[i], user_input[min_idx] = user_input[min_idx], user_input[i]
                print("\nPass", i + 1, ":", user_input)
            print("\nSorted list:", user_input)
        elif choice3 == 2:
            for i in range(len(user_input)):
                min_idx = i
                for j in range(i + 1, len(user_input)):
                    if user_input[min_idx] < user_input[j]:
                        min_idx = j
                user_input[i], user_input[min_idx] = user_input[min_idx], user_input[i]
                print("\nPass", i + 1, ":", user_input)
            print("\nSorted list:", user_input)
    except ValueError:
        print("\nError. Please enter only integers.")
        selection_sort(user_input)

# Function that performs bubble sorting
def bubble_sort(user_input):
    try:
        choice1 = (int(input("\nHow many elements are there on your list: ")))
        choice2 = (int(input("\n(1) INTEGER\n(2) LETTER\nEnter type of element: ")))
        choice3 = (int(input("\n(1) ASCENDING\n(2) DESCENDING\n(3) ALPABETICALLY\nEnter sorting mode: ")))
        if choice3 == 1 or choice3 == 3:
            for i in range(len(user_input)):
                for j in range(0, len(user_input) - i - 1):
                    if user_input[j] > user_input[j + 1]:
                        user_input[j], user_input[j + 1] = user_input[j + 1], user_input[j]
                        print("\nPass", i + 1, ":", user_input)
            print("\nSorted list:", user_input)
        elif choice3 == 2:
            for i in range(len(user_input)):
                for j in range(0, len(user_input) - i - 1):
                    if user_input[j] < user_input[j + 1]:
                        user_input[j], user_input[j + 1] = user_input[j + 1], user_input[j]
                        print("\nPass", i + 1, ":", user_input)
            print("\nSorted list:", user_input)
    except ValueError:
        print("\nError. Please enter only integers.")
        bubble_sort(user_input)

# Function that performs insertion sorting
def insertion_sort(user_input):
    try:
        choice1 = (int(input("\nHow many elements are there on your list: ")))
        choice2 = (int(input("\n(1) INTEGER\n(2) LETTER\nEnter type of element: ")))
        choice3 = (int(input("\n(1) ASCENDING\n(2) DESCENDING\n(3) ALPABETICALLY\nEnter sorting mode: ")))
        if choice3 == 1 or choice3 == 3:
            for i in range(1, len(user_input)):
                key = user_input[i]
                j = i - 1
                while j >= 0 and key < user_input[j]:
                    user_input[j + 1] = user_input[j]
                    j -= 1
                user_input[j + 1] = key
                print("\nPass", i, ":", user_input)
            print("\nSorted list:", user_input)
        elif choice3 == 2:
            for i in range(1, len(user_input)):
                key = user_input[i]
                j = i - 1
                while j >= 0 and key > user_input[j]:
                    user_input[j + 1] = user_input[j]
                    j -= 1
                user_input[j + 1] = key
                print("\nPass", i, ":", user_input)
            print("\nSorted list:", user_input)
    except ValueError:
        print("\nError. Please enter only integers.")
        insertion_sort(user_input)

def choice4(user_input):
    choice1 = (int(input("\nHow many elements are there on your list: ")))
    choice2 = (int(input("\n(1) INTEGER\n(2) LETTER\nEnter type of element: ")))
    choice3 = (int(input("\n(1) ASCENDING\n(2) DESCENDING\n(3) ALPABETICALLY\nEnter sorting mode: ")))
    if choice3 == 1 or choice3 == 3:
        merge_sort_ascending(user_input)
    elif choice3 == 2:
        merge_sort_descending(user_input)

# Function that performs merge sorting
def merge_sort_ascending(user_input):
    try:
        print("\nUnsorted list:", user_input)
        if len(user_input) > 1:
            mid = len(user_input) // 2
            left = user_input[:mid]
            right = user_input[mid:]

            merge_sort_ascending(left)
            merge_sort_ascending(right)

            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    user_input[k] = left[i]
                    i += 1
                else:
                    user_input[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                user_input[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                user_input[k] = right[j]
                j += 1
                k += 1
            print("\nPass", k, ":", user_input)
        print("\nSorted list:", user_input)        

    except ValueError:
        print("\nError. Please enter only integers.")
        merge_sort_ascending(user_input)

# Function that performs merge sorting
def merge_sort_descending(user_input):
    try:
        print("\nUnsorted list:", user_input)
        if len(user_input) > 1:
            mid = len(user_input) // 2
            left = user_input[:mid]
            right = user_input[mid:]

            merge_sort_descending(left)
            merge_sort_descending(right)

            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] > right[j]:
                    user_input[k] = left[i]
                    i += 1
                else:
                    user_input[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                user_input[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                user_input[k] = right[j]
                j += 1
                k += 1
            print("\nPass", k, ":", user_input)
        print("\nSorted list:", user_input)
    except ValueError:
        print("\nError. Please enter only integers.")
        merge_sort_descending(user_input)

main()