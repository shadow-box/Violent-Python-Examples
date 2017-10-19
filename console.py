import cmd, sys

#
#Place imports for functions here. Call them in the do_ functions
#
class Console(cmd.Cmd):
    intro = 'Welcome to console.py... Type help or ? for a list of commands.\n'
    prompt = 'console> '
    file = None

    def do_hello(self, args):
        #"""Says hello. If you provide a name, it will greet you with it."""
        if len(args) == 0:
            name = 'stranger'
        else:
            name = args
        print "Hello, %s" % name

    def do_quit(self, args):
        #"""Quits the program."""
        print "Quitting."
        raise SystemExit
        
    def do_help(self, args):
        if len(args) == 0:
            f = open('help.txt', 'r')
            f.open
            for line in f:
                print(line, end=' ')
            f.close()
        else:
            
            


if __name__ == '__main__':
    prompt.prompt = '> '
    Console().cmdloop('Welcome to ')
