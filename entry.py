class Entry:
    def __init__(self, address, available, last_used):
        """
        Constructor for Entry data structure.

        self.address -> str
        self.available -> bool
        self.last_used -> datetime
        """

        self.address = address
        self.available = available
        self.last_used = last_used

    def __gt__(self, other):
        if self.address > other.address:
            return True
        else:
            return False
