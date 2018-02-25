from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# user goes to home page of the app
		self.browser.get("http://localhost:8000")

		self.assertIn('To-Do', self.browser.title)
		# user notices the page title and header mention to-do lists
		self.fail('Finish the test!')

		# user is invited to enter a to-do item straight away

		# user types "buy milk" into text box

		# user hits enter, the page updates and the new page lists
		# "1: Buy milk" as an item in a to-do list

		# There is still a text box asking her to add another item,
		# She enters "Buy tea"

		# The page updates again and now shows both items

		# User notices the site has generated a unique url, and
		# shows an explanation message

		# User vistis URL and the to-dist is still there


if __name__ == '__main__':
	unittest.main()