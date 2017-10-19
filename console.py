import cmd, sys, os

#
#Place imports for functions here. Call them in the do_ functions
#

class Console(cmd.Cmd):
    intro = 'Welcome to console.py... Type help or ? for a list of commands.\n'
    prompt = 'console> '
    file = None

    def do_shell(self, args):
        """Pass shell commands.
        Syntax: shell <command> OR ! <command>"""
        if len(args) == 0:
            print('Please pass a shell command to execute')
        else:
            command = args
            os.system(command)

    def do_quit(self, args):
        """Quits the program."""
        print('Quitting.')
        raise SystemExit
    
    def emptyline(self):
        pass
    
if __name__ == '__main__':
    Console().cmdloop('Welcome to ')
