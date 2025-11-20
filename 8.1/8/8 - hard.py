player = input()
player = player.split()
player = list(map(int, player))
print(player)
"""
with open("/home/adam/Desktop/Local storage/6/8/ina_situacia.txt", "r") as subor:
"""
with open(r"C:\Users\adamj\Documents\VS Code projects\Python\8\modre.txt", "r") as subor:
    playfield = subor.readlines()
    for i in range(len(playfield)):
        playfield[i] = playfield[i].strip().split()
        print(playfield[i])
print()

def insertplayer(player, playfield):
    y = player[0]
    x = player[1]
    player_rank = str(player[2])
    ranks = {"-1" : 1, "1" : 1, "-2" : 2, "2" : 2}
    i = -1
    while i != 2:
        tile_y = y+i
        # Test whether the index isn´t out of range:
        if tile_y >= 0 and tile_y < len(playfield):
            j = -1
            while j != 2:
                tile_x = x+j
                # Test whether the index isn´t out of range:
                if tile_x >= 0 and tile_x < len(playfield):
                    if (tile_x == x and tile_y == y) or playfield[tile_y][tile_x] == "0":
                        j += 1
                        continue
                    # Move or erase a player if possible:
                    if ranks[playfield[tile_y][tile_x]] <= ranks[player_rank]:
                        if tile_y+i < 0 or tile_y+i > len(playfield)-1 or tile_x+j < 0 or tile_x+j > len(playfield)-1:
                            playfield[tile_y][tile_x] = "0"
                        elif playfield[tile_y+i][tile_x+j] == "0":
                            changed_element = playfield[tile_y][tile_x]
                            playfield[tile_y][tile_x] = "0"
                            playfield[tile_y+i][tile_x+j] = changed_element
                j += 1
        i += 1
    playfield[y][x] = player_rank
    return playfield


def add_another_player(player, playfield, i, j):
    player = [i, j, player[3]]
    return insertplayer(player, playfield)

def count_triples(playfield, player):
    ranks = {"-1" : "yellow", "1" : "blue", "-2" : "yelow", "2" : "blue"}
    player_rank = ranks[str(player[3])]
    overall_count = 0
    # Horizontal count
    for i in range(len(playfield)):
        count = 0
        for j in range(len(playfield)):
            if playfield[i][j] != "0" and ranks[playfield[i][j]] == player_rank:
                count += 1
            else:
                if count >= 3:
                    overall_count += (count//3+count%3)
                count = 0
        if count >= 3:
            overall_count += (count//3+count%3)

    # Vertical count
    for i in range(len(playfield)):
        count = 0
        for j in range(len(playfield)):
            if playfield[j][i] != "0" and ranks[playfield[j][i]] == player_rank:
                count += 1
            else:
                if count >= 3:
                    overall_count += (count//3+count%3)
                count = 0
        if count >= 3:
            overall_count += (count//3+count%3)
            
    # Diagonal lefto to right count
    i = 0
    j = len(playfield)-1
    while i != len(playfield)-1:
        count = 0
        while j != -1:
            if playfield[i][j] != "0" and ranks[playfield[i][j]] == player_rank:
                count += 1
            else:
                if count >= 3:
                    overall_count += (count//3+count%3)
                count = 0
            j -= 1
        if count >= 3:
            overall_count += (count//3+count%3)
        i += 1
    return overall_count


list = insertplayer(player, playfield)
for i in range(len(list)):
    print(list[i])

print()

"""
def main(playfield, player):
    matrix = insertplayer(player, playfield)
    triples = []
    coords = []
    for i in range(6):
        for j in range(6):
            if playfield[i][j] == "0":
                playfield_after_added = add_another_player(player, matrix, i, j)
                triple = count_triples(playfield_after_added, player)
                if triple != 0 and triple not in triples:
                    triples.append((triple))
                    coords.append((i,j))
                playfield[i][j] = "0"
            
    return triples, coords
            

print(main(playfield, player))
"""

triples = []
coords = []
for i in range(6):
    for j in range(6):
        original = [row[:] for row in insertplayer(player, playfield)]
        if playfield[i][j] == "0":
            playfield_after_added = add_another_player(player, original, i, j)
            triple = count_triples(playfield_after_added, player)
            if triple != 0:
                triples.append(triple)
                coords.append((i,j))
print(triples, coords)