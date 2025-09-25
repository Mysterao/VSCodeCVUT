# matrix = [[1,2,3,4,5,6],[1,2,3,2,5,6],[3,1,2,3,5,7]]
# matrix = [[10,8,3,4,5,6],[10,8,3,2,5,6],[3,1,10,3,5,2]]
matrix = []

error = False
for i in range(3):
    n = input().split()
    player = list(map(int, n))
    matrix.append(player)
    if len(player) != len(matrix[0]):
        error = True
    for element in player:
        if element < 0:
            error = True

def take(matrix):
    points = [0, 0, 0]
    bank = 0

    for i in range(len(matrix[0])):
        first = matrix[0][i]
        second = matrix[1][i]
        third = matrix[2][i]
        biggest = max(first, second, third)

        get_points1 = False
        get_points2 = False
        get_points3 = False

        more_than_one = 0
        if first == biggest:
            more_than_one += 1
            get_points1 = True
        if second == biggest:
            more_than_one += 1
            get_points2 = True
        if third == biggest:
            more_than_one += 1
            get_points3 = True
        bank += 3
        if more_than_one == 1:
            if get_points1 == True:
                points[0] += bank
                bank = 0
            if get_points2 == True:
                points[1] += bank
                bank = 0
            if get_points3 == True:
                points[2] += bank
                bank = 0
    return points

if error == True:
    print("ERROR")
else:
    print(*take(matrix), sep = " ")