class Heap:
    '''
    Implementation of Heap ADT
    '''
    def __init__(self):
        self.heap = []

    def heapify(self,parent_node_to_heapify_from):
        """
        Top-down heapify
        :return:
        """
        pass

    def inverse_heapify(self,child_node_to_inverse_heapify_from):
        """
        Bottom-up heapify
        :return:
        """
        pass

    def poll(self):
        """
        Remove min element from heap
        :return:
        """
        if len(self.heap) == 0:
            raise ValueError("Can't poll because heap is empty!")
        min_element = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify(0)
        print("Polled element : {} !".format(min_element))
        return min_element

    def find_and_remove(self):
        """
        Finds and removes an element
        :return:
        """
        pass

    def add(self,elem):
        """
        Adds element elem to the heap
        :param element:
        :return:
        """
        self.heap.append(elem)
        self.inverse_heapify(len(self.heap)-1)

    def heap_sort(self):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass