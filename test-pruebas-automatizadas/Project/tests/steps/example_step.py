from behave import given, when, then

from framework.webapp import WebApp

from data.config import settings


@given(u'example')
def test_step_impl(context):
    web_app = WebApp(context.driver)
    web_app.load_website()


@when(u'example')
def test_step_impl(context):
    pass



