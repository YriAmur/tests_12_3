import tests_12_3
import unittest


testST = unittest.TestSuite()
#calkST.addTest(unittest.makeSuite(test_calk.CalkTest))
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
testST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(testST)