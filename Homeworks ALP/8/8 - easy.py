player = input()
player = player.split()
player = list(map(int, player))
print(player)

# with open(r"C:\Users\adamj\Documents\VS Code projects\Python\Github repo local\8\situace.txt", "r") as subor:
with open(r"C:\Users\adamj\Documents\VS Code projects\Python\Github repo local\8\ina_situacia.txt", "r") as subor:
    playfield = subor.readlines()
    for i in range(len(playfield)):
        playfield[i] = playfield[i].strip().split()
        print(playfield[i])

def insertplayer(player, playfield):
    y = player[0]
    x = player[1]
    ranks = {"-1" : 1, "1" : 1, "-2" : 2, "2" : 2}
    i = -1
    while i != 2:
        tile_y = y+i
        # Test whether the index isn´t out of range
        if tile_y > 0 and tile_y < len(playfield)-1:
            j = -1
            while j != 2:
                tile_x = x+j
                # Test whether the index isn´t out of range:
                if tile_x > 0 and tile_y < len(playfield)-1:
                    if tile_x == x and tile_y == y:
                        j += 1
                        continue
                    if ranks[playfield[tile_y][tile_x]] >= ranks[player[2]]:
                        if tile_y+i < 0 or tile_y+i > len(playfield)-1 or tile_x+j < 0 or tile_x+j > len(playfield):
                            playfield.pop(playfield[tile_y+i][tile_x+j])
                else:
                    j += 1
        i += 1

print(insertplayer(player, playfield))