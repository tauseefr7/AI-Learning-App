import random
import ast
import streamlit as st

def string_to_list(s):
    """
    Convert a string representation of a list into a Python list.
    If the string is not a valid list, an error message is displayed.
    """
    try:
        return ast.literal_eval(s)
    except (SyntaxError, ValueError) as e:
        st.error(f"""
        Error: Please check the provided input as it is incorrectly formatted. {e}
        
        Accepted input formats include:
        - List of integers: "[1, 2, 3]" 
        - List of floats: "[1.0, 2.0, 3.0]"
        - List of strings: "['a', 'b', 'c']"
        - List of booleans: "[True, False, True]"
        - List of None values: "[None, None, None]"
        - List of mixed types: "[1, 'a', True, 3.14, None]"
        - Nested lists: "[1, [2, 3], ['a', 'b']]"
        - List of tuples: "[(1, 2), (3, 4)]"
        - List of dictionaries: "[{'key1': 'value1'}, {'key2': 'value2'}]"
        
        Ensure the input string is properly formatted and represents a valid Python list.
        """)
        st.stop()

def get_randomized_options(options):
    """
    Randomize the order of a list of options and return the randomized list along with the original first option.
    
    Parameters:
    - options: list of options to randomize. The first option is considered the correct answer.
    
    Returns:
    - A tuple containing the randomized list and the original correct answer.
    """
    correct_answer = options[0]  # The first option is considered the correct answer
    random.shuffle(options)  # Randomize the order of options
    return options, correct_answer  # Return the randomized options and the correct answer
