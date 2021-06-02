import page
from base.base import Base


class PageLogin(Base):
    def page_input_username(self, username):
        self.base_input(page.input_username, username)
    def page_input_password(self, password):
        self.base_input(page.input_password, password)
    def page_click_login(self):
        self.base_click(page.click_login)
    def page_login(self, username, password):
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login()