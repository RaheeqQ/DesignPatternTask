# adapter method
from abc import ABC, abstractmethod


class Gateway(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass


class StripeGateway(Gateway):
    def process_payment(self, amount):
        print(f"Charging ${amount} with Stripe")


class PayPalGateway(Gateway):
    def process_payment(self, amount):
        print(f"Processing ${amount} with PayPal")


class LocalBankAPIGateway(Gateway):
    def process_payment(self, amount):
        print(f"Handling ${amount} with LocalBankAPI")


def checkout(processor: Gateway, amount): 
    processor.process_payment(amount)


if __name__ == "__main__":
    checkout(StripeGateway(), 99.9)
    checkout(PayPalGateway(), 99.9)
    checkout(LocalBankAPIGateway(), 1000)
