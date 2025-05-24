checklist = [
    "Check for open directories",
    "Test for Cross-Site Scripting (XSS)",
    "Check authentication mechanisms",
    "Try SQL Injection on inputs",
    "Look for exposed sensitive files",
    "Test for security misconfigurations",
    "Check for sensitive data leaks",
]

def run_checklist():
    print("\n=== Manual Bug Hunting Checklist ===")
    for i, item in enumerate(checklist, 1):
        input(f"{i}. {item} — Press Enter when done...")
    print("Checklist complete! Proceed with detailed manual testing.\n")
