import time
from abc import ABC, abstractmethod

class User:
    def __init__(self, name):
        self.name = name
        self.email_enabled = True
        self.sms_enabled = False
        self.push_enabled = True


class Order:
    def __init__(self, order_id, user):
        self.order_id = order_id
        self.user = user
        self.status = "Created"


# decorator pattern 
def before_processing(handler):
    def wrapped(*args, **kwargs):
        print("Checking [Before Processing] order processing")
        return handler(*args, **kwargs) 
    return wrapped

    
def after_processing(handler):
    def wrapped(*args, **kwargs):
        result = handler(*args, **kwargs)
        print("Checking [After Processing] ended successfully")
        return result
    return wrapped


class OrderProcessor:
    @after_processing
    @before_processing
    def process_order(self, order, subject):
        print(f"Processing order {order.order_id} for user {order.user.name}")
        delay = Delay()
        delay.set_time(1)
        order.status = "Processed"
        print(f"Order {order.order_id} processed")
        subject.send_notifications(order)


# command pattern
class Command(ABC):
    def __init__(self, receiver):
        self.receiver = receiver
    @abstractmethod
    def change_status(self):
        pass
    @abstractmethod
    def undo_status(self):
        pass


class OrderStatus(Command):
    def __init__(self, order, new_status):
        self.order = order
        self.prev_state = None
        self.new_status = new_status
    def change_status(self):
        self.prev_status = self.order.status
        self.order.status = self.new_status
        print(f"Order {self.order.order_id} status changed to {self.new_status}")
    def undo_status(self):
        self.order.status = self.prev_status
        print(f"Undo: Order {self.order.order_id} status reverted to {self.prev_status}")


class Invoker:
    def __init__(self):
        self.history = []
        self.redo_stack = []
    def change_status(self, command):
        command.change_status()
        self.history.append(command)
        self.redo_stack.clear()
    def undo_status(self):
        if self.history:
            command = self.history.pop()
            command.undo_status()
            self.redo_stack.append(command)
        else:
            print("Nothing to undo")
    def redo_status(self):
        if self.redo_stack:
            command = self.redo_stack.pop()
            command.change_status()
            self.history.append(command)
        else:
            print("Nothing to redo")


# strategy pattern 
class Context:
    def __init__(self, loglevel):
        self.loglevel = loglevel
    def set_strategy(self, new_strategy):
        self.loglevel = new_strategy
    def log(self, message):
        return self.loglevel.message_level(message)

class LogLevels(ABC):
    @abstractmethod
    def message_level(self, message):
        pass


class DebugLevel(LogLevels):
    def message_level(self, message):
        print(f"[DEBUG] {time.strftime('%H:%M:%S')}: {message}")


class InfoLevel(LogLevels):
    def message_level(self, message):
        print(f"[INFO] {time.strftime('%H:%M:%S')}: {message}")


class ErrorLevel(LogLevels):
    def message_level(self, message):
        print(f"[ERROR] {time.strftime('%H:%M:%S')}: {message}")


# observer pattern 
class Subject:
    def __init__(self):
        self.observers = []
    def attach(self, observer):
        self.observers.append(observer)
    def detach(self, observer):
        self.observers.remove(observer)
    def notify(self, order):
        for observer in self.observers:
            observer.update(order)
    def send_notifications(self, order):
        self.notify(order)


class Services(ABC):
    @abstractmethod
    def update(self, order):
        pass


class EmailService(Services):
    def update(self, order):
        user = order.user
        msg = f"Your order {order.order_id} is now {order.status}"
        print(f"[Email] Sent to {user.name}: {msg}")


class SMSService(Services):
    def update(self, order):
        user = order.user
        msg = f"Your order {order.order_id} is now {order.status}"
        print(f"[SMS] Sent to {user.name}: {msg}")


class PushService(Services):
    def update(self, order):
        user = order.user
        msg = f"Your order {order.order_id} is now {order.status}"
        print(f"[Push] Sent to {user.name}: {msg}")


# facade pattern 
class Facade:
    def __init__(self):
        self.user = User("Bob")
        self.order = Order(1001, self.user)
        self.subject = Subject()
        self.processor = OrderProcessor()
        self.invoker = Invoker()
        self.context = Context(DebugLevel())
    def notify_order(self):
        if self.user.email_enabled:
            self.subject.attach(EmailService())
        if self.user.sms_enabled:
            self.subject.attach(SMSService())
        if self.user.push_enabled:
            self.subject.attach(PushService())

        self.processor.process_order(self.order, self.subject)
    def order_status(self):
        cmd1 = OrderStatus(self.order, "Shipped")
        self.invoker.change_status(cmd1)
        self.invoker.undo_status()
        self.invoker.redo_status()
    def log(self):
        self.context.set_strategy(ErrorLevel())
        self.context.log("ERROR MESSAGE")


# handle asynchronous or delayed operations
class Delay:
    def set_time(self, seconds):
        time.sleep(seconds)

# main function
def main():
    facade = Facade()
    facade.notify_order()
    facade.order_status()
    facade.log() 

if __name__ == "__main__":
    main()