#abstract factory method 
from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def draw(self):
        pass
class ScrollBar(ABC):
    @abstractmethod
    def draw(self):
        pass


class WindowsButton(Button):
    def draw(self):
        print("Drawing Windows button")
class WindowsScrollBar(ScrollBar):
    def draw(self):
        print("Drawing Windows scrollbar")


class MacButton(Button):
    def draw(self):
        print("Drawing macOS button")
class MacScrollBar(ScrollBar):
    def draw(self):
        print("Drawing macOS scrollbar")


class LinuxButton(Button):
    def draw(self):
        print("Drawing Linux button")
class LinuxScrollBar(ScrollBar):
    def draw(self):
        print("Drawing Linux scrollbar")


class OSFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass
    @abstractmethod
    def create_scrollbar(self):
        pass


class WindowsFactory(OSFactory):
    def create_button(self):
        return WindowsButton()
    def create_scrollbar(self):
        return WindowsScrollBar()


class MacFactory(OSFactory):
    def create_button(self):
        return MacButton()
    def create_scrollbar(self):
        return MacScrollBar()


class LinuxFactory(OSFactory):
    def create_button(self):
        return LinuxButton()
    def create_scrollbar(self):
        return LinuxScrollBar()


def main():
    factory = WindowsFactory()
    button = factory.create_button()
    scrollbar = factory.create_scrollbar()

    button.draw()
    scrollbar.draw()
main()