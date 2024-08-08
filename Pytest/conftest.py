
import pytest


@pytest.fixture(scope='function')
class Test01():
    def func(self):
        print("Geometry")