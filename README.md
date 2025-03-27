# Fuel Siphonage Detection

## Project Overview
This project detects **fuel siphonage events** from fleet telemetry logs. Fuel siphonage is defined as a **significant drop in fuel level** while the vehicle is **stationary and the engine is off**. The system processes telemetry data and flags suspicious events.


## Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/GIOVESS/fuel-siphonage-detector.git
cd fuel-siphonage-detector
```

### 2️⃣ Create a Virtual Environment & Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Run the Detection Script
```bash
python app/main.py --file data/sample_fuel_telemetry.csv
```

## How It Works
1. Reads a telemetry log CSV file.
2. Detects **fuel level drops** when the engine is OFF.
3. Flags potential siphonage events.
4. Outputs results to the console or a new CSV file.

## Running the Streamlit App 
```bash
streamlit run app/main.py
```

## Running Tests
```bash
pytest tests/
```

## Example Output 
| Vehicle ID | Timestamp        | Location Lat | Location Lon | Engine Status | Fuel Level (L) | Siphonage Flag |
|------------|-----------------|--------------|--------------|--------------|----------------|----------------|
| V1         | 3/25/2025 8:00  | -1.2921      | 36.8219      | OFF          | 60             | ❌              |
| V2         | 3/25/2025 8:30  | -1.2921      | 36.8219      | OFF          | 40             | ✅              |

## 👨‍💻 Author
**Giovanni Bwayo**  
[GitHub](https://github.com/GIOVESS) | [LinkedIn](https://www.linkedin.com/in/giovannibwayo/)

