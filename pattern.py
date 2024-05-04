def print_right_triangle(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

if __name__ == "__main__":
    rows = int(input("Enter the number of rows: "))
    print("Printing Right Triangle Pattern:")
    print_right_triangle(rows)



def print_left_triangle(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        print("*" * i)

if __name__ == "__main__":
    rows = int(input("Enter the number of rows: "))
    print("Printing Left Triangle Pattern:")
    print_left_triangle(rows)



def print_pyramid(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * i)

if __name__ == "__main__":
    rows = int(input("Enter the number of rows: "))
    print("Printing Pyramid Pattern:")
    print_pyramid(rows)



def print_diamond(rows):
    # Upper triangle
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * i)

    # Lower triangle
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i) + "* " * i)

if __name__ == "__main__":
    rows = int(input("Enter the number of rows: "))
    print("Printing Diamond Pattern:")
    print_diamond(rows)



def print_hollow_diamond(rows):
    # Upper triangle
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "* " * i)

    # Lower triangle
    for i in range(rows - 1, 0, -1):
        print(" " * (rows - i) + "* " * i)

if __name__ == "__main__":
    rows = int(input("Enter the number of rows: "))
    print("Printing Hollow Diamond Pattern:")
    print_hollow_diamond(rows)




def print_alphabet_pattern(rows):
    for i in range(1, rows + 1):
        current_char = 65  # ASCII value of 'A'
        for j in range(1, i + 1):
            print(chr(current_char), end=" ")
            current_char += 1
        print()

if __name__ == "__main__":
    rows = int(input("Enter the number of rows: "))
    print("Printing Alphabet Pattern:")
    print_alphabet_pattern(rows)




def print_number_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

if __name__ == "__main__":
    rows = int(input("Enter the number of rows: "))
    print("Printing Number Pattern:")
    print_number_pattern(rows)




