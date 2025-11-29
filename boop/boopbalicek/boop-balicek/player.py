import base as BASE
import random, copy

"""
This file contains Player class, where you implement your player according the Boop rules.
To test your player, use section "if __name__ == "__main__" at the end of the file
You can run this file: python3 player.py, which should simulate a game of teo players and provide a set of png images.

However, this file does not verify if you play according to the rules or not. This functionality is on Brute only.
Anyway, if running this script produces an error, you have to fix it first before uploading to Brute.
Please do not use Brute as debugger tool :-)

"""


class Player(BASE.Base):
    def __init__(self, name, color):
        BASE.Base.__init__(self, color)     #we call constructor of the Base class first. Do not remove this line
        self.studentName = name             #parameter name will be filled with Brute and it contains your login
        self.studentTag = "Boop master"     #fill the name of your player/strategy/version etc.. 
    
    def insertplayer(self, player, color, playfield):
        y = player[0]
        x = player[1]
        player_rank = str(color)
        ranks = {"-1" : 1, "1" : 1, "-2" : 2, "2" : 2}
        i = -1
        while i != 2:
            tile_y = y+i
            # Test whether the index is not out of range:
            if tile_y >= 0 and tile_y < len(playfield):
                j = -1
                while j != 2:
                    tile_x = x+j
                    # Test whether the index is not out of range:
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

    def detect_triples(self, playfield, player):
        if player > 0:
            race = [1, 2]
        if player < 0:
            race = [-1, -2]
        # Horizontal count
        for i in range(len(playfield)):
            count = 0
            for j in range(len(playfield)):
                if playfield[i][j] != "0" and playfield[i][j] in race:
                    count += 1
                else:
                    if count = 3:
                        return triples = [(i, j-2), (i, j-1), (i, j)]
                    count = 0
            if count = 3:
                return triples = [(i, j-2), (i, j-1), (i, j)]
        # Vertical count
        for i in range(len(playfield)):
            count = 0
            for j in range(len(playfield)):
                if playfield[j][i] != "0" and playfield[j][i] in race:
                    count += 1
                else:
                    if count = 3:
                        return triples = [(i-2,j), (i-1,j), (i,j)]
                    count = 0
            if count = 3:
                return triples = [(i-2,j), (i-1,j), (i,j)]
        # Diagonal right to left count
        j = 0
        for i in range(3, -4, -1):
            count = 0
            if i < 0:
                j = abs(i)
            if i >= 0:
                k = i
            l = 0
            while l+j != 6 and l+k != 6:
                if playfield[l+j][l+k] != "0" and playfield[l+j][l+k] in race:
                    count += 1
                else:
                    if count = 3:
                        return triples = [(i-2,j+2), (i-1,j+1), (i,j)]
                    count = 0
                l += 1
            if count = 3:
                return triples = [(i-2,j+2), (i-1,j+1), (i,j)]
        # Diagonal left to right count
        k = 0
        for i in range(2, 9):
            count = 0
            if i <= 5:
                j = i
                k = 0
            if i > 5:
                k = i-5
                j = 5
            l = 0
            while j-l != -1 and l+k != 6:
                if playfield[l+k][j-l] != "0" and playfield[l+k][j-l] in race:
                    count += 1
                else:
                    if count = 3:
                        return triples = [(i-2,j-2), (i-1,j-1), (i,j)]
                    count = 0
                l += 1
            if count = 3:
                return triples = [(i-2,j-2), (i-1,j-1), (i,j)]
        return []
    
    def count_cats(self, playfield, color):
        # Function to check whether the number of cats on the board is has reached limit and player won
        if color > 0:
            cat = 2
        if color < 0:
            cat = -2
        counter = 0
        for i in range(len(playfield)):
            for item in playfield[i]:
                if item == cat:
                    counter += 1
        if counter == 8:
            return True
        else:
            return False

    def board_is_empty(self, playfield):
        i = 0
        empty = True
        while i != len(playfield):
            j = 0
            while j != len(playfield[i]):
                if playfield[i][j] != "0":
                    empty = False
                j += 1
            i += 1
        return empty
    
    # def lonely_kittens(self, playfield):

    def insertion_options_one(self, playfield, row, column)
        y = row
        x = column
        i = -1
        moves = []
        bestmove = False
        while i != 2 and bestmove == False:
            tile_y = y+i
            # Test whether the index is not out of range:
            if tile_y >= 0 and tile_y < len(playfield):
                j = -1
                while j != 2 and bestmove == False:
                    tile_x = x+j
                    # Test whether the index is not out of range:
                    if tile_x >= 0 and tile_x < len(playfield):
                        if tile_x == x and tile_y == y:
                            j += 1
                            continue
                        elif playfield[tile_y][tile_x] == "0" and tile_y-2*i >= 0 and tile_y-2*i <= len(playfield)-1 and tile_x-2*j >= 0 and tile_x-2*j <= len(playfield)-1:
                            if playfield[tile_y-2*i][tile_x-2*j] != "0" and (tile_y+i >= 0 or tile_y+i <= len(playfield)-1 or tile_x+j >= 0 or tile_x+j <= len(playfield)-1) and playfield[tile_y][tile_x] == "0":
                                bestmove = True
                                moves = []
                                moves.append((tile_y, tile_x))
                            else:
                                moves.append((tile_y, tile_x))
                    j += 1
            i += 1
        return moves

    def insertion_options_two(self, playfield, row, column)
        y = row
        x = column
        i = -1
        moves = []
        bestmove = False
        while i != 2 and bestmove == False:
            tile_y = y+i
            # Test whether the index is not out of range:
            if tile_y >= 0 and tile_y < len(playfield):
                j = -1
                while j != 2 and bestmove == False:
                    tile_x = x+j
                    # Test whether the index is not out of range:
                    if tile_x >= 0 and tile_x < len(playfield):
                        if tile_x == x and tile_y == y:
                            j += 1
                            continue
                        elif playfield[tile_y][tile_x] == "0" and tile_y-2*i >= 0 and tile_y-2*i <= len(playfield)-1 and tile_x-2*j >= 0 and tile_x-2*j <= len(playfield)-1:
                            if playfield[tile_y-2*i][tile_x-2*j] != "0" and (tile_y+i >= 0 or tile_y+i <= len(playfield)-1 or tile_x+j >= 0 or tile_x+j <= len(playfield)-1) and playfield[tile_y][tile_x] == "0":
                                bestmove = True
                                moves = []
                                moves.append((tile_y, tile_x))
                            else:
                                moves.append((tile_y, tile_x))
                    j += 1
            i += 1
        return moves

    def search_two_entities(self, color, playfield):
        if color < 0:
            race = [-1, -2]
        if color > 0:
            race = [1, 2]
        options_single = []
        options_double = []
        # Horizontal count
        for i in range(len(playfield)):
            count = 0
            for j in range(len(playfield)):
                if playfield[i][j] in race:
                    count += 1
                    # Only one search for good moves with single entity
                    if len(self.insertion_options(color, playfield, i, j)) != 0:
                        options_single.append(self.insertion_options(color, playfield, i, j))
                # Test for free spaces around double
                if count == 2
                    if j+1 < len(playfield) and playfield[i][j+1] == "0":
                        options_double.append((i,j+1))
                        return options_double
                    if j-2 > -1 and playfield[i][j-2] == "0":
                        options_double.append((i,j-2))
                        return options_double
                else:
                    count = 0
            # Test for free spaces around double
            if count == 2:
                if j-2 > -1 and playfield[i][j-2] == "0":
                        options_double.append((i,j-2))
                        return options_double
        # Vertical count
        for i in range(len(playfield)):
            count = 0
            for j in range(len(playfield)):
                if playfield[j][i] in race:
                    count += 1
                # Test for free spaces around double
                if count == 2:
                    if i+1 < len(playfield) and playfield[i+1][j] == "0":
                        options_double.append((i+1,j))
                        return options_double
                    if i-2 > -1 and playfield[i-2][j] == "0":
                        options_double.append((i-2,j))
                        return options_double
                else:
                    count = 0
            # Test for free spaces around double
            if count == 2:
                if i-2 > -1 and playfield[i-2][j] == "0":
                        options_double.append((i-2,j))
                        return options_double
        # Diagonal right to left count
        j = 0
        for i in range(3, -4, -1):
            count = 0
            if i < 0:
                j = abs(i)
            if i >= 0:
                k = i
            l = 0
            while l+j != 6 and l+k != 6:
                if playfield[l+j][l+k] in race:
                    count += 1
                # Test for free spaces around double
                if count == 2:
                    if i+1 < len(playfield) and j-1 < len(playfield) and playfield[i+1][j-1] == "0":
                        options_double.append((i+1,j-1))
                        return options_double
                    if i-2 > -1 and j+2 < len(playfield) and playfield[i-2][j+2] == "0":
                        options_double.append((i-2,j-2))
                        return options_double
                else:
                    count = 0
                l += 1
            # Test for free spaces around double
            if count == 2:
                if i-2 > -1 and j+2 < len(playfield) and playfield[i-2][j+2] == "0":
                        options_double.append((i-2,j-2))
                        return options_double
        # Diagonal left to right count
        k = 0
        for i in range(2, 9):
            count = 0
            if i <= 5:
                j = i
                k = 0
            if i > 5:
                k = i-5
                j = 5
            l = 0
            while j-l != -1 and l+k != 6:
                if playfield[l+k][j-l] in race:
                    count += 1
                # Test for free spaces around double
                if count == 2:
                    if i+1 < len(playfield) and j+1 < len(playfield) and playfield[i+1][j+1] == "0":
                        options_double.append((i+1,j+1))
                        return options_double
                    if i-2 > -1 and i-2 > -1 and playfield[i-2][j-2] == "0":
                        options_double.append((i-2,j-2))
                        return options_double
                else:
                    count = 0
                l += 1
            # Test for free spaces around double
            if count == 2:
                if i-2 > -1 and i-2 > -1 and playfield[i-2][j-2] == "0":
                    options_double.append((i-2,j-2))
                    return options_double

        if len(options_single)+len(options_double) == 0:
            options_single = self.insertion_options(color, playfield, 3, 3)
        if len(options_double) > 0:
            return options_double
        else:
            return options_double
    
    def remove_kitten(self, row, col, playfield):
        return playfield[row][col] = 0
            
    def play(self):
        if self.tournament:
            print(self.maxMoves) # Placeholder
        else:
            color = self.player
            kittens = self.kittens
            cats = self.cats
            move = []
            # Determine which entity to use----------------------------------------------------
            if cats > 0:
                if color > 0:
                    move.append(2)
                else:
                    move.append(-2)
            elif kittens > 0:
                if color > 0:
                    move.append(1)
                else:
                    move.append(-1)
            elif cats+kittens == 0:
                if self.count_cats(self.board, color):
                    return []
                # Insert a loop to search for lonely kittens
                row = "sth"
                col = "sth"
                animal = 10
                # newboard = copy.deepcopy(self.board)
                newboard = self.remove_kitten(row, col, copy.deepcopy(self.board))
                triple = []
            # ---------------------------------------------------------------------------------
            # Initial move. Activated only if player plays first
            if self.board_is_empty(self.board):
                row = 2
                col = 2
                animal = move[0]
                newboard = copy.deepcopy(self.board)
                newboard[2][2] == move[0]
                triple = []
                return [row, col, animal, newboard, triple]
            # ---------------------------------------------------
            #Phase 2 --------------------------------------------------
            else:
                moves = self.search_two_entities(color, self.board)
                move = 
                
            
            print(color)
            print(len(self.board))
            return []

    # -------------------------------------------------------------------------------------------------------------------------------------------


"""
PUT ALL YOUR TEST INTO THIS SECTION:

The simple game here assumes that you play correctly. There are no checks here if the moves are valid or not.

"""

if __name__ == "__main__":

    p1 = Player("Positive player",1)     #we create two instances of your player. One for +1 color
    p2 = Player("Negative player",-1)    #and second for the -1 color

    p1.kittens = 8                      #set up how many cats/kittens you have
    p1.cats = 0

    p2.kittens = 8                      #set this up for both player
    p2.cats = 0

    p1.otherCats = p2.cats              #these variables inform other player about your pieces
    p1.otherKittens = p2.kittens
    p2.otherCats = p1.cats
    p2.otherKittens = p1.kittens

    # p1.draw(p1.board, "base.png")       #draw (empty) board and save in into base.png
    
    moveIdx = 0                         #index of the move, also use to index images
    while True:
        move1 = p1.play()               #the first player is on move
        if len(move1) > 0:
            row, col, animal, newboard, triple = move1  #unpack the move
            isEnd = BASE.updatePlayer(p1,p2,newboard, row, col, animal, triple, "move-{:03d}-p1".format(moveIdx))  #update the players, and save image
            if isEnd:
                print(p1.studentName, "wins")
                break

        move2 = p2.play()               #the second player is on move
        if len(move2) > 0:
            row, col, animal, newboard, triple = move2  #unpack move
            isEnd = BASE.updatePlayer(p2,p1,newboard, row, col, animal, triple, "move-{:03d}-p2".format(moveIdx))
            if isEnd:
                print(p2.studentName,"wins")
                break

        if len(move1) == 0 and len(move2) == 0:
            print("Both players return []")
            break
        moveIdx += 1
        if moveIdx > 150:
            print("Maximum number of moves reached")
            break

print("End of game")