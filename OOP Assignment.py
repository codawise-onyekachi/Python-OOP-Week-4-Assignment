"""
Create a Python class named Person.
The Person class should have the following attributes:
name: representing the person's name.
age: representing the person's age.
gender: representing the person's gender.
Implement a method called introduce that prints a message introducing the person with their name, age, and gender.
Create an instance of the Person class and call the introduce method to display the person's information.
Create a GitHub repository for your assignment and submit the link."""

class Person:
    #name = "Mark"
    #age = 40
    #gender = "Male"

    def Introduce(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        print("May I introduce Mr.", name,'to you all. He is', age, 'years old, and he is a', gender, 'gender')


person = Person()

person.Introduce(name="Mark", age= 40, gender="male")
#person.name
#person.age
#print(person.gender)

#print(Person.Introduce("Mark", 40, "Male"))