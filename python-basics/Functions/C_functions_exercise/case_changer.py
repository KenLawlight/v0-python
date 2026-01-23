def case_change(text, to_upper):
    return text.upper() if to_upper else text.lower()

print(case_change("Super", True))
print(case_change("Super", False))
print(case_change("tAmBourine", True))
print(case_change("tAmBourine", False))
