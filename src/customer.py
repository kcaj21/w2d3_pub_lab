
class Customer:
    def __init__(self, name, wallet, age, drunkeness):

        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunkeness = 0

    def reduce_wallet_amount(self, amount):
        self.wallet -= amount

    def get_customer_age(self, age):
        return age
    
    def check_customer_age(self, age):
        if age >= 18:
            return True
        else:
            return False
        
    def add_drunkeness(self, strength):
        self.drunkeness += strength


    # def check_drunkeness(self, strength):
    #     if self.drunkeness <10:
    #         self.drunkeness += strength
    #     elif self.drunkeness > 10:
    #         print("You're too drunk")
        
    
