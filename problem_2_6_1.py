#my answer
import abc

class MFD(abc.ABC):
    serial_number = 0
    max_resolution = 420

    def __init__(self):
        MFD.serial_number += 1

    @abc.abstractmethod
    def scan_document(self):
        return "Document has been scanned"

    @abc.abstractmethod
    def get_scanner_status(self):
        status = (MFD.max_resolution, MFD.serial_number)
        return status

class Printer(abc.ABC):
    serial_number = 0
    max_resolution = 720

    def __init__(self):
        Printer.serial_number += 1

    @abc.abstractmethod
    def print_document(self):
        return "Document has been printed"

    @abc.abstractmethod
    def get_printer_status(self):
        return (Printer.max_resolution, Printer.serial_number)

# a cheap device made for a cheap printer and a cheap scanner
class MFD1(Printer):
    device_resolution = 360
    def __init__(self):
        super().__init__()

    def print_document(self):
        print("Document has been printed with MFD1")

    def get_serial_number(self):
        status = super().get_printer_status()
        return status[1]

    def get_printer_status(self):
        return(MFD1.device_resolution)

mfd1 = MFD1()

print(mfd1.get_printer_status())
print(mfd1.get_serial_number())

# their answer
import abc

class Scanner(abc.ABC):
    def scan_document(self):
        return 'Document was scanned'

    @abc.abstractmethod
    def get_scanner_status(self):
        pass

class Printer(abc.ABC):
    def print_document(self):
        return 'Document was printed'

    @abc.abstractmethod
    def get_printer_status(self):
        pass

class MFD1(Scanner, Printer):
    def get_scanner_status(self):
        return 'Max scan resolution is low, S/N: S001'

    def get_printer_status(self):
        return 'Max print resolution is low, S/N: P001'

class MFD2(Scanner, Printer):
    def get_scanner_status(self):
        return 'Max scan resolution is fine, S/N: S002'

    def get_printer_status(self):
        return 'Max print resolution is fine, S/N: P002'

    def get_history(self):
        return 'The history is...'

class MFD3(Scanner, Printer):
    def get_scanner_status(self):
        return 'Max scan resolution is high, S/N: S003'

    def get_printer_status(self):
        return 'Max print resolution is high, S/N: P003'

    def get_history(self):
        return 'The history is...'

    def send_fax(self):
        print('sending fax')

    def receive_fax(self):
        print('receiving fax')
mfd1 = MFD1()
print(mfd1.print_document())
print(mfd1.get_printer_status())

mfd2 = MFD2()
print(mfd2.print_document())
print(mfd2.get_printer_status())

mfd3 = MFD3()
print(mfd3.print_document())
print(mfd3.get_printer_status())
