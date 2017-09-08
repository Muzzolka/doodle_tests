from behave import given, when, then
from selenium.webdriver.common.keys import Keys
import page


@when(u'I enter occasion {occasion}')
def step_impl(context, occasion):
	context.page_object = context.page_object.enter_occasion(occasion)

@when(u'I click submit')
def step_impl(context):
	context.page_object = context.page_object.submit()

@when(u'I click close modal button')
def step_impl(context):
	context.page_object = context.page_object.click_close_modal_button()
	
@when(u'I enter location {location}')
def step_impl(context, location):
	context.page_object = context.page_object.enter_location(location)
	
@when(u'I click continue button')
def step_impl(context):
	context.page_object = context.page_object.click_continue_button()
	
@when(u'I choose date {day}')
def step_impl(context, day):
	context.page_object = context.page_object.choose_date(day)

@when(u'I enter credentials {name} {email}')
def step_impl(context, name, email):
	context.page_object = context.page_object.enter_credentials(name, email)
	
@when(u'I click finish button')
def step_impl(context):
	context.page_object = context.page_object.click_finish_button()
	
@then(u'I am on the finish page')
def step_impl(context):
	context.page_object = context.page_object.assert_is_text()
