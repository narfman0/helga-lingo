import json
from unittest import TestCase

class TestResults(TestCase):
    example_data = """{"tags":["black","tag1"],"list":[{"word":"what","definition":"definitionwhat"},{"word":"what2","definition":"definitionwhat2"}]}"""

    def setUp(self):
        from helga_lingo import plugin
        self.plugin = plugin

    def test_parse_args_simple(self):
        """ verify single arg works """
        term, idx = self.plugin.parse_args('testsimple')
        self.assertEqual(term, 'testsimple')

    def test_parse_args_dual(self):
        """ verify two args works """
        term, idx = self.plugin.parse_args('test simple')
        self.assertEqual(term, 'test%20simple')

    def test_parse_args_number(self):
        """ verify single arg with idx works """
        term, idx = self.plugin.parse_args('test 1')
        self.assertEqual(term, 'test')
        self.assertEqual(idx, 1)

    def test_parse_args_complex(self):
        """ verify complex args works """
        term, idx = self.plugin.parse_args('test complex 1')
        self.assertEqual(term, 'test%20complex')
        self.assertEqual(idx, 1)

    def test_define_first(self):
        """ verify the first definition is as it should be """
        data = json.loads(self.example_data)
        self.assertEqual(self.plugin.define('what', data), "definitionwhat")

    def test_define_first_id(self):
        """ verify the first definition by index is as it should be """
        data = json.loads(self.example_data)
        self.assertEqual(self.plugin.define('what', data, 1), "definitionwhat")

    def test_define_second(self):
        """ verify the second definition is as it should be """
        data = json.loads(self.example_data)
        self.assertEqual(self.plugin.define('what', data, 2), "definitionwhat2")
