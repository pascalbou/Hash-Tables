# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''

        hashed_key = 0
        for letter in key:
            hashed_key += ord(letter)

        return hashed_key

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Fill this in.
        '''
        hashed_index = self._hash_mod(key)

        # if there is nothing at this index, add the value
        if not self.storage[hashed_index]:
            self.storage[hashed_index] = LinkedPair(key, value)
        else:
            p = self.storage[hashed_index]
            # check the first key is it already exists
            if p.next == None:
                if p.key == key:
                    p.value = value
            # else check the key within the elements on the linked list
            else:
                while p.next:
                    if p.key == key:
                        p.value = value
                    p = p.next
            # add the value at the end of the linked list
            p.next = LinkedPair(key, value)

    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Fill this in.
        '''

        hashed_index = self._hash_mod(key)
        p = self.storage[hashed_index]
        value = ''

        if not p.key:
            print(f'This {key} does not exist')
            return None
        else:
            while p.key != key:
                p = p.next
            value = p.value
            p.value = None           

        return value

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Fill this in.
        '''
        hashed_index = self._hash_mod(key)
        p = self.storage[hashed_index]
        
        if not p.key:
            return None
        else:
            # search through the linked list while key is not found
            while p.key != key:
                p = p.next
            value = p.value

        return value

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Fill this in.
        '''
        self.capacity *= 2

        # saves old storage
        temp_storage = [None] * len(self.storage)
        for i in range(len(self.storage)):
            temp_storage[i] = self.storage[i]
        
        # erase storage and double its size
        self.storage = [None] * self.capacity

        # loop through old storage including all values in linked list and re-insert in new storage
        for i in range(len(temp_storage)):
            self.insert(temp_storage[i].key, temp_storage[i].value)
            p = temp_storage[i].next
            while p:
                self.insert(temp_storage[i].next.key, temp_storage[i].next.value)
                p = p.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
