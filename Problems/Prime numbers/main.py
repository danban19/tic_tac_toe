prime_numbers = [element for element in range(2, 1001) if not any([element1 for element1 in range(2, element) if element % element1 == 0])]
