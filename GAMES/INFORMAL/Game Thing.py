from os import system as cmd
from sys import platform
from random import randint as rand
from math import floor

SIZE_OF_GRID = [32, 32]

EMPTY  = 0
FOOD   = 1
PLAYER = 2
WALL   = 3
AI     = 4
ENEMY  = 5


NORTH = 0
WEST  = 1
EAST  = 2
SOUTH = 3

population = {
    EMPTY: 0,
    FOOD: 0,
    PLAYER: 0,
    WALL: 0,
    AI: 0,
    ENEMY: 0
}

grid = [[0 for _ in range(SIZE_OF_GRID[0])] for _ in range(SIZE_OF_GRID[1])]

organisms = []

class Organism:
    def __init__(self, pos, type) -> None:
        # pos: int[2]
        # type: int

        self.type = type

        population[type] += 1

        self.needs = {"food": 50}
        self.food_eaten = 0
        self.target = None

        self.set_pos(pos)

        if self.type == ENEMY:
            self.set_target(AI)
        else:
            self.set_target(FOOD)

        organisms.append(self)

    def set_pos(self, pos):
        x, y = pos
        grid[x][y] = self.type
        self.pos = pos

    def drain_needs(self):
        for i in self.needs:
            self.needs[i] -= 1
            if self.needs[i] <= 0:
                self.kill(self)
                return

    def kill(self, target):
        population[target.type] -= 1
        if (population[target.type] < 0):
            population[target.type] = 0

        target.type = EMPTY
        target.set_pos(self.pos)
        try:
            organisms.remove(target)
        except Exception:
            pass

    def move(self, dir, times = 0):
        x, y = self.pos
        old_x, old_y = self.pos

        if dir == NORTH:
            x -= 1
        elif dir == WEST:
            y -= 1
        elif dir == EAST:
            y += 1
        elif dir == SOUTH:
            x += 1
        
        if x < 0:
            x = len(grid) - 1
        if y < 0:
            y = len(grid[x]) - 1
        if x > len(grid) - 1:
            x = 0
        if y > len(grid[x]) - 1:
            y = 0

        cell = grid[x][y]

        if cell != EMPTY:
            if cell == FOOD and self.type != ENEMY:
                self.eat([x, y])
            elif cell == AI:
                if self.type == ENEMY:
                    self.eat([x, y])
                else:
                    self.kill(self)
            elif cell == ENEMY:
                if self.type == ENEMY:
                    self.eat([x, y])
            else:
                if times < 500:
                    self.move(rand(0, 3), times + 1)
                else:
                    self.kill(self)

        self.set_pos([x, y])
        grid[old_x][old_y] = EMPTY

        return True

    def set_target(self, target):
        if population[target] == 0:
            return False

        x = rand(0, len(grid) - 1)
        y = rand(0, len(grid[x]) - 1)

        tries = 0
        while grid[x][y] != target:
            if tries > 9999:
                return False

            x = rand(0, len(grid) - 1)
            y = rand(0, len(grid[x]) - 1)
            tries += 1

        self.target = [x, y]

        return True

    def move_towards_target(self, target):
        if self.target is None or population[target] == 0:
            if not self.set_target(target):
                self.move(rand(0, 3))

                return False
            else:
                return self.move_towards_target(target)

        px, py = self.pos
        tx, ty = self.target

        if grid[tx][ty] != target:
            self.target = None
            if not self.set_target(target):
                self.move(rand(0, 3))
            else:
                self.move_towards_target(target)

        elif px > tx:
            self.move(NORTH)
        elif px < tx:
            self.move(SOUTH)
        elif py > ty:
            self.move(WEST)
        elif py < ty:
            self.move(EAST)

        if self.pos == self.target:
            self.target = None

            if self.type == ENEMY:
                if rand(0, 1) == 0:
                    self.set_target(AI)
                else:
                    self.set_target(ENEMY)
            else:
                self.set_target(FOOD)

    def reproduce(self):
        x, y = get_random_position()

        offspring = Organism([x, y], self.type)
        offspring.move(rand(0, 3))

        return True

    def eat(self, pos):
        x, y = pos

        if grid[x][y] != FOOD and self.type != ENEMY:
            print("ERROR: Can only eat food!")
            return False

        for i in organisms:
            if i.pos == pos:
                self.kill(i)
                return

        self.needs["food"] += 10
        self.food_eaten += 1

        population[grid[x][y]] -= 1
        if (population[grid[x][y]] < 0):
            population[grid[x][y]] = 0

        if self.food_eaten % 2 == 0:
            self.reproduce()

        return True

    def betray(self):
        a = self.type

        if self.type == AI:
            self.type = ENEMY
            self.set_target(AI)
        #elif self.type == ENEMY:
        #    self.type = AI
        #   self.set_target(FOOD)

        population[a] -= 1
        population[self.type] += 1
        
        if (population[a] < 0):
            population[a] = 0


CLEAR = "cls" if platform == "win32" else "clear"

def get_random_position():
    x = rand(0, len(grid) - 1)
    y = rand(0, len(grid[x]) - 1)

    while grid[x][y] != EMPTY:
        x = rand(0, len(grid) - 1)
        y = rand(0, len(grid[x]) - 1)

    return [x, y]

plr = Organism(pos=get_random_position(), type=PLAYER)

Organism(pos=get_random_position(), type=AI)
#Organism(pos=get_random_position(), type=ENEMY)

plr.kill(plr)

step = 0

autorun = False
autorun_finished_gen = 1000
autorun_started = 0

render_bool = True

def render():
    cmd(CLEAR)

    gen_text = f"=== Gen {floor(step * 0.1)} ==="

    print(f"{'=' * len(gen_text)}\n{gen_text}\n{'=' * len(gen_text)}\n")

    for i in grid:
        res = ""
        for v in i:
            if v == EMPTY:
                res += " "
                continue
            res += f"{v}"
        print(res[:-2])

    print()

    try:
        if plr.type == PLAYER:
            print(f"FOOD: {plr.needs['food']}\n")
    except NameError:
        pass
    
    print("POPULATION:")
    for i in population:
        type = ""

        if i == EMPTY:
            type = "EMPTY "
        elif i == FOOD:
            type = "FOOD  "
        elif i == PLAYER:
            type = "PLAYER"
        elif i == WALL:
            type = "WALL  "
        elif i == AI:
            type = "AI    "
        elif i == ENEMY:
            type = "ENEMY "

        print(f"{type}: {population[i]}")

def main():
    global step, autorun, render_bool, autorun_started, autorun_finished_gen

    while True:
        if step > autorun_started + (autorun_finished_gen * 10):
            autorun = False

        population[EMPTY] = 0

        for i in grid:
            for v in i:
                if v == EMPTY:
                    population[EMPTY] += 1

        if render_bool:
            render()
        
        command = ""

        if not autorun:
            command = input("\n>> ").lower()

        if command == "w":
            plr.move(NORTH)
        elif command == "s":
            plr.move(SOUTH)
        elif command == "a":
            plr.move(WEST)
        elif command == "d":
            plr.move(EAST)
        elif command.startswith("autorun"):
            command = command.split(" ")
            if len(command) > 1:
                autorun_finished_gen = int(command[1])

            autorun_started = step
            autorun = True
        elif command == "render":
            render_bool = not render_bool

        for i in organisms:
            if i != plr:
                if i.type == ENEMY:
                    i.move_towards_target(AI)
                else:
                    i.move_towards_target(FOOD)
            i.drain_needs()

            if i.needs["food"] < 20:
                if rand(1, 2) == 1:
                    i.betray()

        for _ in range(1):
            x, y = get_random_position()

            grid[x][y] = FOOD
            population[FOOD] += 1

            if population[AI] < 1:
                x, y = get_random_position()

                grid[x][y] = AI

        step += 1
        

if __name__ == "__main__":
    main()
    