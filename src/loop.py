from tasks.sum_list import TASK
from generator.llm_generator import generate_code
from evaluator.evaluator import evaluate_code

def main():
    print(f"Feladat: {TASK['name']}")
    print(f"Leírás: {TASK['description']}\n")

    print("Kód generálása...")
    code = generate_code(TASK["description"])
    print("\nGenerált kód:")
    print("-" * 40)
    print(code)
    print("-" * 40)

    print("\nKiértékelés...")
    result = evaluate_code(code, TASK["tests"])

    print(f"\nEredmény: {result['passed']}/{result['total']} teszt sikeres")
    print(f"Score: {result['score']:.2f}")

    if result.get("errors"):
        print("\nHibák:")
        for err in result["errors"]:
            print(f"  - {err}")

if __name__ == "__main__":
    main()