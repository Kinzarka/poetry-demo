# Создайте любой класс с произвольным количеством подклассов, экземпляров, атрибутов и методов
# как минимум один атрибут должен быть с уровнем доступа private. Соответственно, для получания значений этого атрибута
# нужно использовать методы get и set

class Human():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def speak(self, name):
        return print("I`m a {}.".format(name))

class Tester(Human):

    def __init__(self, name, age, sex, language):
        super().__init__(name, age, sex,)
        self.__language = language

    def test(self):
        return print("I do-do-doooo.")

    def get_language(self):
        return print("My language is {}.".format(self.__language))

    def set_language(self, newlang):
        self.__language = newlang

tester1 = Tester("Peter","31","Male","Russian")
tester1.speak("Tester")
tester1.test()
tester1.get_language()
tester1.set_language("English")
tester1.get_language()



