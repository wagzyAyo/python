import cmd


class Prompt(cmd.Cmd):

    def do_name(self, arg):
        """Set users name"""
        name = input("What is your name? ").title()
        print("Hello {} how are you doing today".format(name))

    def do_EOF(self, arg):
        """Return true and close the prompt"""

        return True

    # def complete_name(self, text, arg, begidx, endidx):
    #    """ Auto complete names """

    #    if not text:
    #       comp = self.NAMES[:]
    #   else:
    #        comp = [f for f in self.NAMES if f.startswith(text)]

    #   return comp
