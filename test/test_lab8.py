import unittest
from io import StringIO
import csv

from src import lab8

class TestMaxFlow(unittest.TestCase):
    def setUp(self):
        self.csv_data = """F1,F2
S1,S2
F1,X1,5
X1,S1,4
F2,X2,6
X2,S2,3
X1,X2,2
"""

        self.expected_max_flow = 7

        self.fake_file = StringIO(self.csv_data)
        self.rows = list(csv.reader(self.fake_file))
        self.fake_file.close()

    def test_read_csv(self):
        farms = [x.strip() for x in self.rows[0]]
        stores = [x.strip() for x in self.rows[1]]
        roads = []
        for row in self.rows[2:]:
            u, v, c = row[0].strip(), row[1].strip(), int(row[2].strip())
            roads.append((u, v, c))

        self.assertEqual(farms, ['F1', 'F2'])
        self.assertEqual(stores, ['S1', 'S2'])
        self.assertIn(('F1', 'X1', 5), roads)

    def test_graph_and_flow(self):
        farms = ['F1', 'F2']
        stores = ['S1', 'S2']
        roads = [
            ('F1', 'X1', 5),
            ('X1', 'S1', 4),
            ('F2', 'X2', 6),
            ('X2', 'S2', 3),
            ('X1', 'X2', 2)
        ]
        graph = lab8.build_graph(farms, stores, roads)
        result = lab8.edmonds_karp(graph, 'SRC', 'SNK')
        self.assertEqual(result, self.expected_max_flow)

    def test_zero_flow(self):
        farms = ['F1']
        stores = ['S1']
        roads = ['F1', 'X', 3],
        graph = lab8.build_graph(farms, stores, roads)
        result = lab8.edmonds_karp(graph, 'SRC', 'SNK')
        self.assertEqual(result, 0)

    def test_multiple_paths(self):
        farms = ['F1']
        stores = ['S1']
        roads = [
            ('F1', 'A', 3),
            ('F1', 'B', 4),
            ('A', 'S1', 2),
            ('B', 'S1', 2),
        ]
        graph = lab8.build_graph(farms, stores, roads)
        result = lab8.edmonds_karp(graph, 'SRC', 'SNK')
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()
