class Handler:
    def __init__(self):
        self.next = None

    def set_next(self, next):
        self.next=next

    def handle(self, type, message):
        pass


class Paznic(Handler):
    def __init__(self):
        super().__init__()

    def handle(self, type, message):
        if type == 5:
            print("Paznic:" + message)
        else:
            if self.next:
                self.next.handle(type,message)


class Politie(Handler):
    def __init__(self):
        super().__init__()

    def handle(self, type, message):
        if type == 4:
            print("Politie:" + message)
        else:
            if self.next:
                self.next.handle(type,message)


class Sri(Handler):
    def __init__(self):
        super().__init__()

    def handle(self, type, message):
        if type == 3:
            print("Sri:" + message)
        else:
            if self.next:
                self.next.handle(type,message)


class Sie(Handler):
    def __init__(self):
        super().__init__()

    def handle(self, type, message):
        if type == 2:
            print("Sie:" + message)
        else:
            if self.next:
                self.next.handle(type,message)


class Csat(Handler):
    def __init__(self):
        super().__init__()

    def handle(self, type, message):
        if type == 1:
            print("Csat a preluat mesajul" + message)
        else:
            if self.next:
                self.next.handle(type,message)


class Nato(Handler):
    def __init__(self):
        super().__init__()

    def handle(self, type, message):
        if type == 0:
            print("Nato a preluat mesajul" + message)
        else:
            print("Tip gresit")


def main():
    nato = Nato()
    csat = Csat()
    sie = Sie()
    sri = Sri()
    politie = Politie()
    paznic = Paznic()
    paznic.set_next(politie)
    politie.set_next(sri)
    sri.set_next(sie)
    sie.set_next(csat)
    csat.set_next(nato)
    paznic.handle(0, "Message1")
    politie.handle(5,"da")


if __name__ == '__main__':
    main()
