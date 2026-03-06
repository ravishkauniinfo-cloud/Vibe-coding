def get_valid_marks(subject):
    """Get valid marks for a subject (0-100)."""
    while True:
        try:
            marks = float(input(f"Enter marks for {subject} (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print(f"\033[91mError: Marks must be between 0 and 100. Please try again.\033[0m")
        except ValueError:
            print(f"\033[91mError: Please enter a valid number.\033[0m")


def get_letter_grade(average):
    """Get letter grade based on average."""
    if average >= 75:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 40:
        return "C"
    else:
        return "F"


def main():
    # ANSI color codes
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"
    
    print(f"{CYAN}{'='*50}")
    print(f"{'GRADE CALCULATOR':^50}")
    print(f"{'='*50}{RESET}")
    
    # Get student name
    name = input(f"\n{CYAN}Enter student's name: {RESET}")
    
    # Get marks for each subject
    print(f"\n{CYAN}Enter marks for each subject (0-100):{RESET}")
    math_marks = get_valid_marks("Mathematics")
    science_marks = get_valid_marks("Science")
    english_marks = get_valid_marks("English")
    
    # Calculate average
    average = (math_marks + science_marks + english_marks) / 3
    letter_grade = get_letter_grade(average)
    
    # Determine pass/fail
    status = "PASS" if average >= 40 else "FAIL"
    status_color = GREEN if average >= 40 else RED
    
    # Display results
    print(f"\n{CYAN}{'='*50}")
    print(f"{'RESULT':^50}")
    print(f"{'='*50}{RESET}")
    
    print(f"\n{CYAN}Student Name:{RESET} {name}")
    print(f"\n{CYAN}Subject Marks:{RESET}")
    print(f"  Mathematics: {math_marks:.2f}")
    print(f"  Science: {science_marks:.2f}")
    print(f"  English: {english_marks:.2f}")
    
    print(f"\n{CYAN}Average:{RESET} {average:.2f}")
    print(f"{CYAN}Letter Grade:{RESET} {letter_grade}")
    
    print(f"\n{status_color}Status: {status}{RESET}")
    print(f"\n{CYAN}{'='*50}{RESET}")


if __name__ == "__main__":
    main()
