import pytest


class Test:

    @pytest.fixture(scope='class',autouse=True)
    def myfixture(self):
        print("my fixture is called")
    def test_method1(self):
        print("Method-1 is called")


    def test_method2(self):
        print("method-2 is called")