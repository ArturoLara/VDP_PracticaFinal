# -*- coding: UTF-8 -*-

import sys
sys.path.append("..")
from aplication.get_text_from_url import get_text_from_url
import unittest
import urllib2
from mock import patch


class tester_text_data_miner(unittest.TestCase):

    @patch('urllib2.urlopen')
    def test_short_tesx(self, mocked_f):
        mocked_f.return_value = "<p>Maravilloso</p>"
        result = get_text_from_url("mocked_url.html")
        assert result == [u'Maravilloso']

    @patch('urllib2.urlopen')
    def test_complex_text(self, mocked_f):
        mocked_f.return_value = "<p>Maravilloso</p> <p>Increible</p> <a> Esto no saldra </a>"
        result = get_text_from_url("mocked_url.html")
        assert result == [u'Maravilloso', u'Increible']

    def test_invalid_url(self):
        self.assertRaises(ValueError, get_text_from_url, "invalidUrl")

    def test_httpError(self):
        self.assertRaises(urllib2.URLError, get_text_from_url, "http://mentira.html")

if __name__ == '__main__':
    unittest.main()