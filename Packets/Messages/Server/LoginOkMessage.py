from Utils.Writer import Writer


class LoginOk(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.Player = player
        self.ID = 20758
        self.Version = 1

    def encode(self):
        self.writeInt(0)  # HighId
        self.writeInt(1)  # LowId

        self.writeInt(0)  # HighId
        self.writeInt(1)  # LowId

        self.writeString('a621cb184d0a87036bc3d41b296bfa8f6fe5ab63') # Pass Token

        self.writeString()  # GameCenterId
        self.writeString()  # FacebookId

        self.writeVint(3)    # MajorVersion
        self.writeVint(162)  # Build
        self.writeVint(162)  # Build
        self.writeVint(1)    # MinorVersion

        self.writeString("prod")  # Environment

        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)

        self.writeString()  # FacebookAppId
        self.writeString()  # ServerTime
        self.writeString()  # AccountCreatedDate

        self.writeString("RO") # Region
        self.writeString("Bucharest") # City

        self.writeString()

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(2)

        # Game Assets URL
        self.writeString("http://game-assets.clashroyaleapp.com/")

        # Cdn URL
        self.writeString("https://99faf1e355c749a9a049-2a63f4436c967aa7d355061bd0d924a1.ssl.cf1.rackcdn.com/")

        self.writeVint(1)

        # Event Assets URL
        self.writeString("https://event-assets.clashroyale.com")





