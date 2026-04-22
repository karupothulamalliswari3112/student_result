# Advanced Student Result Management System
def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"

def get_valid_marks(subject):
    while True:
        try:
            marks = int(input(f"Enter marks for {subject} (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("❌ Marks must be between 0 and 100.")
        except:
            print("❌ Please enter a valid number.")

students = []

while True:
    print("\n===== Student Result Management System =====")
    print("1. Add Student")
    print("2. View Results")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")

        marks = []
        for i in range(3):
            m = get_valid_marks(f"Subject {i+1}")
            marks.append(m)

        total = sum(marks)
        avg = total / 3
        grade = calculate_grade(avg)

        students.append({
            "name": name,
            "marks": marks,
            "total": total,
            "average": avg,
            "grade": grade
        })

        print(f"✅ {name}'s data added successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("⚠️ No student data available.")
        else:
            print("\n--- Student Results ---")

            topper = students[0]

            for s in students:
                print("\n------------------------")
                print("Name:", s["name"])
                print("Marks:", s["marks"])
                print("Total:", s["total"])
                print("Average:", round(s["average"], 2))
                print("Grade:", s["grade"])

                if s["total"] > topper["total"]:
                    topper = s

            print("\n🏆 Topper:", topper["name"], "-", topper["total"], "marks")

            # Save to file
            with open("results.txt", "w") as f:
                for s in students:
                    f.write(f"{s['name']} | Total: {s['total']} | Grade: {s['grade']}\n")

            print("\n💾 Results saved to results.txt")

    elif choice == "3":
        print("👋 Exiting program...")
        break

    else:
        print("❌ Invalid choice. Try again.")
        