from command import Prompt


name = Prompt()
name.prompt = "$ "
name.cmdloop("Welcome to the prompt type 'name' to enter your name")
