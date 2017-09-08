from splinter import Browser
from page import DoodleMain

def before_scenario(context, scenario):
	context.browser = Browser('firefox')
	context.browser.visit("https://beta.doodle.com/")
	context.page_object = DoodleMain(context.browser)
	
def after_scenario(context, scenario):
	context.browser.quit()