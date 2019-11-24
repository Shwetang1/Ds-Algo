class Heap:
    '''
    Implementation of Heap ADT
    '''

    def __init__(self, heap_type="min", heap=None):
        if heap is None:
            self.heap = []
        else:
            self.heap = heap
        self.heap_type = heap_type

    def heapify(self, parent_node_index_to_heapify_from):
        """
        Top-down heapify --> Bubble down karna hoga ismein!
        :return:
        """
        if self.heap_type == "min":
            if len(self.heap) == 1:
                return
            parent_index = parent_node_index_to_heapify_from
            while 2 * parent_index < (len(self.heap) - 2):
                left_child = 2 * parent_index + 1
                right_child = 2 * parent_index + 2
                if self.heap[parent_index] >= self.heap[left_child]:
                    child_to_swap_with = left_child
                elif self.heap[parent_index] >= self.heap[right_child]:
                    child_to_swap_with = right_child
                else:
                    return
                self.heap[parent_index], self.heap[child_to_swap_with] = self.heap[child_to_swap_with], self.heap[
                    parent_index]
                parent_index = child_to_swap_with

        else:
            # TODO: Implement for max heap!
            pass

    def inverse_heapify(self, child_node_to_inverse_heapify_from):
        """
        Bottom-up heapify --> bubble up karna hoga ismein!
        :return:
        """
        pass

    def poll(self):
        """
        Remove min element from heap --> yeh heap sort mein use hoga!
        :return:
        """
        if len(self.heap) == 0:
            raise ValueError("Can't poll because heap is empty!")
        min_element = self.heap[0]

        if len(self.heap) > 1:
            last_element = self.heap.pop()
            self.heap[0] = last_element
            self.heapify(0)
        else:
            print("Polled element : {} !".format(self.heap[0]))
            return self.heap[0]
        print("Polled element : {} !".format(min_element))
        return min_element

    def find_and_remove(self):
        """
        Finds and removes an element
        :return:
        """
        pass

    def add(self, elem):
        """
        Adds element elem to the heap
        :param element:
        :return:
        """
        self.heap.append(elem)
        self.inverse_heapify(len(self.heap) - 1)

    def heap_sort(self):
        sorted_list = []
        heap_copy = self.heap.copy()
        while len(self.heap) > 0:
            sorted_list.append(self.poll())
        self.heap = heap_copy
        print("Sorted list is : {}".format(sorted_list))
        return sorted_list

    def __repr__(self):
        pass

    def __str__(self):
        return 'Heap : {}'.format(self.heap)


if __name__ == "__main__":
    h = Heap(heap=[0, 2, 3, 4, 5, 6, 4])
    h.poll()
    print(h)
    h.poll()
    print(h)
    h.poll()
    print(h)
    h.poll()
    print(h)
    h.poll()
    print(h)
    h.poll()
    print(h)
    h.poll()
    print(h)
