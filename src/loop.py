from tasks.format_number import TASK as FORMAT_NUMBER_TASK
from generator.llm_generator import generate_code
from evaluator.evaluator import evaluate_code

# Itt választod ki, melyik feladatot futtatod
CURRENT_TASK = FORMAT_NUMBER_TASK


MAX_ITERATIONS = 10


def main():
    print(f"Feladat: {CURRENT_TASK['name']}")
    print(f"Leírás: {CURRENT_TASK['description']}\n")

    previous_code = None
    errors = None
    result = None
    iteration = 0

    for iteration in range(1, MAX_ITERATIONS + 1):
        print(f"=== {iteration}. próbálkozás ===")
        print("Kód generálása...")
        code = generate_code(
            CURRENT_TASK["description"],
            previous_code=previous_code,
            errors=errors,
            attempt=iteration,
        )

        # Ha a modell szó szerint ugyanazt a kódot adja vissza, mint az előző
        # körben, helyi minimumban ragadt - a további próbálkozások valószínűleg
        # ugyanezt ismételnék, ezért itt megállunk.
        if previous_code is not None and code.strip() == previous_code.strip():
            print("\n⚠️  A modell szó szerint ugyanazt a kódot generálta, mint előző körben.")
            print("Helyi minimumban ragadt, megszakítom a ciklust a felesleges ismétlés helyett.\n")
            break

        print("\nGenerált kód:")
        print("-" * 40)
        print(code)
        print("-" * 40)

        print("\nKiértékelés...")
        result = evaluate_code(code, CURRENT_TASK["tests"])

        print(f"\nEredmény: {result['passed']}/{result['total']} teszt sikeres")
        print(f"Score: {result['score']:.2f}")

        if result.get("errors"):
            print("\nHibák:")
            for err in result["errors"]:
                print(f"  - {err}")

        if result["success"]:
            print(f"\n✅ Sikerült a(z) {iteration}. próbálkozásra!\n")
            return

        previous_code = code
        errors = result.get("errors")
        print()

    if result is not None:
        print(f"❌ {iteration} próbálkozás után nem sikerült minden tesztet teljesíteni.")
        print(f"Legjobb elért score: {result['score']:.2f}")


if __name__ == "__main__":
    main()