from selenium import webdriver
import unittest

class Myclass(unittest.TestCase):

    def setUp(self):
        print("before")
        self.driver = webdriver.Chrome()

    def tearDown(self):
        print("after")
        self.driver.quit()


    def test001(self):
        print("test001")
        self.driver.get("https://www.baidu.com")
        self.assertEqual(self.driver.title, "百度一下，你就知道")

if __name__ == "__main__":
    unittest.main()