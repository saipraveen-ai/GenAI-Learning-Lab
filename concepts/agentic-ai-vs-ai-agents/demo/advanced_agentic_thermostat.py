"""
Advanced Agentic AI Thermostat
===============================
This demonstrates a sophisticated Agentic AI Thermostat that exhibits:

🎯 Goal Understanding: "Keep room comfortable for sleeping"
📋 Multi-step Planning: Pre-cool room before bedtime considering context
🌍 Context Awareness: Weather, energy pricing, user schedule
🔧 Tool Integration: Weather API, sleep tracker, energy dashboard
🧠 Reflection & Learning: "Did the room reach target temp on time last night?"
⚡ Adaptive Optimization: Dynamic adjustment based on real-time conditions

Features demonstrated:
- Goal-oriented behavior with complex objectives
- Multi-step planning with contingencies
- Context-aware decision making
- Tool use and API integration
- Memory and reflection for continuous improvement
- Dynamic adaptation to changing conditions
- User feedback integration
"""

import datetime
import time
import random
from typing import Dict, List, Optional
from dataclasses import dataclass

@dataclass
class PerformanceMemory:
    """Stores performance data for reflection and learning"""
    date: str
    target_temp: float
    start_time: str
    actual_completion_time: str
    energy_cost: float
    user_satisfaction: int  # 1-10 scale
    weather_factor: str
    lessons_learned: str

class WeatherAPI:
    """Mock weather API with realistic data"""
    @staticmethod
    def get_current_weather() -> Dict:
        return {
            "current_temp": random.randint(25, 35),
            "humidity": random.randint(40, 80),
            "forecast_next_3h": random.randint(20, 30),
            "cooling_rate": random.uniform(2, 5),  # degrees per hour
            "heatwave_warning": random.choice([True, False])
        }

class EnergyAPI:
    """Mock energy pricing API"""
    @staticmethod
    def get_pricing_forecast() -> Dict:
        current_hour = datetime.datetime.now().hour
        prices = []
        for hour in range(24):
            if 18 <= hour <= 21:  # Peak hours
                price = random.uniform(0.25, 0.35)
            elif 22 <= hour <= 6:  # Off-peak
                price = random.uniform(0.12, 0.18)
            else:  # Standard
                price = random.uniform(0.18, 0.25)
            prices.append({"hour": hour, "price": price})
        
        return {
            "current_price": prices[current_hour]["price"],
            "hourly_forecast": prices,
            "peak_hours": [18, 19, 20, 21],
            "off_peak_hours": list(range(22, 24)) + list(range(0, 7))
        }

class SleepTrackerAPI:
    """Mock sleep tracker integration"""
    @staticmethod
    def get_sleep_preferences() -> Dict:
        return {
            "preferred_sleep_temp": random.uniform(20, 23),
            "bedtime": "22:00",
            "wake_time": "07:00",
            "sleep_quality_last_night": random.randint(6, 10),
            "temperature_complaints": random.choice([None, "too_hot", "too_cold"])
        }

class AdvancedAgenticThermostat:
    """
    Advanced Agentic AI Thermostat that demonstrates sophisticated AI capabilities
    beyond simple rule-based systems or basic AI agents.
    """
    
    def __init__(self):
        self.goal = "Ensure room is 22°C by 10:00 PM and maintain during sleep"
        self.performance_memory: List[PerformanceMemory] = []
        self.user_preferences = {
            "target_temp": 22.0,
            "bedtime": "22:00",
            "energy_priority": "balanced",  # "cost", "comfort", "balanced"
            "notification_preference": True
        }
        self.current_plan = None
        
    def perceive_environment(self) -> Dict:
        """Gather comprehensive environmental and contextual data"""
        current_time = datetime.datetime.now()
        
        context = {
            "current_time": current_time.strftime("%H:%M"),
            "current_temp": random.randint(25, 30),
            "weather": WeatherAPI.get_current_weather(),
            "energy": EnergyAPI.get_pricing_forecast(),
            "sleep_data": SleepTrackerAPI.get_sleep_preferences(),
            "day_of_week": current_time.strftime("%A"),
            "season": self._get_season(current_time.month)
        }
        
        print(f"🌡️ Current Context:")
        print(f"   Time: {context['current_time']}")
        print(f"   Indoor Temp: {context['current_temp']}°C")
        print(f"   Outdoor Temp: {context['weather']['current_temp']}°C")
        print(f"   Energy Price: ${context['energy']['current_price']:.3f}/kWh")
        print(f"   Target Bedtime: {context['sleep_data']['bedtime']}")
        
        return context
    
    def reflect_on_past_performance(self) -> Dict:
        """Analyze past performance to improve future decisions"""
        if not self.performance_memory:
            return {
                "avg_cooling_time": 1.5,
                "success_rate": 0.8,
                "energy_efficiency": "unknown",
                "user_satisfaction": 7.0,
                "key_insights": ["No historical data available - using defaults"]
            }
        
        recent_performance = self.performance_memory[-7:]  # Last week
        
        avg_satisfaction = sum(p.user_satisfaction for p in recent_performance) / len(recent_performance)
        avg_energy_cost = sum(p.energy_cost for p in recent_performance) / len(recent_performance)
        
        insights = self._generate_insights(recent_performance)
        
        reflection = {
            "avg_cooling_time": random.uniform(1.2, 2.0),
            "success_rate": random.uniform(0.8, 0.95),
            "avg_energy_cost": avg_energy_cost,
            "user_satisfaction": avg_satisfaction,
            "key_insights": insights
        }
        
        print(f"🧠 Reflection on Past Performance:")
        for insight in insights:
            print(f"   💡 {insight}")
            
        return reflection
    
    def plan_optimal_cooling_strategy(self, context: Dict, reflection: Dict) -> Dict:
        """Create multi-step plan considering all factors"""
        bedtime_hour = int(context['sleep_data']['bedtime'].split(':')[0])
        current_hour = int(context['current_time'].split(':')[0])
        hours_until_bedtime = bedtime_hour - current_hour
        
        if hours_until_bedtime <= 0:
            hours_until_bedtime += 24  # Next day
        
        temp_difference = context['current_temp'] - self.user_preferences['target_temp']
        cooling_needed = max(0, temp_difference)
        
        # Estimate cooling time based on weather and past performance
        base_cooling_time = cooling_needed / context['weather']['cooling_rate']
        adjusted_cooling_time = base_cooling_time * random.uniform(0.9, 1.2)  # Add uncertainty
        
        # Consider energy pricing
        energy_forecast = context['energy']['hourly_forecast']
        optimal_start_time = self._find_optimal_start_time(
            hours_until_bedtime, adjusted_cooling_time, energy_forecast
        )
        
        # Generate adaptive plan
        plan = {
            "strategy": "adaptive_pre_cooling",
            "start_time": optimal_start_time,
            "estimated_duration": adjusted_cooling_time,
            "target_temp": self.user_preferences['target_temp'],
            "energy_optimization": True,
            "contingencies": self._create_contingency_plans(context),
            "monitoring_intervals": [0.5, 1.0, 1.5],  # Check progress every 30 mins
            "success_criteria": {
                "temp_achieved": True,
                "on_time": True,
                "energy_budget": True
            }
        }
        
        print(f"📋 Optimal Cooling Strategy:")
        print(f"   🕒 Start Time: {optimal_start_time}")
        print(f"   ⏱️  Duration: {adjusted_cooling_time:.1f} hours")
        print(f"   🎯 Target: {plan['target_temp']}°C by {context['sleep_data']['bedtime']}")
        print(f"   ⚡ Energy Optimized: {plan['energy_optimization']}")
        
        return plan
    
    def execute_plan_with_monitoring(self, plan: Dict, context: Dict) -> Dict:
        """Execute the plan with real-time monitoring and adaptation"""
        print(f"\n🚀 Executing Cooling Plan...")
        
        execution_log = []
        start_time = datetime.datetime.now()
        
        # Simulate plan execution with monitoring
        for i, checkpoint in enumerate(plan['monitoring_intervals']):
            print(f"\n⏱️  Checkpoint {i+1} ({checkpoint} hours elapsed):")
            
            # Simulate progress
            progress = checkpoint / plan['estimated_duration']
            current_temp = context['current_temp'] - (progress * (context['current_temp'] - plan['target_temp']))
            
            print(f"   🌡️ Current Temp: {current_temp:.1f}°C")
            
            # Check if adaptation is needed
            if self._adaptation_needed(current_temp, progress, plan):
                adaptation = self._adapt_plan(current_temp, progress, plan, context)
                print(f"   🔄 Adaptation: {adaptation['reason']}")
                plan.update(adaptation['adjustments'])
                execution_log.append(f"Adapted: {adaptation['reason']}")
            else:
                print(f"   ✅ On track - no adaptation needed")
                execution_log.append(f"Checkpoint {i+1}: On track")
            
            time.sleep(0.5)  # Simulate time passing
        
        # Final result
        final_temp = plan['target_temp'] + random.uniform(-0.5, 0.5)
        completion_time = datetime.datetime.now()
        
        result = {
            "success": abs(final_temp - plan['target_temp']) <= 1.0,
            "final_temp": final_temp,
            "actual_duration": (completion_time - start_time).total_seconds() / 3600,
            "energy_used": random.uniform(2.5, 4.0),  # kWh
            "execution_log": execution_log,
            "user_message": self._generate_user_message(plan, final_temp)
        }
        
        print(f"\n✅ Plan Execution Complete:")
        print(f"   🎯 Final Temperature: {final_temp:.1f}°C")
        print(f"   ⏱️  Actual Duration: {result['actual_duration']:.1f} hours")
        print(f"   ⚡ Energy Used: {result['energy_used']:.1f} kWh")
        print(f"   📱 User Message: {result['user_message']}")
        
        return result
    
    def learn_from_experience(self, context: Dict, plan: Dict, result: Dict):
        """Store performance data and learn for future improvement"""
        # Simulate user feedback
        user_satisfaction = random.randint(7, 10) if result['success'] else random.randint(4, 7)
        
        memory_entry = PerformanceMemory(
            date=datetime.datetime.now().strftime("%Y-%m-%d"),
            target_temp=plan['target_temp'],
            start_time=plan['start_time'],
            actual_completion_time=context['sleep_data']['bedtime'],
            energy_cost=result['energy_used'] * context['energy']['current_price'],
            user_satisfaction=user_satisfaction,
            weather_factor=f"Outside: {context['weather']['current_temp']}°C",
            lessons_learned=self._extract_lessons(plan, result)
        )
        
        self.performance_memory.append(memory_entry)
        
        # Update preferences based on learning
        if user_satisfaction >= 8:
            print(f"🎓 Learning: Strategy was successful - reinforcing approach")
        else:
            print(f"🎓 Learning: Room for improvement - adjusting future strategies")
            
        # Keep only recent memory (last 30 days)
        if len(self.performance_memory) > 30:
            self.performance_memory = self.performance_memory[-30:]
    
    def run_agentic_thermostat_cycle(self):
        """Complete agentic cycle: Perceive → Reflect → Plan → Execute → Learn"""
        print("🌟" * 50)
        print("🧠 ADVANCED AGENTIC AI THERMOSTAT")
        print("🌟" * 50)
        print(f"🎯 Goal: {self.goal}")
        print()
        
        # 1. Perceive Environment
        print("1️⃣ ENVIRONMENTAL PERCEPTION")
        print("=" * 40)
        context = self.perceive_environment()
        print()
        
        # 2. Reflect on Past Performance
        print("2️⃣ PERFORMANCE REFLECTION")
        print("=" * 40)
        reflection = self.reflect_on_past_performance()
        print()
        
        # 3. Plan Optimal Strategy
        print("3️⃣ STRATEGIC PLANNING")
        print("=" * 40)
        plan = self.plan_optimal_cooling_strategy(context, reflection)
        print()
        
        # 4. Execute with Monitoring
        print("4️⃣ ADAPTIVE EXECUTION")
        print("=" * 40)
        result = self.execute_plan_with_monitoring(plan, context)
        print()
        
        # 5. Learn from Experience
        print("5️⃣ EXPERIENTIAL LEARNING")
        print("=" * 40)
        self.learn_from_experience(context, plan, result)
        print()
        
        print("🏆 AGENTIC CYCLE COMPLETE")
        print("=" * 40)
        print("This demonstrates advanced AI capabilities:")
        print("✅ Goal understanding and multi-objective optimization")
        print("✅ Context-aware planning with external tool integration")
        print("✅ Real-time adaptation and dynamic decision making")
        print("✅ Reflection and continuous learning from experience")
        print("✅ User-centric communication and feedback integration")
        print()
    
    # Helper methods
    def _get_season(self, month: int) -> str:
        if month in [12, 1, 2]:
            return "winter"
        elif month in [3, 4, 5]:
            return "spring"
        elif month in [6, 7, 8]:
            return "summer"
        else:
            return "autumn"
    
    def _generate_insights(self, performance_data: List[PerformanceMemory]) -> List[str]:
        insights = [
            "Hot weather requires earlier cooling start times",
            "User prefers slightly warmer temperatures on weekends",
            "Energy costs are 30% lower after 10 PM",
            "Cooling efficiency improved 15% with staged approach"
        ]
        return random.sample(insights, 2)
    
    def _find_optimal_start_time(self, hours_available: int, cooling_time: float, energy_forecast: List) -> str:
        # Simple optimization: avoid peak hours when possible
        optimal_hour = max(0, int(hours_available - cooling_time - 1))
        current_hour = datetime.datetime.now().hour
        start_hour = (current_hour + optimal_hour) % 24
        return f"{start_hour:02d}:30"
    
    def _create_contingency_plans(self, context: Dict) -> List[str]:
        return [
            "If cooling slower than expected: Increase cooling rate by 20%",
            "If energy prices spike: Shift to maintenance mode until prices drop",
            "If outdoor temperature rises: Extend cooling duration by 30 minutes"
        ]
    
    def _adaptation_needed(self, current_temp: float, progress: float, plan: Dict) -> bool:
        expected_temp = plan['target_temp'] + (1 - progress) * (28 - plan['target_temp'])
        return abs(current_temp - expected_temp) > 1.5
    
    def _adapt_plan(self, current_temp: float, progress: float, plan: Dict, context: Dict) -> Dict:
        if current_temp > plan['target_temp'] + 2:
            return {
                "reason": "Cooling behind schedule - increasing intensity",
                "adjustments": {"cooling_rate": 1.2}
            }
        else:
            return {
                "reason": "Ahead of schedule - optimizing energy usage",
                "adjustments": {"cooling_rate": 0.9}
            }
    
    def _generate_user_message(self, plan: Dict, final_temp: float) -> str:
        if abs(final_temp - plan['target_temp']) <= 0.5:
            return f"Perfect! Room reached {final_temp:.1f}°C on schedule. Sweet dreams! 😴"
        elif final_temp > plan['target_temp']:
            return f"Room is {final_temp:.1f}°C - slightly warm but comfortable. Adjusting for tomorrow."
        else:
            return f"Room cooled to {final_temp:.1f}°C - nice and cool for great sleep!"
    
    def _extract_lessons(self, plan: Dict, result: Dict) -> str:
        if result['success']:
            return "Optimal timing and energy management achieved target efficiently"
        else:
            return "Need longer cooling time or earlier start for similar conditions"

def demonstrate_agentic_features():
    """Demonstrate specific agentic AI features with examples"""
    print("\n🧪 AGENTIC AI FEATURES DEMONSTRATION")
    print("=" * 50)
    
    features = {
        "Goal Understanding": "\"Keep room comfortable for sleeping\" → Translates to specific temperature and timing requirements",
        "Context Awareness": "Considers weather (35°C outside), energy pricing ($0.20/kWh peak), user schedule (bedtime 10 PM)",
        "Multi-step Planning": "Weather check → Price forecast → Schedule optimization → Contingency planning",
        "Tool Integration": "Weather API + Energy API + Sleep Tracker + User Preferences",
        "Adaptive Execution": "Real-time monitoring with 30-min checkpoints and dynamic adjustments",
        "Reflection & Learning": "\"Last night took 1.5 hours\" → Improves future time estimates",
        "User Communication": "\"Starting cooling at 8:30 PM based on weather and energy prices to save 15% on costs\""
    }
    
    for feature, example in features.items():
        print(f"🔹 {feature}:")
        print(f"   {example}")
        print()

if __name__ == "__main__":
    # Run the complete demonstration
    thermostat = AdvancedAgenticThermostat()
    thermostat.run_agentic_thermostat_cycle()
    
    # Show feature breakdown
    demonstrate_agentic_features()
