import random
import time
import json

# Simulate sensor data from an industrial environment
def simulate_sensor_data(sensor_id, data_type):
    if data_type == "temperature":
        # Simulate temperature fluctuations, potentially indicating an anomaly
        base_temp = 25.0
        fluctuation = random.uniform(-2.0, 2.0)
        if random.random() < 0.05: # 5% chance of a significant anomaly
            fluctuation += random.uniform(5.0, 10.0)
        return round(base_temp + fluctuation, 2)
    elif data_type == "vibration":
        # Simulate vibration levels, higher might indicate wear
        base_vibration = 0.5
        fluctuation = random.uniform(-0.2, 0.2)
        if random.random() < 0.03: # 3% chance of high vibration
            fluctuation += random.uniform(1.0, 3.0)
        return round(base_vibration + fluctuation, 2)
    elif data_type == "pressure":
        # Simulate pressure readings
        base_pressure = 100.0
        fluctuation = random.uniform(-1.0, 1.0)
        return round(base_pressure + fluctuation, 2)
    else:
        return None

# Simulate an AI decision-making process based on sensor data
def analyze_data_and_decide(sensor_readings):
    alerts = []
    # Simple AI logic: check for abnormal readings
    if sensor_readings.get("machine_temp") > 30.0:
        alerts.append("High temperature detected on machine. Potential overheating.")
    if sensor_readings.get("machine_vibration") > 1.5:
        alerts.append("High vibration detected on machine. Possible wear or imbalance.")
    if sensor_readings.get("pump_pressure") < 98.0:
        alerts.append("Low pressure detected on pump. Check for leaks or blockages.")

    if alerts:
        print("\n--- AI Decision --- ")
        print("Alerts:")
        for alert in alerts:
            print(f"- {alert}")
        print("Recommended Action: Investigate anomalies.")
        return True # Decision made to alert
    else:
        print("\n--- AI Decision --- ")
        print("All systems nominal. No immediate action required.")
        return False # No alert

# Main simulation loop
if __name__ == "__main__":
    print("Starting Industrial AI/IoT Sensor Simulation...")
    print("Press Ctrl+C to stop.")

    try:
        while True:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S")

            # Simulate data from different IoT sensors
            sensor_data = {
                "timestamp": current_time,
                "machine_temp": simulate_sensor_data("machine_1", "temperature"),
                "machine_vibration": simulate_sensor_data("machine_1", "vibration"),
                "pump_pressure": simulate_sensor_data("pump_1", "pressure")
            }

            print(f"\n--- Sensor Data ({current_time}) ---")
            print(json.dumps(sensor_data, indent=2))

            # AI analyzes the data and makes a decision
            analyze_data_and_decide(sensor_data)

            time.sleep(5) # Simulate data collection every 5 seconds

    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")
