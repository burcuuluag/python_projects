import unittest
from unittest.mock import Mock, patch
from main import (get_feed_rss, compare_ids, format_message)
from datetime import datetime
import time

class TestMain(unittest.TestCase):
    @patch('main.feedparser.parse')
    def test_get_feed_rss(self, mock_parse):
        response = Mock()
        response.entries = [
            Mock(title = 'This is a first title',
                 link = 'https://news.google.com/rss/articles',
                 guid = '2163875973',
                 published = 'Wed, 21 Jun 2023 07:15:00 GMT',
                 published_parsed=time.struct_time((2023, 6, 21, 7, 15, 0, 2, 172, 0)))
        ]

        mock_parse.return_value = response

        expected = [{'title': 'This is a first title',
                    'link': 'https://news.google.com/rss/articles',
                    'guid': '2163875973',
                    'published': 'Wed, 21 Jun 2023 07:15:00 GMT',
                    'published_parsed': time.struct_time((2023, 6, 21, 7, 15, 0, 2, 172, 0))}]

        result = get_feed_rss()
        self.assertEqual(result, expected)


    def test_compare_ids_if_ids_list_is_none(self):
        test_ids_info = None
        test_entry_list = [
            {
                "guid": '2163875973',
                "published_parsed": (2023, 6, 21, 7, 15, 0, 2, 172, 0)
            },
            {
                "guid": '2163875974',
                "published_parsed": (2023, 6, 20, 13, 34, 0, 1, 171, 0)
            }
        ]

        expected = [
            {
                "guid": '2163875973',
                "published_parsed": (2023, 6, 21, 7, 15, 0, 2, 172, 0)
            },
            {
                "guid": '2163875974',
                "published_parsed": (2023, 6, 20, 13, 34, 0, 1, 171, 0)
            }
        ]

        result = compare_ids(test_ids_info, test_entry_list)
        self.assertEqual(result, expected)


    def test_format_message(self):
        test_data = [
            {
                "title": "this is a first title",
                "link": "https://news.google.com/rss/articles",
                "guid": '2163875973',
                "published_parsed": 'Thu, 22 Jun 2023 07:58:32 GMT'
            }
        ]

        expected = ['[this is a first title](https://news.google.com/rss/articles)\n']
        result = format_message(test_data)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()