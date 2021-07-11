import unittest


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self, inc=5000):
        self.salary += inc
        return self.salary


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.employee = Employee('HTY', 10000)
        self.salary = [15000, 20000]

    def test_give_default_raise(self):
        self.assertIn(self.employee.give_raise(), self.salary)

    def test_give_custom_raise(self):
        self.assertIn(self.employee.give_raise(10000), self.salary)


if __name__ == '__main__':
    unittest.main()
