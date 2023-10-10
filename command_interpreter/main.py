from command import Prompt

if __name__ == "__main__":
    name = Prompt()
    name.prompt = "$ "
    name.cmdloop("Welcome to the prompt type 'name' to enter your name")
