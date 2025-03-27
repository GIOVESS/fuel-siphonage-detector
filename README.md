# Fuel Siphonage Detection

## Project Overview
This project detects **fuel siphonage events** from fleet telemetry logs. Fuel siphonage is defined as a **significant drop in fuel level** while the vehicle is **stationary and the engine is off**. The system processes telemetry data and flags suspicious events.


## Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/GIOVESS/fuel-siphonage-detector.git
cd fuel-siphonage-detector
```
## 2️⃣ Create a Virtual Environment & Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## How It Works
1. Reads a telemetry log CSV file.
2. Detects **fuel level drops** when the engine is OFF.
3. Flags potential siphonage events.
4. Outputs results to a new CSV file.

## Running the Streamlit App

```bash
export PYTHONPATH=$(pwd)
streamlit run app/main.py
```

## Running Tests

```bash
pytest tests/test_detector.py
```

## Example Output

| Timestamp        | Vehicle ID | Fuel Drop (L) | Location Lat | Location Lon |  
|-----------------|------------|--------------|--------------|--------------|  
| 2025-03-25 08:30 | V1         | -6.0         | 1.2921       | 36.8219      |  

## 👨‍💻 Author

**Giovanni Bwayo**  
[LinkedIn](https://www.linkedin.com/in/giovannibwayo/)

