from Utils.Writer import Writer


class OwnHomeDataMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.ID = 21217
        self.Player = player

    def encode(self):
        # LOGIC CLIENT HOME #

        self.writeVint(0)  # High ID
        self.writeVint(0)  # Low ID

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        # Decks
        self.writeVint(5)  # Decks Count

        # Player Decks array
        for x in range(5):
            self.writeVint(8)  # cards count
            self.writeVint(26000000)
            self.writeVint(26000001)
            self.writeVint(26000005)
            self.writeVint(28000001)
            self.writeVint(28000000)
            self.writeVint(26000003)
            self.writeVint(26000002)
            self.writeVint(26000004)

        self.writeVint(8)
        self.writeHexa('''FF''')

        # Current Deck
        cardsList = [1, 2, 6, 91, 90, 4, 3, 5]

        for cardID in cardsList:
            # Card ID
            self.writeVint(cardID)
            # Card Level
            self.writeVint(100)
            # Card Star Level
            self.writeVint(3)
            self.writeVint(0)
            # Card Points
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)

        cardsList = [i for i in range(7, 108)]

        self.writeVint(len(cardsList))

        for cardID in cardsList:
            # Card ID
            self.writeVint(cardID)
            # Card Level
            self.writeVint(100)
            # Card Star Level
            self.writeVint(3)
            self.writeVint(0)
            # Card Points
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)

        self.writeVint(0)  # Current Selected Deck

        self.writeVint(8)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(1)
        self.writeVint(0)

        # Events
        count = len(self.Player.events)

        self.writeVint(count)  # Events Count

        for event in self.Player.events:
            self.writeVint(event["ID"])
            self.writeInt(0)

            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(event["Type"])
            self.writeVint(event["StartTime"])
            self.writeVint(event["EndTime"])
            self.writeVint(event["VisibleOn"])

            self.writeInt(0)
            self.writeInt(0)
            self.writeInt(0)

            self.writeVint(0)
            self.writeVint(1)
            self.writeString(event["JSON"])

            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)

        self.writeInt(0)

        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)  # Timestamp

        self.writeVint(0)
        self.writeVint(0)

        self.writeInt(0)

        self.writeVint(0)  # array
        self.writeVint(0)  # array

        self.writeVint(1)
        self.writeVint(0)

        # Chests
        count = len(self.Player.chests)

        self.writeVint(count)

        for chest in self.Player.chests:
            self.writeVint(1)

            # Chest SCID
            self.writeVint(19)
            self.writeVint(chest['ID'])

            # Chest Status
            self.writeVint(chest['Status'])

            # Chest Slot
            self.writeVint(9 - chest['Slot'])
            self.writeVint(0)
            self.writeVint(chest['Slot'])

            self.writeInt(2)

            self.writeVint(0)
            self.writeVint(0)

            self.writeString()

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(2)

        self.writeVint(13)
        self.writeVint(54)
        self.writeVint(12)
        self.writeVint(54)

        self.writeVint(12)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(3)
        self.writeVint(1945)
        self.writeVint(1)

        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(1)
        self.writeVint(13)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(2)

        self.writeVint(8)
        self.writeHexa('''FF''')

        # Current Deck
        cardsList = [1, 2, 6, 91, 90, 4, 3, 5]

        for cardID in cardsList:
            # Card ID
            self.writeVint(cardID)
            # Card Level
            self.writeVint(100)
            # Card Star Level
            self.writeVint(3)
            self.writeVint(0)
            # Card Points
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(5)
        self.writeVint(32)

        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeNullVint()

        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(1)
        self.writeVint(2)
        self.writeVint(1)
        self.writeVint(3)

        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        
        self.writeVint(0)

        self.writeVint(7)

        # Shop Cards
        count = len(self.Player.shopCards)
        self.writeVint(count)

        for card in self.Player.shopCards:
            self.writeVint(1)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(1)
            # Card Cost
            self.writeVint(card['Cost'])
            self.writeVint(5)
            self.writeVint(1)
            # Card SCID
            self.writeVint(28)
            self.writeVint(card['ID'])
            self.writeVint(card['Multiplier'])

            self.writeVint(self.Player.shopCards.index(card) + 1)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)

        # Shop Chests
        count = len(self.Player.shopChests)
        self.writeVint(count)

        for chest in self.Player.shopChests:
            # Chest SCID
            self.writeVint(19)
            self.writeVint(chest['ID'])
            # Chest Status
            self.writeVint(chest['Status'])

            self.writeVint(0)
            # Chest Name
            self.writeString(chest['Name'])

            self.writeVint(1)
            # Chest Slot
            self.writeVint(chest['Slot'])

            self.writeVint(0)
            self.writeNullVint()
            self.writeVint(0)
            self.writeNullVint()


        self.writeHexa('''03 00 01 02 00 00 00 00 00 00 00 00 05 00 00 00 00 01 00 00 00 01 00 00 00 00 03 00 00 00 11 6B 69 6E 67 5F 68 61 70 70 79 5F 30 31 2E 77 61 76 00 00 00 37 2F 32 64 37 63 35 39 66 61 2D 66 34 37 66 2D 34 62 31 37 2D 61 35 35 61 2D 62 30 36 37 65 66 30 61 64 61 32 37 5F 6B 69 6E 67 5F 68 61 70 70 79 5F 30 31 2E 77 61 76 00 00 00 20 32 65 31 39 63 36 35 65 61 61 39 31 33 33 32 65 37 31 61 35 66 34 65 37 31 38 65 35 31 61 64 38 00 00 00 14 65 6D 6F 74 65 73 5F 6B 69 6E 67 5F 30 31 5F 64 6C 2E 73 63 00 00 00 3A 2F 62 33 61 35 37 61 30 65 2D 65 34 37 62 2D 34 37 61 31 2D 39 33 34 39 2D 37 63 31 36 62 65 62 38 31 34 30 38 5F 65 6D 6F 74 65 73 5F 6B 69 6E 67 5F 30 31 5F 64 6C 2E 73 63 00 00 00 20 33 32 66 38 62 64 39 64 37 39 37 64 36 39 62 39 62 33 36 31 30 39 36 61 65 62 36 30 30 39 63 63 01 00 88 02 00 00 00 01 00 00 00 00 00 00 00 01 00 00 00 01 00 00 00 01 00 00 00 02 00 00 00 01 00 00 00 03 00 00 00 02 00 00 00 00 00 00 00 02 00 00 00 01 00 00 00 02 00 00 00 02 00 00 00 02 00 00 00 03 00 00 00 03 00 00 00 00 00 00 00 03 00 00 00 01 00 00 00 03 00 00 00 02 00 00 00 03 00 00 00 03 00 00 00 04 00 00 00 00 00 00 00 04 00 00 00 01 00 00 00 04 00 00 00 02 00 00 00 04 00 00 00 03 00 00 00 05 00 00 00 00 00 00 00 05 00 00 00 01 00 00 00 05 00 00 00 02 00 00 00 05 00 00 00 03 00 00 00 06 00 00 00 00 00 00 00 06 00 00 00 01 00 00 00 06 00 00 00 02 00 00 00 06 00 00 00 03 00 00 00 07 00 00 00 00 00 00 00 07 00 00 00 01 00 00 00 07 00 00 00 02 00 00 00 07 00 00 00 03 00 00 00 08 00 00 00 00 00 00 00 08 00 00 00 01 00 00 00 08 00 00 00 02 00 00 00 08 00 00 00 03 00 00 00 09 00 00 00 00 00 00 00 09 00 00 00 01 00 00 00 09 00 00 00 02 00 00 00 09 00 00 00 03 00 00 00 0A 00 00 00 00 00 00 00 0A 00 00 00 01 00 00 00 0A 00 00 00 02 00 00 00 0A 00 00 00 03 00 00 00 0B 00 00 00 00 00 00 00 0B 00 00 00 01 00 00 00 0B 00 00 00 02 00 00 00 0B 00 00 00 03 00 00 00 0C 00 00 00 00 00 00 00 0C 00 00 00 01 00 00 00 0C 00 00 00 02 00 00 00 0C 00 00 00 03 00 00 00 0D 00 00 00 00 00 00 00 0D 00 00 00 01 00 00 00 0D 00 00 00 02 00 00 00 0D 00 00 00 03 00 00 00 0E 00 00 00 00 00 00 00 0E 00 00 00 01 00 00 00 0E 00 00 00 02 00 00 00 0E 00 00 00 03 00 00 00 0F 00 00 00 00 00 00 00 0F 00 00 00 01 00 00 00 0F 00 00 00 02 00 00 00 0F 00 00 00 03 00 00 00 10 00 00 00 00 00 00 00 10 00 00 00 01 00 00 00 10 00 00 00 02 00 00 00 10 00 00 00 03 00 00 00 11 00 00 00 00 00 00 00 11 00 00 00 01 00 00 00 11 00 00 00 02 00 00 00 11 00 00 00 03 00 00 00 12 00 00 00 00 00 00 00 12 00 00 00 01 00 00 00 12 00 00 00 02 00 00 00 12 00 00 00 03 00 00 00 14 00 00 00 00 00 00 00 15 00 00 00 00 00 00 00 15 00 00 00 01 00 00 00 16 00 00 00 00 00 00 00 16 00 00 00 01 00 00 00 17 00 00 00 00 00 00 00 17 00 00 00 01 00 00 00 17 00 00 00 02 00 00 00 17 00 00 00 03 00 00 00 18 00 00 00 00 00 00 00 18 00 00 00 01 00 00 00 18 00 00 00 02 00 00 00 18 00 00 00 03 00 00 00 19 00 00 00 00 00 00 00 19 00 00 00 01 00 00 00 19 00 00 00 02 00 00 00 1A 00 00 00 00 00 00 00 1A 00 00 00 01 00 00 00 1A 00 00 00 02 00 00 00 1B 00 00 00 00 00 00 00 1C 00 00 00 00 00 00 00 1C 00 00 00 01 00 00 00 1D 00 00 00 00 00 00 00 1D 00 00 00 01 00 00 00 1D 00 00 00 02 00 00 00 1D 00 00 00 03 00 00 00 1E 00 00 00 00 00 00 00 1E 00 00 00 01 00 00 00 1F 00 00 00 00 00 00 00 1F 00 00 00 01 00 00 00 1F 00 00 00 02 00 00 00 1F 00 00 00 03 00 00 00 20 00 00 00 00 00 00 00 20 00 00 00 01 00 00 00 20 00 00 00 02 00 00 00 20 00 00 00 03 00 00 00 21 00 00 00 00 00 00 00 22 00 00 00 00 00 00 00 24 00 00 00 00 00 00 00 24 00 00 00 01 00 00 00 24 00 00 00 02 00 00 00 24 00 00 00 03 00 00 00 25 00 00 00 00 00 00 00 27 00 00 00 00 00 00 00 28 00 00 00 00 00 00 00 28 00 00 00 01 00 00 00 28 00 00 00 02 00 00 00 29 00 00 00 00 00 00 00 29 00 00 00 01 00 00 00 2A 00 00 00 00 00 00 00 2C 00 00 00 00 00 00 00 2D 00 00 00 00 00 00 00 2E 00 00 00 00 00 00 00 2F 00 00 00 00 00 00 00 31 00 00 00 00 00 00 00 31 00 00 00 01 00 00 00 32 00 00 00 00 00 00 00 32 00 00 00 01 00 00 00 32 00 00 00 02 00 00 00 32 00 00 00 03 00 00 00 33 00 00 00 00 00 00 00 34 00 00 00 00 00 00 00 34 00 00 00 01 00 00 00 34 00 00 00 02 00 00 00 01 00 00 00 00 00 00 00 01 00 00 00 01 00 00 00 01 00 00 00 02 00 00 00 01 00 00 00 03 00 00 00 02 00 00 00 00 00 00 00 02 00 00 00 01 00 00 00 02 00 00 00 02 00 00 00 02 00 00 00 03 00 00 00 00 00 01 81 CE D2 59 00 00 00 19 74 6F 77 65 72 73 6B 69 6E 5F 73 65 61 73 6F 6E 5F 30 31 5F 64 6C 2E 73 63 00 00 00 3F 2F 33 66 32 38 30 33 61 30 2D 37 36 34 66 2D 34 62 61 39 2D 38 35 32 36 2D 63 37 39 61 32 37 38 30 36 37 62 33 5F 74 6F 77 65 72 73 6B 69 6E 5F 73 65 61 73 6F 6E 5F 30 31 5F 64 6C 2E 73 63 00 00 00 20 61 30 32 38 30 35 62 32 36 33 66 33 39 64 62 31 33 33 66 62 30 65 30 30 62 61 33 61 32 65 37 32 00 00 00 0A 53 68 61 72 6B 20 54 61 6E 6B 01 00 00 00 09 6B 69 6E 67 74 6F 77 65 72 01 00 00 00 10 73 68 61 72 6B 5F 6B 69 6E 67 5F 64 65 61 74 68 01 00 00 00 0D 70 72 69 6E 63 65 73 73 74 6F 77 65 72 01 00 00 00 14 73 68 61 72 6B 5F 70 72 69 6E 63 65 73 73 5F 64 65 61 74 68''')

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)  # array
        self.writeVint(0)  # array

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(1)

        self.writeNullVint()
        self.writeVint(0)
        self.writeVint(1)

        self.writeVint(104003009)

        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(7000)
        self.writeVint(6900)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(600)

        self.writeVint(600)
        self.writeVint(600)
        self.writeVint(1)
        self.writeVint(13)

        self.writeVint(600)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(1)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        # LOGIC CLIENT AVATAR #

        for i in range(3):
            self.writeVint(0)  # High ID
            self.writeVint(0)  # Low ID

        self.writeString(self.Player.Name)  # Username

        self.writeVint(13)  # Current Arena + 1

        self.writeVint(0)

        self.writeVint(7000)  # Trophies
        self.writeVint(0)     # Legend Trophies
        self.writeVint(0)     # Season Record

        self.writeNullVint()

        self.writeVint(0)     # Best Season Rank
        self.writeVint(7000)  # Best Season Trophies

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)

        self.writeVint(9)

        # Game Variables array
        self.writeVint(2)

        # Gold
        self.writeVint(5)  # CSV ID
        self.writeVint(1)  # Resource ID
        self.writeVint(self.Player.Gold)

        # StarPoints
        self.writeVint(5)  # CSV ID
        self.writeVint(49) # Resource ID
        self.writeVint(self.Player.ExpPoints)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)


        # Profile Statistics array
        self.writeVint(4)

        # MaxScore
        self.writeVint(5)  # CSV ID
        self.writeVint(6)  # Resource ID
        self.writeVint(7000)

        # ThreeCrownWins
        self.writeVint(5)  # CSV ID
        self.writeVint(7)  # Resource ID
        self.writeVint(99999)

        # CardCount
        self.writeVint(5)  # CSV ID
        self.writeVint(8)  # Resource ID
        self.writeVint(95)

        # MaxArena
        self.writeVint(5)   # CSV ID
        self.writeVint(27)  # Resource ID
        self.writeVint(12)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(self.Player.Gems)  # Player Gems
        self.writeVint(self.Player.Gems)  # Player Free Gems

        self.writeVint(self.Player.ExpPoints)  # Exp Points
        self.writeVint(self.Player.ExpLevel)   # Level

        self.writeVint(0)

        self.writeVint(1)  # is user in clan (1 = No, 9 = Yes)

        # Battle Statistics
        self.writeVint(0)  # Battles Played
        self.writeVint(0)  # Tourney Battles Played
        self.writeVint(0)
        self.writeVint(0)  # Wins
        self.writeVint(0)  # Loses

        self.writeVint(0)

        # Tutorials
        self.writeVint(7)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)

        self.writeNullVint()

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(1)

        self.writeVint(0)

        self.writeVint(1612095424)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

