import unittest
from unittest.mock import Mock, patch
from main import (parse_rss_announcement, change_date_format, compare_date_info,
                  add_ascape_chararacter, format_message)


class TestMain(unittest.TestCase):
    @patch('main.feedparser.parse')
    def test_parse_rss_announcement(self, mock_parse):
        response = Mock()
        response.entries = [
            Mock(title='2023-2024 EĞİTİM ÖĞRETİM YILI GÜZ YARIYILI LİSANSÜSTÜ',
                 link='https://sbe.deu.edu.tr/duyurular/2023-2024-guz-yariyili',
                 updated='Mon, 19 Jun 2023 11:33:34 +0000')
        ]

        mock_parse.return_value = response

        expected = [{'title': '2023-2024 EĞİTİM ÖĞRETİM YILI GÜZ YARIYILI LİSANSÜSTÜ',
                     'link': 'https://sbe.deu.edu.tr/duyurular/2023-2024-guz-yariyili',
                     'updated': 'Mon, 19 Jun 2023 11:33:34 +0000'}]

        result = parse_rss_announcement()
        self.assertEqual(result, expected)


    def test_change_date_format(self):
        test_data = [{'title': '2023-2024 EĞİTİM ÖĞRETİM YILI GÜZ YARIYILI LİSANSÜSTÜ',
                     'link': 'https://sbe.deu.edu.tr/duyurular/2023-2024-guz-yariyili',
                      'updated': 'Mon, 19 Jun 2023 11:33:34 +0000'}]

        expected = [{'title': '2023-2024 EĞİTİM ÖĞRETİM YILI GÜZ YARIYILI LİSANSÜSTÜ',
                     'link': 'https://sbe.deu.edu.tr/duyurular/2023-2024-guz-yariyili',
                     'updated': '2023-06-19T11:33:34.000000Z'}]

        result = change_date_format(test_data)
        self.assertEqual(result, expected)


    def test_compare_date_info_is_not_null(self):
        test_date_info = '2023-05-16T13:10:30.000000Z'

        test_updated_date_list = [
            {'title': '2023-2024 EĞİTİM ÖĞRETİM YILI',
             'link': 'https://sbe.deu.edu.tr/duyurular/',
             'updated': '2023-06-19T11:33:34.000000Z'},
            {'title': 'Dokuz Eylül Üniversitesi Kariyer Günlükleri',
             'link': 'https://sbe.deu.edu.tr/duyurular/',
             'updated': '2023-05-16T13:10:30.000000Z'},
            {'title': 'MAXQDA ile Nitel Veri Analizi Semineri',
             'link': 'https://sbe.deu.edu.tr/duyurular/',
             'updated': '2023-03-10T09:56:57.000000Z'}
        ]

        expected = [
            {'title': '2023-2024 EĞİTİM ÖĞRETİM YILI', 
             'link': 'https://sbe.deu.edu.tr/duyurular/', 
             'updated': '2023-06-19T11:33:34.000000Z'}
        ]

        result = compare_date_info(test_date_info, test_updated_date_list)
        self.assertEqual(result, expected)
        self.assertEqual(len(result), 1)


    def test_compare_date_info_is_null(self):
        test_date_info = ''
        test_updated_date_list = [
            {'title': '2023-2024 EĞİTİM ÖĞRETİM YILI',
             'link': 'https://sbe.deu.edu.tr/duyurular/',
             'updated': '2023-06-19T11:33:34.000000Z'},
            {'title': 'Dokuz Eylül Üniversitesi Kariyer Günlükleri',
             'link': 'https://sbe.deu.edu.tr/duyurular/',
             'updated': '2023-05-16T13:10:30.000000Z'},
            {'title': 'MAXQDA ile Nitel Veri Analizi Semineri',
             'link': 'https://sbe.deu.edu.tr/duyurular/',
             'updated': '2023-03-10T09:56:57.000000Z'}
        ]

        expected = [{'title': 'MAXQDA ile Nitel Veri Analizi Semineri',
                     'link': 'https://sbe.deu.edu.tr/duyurular/',
                     'updated': '2023-03-10T09:56:57.000000Z'},
                    {'title': 'Dokuz Eylül Üniversitesi Kariyer Günlükleri',
                     'link': 'https://sbe.deu.edu.tr/duyurular/',
                     'updated': '2023-05-16T13:10:30.000000Z'},
                    {'title': '2023-2024 EĞİTİM ÖĞRETİM YILI',
                     'link': 'https://sbe.deu.edu.tr/duyurular/',
                     'updated': '2023-06-19T11:33:34.000000Z'}]

        result = compare_date_info(test_date_info, test_updated_date_list)
        self.assertEqual(result, expected)


    def test_add_ascape_chararacter(self):
        test_sorted_date_list = [
            {'title': '2023_2024 EĞİTİM ÖĞRETİM YILI GÜZ YARIYILI LİSANSÜSTÜ',
                'link': 'https://sbe.deu.edu.tr/duyurular/', 'updated': '2023-06-19T11:33:34.000000Z'},
            {'title': 'Dokuz Eylül Üniversitesi* Kariyer Günlükleri',
                'link': 'https://sbe.deu.edu.tr/duyurular/', 'updated': '2023-05-16T13:10:30.000000Z'},
            {'title': 'MAXQDA ile [Nitel Veri] Analizi Semineri',
                'link': 'https://sbe.deu.edu.tr/duyurular/', 'updated': '2023-03-10T09:56:57.000000Z'}
        ]

        expected = [{'title': '2023\\_2024 EĞİTİM ÖĞRETİM YILI GÜZ YARIYILI LİSANSÜSTÜ',
                     'link': 'https://sbe.deu.edu.tr/duyurular/', 'updated': '2023-06-19T11:33:34.000000Z'},
                    {'title': 'Dokuz Eylül Üniversitesi\\* Kariyer Günlükleri',
                        'link': 'https://sbe.deu.edu.tr/duyurular/', 'updated': '2023-05-16T13:10:30.000000Z'},
                    {'title': 'MAXQDA ile \\[Nitel Veri] Analizi Semineri',
                        'link': 'https://sbe.deu.edu.tr/duyurular/', 'updated': '2023-03-10T09:56:57.000000Z'}]

        result = add_ascape_chararacter(test_sorted_date_list)
        self.assertEqual(result, expected)


    def test_format_message(self):
        test_sorted_date_list = [{'title': '2023\\_2024 EĞİTİM ÖĞRETİM YILI',
                                  'link': 'https://sbe.deu.edu.tr/duyurular/',
                                  'updated': '2023-06-19T11:33:34.000000Z'},
                                 {'title': 'Dokuz Eylül Üniversitesi\\* Kariyer Günlükleri',
                                     'link': 'https://sbe.deu.edu.tr/duyurular/',
                                     'updated': '2023-05-16T13:10:30.000000Z'},
                                 {'title': 'MAXQDA ile \\[Nitel Veri] Analizi Semineri',
                                  'link': 'https://sbe.deu.edu.tr/duyurular/',
                                  'updated': '2023-03-10T09:56:57.000000Z'}]

        expected = [
            '📣 [2023\\_2024 EĞİTİM ÖĞRETİM YILI](https://sbe.deu.edu.tr/duyurular/)\n\n🗓 *Tarih:* 19-06-2023  11:33:34\n',
            '📣 [Dokuz Eylül Üniversitesi\\* Kariyer Günlükleri](https://sbe.deu.edu.tr/duyurular/)\n\n🗓 *Tarih:* 16-05-2023  13:10:30\n',
            '📣 [MAXQDA ile \\[Nitel Veri] Analizi Semineri](https://sbe.deu.edu.tr/duyurular/)\n\n🗓 *Tarih:* 10-03-2023  09:56:57\n'
        ]

        result = format_message(test_sorted_date_list)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
