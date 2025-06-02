class StudentGradeTracker:

    def __init__(self):
        self.Students = {}

    def add_student(self, Name, English, Urdu, Math, Science):

        self.Students.update(
            {Name: {"English": English, "Urdu": Urdu, "Math": Math, "Science": Science}}
        )

        print(f"\n{Name} added successfully!")

    def delete_student(self, Name):

        if Name in self.Students:
            del self.Students[Name]

            print(f"\n{Name} deleted successfully!")

        else:
            print(f"\n{Name} not found!")

    def average_marks(self, top_n=3):
        average = []

        for name, subjects in self.Students.items():

            if subjects:

                total = sum(subjects.values())
                count = len(subjects.values())

                avg = total / count

                average.append((name, avg))

        sorted_avg = sorted(
            average, key=lambda x: x[1], reverse=True
        )  # x[0] : the name (e.g., "Ali")  x[1] : the average marks (e.g., 33.0)

        print(f"\nTop {top_n} Students:")

        for name, avg in sorted_avg[:top_n]:
            print(f"\n{name} : {avg:.2f}")

    def update_marks(self, name):

        if name in self.Students:
            subject = (
                input("\nWhich subject marks you want to update: ").strip().title()
            )

            if subject in self.Students[name]:
                new_marks = int(input("\nEnter new marks for the subject: "))

                self.Students[name][subject] = new_marks

                print(f"\n{name}'s {subject} marks updated successfully!")

            else:
                print("\nSubject not found!")

        else:
            print(f"\n{name} not found!")