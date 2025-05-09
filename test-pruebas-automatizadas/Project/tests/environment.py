from framework.webapp import WebApp
from data.config import settings
import logging
import os
import traceback
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from behavex_images import image_attachments
from behavex_images.image_attachments import AttachmentsCondition
from selenium.common.exceptions import WebDriverException

logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def before_all(context):
    try:
        image_attachments.set_attachments_condition(context, AttachmentsCondition.ONLY_ON_FAILURE)
    except Exception as ex:
        logger.error(f"Error en before_all: {ex}")
        raise


def before_scenario(context, scenario):
    try:
        grid_url = 'http://selenium-hub:4444/wd/hub'
        browser = os.getenv("BROWSER", "chrome").lower()

        if browser == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument('--disable-gpu')
            options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})
        elif browser == 'firefox':
            options = webdriver.FirefoxOptions()
            options.log.level = "trace"
        else:
            raise ValueError(f"Navegador no soportado: {browser}")

        # Intentar crear el driver remoto
        driver = webdriver.Remote(
            command_executor=grid_url,
            options=options
        )

        driver.implicitly_wait(10)
        driver.set_script_timeout(30)

        context.driver = driver
        context.app = WebApp(driver)

        print(f"Escenario '{scenario.name}' ejecutándose en {browser.upper()}")

    except WebDriverException as ex:
        logger.error(f"❌ No se pudo crear una sesión WebDriver ({browser.upper()}): {ex}")
        raise
    except Exception as ex:
        logger.error(f"❌ Error en before_scenario: {ex}")
        raise
def after_step(context, step):
    if step.status == 'failed':
        try:
            image_attachments.attach_image_binary(context, context.driver.get_screenshot_as_png())
        except Exception as ex:
            logger.error(f"Error al adjuntar captura en after_step: {ex}")

def after_scenario(context, scenario):
    logger.info(f"Finalizando escenario: {scenario.name}")
    driver = getattr(context, 'driver', None)
    if driver:
        try:
            if scenario.status == 'failed':
                try:
                    logs = driver.get_log('browser') if 'goog:loggingPrefs' in driver.capabilities else []
                    for entry in logs:
                        logger.error(f"Log entry: {entry}")
                except Exception as log_error:
                    logger.error(f"Error al obtener logs del navegador: {log_error}")
            driver.quit()
        except Exception as e:
            logger.error(f"Error al cerrar el navegador: {e}")
            logger.error(traceback.format_exc())
        finally:
            context.driver = None
