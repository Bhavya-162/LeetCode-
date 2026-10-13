class Solution:
    def isNumber(self, s: str) -> bool:
        # State tracking flags
        seen_digit = False
        seen_dot = False
        seen_exponent = False
        
        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
                
            elif char in ('+', '-'):
                # Signs can only appear at the very beginning of the string
                # or immediately following an exponent character 'e' or 'E'
                if i > 0 and s[i - 1] not in ('e', 'E'):
                    return False
                    
            elif char in ('e', 'E'):
                # Exponents can only appear once and MUST be preceded by at least one digit
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                # Reset digit flag because an integer must follow the exponent
                seen_digit = False
                
            elif char == '.':
                # Dots can only appear once and CANNOT appear after an exponent
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
                
            else:
                # Any other character (like alphabets or special symbols) makes it invalid
                return False
                
        # The string is valid only if it ends with a valid digit sequence
        return seen_digit
