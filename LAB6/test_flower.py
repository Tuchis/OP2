import unittest
from flower import Flower, Tulip, Rose, Chamomile, FlowerSet, Bucket

# Реалізуйте клас Flower, що має три атрибути: color - колір, petals - кількість пелюсток та price - ціну.
#  Ваш клас повинен містити метод ініціалізації, де кожна змінна створюється відповідно до переданого для неї значення,
class TestFlower(unittest.TestCase):
    def test_flower_basics(self):
        fl = Flower('red', 5, 28)
        self.assertEqual(fl.color, 'red')
        self.assertEqual(fl.petals, 5)
        self.assertEqual(fl.price, 28)
#
#   а також методи, що відповідатимуть за те, що атрибуту об’єкта було присвоєно коректне значення
#  (кількість пелюсток - int, невід'ємне; вартість - int, невід'ємне; колір - str),
#   якщо значення неправильні - збуджувати виняток.`

    def test_correct_value(self):
        with self.assertRaises(TypeError):
            Flower(3, 5, 29).color_type_check()
        with self.assertRaises(ValueError):
            Flower("blue", 5.5, 29).value_check()
        with self.assertRaises(ValueError):
            Flower("blue", 5, -29).value_check()

    def test_inherited_classes(self):
        # Tulip
        tul = Tulip(10, 26)
        self.assertTrue(issubclass(Tulip, Flower))
        self.assertEqual(tul.color, 'pink')
        # Rose
        rose = Rose(15, 109)
        self.assertTrue(issubclass(Rose, Flower))
        self.assertEqual(rose.color, 'red')
        # Chamomile
        cham = Chamomile(20, 265)
        self.assertTrue(issubclass(Chamomile, Flower))
        self.assertEqual(cham.color, 'white')

    def test_flower_set_bucket(self):
        # First set
        flower_set_1 = FlowerSet()
        tul = Tulip(10, 26)
        rose = Rose(15, 109)
        flower_set_1.add_flower(tul)
        flower_set_1.add_flower(rose)
        flower_set_1.add_flower(Flower('blue', 50, 230))
        self.assertEqual(len(flower_set_1.flowers), 3)
        flower_set_1.add_flower(Flower('yellow', 2, 25))
        self.assertEqual(len(flower_set_1.flowers), 4)
        # Second set
        flower_set_2 = FlowerSet()
        flower_set_2.add_flower(rose)
        flower_set_2.add_flower(Flower('navy', 50, 230))
        flower_set_2.add_flower(Flower('gold', 120, 400))
        self.assertEqual(len(flower_set_2.flowers), 3)
        # Bucket
        bucket = Bucket()
        bucket.add_set(flower_set_1)
        bucket.add_set(flower_set_2)
        self.assertEqual(bucket.total_price(), 1129)
        self.assertEqual(len(bucket.bucket), 2)

if __name__ == "__main__":
    unittest.main()
