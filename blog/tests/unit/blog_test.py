from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test title', 'Test author')

        self.assertEqual('Test title', b.title)
        self.assertEqual('Test author', b.author)
        self.assertListEqual([], b.post)
        # another way for above
        self.assertEqual(0, len(b.post))

    def test_repr_no_post(self):
        b = Blog('Test title', 'Test author')
        b1 = Blog('Make my day', 'Sreenuraj')

        self.assertEqual(b.__repr__(), "Test title by Test author (0 Posts)")
        self.assertEqual(b1.__repr__(), "Make my day by Sreenuraj (0 Posts)")

    def test_repr_with_posts(self):
        b = Blog('Test title', 'Test author')
        b1 = Blog('Make my day', 'Sreenuraj')
        b.post = ['test']
        b1.post = ['test', 'test1']

        self.assertEqual(b.__repr__(), "Test title by Test author (1 Post)")
        self.assertEqual(b1.__repr__(), "Make my day by Sreenuraj (2 Posts)")


