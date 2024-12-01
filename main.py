from parser import (
    parse_hex_string,
    parse_hex_string_gt06,
    parse_hex_string_translated,
    parse_hex_string_translated_gt06
)

from utils.util import display_parsed_packet

def parse_and_display(hex_input, parser_function, translated=False):

    try:
        result = parser_function(hex_input)
        display_parsed_packet(result, translated)
    except ValueError as e:
        print("Error:", e)

def sub_menu():

    while True:
        print("\nChoose an option:")
        print("1. Parse packet and display fields")
        print("2. Parse packet and display translated fields")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice in {'1', '2'}:
            hex_input = input("Enter the packet to parse (or 'exit' to quit): ")
            if hex_input.lower() == 'exit':
                break
            if choice == '1':
                parser = parse_hex_string
                translated = False
            else:
                parser = parse_hex_string_translated
                translated = True
            parse_and_display(hex_input, parser, translated)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def sub_menu_gt06():

    while True:
        print("\nChoose an option:")
        print("1. Parse packet and display fields")
        print("2. Parse packet and display translated fields")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice in {'1', '2'}:
            hex_input = input("Enter the packet to parse (or 'exit' to quit): ")
            if hex_input.lower() == 'exit':
                break
            if choice == '1':
                parser = parse_hex_string_gt06
                translated = False
            else:
                parser = parse_hex_string_translated_gt06
                translated = True
            parse_and_display(hex_input, parser, translated)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

def main_menu():

    while True:
        print("\nChoose an option:")
        print("1. Parse packet GTK Lite 4G")
        print("2. Parse packet GTK LW 4G")
        print("3. Parse packet GTK OBD 4G")
        print("4. Parse packet Generic GPS TRACKER")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice in {'1', '4'}:
            sub_menu_gt06()
        elif choice in {'2', '3'}:
            sub_menu()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main_menu()
