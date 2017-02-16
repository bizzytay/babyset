# test_babyset.py
import unittest

from baby_set import BabySet

class TestBabySetMethods(unittest.TestCase):
    #needed changes
    def test_init(self):
        bset = BabySet([2, 4, 4])
        self.assertEqual(bset.size(), 3)

    def test_init_empty(self):
        bset = BabySet()
        self.assertEqual(bset.size(), 0)
    #needed changes
    def test_add(self):
        bset = BabySet([2, 4, 4])
        bset.add(4)
        self.assertEqual(bset.size(), 3)
    #needed changes
    def test_addSeq(self):
        bset = BabySet([2, 4, 4])
        bset.addSeq([3, 4, 5,])
        self.assertEqual(bset.size(), 5)

    def test_get(self):
    	bset = BabySet([2, 4, 4])
        with self.assertRaises(KeyError):
            bset.get(3)

    def test_remove(self):
        baby = BabySet([2,2,4])
        with self.assertRaises(KeyError):
            baby.remove(6)

    def test_clear(self):
    	baby = BabySet([2,2,4])
        baby.clear()
        self.assertEqual(baby.size(),0)

if __name__ == '__main__':
    unittest.main()
