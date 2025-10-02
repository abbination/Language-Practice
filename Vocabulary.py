#Lay the groundwork for inserting new vocabularly words
#TO DO: set up database and an etl pipeline
class Vocabulary:
    __slots__ = ("vocab", "meaning")
    
    def __init__ (self, vocab, meaning):
        self.vocab = vocab
        self.meaning = meaning


class Verb (Vocabulary):
    __slots__ = ("is_irregular",)
    
    def __init__ (self, vocab, meaning, is_irregular):
        super().__init__(vocab, meaning)
        self.is_irregular = is_irregular


class Noun:
    __slots__ = ("gender",)
    
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
