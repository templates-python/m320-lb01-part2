import pytest

from department import Department
from employee import Employee


@pytest.fixture
def sut():
    return Department("Dep1")


def test_creation(sut):
    assert True


def test_get_name(sut):
    assert sut.get_name() == "Dep1"


def test_eq(sut):
    assert sut == Department("Dep1")


def test_str(sut):
    assert "Dep1" in sut.__str__()


def test_add_employee(sut):
    max = "Max"
    sut.add_employee(Employee(max))
    assert max in sut.__str__()


def test_add_employee_twice_has_no_effect(sut):
    max = "Max"
    sut.add_employee(Employee(max))
    text = sut.__str__()
    sut.add_employee(Employee(max))
    assert text == sut.__str__()