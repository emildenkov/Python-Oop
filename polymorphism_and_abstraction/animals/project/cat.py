from project.animal import Animal


class Cat(Animal):

    @staticmethod
    def make_sound() -> str:
        return "Meow meow!"

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"
    