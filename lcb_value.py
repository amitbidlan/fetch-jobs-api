class LCB_Value:
    @staticmethod
    def extract_lcb_substring(input_string):
        # Find the index of the substring '?lcb='
        start_index = input_string.find('?lcb=')

        if start_index != -1:
            # Extract the substring from '?lcb=' to the end of the input string
            lcb_substring = input_string[start_index + len('?lcb='):]
            return lcb_substring
        else:
            return None  # Return None if the substring '?lcb=' is not found
