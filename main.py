from parser_packet import parse_hex_string
from parser_packet_translated import parse_hex_string_translated

def parse_and_display(hex_input):
    try:
        result = parse_hex_string(hex_input)
        for key, value in result.items():
            if isinstance(value, dict):
                print(f'{key}:')
                for sub_key, sub_value in value.items():
                    print(f'    {sub_key}: {sub_value}')
            else:
                print(f'{key}: {value}')
    except ValueError as e:
        print("Error:", e)

def parse_and_display_translated(hex_input):
    try:
        result = parse_hex_string_translated(hex_input)
        for key, value in result.items():
            if isinstance(value, dict):
                print(f'{key}:')
                for sub_key, sub_value in value.items():
                    if isinstance(sub_value, dict):
                        print(f'    {sub_key}:')
                        for inner_key, inner_value in sub_value.items():
                            print(f'        {inner_key}: {inner_value}')
                    else:
                        print(f'    {sub_key}: {sub_value}')
            else:
                print(f'{key}: {value}')
    except ValueError as e:
        print("Error:", e)

def main():
    while True:
        print("\nChoose an option:")
        print("1. Parse packet and display fields")
        print("2. Parse packet and display translated fields")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            hex_input = input("Enter the packet to parse (or 'exit' to quit): ")
            if hex_input.lower() == 'exit':
                break
            parse_and_display(hex_input)
        elif choice == '2':
            hex_input = input("Enter the packet to parse (or 'exit' to quit): ")
            if hex_input.lower() == 'exit':
                break
            parse_and_display_translated(hex_input)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
