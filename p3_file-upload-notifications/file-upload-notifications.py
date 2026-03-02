from abc import ABC, abstractmethod


class Subject:
    def __init__(self):
        self.observers = []
    def attach(self, observer):
        self.observers.append(observer)
    def detach(self, observer):
        self.observers.remove(observer)
    def notify(self, user, filename):
        for observer in self.observers:
            observer.update(user, filename)
    def upload_file(self, user, filename):
        print(f"{user} uploaded {filename}")
        self.notify(user, filename)


class Observers(ABC):
    @abstractmethod
    def update(self, user, filename):
        pass 


class EmailObserver(Observers):
    def update(self, user, filename):
        # Send email
        print(f"Email sent to {user} confirming upload of {filename}")


class LogObserver(Observers):
    def update(self, user, filename):
        # Log upload
        print(f"[LOG] {user} uploaded {filename}")


class DashboardObserver(Observers):
    def update(self, user, filename):
        # Update dashboard
        print(f"Dashboard updated for {user}")


def main():
    subject = Subject()

    observer1 = EmailObserver()
    observer2 = LogObserver()
    observer3 = DashboardObserver()

    subject.attach(observer1)
    subject.attach(observer2)
    subject.attach(observer3)

    subject.upload_file("alice", "report.pdf")

    subject.detach(observer1)

    subject.upload_file("Bob", "report2.pdf")
main()