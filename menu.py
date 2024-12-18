menu = ['fries', 'sandwich', 'cheeseburger', 'coffee', 'soda']

print("Welcome to our restaurant ! Here's our menu :")
for i, item in enumerate(menu):
    print(f"{i}: {item}")

while True:
    user_input = input("\nEnter your number corresponding to your choice (or type 'quit' to exit): ")

    if user_input.lower() == 'quit':
        print("Thank for you visiting! Goodbye!") 
        break

    try:
        choice = int(user_input)
        
        if 0 <= choice < len(menu):
            print(f"\nYou have choosen: {menu[choice]}")
            print("Thanks for your order!")
            break
        else:
            print("Item not found. Please choose a valid number from the menu")
    except ValueError:
        print("Invalid input. Please enter a number or type 'quit' to exit")
    except IndexError:
        print("Item not found. Please choose a valid from the menu")