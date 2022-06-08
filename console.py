#!/usr/bin/python3

"""
Defines a class HBNBCommand(cmd.Cmd)
"""

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    def do_greet(self, line):
        print("Hello there")

    def do_EOF(self, line):
        """
        Used to exit the program
        """
        return True

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
