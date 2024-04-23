# TODO-1: add convert_to_letter_grade(score) function
    
def convert_to_letter_grade(score):
    if not type(score) is int:
        raise TypeError("Score must be a numeric value.")
    
    elif score > 100 or score < 0:
        raise ValueError("Score must be between 0 and 100.")
    
    elif score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
