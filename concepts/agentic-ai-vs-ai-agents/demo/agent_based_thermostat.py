"""
Agent-Based Thermostat System

An intelligent thermostat that learns, remembers, and adapts its behavior.
This represents agent-based system approaches with memory and learning.

Key Characteristics:
- Has memory of past temperatures and actions
- Learns from patterns and adapts preferences
- Context-aware decision making
- Evolves behavior over time
"""

from typing import List

class AgentBasedThermostat:
    """
    Agent-based system with memory, learning, and adaptation.
    
    Agent Capabilities:
    - PERCEIVES: Tracks temperature history
    - REMEMBERS: Stores past decisions and outcomes  
    - LEARNS: Adjusts preferred temperature based on patterns
    - ADAPTS: Changes behavior over time
    """
    
    def __init__(self, initial_preferred_temp: float = 22.0):
        # Agent memory and state
        self.preferred_temp = initial_preferred_temp
        self.temperature_history: List[float] = []
        self.action_history: List[str] = []
        self.learning_rate = 0.1
        self.tolerance = 2.0  # Comfort zone around preferred temp
        
        print("🧠 Agent-Based Thermostat initialized")
        print(f"   Initial preferred temperature: {self.preferred_temp}°C")
        print(f"   Tolerance zone: ±{self.tolerance}°C")
        print(f"   Learning rate: {self.learning_rate}")
        print("   System will LEARN and ADAPT over time")
    
    def perceive(self, current_temp: float):
        """Agent perceives and stores environmental data."""
        self.temperature_history.append(current_temp)
        # Keep recent history (last 10 readings for efficiency)
        if len(self.temperature_history) > 10:
            self.temperature_history = self.temperature_history[-10:]
    
    def learn_and_adapt(self):
        """Agent learns from recent patterns and adapts preferences."""
        if len(self.temperature_history) >= 3:
            # Analyze recent temperature trends
            recent_temps = self.temperature_history[-3:]
            avg_recent = sum(recent_temps) / len(recent_temps)
            
            # Adaptive learning: adjust preferences based on patterns
            if avg_recent > self.preferred_temp + self.tolerance:
                # It's been consistently hot, maybe user prefers warmer
                self.preferred_temp += self.learning_rate
            elif avg_recent < self.preferred_temp - self.tolerance:
                # It's been consistently cold, maybe user prefers cooler
                self.preferred_temp -= self.learning_rate
            
            # Keep preferences within reasonable bounds
            self.preferred_temp = max(18, min(26, self.preferred_temp))
    
    def decide_action(self, current_temp: float) -> str:
        """
        Agent makes intelligent decisions based on memory and learning.
        Unlike rule-based systems, decisions evolve over time.
        """
        # Step 1: Perceive the environment
        self.perceive(current_temp)
        
        # Step 2: Learn and adapt from recent patterns
        self.learn_and_adapt()
        
        # Step 3: Make decision based on current adaptive preferences
        lower_bound = self.preferred_temp - self.tolerance
        upper_bound = self.preferred_temp + self.tolerance
        
        if current_temp < lower_bound:
            action = "Turn ON Heater"
        elif current_temp > upper_bound:
            action = "Turn ON AC"
        else:
            action = "Maintain"
        
        # Step 4: Remember this action
        self.action_history.append(action)
        if len(self.action_history) > 10:
            self.action_history = self.action_history[-10:]
        
        return action
    
    def get_current_preference(self) -> float:
        """Return agent's current preferred temperature."""
        return round(self.preferred_temp, 1)
    
    def get_info(self) -> dict:
        """Return comprehensive agent state information."""
        return {
            "type": "Agent-Based System",
            "current_preferred_temp": self.get_current_preference(),
            "tolerance": self.tolerance,
            "learning_rate": self.learning_rate,
            "has_memory": True,
            "can_learn": True,
            "adaptable": True,
            "temperature_history": self.temperature_history[-5:],  # Last 5 readings
            "recent_actions": self.action_history[-5:]  # Last 5 actions
        }

if __name__ == "__main__":
    # Demo the agent-based system
    thermostat = AgentBasedThermostat()
    
    print("\n📊 Testing Agent-Based System:")
    test_temps = [16, 19, 22, 26, 28, 24, 20, 21, 27, 18]
    
    for temp in test_temps:
        action = thermostat.decide_action(temp)
        preference = thermostat.get_current_preference()
        print(f"   {temp}°C → {action} (preferred: {preference}°C)")
    
    print(f"\n📋 Final Agent State:")
    info = thermostat.get_info()
    for key, value in info.items():
        print(f"   {key}: {value}")
