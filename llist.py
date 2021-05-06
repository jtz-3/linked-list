class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

	def __repr__(self):
		return self.data

class LinkedList:

	# Builds a link list with the provided list or
	# leaves it empty if no list is given
	# Time: O(n) where n is the number of 
	#       items in the list
	def __init__(self, nodes=None):
		self.head = None
		self.tail = None

		if nodes is not None:
			node = Node(data=nodes.pop(0))

			self.head = node
			self.tail = Node(data=nodes[-1])

			for elem in nodes:
				node.next = Node(data=elem)
				node = node.next

	def __repr__(self):
		node = self.head
		nodes = []

		while node is not None:
			nodes.append(str(node.data))
			node = node.next

		nodes.append("None")
		return " -> ".join(nodes)
	
	def __iter__(self):
		node = self.head
		while node is not None:
			yield node
			node = node.next


	# Adds a node to the front of the LinkedList
	# Time: O(1)
	def add_first(self, node):

		if self.head is None:
			self.tail = node

		node.next = self.head
		self.head = node

	# Add a node to the back of the LinkedList
	# Time: O(1)
	def add_last(self, node):
		node.next = None

		if self.tail is not None:
			self.tail.next = node

		if self.head is None:
			self.head = node

		self.tail = node

	# Adds the specified node after the target data provided
	# Time: O(n)
	def add_after(self, target_node_data, new_node):
		if self.head is None:
			raise Exception("List is empty")

		for node in self:
			if node.data == target_node_data:
				new_node.next = node.next
				node.next = new_node

				# Update "tail" if necessary:
				if new_node.next is None:
					self.tail = new_node

				return

		raise Exception("Node with data '%s' not found" % target_node_data)

	# Adds the specified ndoe before the target data provided
	# Time: O(n)
	def add_before(self, target_node_data, new_node):
		if self.head is None:
			raise Exception("List is empty")

		if self.head.data == target_node_data:
			return self.add_first(new_node) # What is being returned here?

		prev_node = self.head

		for node in self:
			if node.data == target_node_data:
				prev_node.next = new_node
				new_node.next = node

				# Update head if necessary?
				if new_node.next is self.head:
					self.head = prev_node

				return
			prev_node = node

	# Removes the node with the target data
	# Time: O(n)
	def remove_node(self, target_node_data):
		if self.head is None:
			raise Exception("List is empty")

		if self.head.data == target_node_data:
			self.head = self.head.next
			return

		previous_node = self.head
		for node in self:
			if node.data == target_node_data:
				previous_node.next = node.next

				# Update head or tail if necessary
				if node is self.head:
					self.head = node.next

				if node is self.tail:
					self.tail = previous_node

				return
			previous_node = node

		raise Exception("Node with data '%s' is not found" % target_node_data)

llist = LinkedList()
print(repr(llist))

llist.add_first(Node("a"))
llist.add_last(Node("z"))
print(repr(llist))
print("Head is: " + llist.head.data)
print("Tail is: " + llist.tail.data)

llist.add_after("z", Node("b"))
print(repr(llist))
print("Tail is: " + llist.tail.data)

llist.add_before("z", Node(1))
print(repr(llist))
print("Head is: " + llist.head.data)

llist.remove_node("a")
print("Head is: " + str(llist.head.data))
print(repr(llist))

llist.remove_node("b")
print("Tail is: " + str(llist.tail.data))
print(repr(llist))

