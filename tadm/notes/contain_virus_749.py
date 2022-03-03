# https://leetcode.com/problems/contain-virus/
from heapq import heappush, heappop


class Solution:
    def __init__(self):
        self.infected = []
        self.m = 0
        self.n = 0
        self.cell_region_map = {}
        self.region_cell_map = {}
        # already walled cells
        self.walled_cells = {}
        self.region_count = 0

    def init(self, infected: list[list[int]]):
        self.infected = infected
        self.m = len(self.infected)
        self.n = len(self.infected[0])
        self.cell_region_map = {}
        self.region_cell_map = {}
        self.walled_cells = {}
        self.region_count = 0

    def h_key(self, i: int, j: int):
        return str(i) + '_' + str(j)

    # region_cell_map: region -> cells
    # cell_region_map: cell -> region
    # already fenced cells will be in walled_cells and excluded for later processing
    # row by row, forming and (possibly) merging each continuously contaminated region
    def form_regions(self):
        self.cell_region_map = {}
        self.region_cell_map = {}

        for i in range(self.m):
            j = 0
            while j < self.n:
                while j < self.n and (self.infected[i][j] == 0 or self.h_key(i, j) in self.walled_cells):
                    j += 1

                if j >= self.n:
                    continue

                # self.infected[i][j] == 1
                start = j
                j = start + 1
                while j < self.n and (self.infected[i][j] == 1 and self.h_key(i, j) not in self.walled_cells):
                    j += 1
                end = j - 1

                self.region_count += 1

                # [start, end] will be continuous and contaminated, forms a new region
                tmp = []
                for k in range(start, end + 1):
                    tmp.append((i, k))
                    key = self.h_key(i, k)
                    self.cell_region_map[key] = self.region_count
                self.region_cell_map[self.region_count] = tmp
                if i > 0:
                    region_to_merge = []
                    for k in range(start, end + 1):
                        key = self.h_key(i - 1, k)
                        if self.infected[i-1][k] == 1 and key not in self.walled_cells:
                            if self.cell_region_map[key] not in region_to_merge:
                                region_to_merge.append(self.cell_region_map[key])
                    # to merge
                    if len(region_to_merge) > 0:
                        # use current region_count, delete old
                        for r in region_to_merge:
                            r_cells = self.region_cell_map[r]
                            for (ci, ck) in r_cells:
                                key = self.h_key(ci, ck)
                                self.cell_region_map[key] = self.region_count
                                self.region_cell_map[self.region_count].append((ci, ck))

                            del self.region_cell_map[r]

    # calc the count of walls needed and neighboring normal cells which would fall victim next time
    def calc_threats_and_walls(self, heap: []):
        for k in self.region_cell_map.keys():
            threats = 0
            walls = 0
            array = self.region_cell_map[k]
            counted = {}
            for (i, j) in array:
                if j > 0 and self.infected[i][j-1] == 0:
                    key = self.h_key(i, j-1)
                    if key not in counted:
                        threats += 1
                        counted[key] = 1
                    walls += 1
                if (j + 1) < self.n and self.infected[i][j+1] == 0:
                    key = self.h_key(i, j+1)
                    if key not in counted:
                        threats += 1
                        counted[key] = 1
                    walls += 1
                if i > 0 and self.infected[i-1][j] == 0:
                    key = self.h_key(i-1, j)
                    if key not in counted:
                        threats += 1
                        counted[key] = 1
                    walls += 1
                if (i + 1) < self.m and self.infected[i+1][j] == 0:
                    key = self.h_key(i+1, j)
                    if key not in counted:
                        threats += 1
                        counted[key] = 1
                    walls += 1

            heappush(heap, (-threats, k, walls))

    # 1. build up contaminated regions
    # 2. calc threats and walls, prepare a max heap by threats (end loop when heap empty,
    #    meaning all contaminated cells were already fenced)
    # 3. mark walled cells
    # 4. do the evil, contaminate the possible victim
    # 5. jump to step 1
    # note: optimization can be done if we just merge regions instead of forming each loop
    def containVirus(self, isInfected: list[list[int]]) -> int:
        self.init(isInfected)

        # the final result, walls needed
        total_walls = 0

        while True:
            # form contaminated regions at the beginning of each loop
            self.form_regions()

            # calc a max heap of (threats, region, walls)
            # threats mean potential number of victim cells
            heap = []
            self.calc_threats_and_walls(heap)
            if len(heap) == 0:
                break

            # mark fenced cells
            (threats, r, walls) = heappop(heap)
            total_walls += walls
            cells = self.region_cell_map[r]
            for (i, j) in cells:
                key = str(i) + '_' + str(j)
                self.walled_cells[key] = r

            # do evil
            while len(heap) > 0:
                (threats, r, walls) = heappop(heap)
                array = self.region_cell_map[r]
                for (i, j) in array:
                    if j > 0 and self.infected[i][j-1] == 0:
                        self.infected[i][j-1] = 1
                    if (j+1) < self.n and self.infected[i][j+1] == 0:
                        self.infected[i][j+1] = 1
                    if i > 0 and self.infected[i-1][j] == 0:
                        self.infected[i-1][j] = 1
                    if (i+1) < self.m and self.infected[i+1][j] == 0:
                        self.infected[i+1][j] = 1

            # no need to del self.cell_region_map and self.region_cell_map
            # because it will auto-del in next run

        return total_walls


g = Solution()
s1 = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]] # 10
s2 = [[1,1,1],[1,0,1],[1,1,1]] # 4
s3 = [[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]] # 13
print(g.containVirus(s1))
print(g.containVirus(s2))
print(g.containVirus(s3))