import ipaddress
from netaddr import IPNetwork, IPAddress
from vodafone_interview.data_structures.entry import Entry


class NetworkCollection:
    def __init__(self, ipv4_network, raw_entry_list):
        """
        Constructor for NetworkCollection data structure.

        self.ipv4_network -> ipaddress.IPv4Network
        self.entries -> list(Entry)
        """
        self.ipv4_network = ipv4_network
        self.entries = raw_entry_list

    def remove_invalid_records(self):
        """
        Removes invalid objects from the entries list.
        """
        for entry in list(self.entries):
            try:
                if ipaddress.ip_address(entry['address']):
                    if IPAddress(entry['address']) not in IPNetwork(self.ipv4_network):
                        self.entries.remove(entry)
            except:
                self.entries.remove(entry)
        list_of_entry = []
        for entry in self.entries:
            entry_obj = Entry(entry['address'], entry['available'], entry['last_used'])
            list_of_entry.append(entry_obj)
        self.entries = list_of_entry
        self.sort_records()

    def sort_records(self):
        """
        Sorts the list of associated entries in ascending order.
        DO NOT change this method, make the changes in entry.py :)
        """

        self.entries = sorted(self.entries)
