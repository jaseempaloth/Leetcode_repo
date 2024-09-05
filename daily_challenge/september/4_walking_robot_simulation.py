# 874. Walking Robot Simulation
# Topics: Array, Hashtable, Simulation


class Solotion:
    def robot_sim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        x, y = 0, 0
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]] # N, E, S, W
        d = 0
        result = 0
        obstacles = {tuple(o) for o in obstacles}

        for c in commands:
            if c == -1:
                d = (d + 1) % 4
            elif c == -2:
                d = (d - 1) % 4
            else:
                dx, dy = direction[d]
                for _ in range(c):
                    if (x + dx, y + dy) in obstacles:
                        break
                    x, y = x + dx, y + dy
            
            result = max(result, x**2 + y**2)            
        return result
    
s = Solotion()

commands = [4,-1,4,-2,4]
obstacles = [[2, 4]]

print(s.robot_sim(commands, obstacles)) # 65