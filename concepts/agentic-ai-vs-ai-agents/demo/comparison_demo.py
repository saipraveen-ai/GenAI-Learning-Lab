"""
Thermostat Comparison Runner

This script runs both rule-based and agent-based thermostats 
side-by-side to demonstrate the key differences.
"""

from rule_based_thermostat import RuleBasedThermostat
from agent_based_thermostat import AgentBasedThermostat

def run_side_by_side_comparison():
    """Run both systems with the same temperature sequence."""
    print("=" * 80)
    print("🌡️  THERMOSTAT COMPARISON: Rule-Based vs Agent-Based Systems")
    print("=" * 80)
    
    # Initialize both systems
    print("\n🔧 Initializing Systems...")
    rule_system = RuleBasedThermostat()
    print()
    agent_system = AgentBasedThermostat(initial_preferred_temp=22.0)
    
    # Test with the same temperature sequence
    temperatures = [16, 19, 22, 26, 28, 24, 20, 21, 27, 18]
    
    print(f"\n📋 Comparison Results")
    print("Temp (°C)\tRule-Based Action\tAgent-Based Action\tAgent's Preferred Temp")
    print("-" * 80)
    
    for temp in temperatures:
        rule_action = rule_system.decide_action(temp)
        agent_action = agent_system.decide_action(temp)
        agent_preference = agent_system.get_current_preference()
        
        print(f"{temp}\t\t{rule_action}\t\t{agent_action}\t\t{agent_preference}")
    
    return rule_system, agent_system

def show_system_analysis(rule_system, agent_system):
    """Show detailed analysis of both systems."""
    print("\n" + "=" * 80)
    print("📊 SYSTEM ANALYSIS")
    print("=" * 80)
    
    rule_info = rule_system.get_info()
    agent_info = agent_system.get_info()
    
    print("\n🔧 Rule-Based System:")
    for key, value in rule_info.items():
        print(f"   {key}: {value}")
    
    print("\n🧠 Agent-Based System:")
    for key, value in agent_info.items():
        print(f"   {key}: {value}")
    
    print("\n🔍 Key Differences:")
    print("   Rule-Based System:")
    print("   • Same input always produces same output (deterministic)")
    print("   • No memory of past events")
    print("   • Fixed behavior that never changes")
    print("   • Simple and predictable")
    
    print("\n   Agent-Based System:")
    print("   • Same input may produce different outputs (adaptive)")
    print("   • Remembers temperature history and past actions")
    print("   • Behavior evolves based on experience") 
    print("   • Learns patterns and adjusts preferences")

def demonstrate_learning_over_time():
    """Show how the agent learns over multiple scenarios."""
    print("\n" + "=" * 80)
    print("🧠 AGENT LEARNING DEMONSTRATION")
    print("=" * 80)
    
    agent = AgentBasedThermostat(initial_preferred_temp=22.0)
    
    scenarios = [
        ("Normal Week", [20, 21, 22, 23, 22, 21]),
        ("Hot Summer", [28, 29, 27, 28, 26, 27]),
        ("Cold Winter", [15, 16, 14, 17, 16, 15]),
        ("Back to Normal", [21, 22, 20, 23, 22, 21])
    ]
    
    for scenario_name, temps in scenarios:
        print(f"\n📅 {scenario_name}:")
        print(f"   Initial preference: {agent.get_current_preference()}°C")
        
        for temp in temps:
            action = agent.decide_action(temp)
            pref = agent.get_current_preference()
            print(f"     {temp}°C → {action} (preference now: {pref}°C)")
        
        print(f"   Final preference: {agent.get_current_preference()}°C")
        print(f"   Temperature memory: {agent.temperature_history}")

if __name__ == "__main__":
    # Run the complete comparison
    rule_system, agent_system = run_side_by_side_comparison()
    show_system_analysis(rule_system, agent_system)
    demonstrate_learning_over_time()
    
    print("\n" + "=" * 80)
    print("✅ CONCLUSION")
    print("=" * 80)
    print("Rule-Based: Predictable but rigid - follows same rules forever")
    print("Agent-Based: Intelligent and adaptive - learns and evolves over time")
    print("\nThis demonstrates the fundamental difference between:")
    print("• Traditional programming (rules) vs Agent-based systems (intelligence)")
    print("=" * 80)
