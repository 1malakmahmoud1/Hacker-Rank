def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")

if _name_ == '_main_':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)