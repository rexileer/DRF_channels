from django.test import TestCase

from llm_logic import process_message

def test_process_message():
    user_input = "Hello, how are you?"
    response = process_message(user_input)
    assert response == "Echo: Hello, how are you?"
    print("Test passed!")
    
if __name__ == "__main__":
    test_process_message()
