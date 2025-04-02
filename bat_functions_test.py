import pytest
import time
from bat_functions import calculate_bat_power
from bat_functions import signal_strength
from bat_functions import get_bat_vehicle
from bat_functions import fetch_joker_info


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
    
    
@pytest.fixture
def bat_vehicles():
    return {
        'Batmobile': {'speed': 200, 'armor': 80},
        'Batwing': {'speed': 300, 'armor': 60},
        'Batcycle': {'speed': 150, 'armor': 50}
    }
    
def test_get_bat_vehicle(bat_vehicles):
    for vehicle_name, expected in bat_vehicles.items():
        assert get_bat_vehicle(vehicle_name) == expected, "Vehicles should match expected specs"
        
        with pytest.raises(ValueError, match="Unknown vehicle: Batboat"):
            get_bat_vehicle('Batboat')
    
    
def test_fetch_joker_info(mocker):
    custom_response = { #Custom mock response
        'mischief_level': 999,  
        'location': 'Arkham Asylum',  
    }
    
    mock_sleep = mocker.patch('time.sleep', return_value = None) 
    
    mocker.patch('bat_functions_test.fetch_joker_info', return_value = custom_response)
     
    result = fetch_joker_info()
    
    assert result == custom_response, "Fetched Joker info should match custom response"
    
    mock_sleep.assert_not_called() #Ensure that the sleep function is not called in the test