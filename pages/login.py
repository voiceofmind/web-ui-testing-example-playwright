from playwright.sync_api import Page


class LoginPage:
    URL = "https://enotes.pointschool.ru/login"

    def __init__(self, page: Page) -> None:
        self.page = page

        self.login_field = page.locator('id=loginform-username')
        self.password_field = page.locator('id=loginform-password')
        self.submit_btn = page.locator('button[type="submit"][name="login-button"]')

        # other examples of locators:
        # self.submit_btn = page.locator('//button[@type="submit"][@name="login-button"]')
        # self.submit_btn = page.get_by_role("button", name="Вход")
        # self.submit_btn = page.locator('button').locator('nth=1')

    def load(self) -> None:
        self.page.goto(self.URL)
        self.page.wait_for_load_state()

    def submit_credentials(self, login: str = "test", password: str = "test") -> None:
        self.login_field.type(login)
        self.password_field.type(password)
        self.submit_btn.click()
