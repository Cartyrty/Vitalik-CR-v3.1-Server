from Utils.Writer import Writer


class KeepAliveOkMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.ID = 20108

    def encode(self):
        pass
