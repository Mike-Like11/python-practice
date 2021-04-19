import unittest
from own_hash import HashTable


class TestHashTable(unittest.TestCase):
	def setUp(self):
		self.ht = HashTable()


	def test_hash(self):
		self.assertEqual(self.ht.hash("mike"), self.ht.hash("mike"))
		self.assertTrue(self.ht.hash("mike") < self.ht.capacity)


	def test_insert(self):
		self.ht.insert("key", "value")
		self.assertEqual(self.ht.size, 1)
		self.assertEqual(self.ht.buckets[self.ht.hash("key")].value, "value")


	def test_find(self):
		obj = "mike"
		self.ht.insert("nike", obj)
		self.assertEqual(obj, self.ht.find("nike"))
		obj = ["i love", "football"]
		self.ht.insert("hobby", obj)
		self.assertEqual(obj, self.ht.find("hobby"))


	def test_remove(self):
		obj = "19"
		self.ht.insert("age", obj)
		self.assertEqual(1, self.ht.size)
		self.assertEqual(obj, self.ht.remove("age"))
		self.assertEqual(0, self.ht.size)