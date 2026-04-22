def generate_learning_path(skill, level):
    paths = {
        "python": {
            "beginner": [
                "Learn basic syntax",
                "Variables and data types",
                "Loops and conditions",
                "Functions",
                "Simple projects (calculator, quiz)"
            ],
            "intermediate": [
                "OOP concepts",
                "File handling",
                "Modules & packages",
                "Working with APIs",
                "Mini projects"
            ],
            "advanced": [
                "Data structures",
                "Multithreading",
                "Web frameworks (Flask/Django)",
                "Machine Learning basics",
                "Build real-world projects"
            ]
        },
        "web development": {
            "beginner": [
                "HTML basics",
                "CSS styling",
                "JavaScript basics",
                "Build simple webpages"
            ],
            "intermediate": [
                "Responsive design",
                "JavaScript DOM",
                "APIs",
                "Version control (Git)"
            ],
            "advanced": [
                "React or Angular",
                "Backend (Node.js)",
                "Database (MongoDB/MySQL)",
                "Full-stack projects"
            ]
        }
    }

    skill = skill.lower()
    level = level.lower()

    if skill in paths and level in paths[skill]:
        return paths[skill][level]
    else:
        return ["No data available for this skill/level."]

# User Input
skill = input("Enter skill (Python/Web Development): ")
level = input("Enter level (Beginner/Intermediate/Advanced): ")

# Generate Path
learning_path = generate_learning_path(skill, level)

print("\n📚 Your Learning Path:")
for step in learning_path:
    print("👉", step)