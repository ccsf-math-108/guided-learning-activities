def generate_sequence():
    """
    Generate a 2-digit sequence from the digits 1, 2, 3, 4, 5, 6.
    
    Parameters:
    - None
    
    Returns:
    - A list representing the generated 2-digit sequence.
    """
    import random
    digits = [1, 2, 3, 4, 5, 6]
    evens = [2, 4, 6]
    weights = [0.1, 0.1, 0.3, 0.3, 0.1, 0.1]
    weights_evens = [0.3, 0.5, 0.2]
    
    first_digit = random.choices(digits, weights, k=1)[0]
    if first_digit % 2 == 0:
        second_digit = random.choices(digits, weights, k=1)[0]
    else:
        second_digit = random.choices(evens, weights_evens, k=1)[0]
    sequence = [first_digit, second_digit]
    
    return sequence