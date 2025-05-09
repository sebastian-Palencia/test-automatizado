@Orangehrm
Feature: Registro de empleado orange HRM

@registro_1
Scenario: Logueo y creacion de empleado
    Given Me logueo en la plataforma
    When Ingreso el usuario "Admin"
    When Ingreso la contraseña "admin123"
    When Le doy click al boton de login
    When Ingreso al portal de orange HRM
    When Le doy click en el menu lateral izquierdo la opcion PIM
    When Le doy click a el boton de agregar nuevo empleado
    When Le doy click en "Create login details button"
    When Voy a registrar el nombre del empleado "Sebastian"
    When Voy a registrar segundo nombre de el empleado "Felipe"
    When Registrare el apellido "Palencia" del empleado
    When Registrare el id del empleado "0416"
    When Creo el nuevo usuario del empleado "srfeliche"
    When Creo el contraseña "Sfeliche47*" al empleado
    When Confirmo la creacion del contraseña"Sfeliche47*"
    When Le doy click al boton "Save" para guardar los datos del empleado
    When Valido la creacion de usuario con una card al lado que dice succesfull



