import pytest
import pandas as pd
from app.detector import detect_fuel_siphonage
from app.utils import validate_dataframe, convert_timestamp

# Sample test dataset
@pytest.fixture
def sample_data():
    data = {
        "vehicle_id": ["V1"] * 6,  
        "timestamp": pd.date_range(start="2025-03-27 08:00:00", periods=6, freq="1T"),
        "fuel_level": [50, 48, 47, 40, 38, 37],  
        "engine_status": ["ON", "ON", "OFF", "OFF", "OFF", "OFF"],  
        "location_lat": [1.29027] * 6,  
        "location_lon": [36.8219] * 6,
    }
    df = pd.DataFrame(data)
    return convert_timestamp(df)  

# Test for siphonage detection
def test_detect_fuel_siphonage(sample_data):
    results = detect_fuel_siphonage(sample_data, fuel_drop_threshold=5.0)
    
    # Check if siphonage events are detected
    assert not results.empty, "No siphonage events detected, but expected some."
    
    # Validate that the detected event is the expected one
    expected_event_index = 3  # The index where we expect fuel siphonage
    assert expected_event_index in results.index, f"Expected siphonage at index {expected_event_index}, but got {results.index.tolist()}."

# Test for missing columns
def test_missing_columns():
    df = pd.DataFrame({"fuel_level": [50, 48, 47]})  # Missing other required columns
    with pytest.raises(ValueError):
        validate_dataframe(df)  # Using utils function for validation

# Run tests
if __name__ == "__main__":
    pytest.main()
