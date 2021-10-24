import unittest
import user

class TestPerson(unittest.TestCase):
    def test_to_dict(self):
        p1 = Person(name='Phris Coskitt', title='HRH')
        self.assertEqual(p1.to_dict(), {
            'id': None,
            'name': 'Phris Coskitt',
            'title': 'HRH'}
        )