import random

class EcoFlowClient:
    def get_data(self):
        return {
            "battery_soc": random.randint(40, 90),
            "solar_input": random.randint(0, 3000),
            "grid_power": random.randint(-2000, 2000),
            "load_power": random.randint(500, 2500)
        }

    def set_charge_mode(self, mode):
        print(f"Setting charge mode: {mode}")
