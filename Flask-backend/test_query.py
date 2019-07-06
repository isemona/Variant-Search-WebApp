import unittest # Or from unittest import TestCase
import query

class TestQuery(unittest.TestCase):
    def test_create_gene_dict(self):
        self.assertEqual(type(query.create_gene_dict('variants.tsv')), dict)

if __name__ == "__main__":
    unittest.main()
