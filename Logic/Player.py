import json
class Players:
	
	HighID = 0
	LowID = 0
	Token = None

	Gold = 100000
	Gems = 100000
	ExpPoints = 10000
	ExpLevel = 13
	Name = "KiwiCabreaoo"


	events = [
		{
			"ID": 3001,
			"Type": 8,
			"StartTime": 1503298800,
			"EndTime": 1672470000,
			"VisibleOn": 1502694000,
			"JSON": '{"GameMode":"TeamVsTeamLadder","HideTimer":true,"HidePopupTimer":true,"ExtraGameMode":"None","ExtraGameModeChance":0}'
		},

		{
			"ID": 3002,
			"Type": 1,
			"StartTime": 1503298800,
			"EndTime":   1672470000,
			"VisibleOn": 1502694000,
			"JSON": '{"Title":"Free Diamonds Pack","Subtitle":"Have fun!","ShopOffers":[{"Title":"Free 100000 Gems","RewardsV2":[{"Gems":{"Gems":100000},"Type":"Gems"}],"NumTimesPurchasable":2,"Multiplier":1,"Image":{"Path":"/cca5cadb-acc2-477c-97a8-ee13c4c4e4f1_valentines_gift.png"},"PurchasedImage":{"Path":"/7d519f7d-8378-458a-af3f-108d26b2f2bd_valentines_gift_claimed.png"},"CostType":"Free","Template":"shop_item1_center_text"}],"IsSpecial":false,"HideTimer":true,"StartNotification":"Get your Free Diamonds Value Pack from the Shop!","EndNotification":"Still two hours left to get your Free Diamonds Value Pack from the Shop!"}'
		},

		{
			"ID": 3003,
			"Type": 5,
			"StartTime": 1503298800,
			"EndTime":   1672470000,
			"VisibleOn": 1502694000,
			"JSON": '{"GameMode":"Friendly","Title":"Random PvP Friendly","HideTimer":true,"Background":{"Path":"/474aac20-c8ce-4ad7-a216-d43f88bc0e6c_friendly_prodeck.png"}}'
		},

		{
			"ID": 3084,
			"Type": 5,
			"StartTime": 1503298800,
			"EndTime": 1672470000,
			"VisibleOn": 1502694000,
			"JSON": '{"GameMode":"Draft_Competitive","Title":"Triple Draft Friendly","HideTimer":true,"Background":{"Path":"/3ce0e2c9-3647-4eaf-876f-2ce8237e9b50_S5_tripledraft_friendly.png"},"DraftDeck":"Draft"}'
		},

		{
			"ID": 3088,
			"Type": 5,
			"StartTime": 1503298800,
			"EndTime": 1672470000,
			"VisibleOn": 1502694000,
			"JSON": '{"GameMode":"Draft_Competitive","Title":"Triple Draft Friendly","HideTimer":true,"Background":{"Path":"/3ce0e2c9-3647-4eaf-876f-2ce8237e9b50_S5_tripledraft_friendly.png"}}'
		},

		{
			"ID": 3096,
			"Type": 2,
			"StartTime": 1503298800,
			"EndTime": 1672470000,
			"VisibleOn": 1502694000,
			"JSON": '{"GameMode":"Touchdown_Draft","Title":"Touchdown Draft Challenge","Subtitle":"Have fun in the Touchdown Draft Challenge!","Description":"Come play the newest Challenge on Master Royale--voted on in our discord server!","StartNotification":"Touchdown Draft Challenge has begun! All free entries and big rewards! ","EndNotification":"Touchdown Draft Challenge ends soon! Come try it before it ends!","JoinCost":0,"JoinCostResource":"Gems","MaxLosses":3,"Rewards":[{"Gold":700,"Cards":10},{"Gold":1250,"Cards":25},{"Gold":2000,"Cards":65},{"Gold":3100,"Cards":125},{"Gold":4500,"Cards":210},{"Gold":6900,"Cards":335},{"Gold":11000,"Cards":550,"Milestone":{"IsHighlighted":true,"Chest":"Legendary","Type":"Chest"}}],"IconExportName":"icon_mode_touchdown","WinIconExportName":"tournament_open_wins_badge_gold","Arena":"All","UnlockedForXP":"Experienced","Background":{"Path":"/2b2456bd-85e6-43e4-ae57-c55cb36a2a5c_super_touchdown_challenge"},"Background_Complete":{"Path":"/2b2456bd-85e6-43e4-ae57-c55cb36a2a5c_super_touchdown_challenge"}}'
		},

		{
			"ID": 3007,
			"Type": 20,
			"StartTime": 1503298800,
			"EndTime": 1672470000,
			"VisibleOn": 1502694000,
			"JSON": '{"GameMode":"TeamVsTeamLadder","Background":{"Path":"/00d185b3-6a66-4590-b135-111db091acb9_party_mode_2v2.png"}}'
		},

		{
			"ID": 3085,
			"Type": 20,
			"StartTime": 1503298800,
			"EndTime": 1672470000,
			"VisibleOn": 1502694000,
			"JSON": '{"GameMode":"TripleElixir_Ladder","Background":{"Path":"/db964b91-8dc6-42ff-9dec-2c5ae8032003_party_mode_2v2_triple_elixir.png"}}'
		},

		{
			"ID": 3081,
			"Type": 20,
			"StartTime": 1503298800,
			"EndTime": 1672470000,
			"VisibleOn": 1502694000,
			"JSON": '{"GameMode":"Draft_Competitive","Background":{"Path":"/b8dac82d-ca3f-48ad-9e28-191ca853785d_party_mode_triple_draft.png"}}'
		},

		{
			"ID": 3009,
			"Type": 18,
			"StartTime": 1503298800,
			"EndTime": 1672470000,
			"VisibleOn": 1502694000,
			"JSON": '{"SeasonName":"Great Goblin Feast","SeasonNumber":1,"SeasonSC":{"Path":"/3b83c899-f5e6-4e5a-a134-fc91c68c5ceb_season_5_goblinparty_dl.sc","Checksum":"b24c3368f45c0e8dea627d1c18f708e6","File":"season_5_goblinparty_dl.sc"},"Arena":"Arena_Goblin_Party","TrophyRoadTemplate":"SeasonFeatRare","SeasonPassRewardTrackTemplate":"Pro_EarlyTowers","TierOverrides":{"TowerSkin":94000005,"FreeEmote":{},"Emote":{"EmotePackId":52,"EmoteIndex":0}},"GoldBankCapacity":0,"FeaturedSpells":[]}'
		},
	]


	chests = [
		{
			'ID': 384,
			'Status': 0,
			'Slot': 0
		},

		{
			'ID': 381,
			'Status': 0,
			'Slot': 1
		},

		{
			'ID': 382,
			'Status': 0,
			'Slot': 2
		},

		{
			'ID': 380,
			'Status': 0,
			'Slot': 3
		}
	 ]

	shopChests = [
		{
			'ID': 317,
			'Status': 88,
			'Slot': 0,
			'Name': 'Lightning'
		},

		{
			'ID': 329,
			'Status': 88,
			'Slot': 1,
			'Name': 'Fortune'
		},

		{
			'ID': 341,
			'Status': 88,
			'Slot': 2,
			'Name': 'Kings'
		}
	]


	shopCards = [
		{
			'ID': 14,
			'Multiplier': 50,
			'Cost': 2500
		},

		{
			'ID': 2,
			'Multiplier': 10,
			'Cost': 10000
		},

		{
			'ID': 3,
			'Multiplier': 1,
			'Cost': 1000
		}
	]



	def __init__(self, device):
		self.device = device