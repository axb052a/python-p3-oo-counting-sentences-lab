#!/usr/bin/env python3

class MyString:
  
  def __init__(self, value = ""): # Gives it a value property and set it default value to an empty string
    self._value = value
    
  def get_value(self):
    return self._value

  def set_value(self, stringVal): # Verify the value is a string 
    if (type(stringVal) == str):
      self._value = stringVal
    else:
      print("The value must be a string.")

  value = property(get_value, set_value)

  def is_sentence(self): # Verifies True or False with the sentence have the correct punctuation 
    return self._value.endswith(".")

  def is_question(self):
    return self._value.endswith("?")

  def is_exclamation(self):
    return self._value.endswith("!")

  def count_sentences(self): 
    value = self.value
    for punc in ['!','?']: # Uses the string replace method to replace the punctuation with a "."
        value = value.replace(punc, '.')
    
    sentences = [s for s in value.split('.') if s] # Uses the string split method to split the string into a list
    
    return len(sentences) # Return the count of sentences 