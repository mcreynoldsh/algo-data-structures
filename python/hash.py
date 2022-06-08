from operator import truediv


class HashTable:
  def __init__(self, number_of_buckets):
    self.number_of_buckets = number_of_buckets
    self.table = {}
    

  def hash(self, value):
    hash = 0
    for i in value:
      hash = hash + ord(i)
    
    return hash % self.number_of_buckets

  def set(self, value):
    index = self.hash(value)
    self.table[str(index)] = value

  def get(self, value):
    index = self.hash(value)
    return self.table[str(index)]

  def has_key(self, value):
    key_list = self.table.keys()
    for x in key_list:
      if x == str(value):
        return True

    return False    


hash = HashTable(34)

hash.set("hello")
hash.set("there")
print(hash.get("hello"))
print(hash.has_key(22))

