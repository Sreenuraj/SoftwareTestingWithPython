from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):

    def test_create_post(self):
        b = Blog('Test title', 'Test author')
        b.create_post('Test post', 'Test content')

        self.assertEqual(len(b.post), 1)
        self.assertEqual(b.post[0].title, 'Test post')
        self.assertEqual(b.post[0].content, 'Test content')

    def test_json_with_no_post(self):
        b = Blog('Test title', 'Test author')
        expected = {'title': 'Test title', 'author': 'Test author', 'posts': []}

        self.assertDictEqual(expected, b.json())

    def test_json_with_post(self):
        b = Blog('Test title', 'Test author')
        b.create_post('Test post', 'Test content')

        expected = {
            'title': 'Test title',
            'author': 'Test author',
            'posts': [{
                'title': 'Test post',
                'content': 'Test content'
            }]
        }

        self.assertDictEqual(expected, b.json())

