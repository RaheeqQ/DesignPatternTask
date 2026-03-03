# adapter method
class StripeGateway:
    def process_payment(self, amount):
        print(f"Charging ${amount} with Stripe")


class PayPalGateway:
    def process_payment(self, amount):
        print(f"Processing ${amount} with PayPal")


class LocalBankAPIGateway:
    def process_payment(self, amount):
        print(f"Handling ${amount} with LocalBankAPI")


class Adapter:
    def __init__(self, obj, **adapted_methods):
        self.obj = obj 
        for key, value in adapted_methods.items():
            setattr(self, key, value)

if __name__ == "__main__":
    objects = []
    stripeGateway = StripeGateway()
    objects.append(Adapter(stripeGateway, charge = stripeGateway.process_payment))
    paypalGateway = PayPalGateway()
    objects.append(Adapter(paypalGateway, charge = paypalGateway.process_payment))
    localGateway = LocalBankAPIGateway()
    objects.append(Adapter(localGateway, charge = localGateway.process_payment))
    for obj in objects:
        obj.charge(100)
