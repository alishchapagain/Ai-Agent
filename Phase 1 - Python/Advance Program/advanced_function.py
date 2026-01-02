#Advanced Function-Based Student Result System


def validate_marks(marks):
    """
    Ensures marks are valid integers between 0 and 100
    """
    if not isinstance(marks, dict):
        raise ValueError("Marks must be a dictionary")

    for subject, score in marks.items():
        if not isinstance(score, int):
            raise ValueError(f"Invalid score type in {subject}")
        if score < 0 or score > 100:
            raise ValueError(f"Score out of range in {subject}")

    return True


def calculate_percentage(marks):
    return sum(marks.values()) / len(marks)


def assign_grade(percentage):
    if percentage >= 80:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 40:
        return "C"
    else:
        return "Fail"


def generate_result(name, marks):
    validate_marks(marks)

    percentage = calculate_percentage(marks)
    grade = assign_grade(percentage)

    passed = all(score >= 40 for score in marks.values())

    return {
        "name": name,
        "percentage": round(percentage, 2),
        "grade": grade,
        "passed": passed
    }


def save_result_to_file(result, filename="results.txt"):
    with open(filename, "a") as file:
        file.write(
            f"{result['name']}, "
            f"{result['percentage']}, "
            f"{result['grade']}, "
            f"{result['passed']}\n"
        )


def read_results_from_file(filename="results.txt"):
    results = []
    try:
        with open(filename, "r") as file:
            for line in file:
                results.append(line.strip())
    except FileNotFoundError:
        return []

    return results


# -------------------- Program Execution --------------------

student_marks = {
    "Physics": 78,
    "Chemistry": 69,
    "Math": 85
}

try:
    result = generate_result("Alish", student_marks)
    save_result_to_file(result)

    print("Result saved successfully.")
    print("Generated Result:", result)

except ValueError as error:
    print("Error:", error)


print("\nPrevious Results:")
for record in read_results_from_file():
    print(record)
