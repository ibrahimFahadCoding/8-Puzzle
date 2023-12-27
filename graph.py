from typing import Any, Optional
from queue import PriorityQueue



class Node:
    _solvedBoard = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", " "]]
    _solvedBoardDict = {}

    def __init__(self, board: list[list[str]]) -> None:
        self.board = board
        self.neighbors = []
        self.width = len(board[0])
        self.height = len(board)
        if len(Node._solvedBoardDict) == 0:
            Node._cellMap()

    @classmethod
    def _cellMap(cls):
        for r, row in enumerate(cls._solvedBoard):
            for c, number in enumerate(row):
                cls._solvedBoardDict[number] = (r, c)

    def add_neighbor(self, board) -> None:
        self.neighbors.append(Node(board))

    def __lt__(self, other) -> bool:
        return self.board < other.board

    def __eq__(self, other) -> bool:
        if self.__class__ != other.__class__:
            return False
        return self.board == other.board

    def __hash__(self) -> int:
        return hash((self.board, self.neighbors, self.width, self.height))

    def copyBoard(self, board):
        newBoard = []
        for row in board:
            newlist = []
            for number in row:
                newlist.append(number)
            newBoard.append(newlist)
        return newBoard

    def _cloneBoardSwap(self, i: int, j: int) -> list[list[list[str]]]:
        movelist = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
        validMove = []
        for new_i, new_j in movelist:
            if not 0 <= new_i < self.height or not 0 <= new_j < self.width:
                continue
            cloneBoard = self.copyBoard(self.board)
            cloneBoard[new_i][new_j] = " "
            cloneBoard[i][j] = self.board[new_i][new_j]
            validMove.append(cloneBoard)
        return validMove

    def genNeighbors(self) -> None:
        indexEmpty = None
        for i, row in enumerate(self.board):
            for j, number in enumerate(row):
                if number == " ":
                    indexEmpty = (i, j)
                    break
            if indexEmpty is not None:
                break
        clonedBoards = self._cloneBoardSwap(*indexEmpty)

        for clone in clonedBoards:
            self.add_neighbor(clone)

    def __repr__(self) -> str:
        return f"Node(board = {self.board})\n"

    def __str__(self) -> str:
        string = ""
        for row in self.board:
            for number in row:
                string += f"{number} "
            string += "\n"
        return string

    def isSolved(self):
        return self.board == Node._solvedBoard

    def getH(self) -> int:
        if self.isSolved():
            return 0
        board_difference = 0
        for r, row in enumerate(self.board):
            for c, number in enumerate(row):
                row_difference = abs(r - Node._solvedBoardDict[number][0])
                column_difference = abs(c - Node._solvedBoardDict[number][1])
                board_difference += row_difference + column_difference
        return board_difference


class Graph:
    def __init__(self, board: list[list[str]]) -> None:
        self.startNode = Node(board)

    def aStar(self) -> tuple[Optional[list[Node]],int]:
        visited = []
        numNeighborsSeen = 0
        queue = PriorityQueue()
        queue.put((self.startNode.getH(), 0, self.startNode, [self.startNode]))
        while not queue.empty():
            _, depth, node, path = queue.get()
            numNeighborsSeen += 1
            if node in visited:
                continue
            visited.append(node)
            if node.isSolved():
                return path, numNeighborsSeen
            node.genNeighbors()
            g = depth + 1
            for neighbor in node.neighbors:
                h = neighbor.getH()
                f = g + h
                queue.put((f, g, neighbor, path + [neighbor]))
        return None, numNeighborsSeen

    def bfs(self) -> tuple[Optional[list[Node]],int]:
        visited = []
        numNeighborsSeen = 0
        queue = [(self.startNode, [self.startNode])]
        while len(queue) != 0:
            node, path = queue.pop(0)
            numNeighborsSeen += 1
            if node.isSolved():
                return path, numNeighborsSeen
            node.genNeighbors()
            for neighbor in node.neighbors:
                if neighbor in visited:
                    continue
                visited.append(neighbor)
                queue.append((neighbor, path + [neighbor]))
        return None, numNeighborsSeen

