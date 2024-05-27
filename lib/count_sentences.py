#!/usr/bin/env python3

class MyString:
    def __init__(self, value = ''):
        self.value = value if isinstance(value, str) else ValueError("Value must be a string")

    def is_sentence(self):
        return True if self.value.endswith('.') else False

    def is_question(self):
        return True if self.value.endswith('?') else False

    def is_exclamation(self):
      return True if self.value.endswith('!') else False
    
    def count_sentences():
