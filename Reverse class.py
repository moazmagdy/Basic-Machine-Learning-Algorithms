"""
This class reverse a sentence by word.

"""
class reverse:
    def __init__(self, text):
        self.text = text
        
    def  operation(self): 
        reverse_order = ' '.join(reversed(self.text.split()))
        print(reverse_order)