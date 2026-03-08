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


class OrderProcessor:
    def __init__(self):
        self.history = []
        self.redo_stack = []
    def process_order(self, order, subject):
        print(f"Processing order {order.order_id} for user {order.user.name}")
        time.sleep(1)
        order.status = "Processed"
        print(f"Order {order.order_id} processed")
        subject.send_notifications(order)
    def change_status(self, order, new_status):
        prev_status = order.status
        order.status = new_status
        self.history.append((order, prev_status))
        self.redo_stack.clear()
        print(f"Order {order.order_id} status changed to {new_status}")
    def undo_status(self):
        if self.history:
            order, prev_status = self.history.pop()

            self.redo_stack.append((order, order.status))
            order.status = prev_status
            print(f"Undo: Order {order.order_id} status reverted to {prev_status}")
        else:
            print("Nothing to undo")
    def redo_status(self):
        if self.redo_stack:
            order, next_status = self.redo_stack.pop()
            self.history.append((order, order.status))
            order.status = next_status
            print(f"Redo: Order {order.order_id} status changed to {next_status}")
        else:
            print("Nothing to redo")
    def log(self, level, message):
        if level in ("DEBUG", "INFO", "ERROR"):
            print(f"[{level}] {time.strftime('%H:%M:%S')}: {message}")


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


class EmailService:
    def update(self, order):
        user = order.user
        msg = f"Your order {order.order_id} is now {order.status}"
        print(f"[Email] Sent to {user.name}: {msg}")


class SMSService:
    def update(self, order):
        user = order.user
        msg = f"Your order {order.order_id} is now {order.status}"
        print(f"[SMS] Sent to {user.name}: {msg}")


class PushService:
    def update(self, order):
        user = order.user
        msg = f"Your order {order.order_id} is now {order.status}"
        print(f"[Push] Sent to {user.name}: {msg}")


def main():
    user = User("Bob")
    order = Order(1001, user)

    subject = Subject()
    observer1 = EmailService()
    observer2 = SMSService()
    observer3 = PushService()

    subject.attach(observer1)
    subject.attach(observer2)
    subject.attach(observer3)

    processor = OrderProcessor()
    processor.process_order(order, subject)
    processor.change_status(order, "Shipped")
    processor.undo_status()
    processor.redo_status()

if __name__ == "__main__":
    main()