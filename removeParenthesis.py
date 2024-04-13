import logging
import re
class RemoveParenthesis:
    logging.basicConfig(level=logging.DEBUG) 
    def ignore_text_in_parentheses(text):
        """
        Ignore text within parentheses in a given string if parentheses are present.

        Args:
            text (str): The input string.

        Returns:
            str: The modified string with text within parentheses removed (if found).
        """
        # Define a regular expression pattern to match text within parentheses
        pattern = r'\([^)]*\)'  # Matches anything within parentheses
        
        # Use re.sub to replace text within parentheses with an empty string
        modified_text = re.sub(pattern, '', text)
        
        return modified_text.strip()

    # Example usage:
    #input_text_1 = "Shimizu Station (Shizuoka Prefecture)"
    #input_text_2 = "Tokyo Station"

    #result_1 = ignore_text_in_parentheses(input_text_1)
    #result_2 = ignore_text_in_parentheses(input_text_2)

    #print("Original Text 1:", input_text_1)
    #print("Modified Text 1:", result_1)

    #print("Original Text 2:", input_text_2)
    #print("Modified Text 2:", result_2)