from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# user is invited to enter a to-do item straight away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
			
		# user types "buy milk" into text box
		inputbox.send_keys('Buy milk')
		# user hits enter, the page updates and the new page lists
		# "1: Buy milk" as an item in a to-do list
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertTrue(any(row.text == '1: Buy milk' for row in rows))
		# There is still a text box asking her to add another item,
		# She enters "Buy tea"
		self.fail('Finish the test!')
		# The page updates again and now shows both items

		# User notices the site has generated a unique url, and
		# shows an explanation message

		# User vistis URL and the to-dist is still there


if __name__ == '__main__':
	unittest.main()