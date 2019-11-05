class UnionFind:
    def __init__(self,size):
        if size < 0:
            raise ValueError("number of elements cannot be 0 or negative!")
        self.num_components = size
        self.id = list(range(size))
        self.size = [1]*size

    def find(self,elem):
        '''

        :param elem:
        :return:
        '''
        root = elem
        while root != self.id[root]:  # Fining self loop. that will be the root
            root = self.id[root]
        return root
        # Do path compression! How?
        # TODO: Implement path compression!

    def is_connected(self,elem1,elem2):
        """
        Checks if two elements elem1 and elem2 are in the same component
        :param elem1:
        :param elem2:
        :return:
        """
        if self.find(elem1) == self.find(elem2):
            return True
        return False

    def component_size(self,elem):
        return self.size[self.find(elem)]

    def num_components(self):
        return self.num_components

    def union(self,elem1,elem2):
        root1 = self.find(elem1)
        root2 = self.find(elem2)
        if root1 == root2:
            return
        if self.size[root1] < self.size[root2]:
            self.size[root2]+=self.size[root1]
            self.id[root1] = root2
        else:
            self.size[root1] += self.size[root2]
            self.id[root2] = root1

        self.num_components -= 1

    def __str__(self):
        return "num_components :{}, id: {}, size: {}".format(self.num_components,self.id,self.size)


if __name__ == "__main__":
    uf = UnionFind(10)
    uf.union(0,1)
    print(uf)
    uf.union(2,3)
    print(uf)
    uf.union(4,5)
    print(uf)
    uf.union(6,7)
    print(uf)
    uf.union(8,9)
    print(uf)
    uf.union(9,6)
    print(uf)