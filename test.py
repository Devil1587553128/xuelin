import pytest
import random
import yaml
@pytest.mark.flaky(reruns=6, reruns_delay=2)
def test_example():
        print(3)
        assert random.choice([True,False])

@pytest.mark.run(order=2)
def test_foo():
    assert True
@pytest.mark.run(order=1)
def test_bar():
    assert True
