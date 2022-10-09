import gzip
import json
import dotenv
import requests

def statNameFromId(awardId):
    with open('./localization/pl.json', 'r', encoding='utf-8') as jsonFile:
        localizationFile = json.load(jsonFile)
    if f'award.{awardId}.title' in localizationFile.keys():
        title = localizationFile[f'award.{awardId}.title']
        return title
    return 0

def UUIDtoNick(UUID):
    with open('./data/players.json', 'r', encoding='utf-8') as jsonFile:
        players = json.load(jsonFile)
    if UUID in players.keys():
        return players[UUID]['name']
    return 0

def sendCommands(commands):
    config = dotenv.dotenv_values('.env')
    headers = {
    'Accept': 'application/json',
    'Authorization': f'Bearer {config["PTER_API"]}',
    }
    for command in commands:
        data = {"command": command}
        requests.post(config['API_URL'], headers=headers, data=data)

def comparePlaceChange(newAwards):
    summary = json.load(gzip.open('./data/summary.json.gz','rb'))

    firstPlaceOld = {}
    firstPlaceNew = {}
    playersToNotify = {}

    for award in summary['awards']:
        if len(summary['awards'][award]) > 1:
            firstPlaceOld[award] = summary['awards'][award]['best']['uuid']

    for award in newAwards:
        if len(newAwards[award]) > 1:
            firstPlaceNew[award] = newAwards[award]['best']['uuid']

    for newAward, playerUUID in firstPlaceNew.items():
        if newAward not in firstPlaceOld or playerUUID != firstPlaceOld[newAward]:
            if playerUUID not in playersToNotify:
                playersToNotify[playerUUID] = []
            playersToNotify[playerUUID].append(newAward)

    return playersToNotify

def notifyPlayers(newAwards):
    playersToNotify = comparePlaceChange(newAwards)
    commands = []
    for player, awards in playersToNotify:
        nick = UUIDtoNick(player)

        if not nick:
            continue

        command = (
            'tellraw ' +
            UUIDtoNick(player) +
            ' [{"text":"§7Zająłeś/aś właśnie prowadzenie w statystykach: "}'
            )

        i = 0
        for award in awards:
            statName = statNameFromId(award)

            if not statName:
                continue

            i += 1
            command += (
                ',{"text":"§5' +
                statNameFromId(award) +
                '§7","clickEvent":{"action":"open_url","value":"https://serwerwanilia.pl/statystyki/#award:' +
                award +
                '"},"hoverEvent":{"action":"show_text","contents":["§5Link§7"]}}'
                )

            if i != len(playersToNotify[player]):
                command += ',{"text":"§7, "}'

        command += ']'
        commands.append(command)

    if commands:
        sendCommands(commands)
