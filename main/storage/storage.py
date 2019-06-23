import ipfsapi


class Storage:

    def __init__(self):
        self.host = 'Ramesh'
        self.port = 5001
        self.ipfs_client = ipfsapi.Client(self.host, 5001)

    def load_ipfs_file(self, hash):
        self.ipfs_client.get(hash)

    def add_ipfs_file(self, file):
        ipfs_res = self.ipfs_client.add(file)
        print(ipfs_res)
        return ipfs_res

    def save_persona(self, persona):
        return

    def update_file(self, hash):
        ipfs_res = self.ipfs_client.name_publish(hash)
        print(ipfs_res)
        print(self.ipfs_client.resolve(ipfs_res['Name']))
        print(self.ipfs_client.name_resolve())

