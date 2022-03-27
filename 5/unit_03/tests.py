import pytest
from covertable import make

def function(pressure, volume, velocity, low_fuel):
    if pressure < 10:
        if volume > 300:
            if velocity == 5:
                do_something_bad()
            elif low_fuel:
                do_something_good()
        else:
            do_something_good()

def do_something_bad():
    raise Exception("Coś wybuchło !!!")

def do_something_good():
    pass

@pytest.mark.parametrize(["pressure", "volume", "velocity", "low_fuel"],
    make([[5, 10, 15],           # parametr pressure
         [200, 300, 400],        # parametr volume
         [1, 2, 3, 4, 5],        # parametr velocity
         [True, False]], length=4))
def test_function(pressure, volume, velocity, low_fuel):
    function(pressure, volume, velocity, low_fuel)