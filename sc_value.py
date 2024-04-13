import re

class SC_Value:
    @staticmethod
    def extract_numeric_after_alphabetic_prefix(segment):
        # Use regular expression to match the first numeric sequence after alphabetic characters
        match = re.search(r'[a-zA-Z]+(\d+)', segment)
        
        if match:
            # Extract the numeric part from the matched substring
            numeric_part = match.group(1)
            return numeric_part
        else:
            return None

    @staticmethod
    def extract_value_by_index(input_string):
        # Split the input_string into segments based on the '/' delimiter
        segments = input_string.split('/')
        
        # Check if the index is within the valid range of segments
        if len(segments) > 3:  # Ensure there are enough segments (0-indexed)
            # Get the segment at index 3 (4th segment in 0-indexed), which is 'tw_st03636'
            value = segments[3]
            print("value:",value)
            numeric_part = SC_Value.extract_numeric_after_alphabetic_prefix(value)  # Corrected method call

            return numeric_part
        else:
            return None  # Return None if the index is out of range

