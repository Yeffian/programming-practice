class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self):
        return (self.draft - (self.crew * 1.5)) > 20

s = Ship(100, 20)
print(s.is_worth_it())