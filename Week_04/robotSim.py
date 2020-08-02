class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        direction = {
            'up': [0, 1, 'left', 'right'],
            'down': [0, -1, 'right', 'left'],
            'left': [-1, 0, 'down', 'up'],
            'right': [1, 0, 'up', 'down']
        }
        x, y = 0, 0
        dir = 'up'
        obstacles = set(map(tuple, obstacles))
        res = 0
        for com in commands:
            if com > 0:
                for step in range(com):
                    if (x + direction[dir][0], y + direction[dir][1]) not in obstacles:
                        x += direction[dir][0]
                        y += direction[dir][1]
                        res = max(res, x**2 + y**2)
                    else:
                        break
            elif com == -2:
                dir = direction[dir][2]
            elif com == -1:
                dir = direction[dir][3]
        return res