import as_ikea
import unittest


class TestAsIkeaMethods(unittest.TestCase):

    def setUp(self):
        self.ikea_name = as_ikea.as_ikea('Abelev')
        self.replacement_occurrence = 1

    def test_is_latin(self):
        # latin string
        self.assertTrue(as_ikea.is_latin('Abelev'))
        # non-latin string
        self.assertFalse(as_ikea.is_latin('Абелев'))
        # mixed string
        self.assertFalse(as_ikea.is_latin('Абеlev'))

    def test_is_tanslit(self):
        # latin string
        self.assertFalse(as_ikea.is_translit('Abelev'))
        # russian string
        self.assertTrue(as_ikea.is_translit('Абелев'))
        # mixed string
        self.assertTrue(as_ikea.is_translit('Абеlev'))

    def test_convert_to_latin(self):
        # russian string
        s = as_ikea.to_latin('Абелев')
        self.assertTrue(as_ikea.is_latin(s))
        # mixed string
        s1 = as_ikea.to_latin('Абеlev')
        self.assertTrue(as_ikea.is_latin(s1))
        # mixed string 2
        s2 = as_ikea.to_latin('Abeлев')
        self.assertTrue(as_ikea.is_latin(s2))

    def test_abelev_reverse(self):
        self.assertTrue(self.ikea_name.startswith("V"))
        self.assertTrue(self.ikea_name[2] == "l")

    def test_replacement_occurrence(self):
        occurrence = 0
        for letter in self.ikea_name:
            if letter in [x for v in as_ikea.mapper.values() for x in v]:
                occurrence += 1
        self.assertEqual(self.replacement_occurrence, occurrence)
