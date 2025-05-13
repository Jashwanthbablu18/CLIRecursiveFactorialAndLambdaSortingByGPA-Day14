# Day 14 - Lambda & Recursion
# Topic: Recursive Factorial + Lambda Sorting by GPA

# Recursive function to calculates n factorial
# if n is 0 or 1 then it returns 1 due to factorial of them is 1.
# else it calls itself recursively n - 1 times and multiplying factorial of n - 1 with n and continues till n is 0 or 1. 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Lambda function to sort a list of dictionaries based on GPA
# This uses sorted() to sort elements, the lambda function, lambda x: x['GPA'] extracts GPA from each dictionary. reverse = true displays GPA's in  descending order.
def sort_students_by_gpa(students):
    return sorted(students, key=lambda x: x['GPA'], reverse = True)

# This Function to represent introduction of this assignment / Project. Starting with a little welcome message.
def show_intro():
    print("🧠 Welcome to Day 14 - Lambda & Recursion")
    print("🔹 Topic: Recursive Factorial & Sorting with Lambda\n")


# main
def main():

    # Calling show_intro() to display introduction
    show_intro()
    
    # calls factorial() to find factorial of 1
    num = 1
    print(f"🎯 Factorial of {num}: {factorial(num)}")
          
    # calls factorial() to find factorial of 3
    num = 3
    print(f"🎯 Factorial of {num}: {factorial(num)}")
    
    # calls factorial() to find factorial of 5
    num = 5
    print(f"🎯 Factorial of {num}: {factorial(num)}")
    
    # calls factorial() to find factorial of 9
    num = 9
    print(f"🎯 Factorial of {num}: {factorial(num)}")
    
    # calls factorial() to find factorial of 10
    num = 10
    print(f"🎯 Factorial of {num}: {factorial(num)}")

    # This is a list of students dictionaries with their names and GPA's
    students = [
        {"name": "Jashwanth", "GPA": 69},
        {"name": "Navadeep", "GPA": 95},
        {"name": "Ayaan", "GPA": 98},
        {"name": "Narsimha", "GPA": 90}
    ]
    
    
    # Displays sorted students by passing the above students list into sort_students_by_gpa()
    print("\n🎓 Students sorted by GPA (Descending):")
    sorted_students = sort_students_by_gpa(students)

    # This one displays the sorted students list after sorting with name and gpa.
    for student in sorted_students:
        print(f"{student['name']} - GPA: {student['GPA']}")


# Starting point: The script is designed to run when executed directly. The conditional if __name__ == "__main__": main() ensures that main() is called only when the script is run as a standalone program, not when imported as a module.
if __name__ == "__main__":
    main()

