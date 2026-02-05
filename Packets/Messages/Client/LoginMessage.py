from Packets.Messages.Server.LoginOkMessage import LoginOk
from Packets.Messages.Server.OwnHomeDataMessage import OwnHomeDataMessage
from Utils.Reader import CRMessageReader



class Login(CRMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.Player = player
        self.Client = client

    def decode(self):
        self.Player.HighID = self.read_int()
        self.Player.LowID = self.read_int()
        self.Player.Token = self.read_int()


    def process(self):
        LoginOk(self.Client, self.Player).send()
        OwnHomeDataMessage(self.Client, self.Player).send()


