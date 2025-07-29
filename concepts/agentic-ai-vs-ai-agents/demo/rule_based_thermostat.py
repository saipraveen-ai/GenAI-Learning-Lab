"""
Rule-Based Thermostat System

A simple thermostat that follows fixed rules with no memory or learning.
This represents traditional programming approaches.

Key Characteristics:
- Fixed rules that never change
- No memory of past temperatures
- Deterministic: same input always produces same output
- Simple and predictable behavior
"""

class RuleBasedThermostat:
    """
    Rule-based system with fixed thresholds.
    
    Rules:
    - If temperature < 18°C: Turn ON Heater
    - If temperature > 25°C: Turn ON AC  
    - Otherwise: Do Nothing
    """
    
    def __init__(self):
        # Fixed rules - these never change
        self.heat_threshold = 18  # Turn on heater if temp < 18
        self.cool_threshold = 25  # Turn on AC if temp > 25
        
        print("🔧 Rule-Based Thermostat initialized")
        print(f"   Heat threshold: {self.heat_threshold}°C")
        print(f"   Cool threshold: {self.cool_threshold}°C")
        print("   Rules are FIXED and will never change")
    
    def decide_action(self, current_temp: float) -> str:
        """
        Make decision based on fixed rules only.
        No memory, no learning, no adaptation.
        """
        if current_temp < self.heat_threshold:
            return "Turn ON Heater"
        elif current_temp > self.cool_threshold:
            return "Turn ON AC"
        else:
            return "Do Nothing"
    
    def get_info(self) -> dict:
        """Return system information."""
        return {
            "type": "Rule-Based System",
            "heat_threshold": self.heat_threshold,
            "cool_threshold": self.cool_threshold,
            "has_memory": False,
            "can_learn": False,
            "adaptable": False
        }

if __name__ == "__main__":
    # Demo the rule-based system
    thermostat = RuleBasedThermostat()
    
    print("\n📊 Testing Rule-Based System:")
    test_temps = [16, 18, 19, 22, 25, 26, 28]
    
    for temp in test_temps:
        action = thermostat.decide_action(temp)
        print(f"   {temp}°C → {action}")
    
    print(f"\n📋 System Info: {thermostat.get_info()}")
