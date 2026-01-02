#Student Result Evaluation System (Function-Driven)

def calculate_percentage(marks):
    """
    Takes a dictionary of subject marks
    Returns percentage
    """
    if not marks:
        return 0

    total = sum(marks.values())
    percentage = total / len(marks)
    return percentage


def assign_grade(percentage):
    """
    Assigns grade based on percentage
    """
    if percentage >= 80:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "Fail"


def is_pass(marks, pass_mark=40):
    """
    Checks if student passed all subjects
    """
    for score in marks.values():
        if score < pass_mark:
            return False
    return True


def generate_result(name, marks):
    """
    Main function that combines all logic
    """
    percentage = calculate_percentage(marks)
    grade = assign_grade(percentage)
    passed = is_pass(marks)

    return {
        "name": name,
        "percentage": round(percentage, 2),
        "grade": grade,
        "passed": passed
    }


# -------------------- Function Usage --------------------

student_marks = {
    "Physics": 72,
    "Chemistry": 65,
    "Math": 81
}

result = generate_result("Riya", student_marks)

print("Student Result")
print("Name:", result["name"])
print("Percentage:", result["percentage"])
print("Grade:", result["grade"])
print("Passed:", result["passed"])
