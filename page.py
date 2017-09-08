from splinter import Browser

from selenium.webdriver.common.keys import Keys


class BasePageObject:
	def __init__(self, browser):
		self.browser = browser


class DoodleMain(BasePageObject):

	def enter_occasion(self, occasion):
		self.browser.find_by_id("d-pollCreationShortcutTitle").fill(occasion)
		return self

	def submit(self):
		self.browser.find_by_text("Create Doodle poll").click()
		return DoodleStep1(self.browser)


class DoodleStep1(BasePageObject):
	
	def click_close_modal_button(self):
		element = ".d-continueButton"
		self.browser.is_element_present_by_css(element, wait_time=15)
		self.browser.find_by_css(element).click()
		return self


	def enter_location(self, location):
		self.browser.find_by_id("d-pollLocation").fill(location)
		return self
		
	def click_continue_button(self):
		self.browser.find_by_css(".d-send").click()
		return DoodleStep2(self.browser)
		
class DoodleStep2(BasePageObject):
	
	def choose_date(self, day):
		element = "d-calendarContainer"
		self.browser.is_element_present_by_id(element, wait_time=15)
		self.browser.find_by_id(element).find_by_text(str(day)).click()
		return self
		
	def click_continue_button(self):
		self.browser.find_by_css(".d-send")[1].click()
		return DoodleStep3(self.browser)
		
class DoodleStep3(BasePageObject):
	
	def enter_credentials(self, name, email):
		self.browser.find_by_id("d-initiatorName").fill(name)
		self.browser.find_by_id("d-initiatorEmail").fill(email)
		return self
		
	def click_finish_button(self):
		self.browser.find_by_id("d-persistPollButton").click()
		return DoodleFinish(self.browser)

		
class DoodleFinish(BasePageObject):
	
	def assert_is_text(self):
		assert self.browser.find_by_css("input#d-pollLink[value^='https://doodle.com/poll/']")
		return self


 


if __name__ == "__main__":
	browser = Browser('firefox')
	browser.visit("https://beta.doodle.com/")

	page_object = DoodleMain(browser)
	page_object.enter_occasion('imprezka').submit().click_close_modal_button().enter_location("Wroclove").click_continue_button().choose_date(10).click_continue_button().enter_credentials("Gosia","m.staniszew@gmail.com").click_finish_button().assert_is_text()

