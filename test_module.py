import unittest
import demographic_data_analyzer

class DemographicAnalyzerTestCase(unittest.TestCase):
    def test_race_count(self):
        result = demographic_data_analyzer.calculate_demographic_data(False)
        self.assertTrue('White' in result['race_count'])

    def test_average_age_men(self):
        result = demographic_data_analyzer.calculate_demographic_data(False)
        self.assertAlmostEqual(result['average_age_men'], 39.4, delta=0.1)

if __name__ == "__main__":
    unittest.main()