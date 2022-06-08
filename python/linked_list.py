class LinkList:
  
  def __init__(self):
    self.head = None
    self.length = 0
  
  def add(self, data):
    if self.head == None:
      self.head = Node(data)
      return
    
    current = self.head
    
    while current.next != None:
      current = current.next  
    
    current.next = Node(data)
  
  def remove(self, data):
    if self.head == None:
      return
    
    if(self.head.data == data):
      self.head = self.head.next
   
    current = self.head
   
    while current.next != None:
      if(current.next.data == data):
        current.next = current.next.next
        return
      current = current.next

  def get(self, element_to_get):
    current = self.head
    while current != None:
      if current.data == element_to_get:
        return current
      else:
        current = current.next  

  def display(self):
    current = self.head
    current_num = 1
    while current != None:
      print(f"{current_num}: {current.data}")
      current = current.next
      current_num = current_num + 1

# ----- Node ------
class Node:
  def __init__(self,data):
    self.next = None
    self.data = data
  
link_list = LinkList()
link_list.add("hello")
link_list.add("there")
link_list.add("node 3")
link_list.display()
link_list.remove("there")
link_list.display()