class Command:

    def executive(self):
        pass


class Submit(Command):

    def execute(self):
        print("Your work has been submitted!")


class Release(Command):

    def execute(self):
        print("Your work has been released to the printer!")


class JoinQueue(Command):

    def execute(self):
        print("Your work has joined the buffer queue!")


class Print(Command):

    def execute(self):
        print("Your job has been printed!")


class Macro:

    def __init__(self):
        self.commands = []

    def add(self, command):
        self.commands.append(command)

    def execute(self):
        for command in self.commands:
            command.execute()


if __name__ == "__main__":
    submit = Submit()
    release = Release()
    queue = JoinQueue()
    print = Print()

    macro = Macro()
    macro.add(submit)
    macro.add(release)
    macro.add(queue)
    macro.add(print)

    macro.execute()