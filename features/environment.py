from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from selenium.webdriver.edge.options import Options
from selenium.webdriver import Edge
from selenium.webdriver.chrome.options import Options
from app.application import Application
from support.logger import logger
def browser_init(context,scenario_name):
    """
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)

    chrome_options = Options()
    mobile_emulation = {"deviceName": "iPhone 6"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # context.driver = webdriver.Chrome(service=service, options=chrome_options)
    # driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
    #                           desired_capabilities=chrome_options.to_capabilities())

    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    # Command to run tests with Allure & Behave:
    # behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/target_search.feature

    ## HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    ## BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    bs_user = 'santhipala_4GEnaz'
    bs_key = 'JY9EzQeoBJhApNp7NFLt'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # options = Options()
    # bstack_options = {
    #      "os" : "OS X",
    #     "osVersion" : "Big Sur",
    #     'browserName': 'safari',
    #     'sessionName': scenario_name,
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)
    context.driver = webdriver.Remote(command_executor=url, options=chrome_options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)
    logger.info(f'Started scenario:,{scenario.name}')


def before_step(context, step):
    print('\nStarted step: ', step)
    logger.info(f'Started step:,{step}')


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        logger.error(f'Step failed: {step}')


def after_scenario(context, feature):
    context.driver.quit()
