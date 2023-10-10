import cmd


class Prompt(cmd.Cmd):

    def do_name(self, arg):
        """Set users name"""
        name = input("What is your name? ").title()
        print("Hello {} how are you doing today".format(name))

    def do_EOF(self, line):
        """Return true and close the prompt"""
        return True
