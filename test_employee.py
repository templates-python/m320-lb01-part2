import pytest

from department import Department
from employee import Employee


@pytest.fixture
def sut():
    return Employee("Max")


def test_creation(sut):
    assert True


def test_get_name(sut):
    assert sut.get_name() == "Max"


def test_eq(sut):
    assert sut == Employee("Max")


def test_str(sut):
    assert "Max" in sut.__str__()


def test_add_deparment(sut):
    dep1 = "Dep1"
    sut.add_department(Department(dep1))
    assert dep1 in sut.__str__()


def test_add_deparment_twice_has_no_effect(sut):
    dep1 = "Dep1"
    sut.add_department(Department(dep1))
    text = sut.__str__()
    sut.add_department(Department(dep1))
    assert text == sut.__str__()