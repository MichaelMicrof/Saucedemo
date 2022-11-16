import pytest
import random

from pages.login_page import LoginPage
from pages.main_page import MainPage
from locators.login_locators import LoginLocators as ll
from locators.main_locators import MainLocators as ml


class TestSample:
    login_list = ['standard_user', 'locked_out_user', 'problem_user', 'performance_glitch_user']
    password = 'secret_sauce'

    @pytest.mark.parametrize(
        'username, password',
        [('standard_user', 'secret_sauce'),
         ('problem_user', 'secret_sauce'),
         # pytest.param('locked_out_user', 'secret_sauce', marks=[pytest.mark.basic, pytest.mark.xfail], id='First_ID'),
         # pytest.param('performance_glitch_user', 'secret_sauce', marks=pytest.mark.basic, id="Second_ID"),
         ],
    )
    def test_logins(self, username, password):
        lp = LoginPage(self.driver)
        assert lp.login_title() == ll.title
        lp.action_login(username, password)
        lp.action_logout()
        assert lp.login_title() == ll.title

    def test_login_from_list(self):
        username = random.choice(self.login_list)
        lp = LoginPage(self.driver)
        lp.action_login(username, self.password)
        mp = MainPage(self.driver)
        assert mp.get_header().casefold() == ml.product_title.casefold()
