import cmd
from base import BaseModel


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """close The console"""
        return True

    def do_create(self, arg):
        """Create new instance of BaseModel, save it and print the instance.id"""
        if not arg:
            print("** class name missing **")

        try:
            class_name = arg
            new_instance = eval(class_name)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
