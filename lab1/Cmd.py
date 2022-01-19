from cmd import Cmd
import os, sys

class MyPrompt(Cmd):

    def do_hello(self, args):
        """Says hello. If you provide a name, it will greet you with it."""
        if len(args) == 0:
            name = 'stranger'
        else:
            name = args
    
        print ("Hello, %s" % name)

    def do_list(self, args):
        """List all directories."""
        path = '.'
        if len(sys.argv) == 2:
            path = sys.argv[1]
            files = os.listdir(path)
        else:
            files = os.listdir(path)

        for name in files:
            print(name)


    def do_quit(self, args):
        """Quits the program."""
        print("Quitting.")
        raise SystemExit



if __name__ == '__main__':
    prompt = MyPrompt()
    prompt.prompt = '> '
    prompt.cmdloop('Starting prompt...')

