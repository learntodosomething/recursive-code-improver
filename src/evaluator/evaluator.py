def evaluate_code(code: str, tests: list) -> dict:
    local_vars = {}
    
    try:
        exec(code, {}, local_vars)
    except Exception as e:
        return {
            "success": False,
            "score": 0,
            "passed": 0,
            "total": len(tests),
            "error": f"Syntax/Runtime error during definition: {str(e)}"
        }

    # Megkeressük a függvényt
    func = None
    for value in local_vars.values():
        if callable(value):
            func = value
            break

    if func is None:
        return {
            "success": False,
            "score": 0,
            "passed": 0,
            "total": len(tests),
            "error": "Nem található függvény a kódban"
        }

    passed = 0
    errors = []

    for i, test in enumerate(tests):
        try:
            result = func(test["input"])
            if result == test["expected"]:
                passed += 1
            else:
                errors.append(f"Test {i+1}: expected {test['expected']}, got {result}")
        except Exception as e:
            errors.append(f"Test {i+1}: Exception: {str(e)}")

    score = passed / len(tests)

    return {
        "success": passed == len(tests),
        "score": score,
        "passed": passed,
        "total": len(tests),
        "errors": errors
    }