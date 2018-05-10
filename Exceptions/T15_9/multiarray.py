import ex15_9
import copy


class MultiArray:
    def __init__(self, data):
        self._data = {}
        if isinstance(data, (list, tuple, str)):
            for item in data:
                self.add_item(item)
        elif isinstance(data, dict):
            self._data = copy.copy(data)
        elif isinstance(data, MultiArray):
            self._data = copy.copy(data._data)
        else:
            raise ex15_9.WrongDataType(type(data))

    def add_item(self, item):
        if item in self._data:
            self._data[item] += 1
        else:
            self._data[item] = 1

    def get_item(self, item):
        if item in self._data:
            self._data[item] -= 1
            if self._data[item] == 0:
                del self._data[item]
        else:
            raise ex15_9.ItemError(item)

    def set_item(self, item, count):
        self._data[item] = count

    def del_item(self, item):
        del self._data[item]

    def make_empty(self):
        self._data = {}

    def is_empty(self):
        if self._data is {}:
            return True
        else:
            return False

    def count_item(self, item):
        if item in self._data:
            return self._data[item]
        else:
            return 0

    def get_data(self):
        return self._data

    def __repr__(self):
        return str(self._data)

    def union(self, other):
        _union = MultiArray(self)
        for item in other.get_data():
            if _union.count_item(item) < other.count_item(item):
                _union.set_item(item, other.count_item(item))
        return _union

    def intersect(self, other):
        _intersect = MultiArray([])
        for item in self.get_data():
            if item in other.get_data():
                _count = min(self.count_item(item), other.count_item(item))
                _intersect.set_item(item, _count)
        return _intersect

    def __eq__(self, other):
        return self._data == other.get_data()

    def __le__(self, other):
        _flag = True
        for item in self._data:
            if item not in other.get_data() or self.count_item(item) > other.count_item(item):
                _flag = False
                break
        return _flag
