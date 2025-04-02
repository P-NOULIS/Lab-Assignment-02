import pytest
from bat_functions import calculate_bat_power
from bat_functions import signal_strength

def test_bat_power():
    assert calculate_bat_power(1) == 42, "Power level for level 1 should be 42"
    assert calculate_bat_power(2) == 84, "Power level for level 2 should be 84" 
    assert calculate_bat_power(0) == 0, "Power level for level 0 should be 0"
    assert calculate_bat_power(-1) == -42, "Power level for level -1 should be -42"
    assert calculate_bat_power(-2) == -84, "Power level for level -2 should be -84"
    
def test_signal_strength():
    assert signal_strength(1) == 90, "Signal strength at 1 km should be 90"
    assert signal_strength(5) == 50, "Signal strength at 5 km should be 50"
    assert signal_strength(10) == 0, "Signal strength at 10 km should be 0"
    assert signal_strength(0) == 100, "Signal strength at 0 km should be 100"
    assert signal_strength(12) == 0, "Signal strength at 12 km should be 0"