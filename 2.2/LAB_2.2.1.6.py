class MFD:
    def scan(self):
        print('scan() method from MFD class')

    def print(self):
        print('print() method from MFD class')

    def send(self):
        print('send() method from MFD class')


class Scanner(MFD):
    def scan(self):
        print('scan() method from Scanner class')


class Printer(MFD):
    def print(self):
        print('print() method from Printer class')


class Fax(MFD):
    def print(self):
        print('print() method from Fax class')

    def send(self):
        print('send() method from Fax class')


class MFD_SPF(Scanner, Printer, Fax):
    pass


class MFD_SFP(Scanner, Fax, Printer):
    pass


mfd_spf = MFD_SPF()
mfd_sfp = MFD_SFP()

mfd_spf.scan()
mfd_spf.print()
mfd_spf.send()

mfd_sfp.scan()
mfd_sfp.print()
mfd_sfp.send()
