class Refund:
    def __init__(self,firstname,lastname,amount,reason,product):
        self.firstname = firstname
        self.lastname = lastname
        self.amount = amount
        self.reason = reason
        self.product = product

    def informationl_user(self):
        return(f"Our customer {self.firstname} {self.lastname} need a refund of her {self.product} because of {self.reason} which he bought at {self.amount}")
    def sent_message(self):
        return(f"Message sent:Refund request for {self.product} by {self.firstname} {self.lastname} due to {self.reason}")
refund=Refund("Agnes","Karenga","222rwf","it's rotten","apple")
print(refund.informationl_user())
print(refund.sent_message())