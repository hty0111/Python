import unittest


class AnonymousSurvey:
    """收集匿名问卷的答案"""
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store(self, new_question):
        self.responses.append(new_question)

    def show_results(self):
        for response in self.responses:
            print(response)


class MyTestCase(unittest.TestCase):
    """针对类的测试"""
    def setUp(self):
        """创建一个对象和一组答案，供测试方法使用"""
        question = 'What language do you speak?'
        self.my_survey = AnonymousSurvey(question)              # 实例化
        self.responses = ['English', 'Spanish', 'Mandarin']     # 假定有三个response

    def test_store_single_response(self):
        self.my_survey.store(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_response(self):
        for response in self.responses:
            self.my_survey.store(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()
