from src.riot_games_api import RiotGamesApi

token = input("API Token: ")
api = RiotGamesApi(token, "ru")
summoner_name = input("Summoner name: ")
account_id = api.summoner.get_summoner_by_name(summoner_name).account_id
match_id = api.match.get_matchlists(account_id).matches[0].game_id
match = api.match.get_match(match_id)
participant_id = next(i.participant_id for i in match.participant_identities if i.player.summoner_name == summoner_name)
print(match.participants[participant_id - 1].stats)
