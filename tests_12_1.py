import runner, unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        rn = runner.Runner('name')
        for i in range(10):
            rn.walk()
        self.assertEqual(rn.distance, 50)

    def test_run(self):
        rnr = runner.Runner('name')
        for i in range(10):
            rnr.run()
        self.assertEqual(rnr.distance, 100)

    def test_challenge(self):
        rn1 = runner.Runner('name')
        rn2 = runner.Runner('name')
        for i in range(10):
            rn1.run()
            rn2.walk()
        self.assertNotEqual(rn1.distance, rn2.distance)
