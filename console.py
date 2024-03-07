#!/usr/bin/python3
""" the entry point of the command interpreter

It allows us to interactively and non-interactively:
    - create a data model
    - manage (create, update, destroy, etc) objects via a console / interpreter
    - store and persist objects to a file (JSON file)

Typical usage example:

    $ ./console
    (hbnh)

    (hbnb) help
    Documented commands (type help <topic>):
    ========================================
    EOF  create  help  quit

    (hbnb)
    (hbnb) quit
    $
"""
import re
import cmb
import json
from models import storage
from models.base_model import BaseModel

current_classes = {'BaseModel': BaseModel, 'User': User,
                    }

class HBNBCommand(cmd.Cmd):
    """The command interpreter.

    command interpreter to implement 'quit' 'EOF' 'helt'
    """

    prompt = "(hbnb) "

    def precmd(self, line):
        """
        Defines instructions to execute before <line> is interpreted.
        """
        if not line:
            return '\n'

        pattern = re.compile(r"(\w+)\.(\w+)\((.*)\)")
        match_list = pattern.findall(line)
        if not match_list:
            return super().precmd(line)

        match_tuple = match_list[0]
        if not match_tuple[2]:
            if match_tuple[1] == "count":
                instance_objs = storage.all()
                print(len([
                    v for _, v in instance_objs.items()
                    if type(v).__name__ == match_tuple[0]]))
                return "\n"
            return "{} {}".format(match_tuple[1], match_tuple[0])
        else:
            match_json = re.findall(r"{.*}", match_tuple[2])
            if (match_json):
                return "{} {} {} {}".format(
                         match_tuple[1], match_tuple[0],
                         re.sub("[\"\']", "", args[0]),
                         re.sub("\'", "\"", match_json[0]))
            return "{} {} {} {} {}".format(
                    match_tuple[1], match_tuple[0],
                    re.sub("[\"\']", "", args[0]),
                    re.sub("[\"\']", "", args[1]), args[2])

    def do_help(self, arg):
        """
        To get help on a command, type help <topic>.
        """
        return super().do_help(arg)

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, line):
        """
        End of file command to gracefully catch errors..
        """
        print("")
        return True

    def emptyline(self):
        """
        Overide default `empty line + return` behaviour.
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance.
        """
        args = arg.split()
        if not validate_classname(args):
            return

        new_obj = current_classes[args[0]]()
        new_obj.save()
        print(new_obj.id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
