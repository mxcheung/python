from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict, Any
import time

class ValidationRule:
    def __init__(self, name, func, message):
        self.name = name
        self.func = func
        self.message = message

    def validate(self, value):
        time.sleep(0.1)  # simulate work
        ok = self.func(value)
        return {
            "rule": self.name,
            "passed": ok,
            "message": None if ok else self.message
        }


class ParallelValidationEngine:
    def __init__(self, rules: Dict[str, List[ValidationRule]]):
        self.rules = rules

    def validate(self, data: Dict[str, Any], max_workers: int = 4):
        results = {field: [] for field in self.rules}
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = []
            for field, rules in self.rules.items():
                for rule in rules:
                    futures.append(
                        executor.submit(lambda f=field, r=rule: (f, r.validate(data.get(f))))
                    )

            for future in as_completed(futures):
                field, result = future.result()
                results[field].append(result)
        return results