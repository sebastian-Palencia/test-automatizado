from behave import given, when, then
from framework.webapp import WebApp
from pages.orange_page import *


@given(u'Me logueo en la plataforma')
def step_impl(context):
    web_app = WebApp(context.driver)
    web_app.load_website()
    context.orange = login(context.driver)

@when(u'Ingreso el usuario "{user}"')
def step_impl(context,user):
    context.orange.user(user.strip('"'))


@when(u'Ingreso la contraseña "{contraseña}"')
def step_impl(context,contraseña):
    context.orange.contraseña(contraseña.strip('"'))



@when(u'Le doy click al boton de login')
def step_impl(context):
    context.orange.loginButton()


@when(u'Ingreso al portal de orange HRM')
def step_impl(context):
    context.orange.validaciondeportaldeorange()


@when(u'Le doy click en el menu lateral izquierdo la opcion PIM')
def step_impl(context):
    context.orange.pimmenubutton()


@when(u'Le doy click a el boton de agregar nuevo empleado')
def step_impl(context):
    context.orange.addemployed()


@when(u'Le doy click en "Create login details button"')
def step_impl(context):
    context.orange.create_login_details_button()


@when(u'Voy a registrar el nombre del empleado "{text}"')
def step_impl(context,text):
    context.orange.inputform(text.strip('"'),"//input[@placeholder='First Name']")


@when(u'Voy a registrar segundo nombre de el empleado "{text}"')
def step_impl(context,text):
    context.orange.inputform(text.strip('"'),"//input[@placeholder='Middle Name']")


@when(u'Registrare el apellido "{text}" del empleado')
def step_impl(context,text):
    context.orange.inputform(text.strip('"'),"//input[@placeholder='Last Name']")


@when(u'Registrare el id del empleado "{text}"')
def step_impl(context,text):
    context.orange.inputform(text.strip('"'),"//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']")


@when(u'Creo el nuevo usuario del empleado "{text}"')
def step_impl(context,text):
    context.orange.inputform(text.strip('"'),"(//input[@autocomplete='off'])[1]")


@when(u'Creo el contraseña "{text}" al empleado')
def step_impl(context,text):
    context.orange.inputform(text.strip('"'),"(//input[@type='contraseña'])[1]")


@when(u'Confirmo la creacion del Pasword "{text}"')
def step_impl(context,text):
    context.orange.inputform(text.strip('"'),"(//input[@type='contraseña'])[2]")


@when(u'Le doy click al boton "Save" para guardar los datos del empleado')
def step_impl(context):
    context.orange.clicksavebutton()


@when(u'Valido la creacion de usuario con una card al lado que dice succesfull')
def step_impl(context):
    pass