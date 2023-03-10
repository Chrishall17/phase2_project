class GrammarStats:
    def __init__(self):
        self.total = 0
        self.true = 0


    def check(self, text):
        if text == "":
            raise Exception("Cannot validate empty text")
        if text[0].isupper() and text[-1] in ".!?":
            self.total += 1
            self.true += 1
            return True
        else:
            self.total += 1
            return False
        
    

    def percentage_good(self):
        return (self.true/self.total) * 100