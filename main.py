import requests
import json
import sys
import time

from vodafone_interview.data_structures.datacenter import Datacenter
from vodafone_interview.data_structures.network_collection import NetworkCollection
from vodafone_interview.data_structures.cluster import Cluster

URL = "http://www.mocky.io/v2/5e539b332e00007c002dacbe"


def get_data(url, max_retries=5, delay_between_retries=1):
    """
    Fetch the data from http://www.mocky.io/v2/5e539b332e00007c002dacbe
    and return it as a JSON object.
​
    Args:
        url (str): The url to be fetched.
        max_retries (int): Number of retries.
        delay_between_retries (int): Delay between retries in seconds.
    Returns:
        data (dict)
    """
    try:
        response_from_server = requests.get(url=url)
    except Exception:
        print("Error can't connect to server")
        sys.exit(2)
    while max_retries > 1 and response_from_server.status_code != 200:
        try:
            response_from_server = requests.get(url=url)
        except Exception:
            print("Error can't connect to server")
            sys.exit(2)
        if response_from_server.status_code != 200:
            time.sleep(delay_between_retries)
            max_retries -= 1
        else:
            max_retries = 0
    return json.loads(response_from_server.text)


def main():
    """
    Main entry to our program.
    """

    data = get_data(URL)

    if not data:
        raise ValueError('No data to process')

    datacenters = [
        Datacenter(key, value)
        for key, value in data.items()
    ]

    for datacenter in datacenters:
        datacenter.remove_invalid_clusters()
        for clusters in datacenter.cluster:
            dict_of_networks = datacenter.cluster[clusters]['networks']
            list_of_networks = []
            for network in dict_of_networks:
                new_network = NetworkCollection(network, dict_of_networks[network])
                new_network.remove_invalid_records()
                list_of_networks.append(new_network)
            new_cluster = Cluster(name=clusters, security_level=datacenter.cluster[clusters]['security_level'],
                                  network_dict=list_of_networks)
            datacenter.cluster[clusters] = new_cluster

    return datacenters


if __name__ == '__main__':
    main()
