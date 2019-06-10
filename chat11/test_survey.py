import unittest
from survey import AnonymousSurvey
class TestAnonmousSurvey(unittest.TestCase):
    def test_store_single_response(self):
        question = "what language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

unittest.main()