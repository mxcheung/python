class ValidationFilterChain:
    def __init__(self, validators):
        self.validators = validators

    def get_applicable_validators(self, data):
        """Return only validators where is_applicable() is True."""
        return [v for v in self.validators if v.is_applicable(data)]

    def run(self, data, parallel=False):
        applicable = self.get_applicable_validators(data)
        results = []

        if parallel:
            from concurrent.futures import ThreadPoolExecutor, as_completed
            with ThreadPoolExecutor() as executor:
                futures = [executor.submit(v.validate, data) for v in applicable]
                for f in as_completed(futures):
                    results.append(f.result())
        else:
            for v in applicable:
                results.append(v.validate(data))

        return results