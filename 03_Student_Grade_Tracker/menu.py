import StudentGradeTracker as sgt
from time import sleep

tracker = sgt.StudentGradeTracker()


def get_mark(subject):
    while True:
        try:
            mark = int(input(f"\nEnter marks for {subject}: "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("\nMarks must be between 0 and 100.")
        except ValueError:
            print("\nPlease enter a valid integer for marks.")


def menu():
    while True:
        sleep(1)

        print("\nWelcome to Student Grade Tracker\n")

        print(
            """
            1.Add stydent
            2.Delete student
            3.Average marks
            4.Update marks
            5.Quit the program    
            """
        )

        try:
            choice = int(input("Enter your choice: "))

        except ValueError:
            print("\nEnter a numeric value!")
            continue

        if choice == 1:
            name = input("\nEnter the student name: ")

            print()

            eng = get_mark("English")
            urdu = get_mark("Urdu")
            math = get_mark("Math")
            sci = get_mark("Science")

            tracker.add_student(name, eng, urdu, math, sci)

        elif choice == 2:
            del_name = input("\nEnter the student name you want to remove: ")

            tracker.delete_student(del_name)

        elif choice == 3:
            tracker.average_marks()

        elif choice == 4:
            update_name = input(
                "\nEnter the name of the student whoose marks you want to update: "
            )
            tracker.update_marks(update_name)

        elif choice == 5:
            print("\nExiting the program\n")
            break

        else:
            print("\nInvalid choice! Choose from the given choices.")