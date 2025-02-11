class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"{self.name}: {self.score}"

    def __eq__(self, other):
        return self.score == other.score

    def __lt__(self, other):
        return self.score < other.score

    def __gt__(self, other):
        return self.score > other.score


def bubble_sort(students):
    n = len(students)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if students[j] > students[j + 1]:
                students[j], students[j + 1] = students[j + 1], students[j]
                swapped = True
        if not swapped:
            break
    return students


def get_user_input():
    while True:
        try:
            num_students = int(input("Enter the number of students: "))
            if num_students <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    students = []
    for i in range(num_students):
        name = input(f"Enter the name of student {i + 1}: ")
        while True:
            try:
                score = int(input(f"Enter the score of student {i + 1}: "))
                if score < 0:
                    print("Score cannot be negative.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a non-negative integer.")
        students.append(Student(name, score))
    return students


def main():
    print("Student Score Tracker")
    print("--------------------------------------------------------------------------------------------------------------------------------------------")
    students = get_user_input()
    print("\nUnsorted:")
    for student in students:
        print(student)
    sorted_students = bubble_sort(students)
    print("\nSorted by Score (Highest to Lowest):")
    for student in sorted_students:
        print(student)
    print(f"\nTop Performer: {sorted_students[0].name} with a score of {sorted_students[0].score}")
    print(f"\nLowest Performer: {sorted_students[-1].name} with a score of {sorted_students[-1].score}")


if __name__ == "__main__":
    main()