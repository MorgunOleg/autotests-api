import pytest


@pytest.mark.smoke
@pytest.mark.practice
def test_smoke_case():
    assert 1 + 1 == 2


@pytest.mark.practice
def test_regression_case():
    assert 2 * 2 == 4


@pytest.mark.fast
@pytest.mark.practice
def test_fast():
    pass


@pytest.mark.slow
@pytest.mark.practice
def test_slow():
    pass


@pytest.mark.practice
class TestUserAuthentication:

    @pytest.mark.skip(reason="Тестовая фикстура")
    @pytest.mark.smoke
    def test_login(self):
        pass

    @pytest.mark.slow
    def test_password_reset(self):
        pass

    def test_logout(self):
        pass


@pytest.mark.smoke
@pytest.mark.critical
@pytest.mark.practice
def test_critical_login():
    pass


@pytest.mark.api
@pytest.mark.practice
class TestUserInterface:

    @pytest.mark.skip(reason="Тестовая фикстура")
    @pytest.mark.smoke
    @pytest.mark.critical
    def test_login(self):
        pass

    def test_forgot_password(self):
        pass

    @pytest.mark.smoke
    def test_signup(self):
        pass


@pytest.mark.slow
@pytest.mark.practice
def test_heavy_calculation():
    pass


@pytest.mark.integration
@pytest.mark.practice
def test_integration_with_external_api():
    pass


@pytest.mark.smoke
def test_quick_check():
    pass
