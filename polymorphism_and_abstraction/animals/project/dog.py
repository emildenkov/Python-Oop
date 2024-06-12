from project.animal import Animal


class Dog(Animal):

    @staticmethod
    def make_sound() -> str:
        return "Woof!"

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"