def add_expense():
    try:
        category = input("Enter category (Food/Travel/etc.): ")
        amount = float(input("Enter amount: "))

        with open("expenses.txt", "a") as file:
            file.write(f"{category},{amount}\n")

        print("Expense added successfully!\n")

    except ValueError:
        print("Invalid amount! Please enter a number.\n")


def view_expenses():
    try:
        with open("expenses.txt", "r") as file:
            print("\n--- All Expenses ---")
            for line in file:
                category, amount = line.strip().split(",")
                print(f"Category: {category} | Amount: ₹{amount}")
            print()

    except FileNotFoundError:
        print("No expenses found. File does not exist.\n")


def calculate_total():
    total = 0
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                _, amount = line.strip().split(",")
                total += float(amount)

        print(f"\nTotal Expense: ₹{total}\n")

    except FileNotFoundError:
        print("No expenses found. File does not exist.\n")


def category_count():
    counts = {}
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                category, _ = line.strip().split(",")
                counts[category] = counts.get(category, 0) + 1

        print("\n--- Category-wise Count ---")
        for category, count in counts.items():
            print(f"{category}: {count}")
        print()

    except FileNotFoundError:
        print("No expenses found. File does not exist.\n")



while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Category-wise Count")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        calculate_total()
    elif choice == "4":
        category_count()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.\n")