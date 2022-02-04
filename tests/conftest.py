import pytest


@pytest.fixture(autouse=True)
def isolation(fn_isolation):
    pass


@pytest.fixture(scope="module")
def safe_token(accounts, safeERC20):
    yield accounts[0].deploy(safeERC20, "Token", "TKN", 18)


@pytest.fixture(scope="module")
def unsafe_token(accounts, unsafeERC20):
    yield accounts[0].deploy(unsafeERC20, "Token", "TKN", 18)
