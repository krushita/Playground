import traceback

class HashTable:
    def __init__(self):
        self.size = 0
        self.capacity = 10
        self._keys = []
        self.hash_table = [[] for i in range(self.capacity)]

    def hash_index(self, key):
        key_sum = 0
        for c in key:
            key_sum += ord(c)
        return key_sum % self.capacity

    def put(self, key, value):
        index = self.hash_index(key)
        hash_entries_list = self.hash_table[index]
        found = False
        for entry in hash_entries_list:
            if entry[0] == key:
                # Key found, overwrite the value
                entry[1] = value
                found = True
                break
        if not found:
                hash_entries_list.append([key, value])
                self._keys.append(key)
                self.size += 1

    def get(self, key):
        index = self.hash_index(key)
        hash_entries_list = self.hash_table[index]
        found = False
        for entry in hash_entries_list:
            if entry[0] == key:
                return entry[1]
        raise KeyError(key)

    def remove(self, key):
        index = self.hash_index(key)
        hash_entries_list = self.hash_table[index]
        found = False
        for entry in hash_entries_list:
            if entry[0] == key:
                hash_entries_list.remove(entry)
                self._keys.remove(key)
                self.size -= 1
                return
        raise KeyError(key)

    def keys(self):
        return self._keys
        

    def print_hash_table(self):
        for idx, hash_entries_list in enumerate(self.hash_table):
            print idx, ':' + '[' + ",".join([kv[0] + ':' + kv[1] for kv in hash_entries_list]) +']'


if __name__ == "__main__":

    htable = HashTable()

    # Add items in different slots
    htable.put('aaa', 'AAA')
    htable.put('bbb', 'BBB')
    htable.put('ccc', 'CCC')

    htable.print_hash_table()

    # Add items resulting in collisions
    htable.put('aba', 'ABA')
    htable.put('aab', 'AAB')
    htable.put('bab', 'BAB')
    htable.put('bba', 'BBA')

    htable.print_hash_table()

    # Add items resulting in overwrite
    htable.put('aaa', 'aaa')
    htable.put('aab', 'aab')

    htable.print_hash_table()
    
    # Remove item
    htable.remove('aab')
    htable.remove('ccc')
    # Remove non-existing item resulting in keyerror
    try:
        htable.remove('ddd')
    except KeyError, e:
        print str('KeyError! ddd does not exist')
        #traceback.print_exc()

    htable.print_hash_table()

