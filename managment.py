from food import MENU_ITEMS, Hall

def get_int_input(prompt: str, min_val: int, max_val: int) -> int:
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a number between {min_val} and {max_val}")
        except ValueError:
            print("Invalid input. Please enter a number.")

def add_food(table):
    print("\n1: Main Dishes")
    print("2: Extras")
    choice_type = get_int_input("Choose menu type (1 or 2): ", 1, 2)
    
    category = "Main" if choice_type == 1 else "Extra"
    items = [item for item in MENU_ITEMS if item.category == category]
    
    print(f"\n{category} Dishes:")
    for idx, item in enumerate(items, 1):
        print(f"{idx}: {item.name} - {item.price} EGP")
    
    item_choice = get_int_input("Choose item number: ", 1, len(items)) - 1
    selected = items[item_choice]
    
    table.add(selected.name, selected.price)
    print(f"Added: {selected.name} - {selected.price} EGP")

def main():
    print("\n=== Welcome to the Restaurant ===\n")
    
    halls = [Hall(i) for i in range(1, 5)]
    
    for hall in halls:
        print(f"| Hall: {hall.number} |")
    
    hall_num = get_int_input("\nEnter Hall Number (1-4): ", 1, 4) - 1
    hall_obj = halls[hall_num]
    
    print(f"\n=== Hall: {hall_obj.number} ===")
    for table in hall_obj.tables:
        print(f"| Table: {table.number} |")
        
    table_num = get_int_input("\nEnter Table Number (1-5): ", 1, 5) - 1
    table_obj = hall_obj.tables[table_num]
    
    while True:
        print("\n--- Actions ---")
        print("1. Add Food")
        print("2. View Order")
        print("3. Checkout")
        print("4. VIP Mode (10% Off)")
        print("5. Exit")
        
        action = get_int_input("Enter Action: ", 1, 5)
        
        if action == 1:
            add_food(table_obj)
        elif action == 2:
            print(table_obj)
        elif action == 3:
            table_obj.check()
        elif action == 4:
            table_obj.vip = True
            print("✨ VIP Mode Activated! 10% discount applied.")
        elif action == 5:
            print("Thank you for visiting. Goodbye! 👋")
            break

if __name__ == "__main__":
    main()