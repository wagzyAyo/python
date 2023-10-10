import cmd


class Prompt(cmd.Cmd):

    def do_name(self):
        name = input("What is your name? ")
        print("Hello {} how are you doing today".format(name))
