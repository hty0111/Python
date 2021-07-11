import unittest


def get_name(first, last, middle=''):
    if middle:
        name = first + ' ' + middle + ' ' + last
    else:
        name = first + ' ' + last
    return name


# 会运行每个test_开头的方法
class MyTestCase(unittest.TestCase):
    def test_fl_name(self):
        self.assertEqual(get_name('A', 'B'), 'A B')

    def test_fml_name(self):
        self.assertEqual(get_name('A', 'B', 'C'), 'A C B')


if __name__ == '__main__':
    unittest.main()
