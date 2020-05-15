students = [["Will", "B"], ["Kate", "B"], ["Max", "A"],
            ["Elsa", "C"], ["Alex", "B"], ["Chris", "A"]]

print([grade[0] for grade in students if grade[1] == "A"])