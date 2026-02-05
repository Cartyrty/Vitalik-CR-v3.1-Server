from Utils.Reader import CRMessageReader
from Packets.Messages.Server.KeepAliveOkMessage import KeepAliveOkMessage



class KeepAliveMessage(CRMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.Player = player
        self.Client = client

    def decode(self):
        pass

    def process(self):
        KeepAliveOkMessage(self.Client, self.Player).send()