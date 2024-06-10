class Payment:
    def __init__(self, uuid, name, number, address, order, dbase):
        self.uuid = uuid
        self.name = name
        self.number = number
        self.address = address
        self.order = order
        self.status = True  # False
        self.dbase = dbase
        self.create_payment()

    def create_payment(self):
        self.dbase.create_payment(self.uuid, self.name, self.number, self.address, self.order, self.status)
