def decimal_to_roman(decimal):
    """
    Convert a decimal number to its Roman numeral representation.
    
    Args:
        decimal: An integer between 1 and 3999, inclusive.
        
    Returns:
        A string representing the Roman numeral.
        
    Raises:
        ValueError: If decimal is outside the valid range (1-3999).
        TypeError: If decimal is not an integer.
    """
    # Type checking
    if not isinstance(decimal, int):
        raise TypeError("Input must be an integer")
    
    # Range checking
    if decimal < 1 or decimal > 3999:
        raise ValueError("Input must be between 1 and 3999")
    
    # Mapping of decimal values to Roman numerals
    roman_map = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    
    result = ""
    
    # Convert decimal to Roman numeral
    for value, numeral in roman_map:
        while decimal >= value:
            result += numeral
            decimal -= value
    
    return result