# command method
from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self, receiver):
        self.receiver = receiver
    @abstractmethod
    def execute(self):
        pass
    @abstractmethod
    def undo(self):
        pass


class TypeCommand(Command):
    def __init__(self, receiver, text):
        self.receiver = receiver
        self.text = text
        self.prev_state = None
    def execute(self):
        self.prev_state = self.receiver.document
        return self.receiver.type_text(self.text)
    def undo(self):
        self.receiver.document = self.prev_state
        return self.receiver.document


class DeleteCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver
        self.prev_state = None
    def execute(self):
        self.prev_state = self.receiver.document
        return self.receiver.delete_text()
    def undo(self):
        self.receiver.document = self.prev_state
        return self.receiver.document


class MacroCommand(Command):
    def __init__(self, commands):
        self.commands = commands
        self.receiver = None

    def execute(self):
        for cmd in self.commands:
            cmd.execute()
        return self.commands[-1].receiver.document

    def undo(self):
        for cmd in reversed(self.commands):
            cmd.undo()
        return self.commands[0].receiver.document


class Receiver:
    def __init__(self):
        self.document = ""
    def type_text(self, text):
        self.document += text
        return self.document
    def delete_text(self):
        self.document = self.document[:-1]
        return self.document


class Invoker:
    def __init__(self):
        self.commands = []
        self.poped_commands = []
    def execute(self, cmd):
        self.commands.append(cmd)
        self.poped_commands.clear()
        return cmd.execute()
    def undo(self):
        if not self.commands:
            print("Nothing to undo")
            return ""
        last_command = self.commands.pop()
        self.poped_commands.append(last_command)
        return last_command.undo()
    def redo(self):
        if not self.poped_commands:
            print("Nothing to redo")
            return ""
        last_command = self.poped_commands.pop()
        self.commands.append(last_command)
        return last_command.execute()


if __name__ == "__main__":
    receiver = Receiver()
    document = ""

    cmd = TypeCommand(receiver, "Hello")
    invoker = Invoker()
    document = invoker.execute(cmd)
    print(document)

    cmd = TypeCommand(receiver, ", world")
    document = invoker.execute(cmd)
    print(document)

    cmd = DeleteCommand(receiver)
    document = invoker.execute(cmd)
    print(document)

    document = invoker.undo()
    print(document)
    document = invoker.undo()
    print(document)
    document = invoker.undo()
    print(document)
    document = invoker.undo()

    document = invoker.redo()
    print(document)

    cmd1 = TypeCommand(receiver, "!!!")
    cmd2 = TypeCommand(receiver, " Welcome")
    macro = MacroCommand([cmd1, cmd2])
    document = invoker.execute(macro)
    print(document)
    document = invoker.redo()

    document = invoker.undo()
    print(document)