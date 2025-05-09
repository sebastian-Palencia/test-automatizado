from behave import given, when, then
from framework.webapp import WebApp
from pages.example_page import example


@given(u'Me logueo en la plataforma')
def step_impl(context):
    web_app = WebApp(context.driver)
    web_app.load_website()
    context.example_test = example(context.driver)




@when(u'Escribo "{texto}" en face')
def step_impl(context,texto):
    context.example_test.user(texto.strip('"'))


@then(u'Valido la busqueda')
def step_impl(context):
    context.example_test.validador()

