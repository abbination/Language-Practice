#Lay the groundwork for inserting new vocabularly words
#TO DO: set up database and an etl pipeline
class Vocabulary:
    def __init__ (self, vocab, meaning):
        self.vocab = vocab
        self.meaning = meaning

class Verb (Vocabulary):
    def __init__ (self, vocab, meaning, is_irregular):
        super().__init__(vocab, meaning)
        self.is_irregular = is_irregular

class Noun:
    def __init__ (self, vocab, meaning, gender):
        super().__init__(vocab, meaning)
        self.gender = gender

class Adjective:
    def __init__ (self, vocab, meaning):
        super().__init__(vocab, meaning)

class Adverb:
    def __init__ (self, vocab, meaning):
        super().__init__(vocab, meaning)

class Adverb:
    def __init__ (self, vocab, meaning):
        super().__init__(vocab, meaning)

class Preposition:
    def __init__ (self, vocab, meaning):
        super().__init__(vocab, meaning)

class Phrase:
    def __init__ (self, vocab, meaning):
        super().__init__(vocab, meaning)
