class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.childs = []

    def __getitem__(self, item):
        return self.childs[item]

    def insert(self, value):
        self.childs.append(value)

    @staticmethod
    def height1(top):
        '''
        Helper function
        :param top:
        :return:
        '''
        if len(top) and isinstance(top, list):
            heights = []
            for elem in top:
                if isinstance(elem, int):
                    heights.append(1)
                else:
                    heights.append(Node.height1(elem.childs) + 1)
            return max(heights)
        else:
            return 0

        while top is not None:
            heights = []
            if len(top.childs):
                for elem in top.childs:
                    heights.append(Node.height1(elem) + 1)
            if len(heights) == 0:
                return 1
            return max(heights)
        return 0

    def height(self):
        '''
        Return the height of tree
        :return: int
        '''
        return Node.height1(self.childs)