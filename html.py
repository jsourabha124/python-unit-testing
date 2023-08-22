import unittest
import os
import HTMLTestRunner
import test_calc


# Get the Present Working Directory since that is the place where the report
# would be stored

current_directory = os.getcwd()

class HTML_TestRunner_TestSuite(unittest.TestCase):
    def test_unittestHTML(self):

        # Create a TestSuite comprising the two test cases
        consolidated_test = unittest.TestSuite()

        # Add the test cases to the Test Suite
        consolidated_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(test_calc.TestCalc),
        ])

        output_file = open(current_directory + "/HTML_Test_Runner_ReportTest.html", "w")

        html_runner = HTMLTestRunner.HTMLTestRunner(
            stream=output_file,
      
        )

        html_runner.run(consolidated_test)

if __name__ == '__main__':
    unittest.main()