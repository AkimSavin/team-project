from enumes.power_up_type import PowerUpType
from power_Vverh import PowerdVverh


class Explosion:
    bombers = None

    def __init__(self, x, y, r):
        self.sourceX = x
        self.sourceY = y
        self.range = r
        self.time = 300
        self.frame = 0
        self.sectors = []

    def explode1(self, map, bombs, b, power_ups):

        self.bombers = b.bombers
        self.sectors.extend(b.sectors)
        bombs.remove(b)
        self.bomb_chain2(bombs, map, power_ups)

    def bomb_chain2(self, bombs, map, power_ups):

        for s in self.sectors:
            for x in power_ups:
                if x.pos_x == s[0] and x.pos_y == s[1]:
                    power_ups.remove(x)

            for x in bombs:
                if x.pos_x == s[0] and x.pos_y == s[1]:
                    map[x.pos_x][x.pos_y] = 0
                    x.bombers.bomb_limit += 1
                    self.explode1(map, bombs, x, power_ups)

    def clear_sectors(self, map, random, power_ups):

        for i in self.sectors:
            if map[i[0]][i[1]] == 2:
                r = random.randint(0, 9)
                if r == 0:
                    power_ups.append(PowerdVverh(i[0], i[1], PowerUpType.BOMB))
                elif r == 1:
                    power_ups.append(PowerdVverh(i[0], i[1], PowerUpType.FIRE))

            map[i[0]][i[1]] = 0

    def update(self, dt):

        self.time = self.time - dt

        if self.time < 100:
            self.frame = 2
        elif self.time < 200:
            self.frame = 1