import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR))

from assignments.problem01.p1 import run as p1
from assignments.problem02.p2 import run as p2
from assignments.problem03.p3 import run as p3
from assignments.problem04.p4 import run as p4

def main():
    problems = {
        "1": {"name": "Problem 01: Remove scanner beep", "func": p1},
        "2": {"name": "Problem 02: Find the hidden message", "func": p2},
        "3": {"name": "Problem 03: Produce images by exchanging magnitudes & phases", "func": p3},
        "4": {"name": "Problem 04: Produce hybrid image", "func": p4},
### 5, 6 to be added later.... if god wills it
    }

    print("="*45)
    print("   FOURIER PROJECT UTILITY   ")
    print("="*45)
    print("Available Questions:")
    for key, info in problems.items():
        print(f" [{key}] {info['name']}")
    print(" [A] Run All")
    print(" [Q] Quit")
    print("-"*45)

    choice = input("Enter the question number to run: ").strip().upper()

    if choice == 'Q':
        print("Exiting...")
        return

    if choice == 'A':
        for key in problems:
            execute_problem(problems[key])
    elif choice in problems:
        execute_problem(problems[choice])
    else:
        print(f"Error: '{choice}' is not a valid question number.")

def execute_problem(problem_info):
    print(f"\n>>> Executing: {problem_info['name']}...")
    try:
        problem_info['func']()
        print(f">>> Success! Check the 'output/' folder.")
    except Exception as e:
        print(f">>> [ERROR] {e}")

if __name__ == "__main__":
    main()



