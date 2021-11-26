def rps_game_winner(array):
    if len(array) < 3:
        dict = {}
        for i in array:
            dict[i[1]] = i[0]
        if len(dict) == 1:
            return " ".join(array[0])
        elif len(dict) < 3:
            keys = list(dict.keys())
            if keys[0] == 'P' and keys[1] == 'S':
                return " ".join(array[1])
            elif keys[0] == 'S' and keys[1] == 'P':
                return " ".join(array[0])
            elif keys[0] == 'P' and keys[1] == 'R':
                return " ".join(array[0])
            elif keys[0] == 'R' and keys[1] == 'P':
                return " ".join(array[1])
            elif keys[0] == 'S' and keys[1] == 'R':
                return " ".join(array[1])
            elif keys[0] == 'R' and keys[1] == 'S':
                return " ".join(array[0])
            else:
                raise Exception("NoSuchStrategyError")
    else:
        raise Exception("WrongNumberOfPlayersError")


(rps_game_winner([['player1', 'R'], ['player2', 'S']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'S']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'P']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'A']]))
