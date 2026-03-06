def get_positive_number(prompt):
    """Get a positive number input from user."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("\033[91mError: Please enter a positive number.\033[0m")
                continue
            return value
        except ValueError:
            print("\033[91mError: Please enter a valid number.\033[0m")


def main():
    # ANSI color codes
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"
    
    print(f"{CYAN}{'='*50}")
    print(f"{'MONTHLY BUDGET TRACKER':^50}")
    print(f"{'='*50}{RESET}\n")
    
    # Task 01: Get total monthly budget
    print(f"{CYAN}Step 1: Enter Your Total Monthly Budget{RESET}")
    total_budget = get_positive_number(f"{CYAN}Enter total monthly budget (LKR): {RESET}")
    
    print(f"\n{CYAN}Step 2: Enter Your Expenses{RESET}")
    print(f"{CYAN}(Type 'done' when finished entering expenses){RESET}\n")
    
    # Task 03: Allow multiple expenses until user types "done"
    expenses = []
    expense_count = 1
    
    while True:
        try:
            expense_input = input(f"{CYAN}Enter expense #{expense_count} (or 'done' to finish): {RESET}")
            
            # Check if user wants to stop
            if expense_input.lower() == "done":
                if len(expenses) == 0:
                    print(f"{YELLOW}Please enter at least one expense.{RESET}")
                    continue
                break
            
            # Validate expense amount
            expense_amount = float(expense_input)
            if expense_amount < 0:
                print(f"{RED}Error: Expense cannot be negative. Please try again.{RESET}")
                continue
            
            expenses.append(expense_amount)
            expense_count += 1
            
        except ValueError:
            print(f"{RED}Error: Please enter a valid number or type 'done'.{RESET}")
    
    # Task 01: Calculate total expenses and remaining balance
    total_expenses = sum(expenses)
    remaining_balance = total_budget - total_expenses
    
    # Display results
    print(f"\n{CYAN}{'='*50}")
    print(f"{'BUDGET SUMMARY':^50}")
    print(f"{'='*50}{RESET}\n")
    
    print(f"{CYAN}Total Monthly Budget:{RESET} {total_budget:.2f} LKR")
    
    print(f"\n{CYAN}Expenses:({RESET}{len(expenses)} expense(s))")
    for i, expense in enumerate(expenses, 1):
        print(f"  Expense {i}: {expense:.2f} LKR")
    
    print(f"\n{CYAN}Total Expenses:{RESET} {total_expenses:.2f} LKR")
    print(f"{CYAN}Remaining Balance:{RESET} {remaining_balance:.2f} LKR")
    
    # Task 02: Add warning message if balance < 500 LKR
    if remaining_balance < 500:
        print(f"\n{RED}⚠️  WARNING: Low Funds ⚠️{RESET}")
        print(f"{RED}Your remaining balance is below 500 LKR!{RESET}")
    else:
        print(f"\n{GREEN}✓ Good Balance{RESET}")
    
    print(f"\n{CYAN}{'='*50}{RESET}")


if __name__ == "__main__":
    main()
