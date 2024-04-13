class BeforeLCB:
    def get_text_before_last_slash(input_string):
        """
        Extracts the substring before the last occurrence of '/' in the input string.

        Args:
            input_string (str): The input string.

        Returns:
            str: The substring before the last '/' character.
        """
        # Find the index of the last occurrence of '/'
        last_slash_index = input_string.rfind('/')
        
        if last_slash_index != -1:
            # Extract substring before the last '/'
            return input_string[:last_slash_index]
        else:
            # If '/' is not found, return the original string
            return input_string

# Example usage:
#input_string = "/shizuoka/ct_ma60000/tw_sa99127/sc_st04661/?lcb=320112"



# Example usage:
#url = "/shizuoka/ct_ma60000/tw_sa99127/sc_st04661/?lcb=320112"
#query_param = "?lcb=320112"

#result_before = BeforeLCB.get_text_before_last_slash(url)
#print("Part before ?lcb=320112:", result_before)
