class Parent:
    def show_message(self):
        print("Hello from the Parent class!")

class Child(Parent):
    def show_message(self):
        # Call the show_message() method from the Parent class
        super().show_message()
        print("Hello from the Child class!")

# Create an instance of the Child class
piyush = Child()
piyush.show_message()
