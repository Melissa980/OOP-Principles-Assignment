# Task 1: Define Budget Category Class

class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name  # Private attribute for category name
        self.__allocated_budget = allocated_budget  # Private attribute for allocated budget
        self.__remaining_budget = allocated_budget  # Track remaining budget

    # Task 2: Implement Getters and Setters
    
    # Getter for category name
    def get_category_name(self):
        return self.__category_name

    # Setter for category name
    def set_category_name(self, new_name):
        if isinstance(new_name, str) and new_name.strip():
            self.__category_name = new_name
        else:
            print("Invalid category name.")

    # Getter for allocated budget
    def get_allocated_budget(self):
        return self.__allocated_budget

    # Setter for allocated budget
    def set_allocated_budget(self, new_budget):
        if isinstance(new_budget, (int, float)) and new_budget > 0:
            self.__allocated_budget = new_budget
            self.__remaining_budget = new_budget  # Reset remaining budget when re-allocating
        else:
            print("Budget must be a positive number.")

    # Task 3: Add Budget Functionality
    
    def add_expense(self, amount):
        """Subtract expense from the remaining budget if valid."""
        if isinstance(amount, (int, float)) and amount > 0:
            if amount <= self.__remaining_budget:
                self.__remaining_budget -= amount
                print(f"Expense of {amount} added to {self.__category_name}. Remaining budget: {self.__remaining_budget}")
            else:
                print(f"Insufficient budget. You have only {self.__remaining_budget} left.")
        else:
            print("Expense amount must be a positive number.")

    # Task 4: Display Budget Details
    
    def display_category_summary(self):
        """Display the category summary including name, allocated, and remaining budget."""
        print(f"Category: {self.__category_name}")
        print(f"Allocated Budget: {self.__allocated_budget}")
        print(f"Remaining Budget: {self.__remaining_budget}")


# Demonstration script

# Create a BudgetCategory instance for food
food_category = BudgetCategory("Food", 500)

# Add an expense
food_category.add_expense(100)

# Display the category summary
food_category.display_category_summary()

# Try updating the category name
food_category.set_category_name("Groceries")
food_category.display_category_summary()

# Try adding an expense that exceeds the remaining budget
food_category.add_expense(450)

# Update the allocated budget and display the summary again
food_category.set_allocated_budget(700)
food_category.display_category_summary()
