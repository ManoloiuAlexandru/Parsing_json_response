import re


class Datacenter:
    def __init__(self, name, cluster_dict):
        """
        Constructor for Datacenter data structure.

        self.name -> str
        self.clusters -> list(Cluster)
        """

        self.name = name
        self.cluster = cluster_dict

    def remove_invalid_clusters(self):
        """
        Removes invalid objects from the clusters list.
        """
        final_dict = dict(self.cluster)
        for cluster in self.cluster:
            if not re.fullmatch(r'{name_of_cluster}'.format(name_of_cluster=self.name.upper()[0:3]) + "-[0-9]{1,3}",
                                cluster):
                del final_dict[cluster]
        self.cluster = final_dict
