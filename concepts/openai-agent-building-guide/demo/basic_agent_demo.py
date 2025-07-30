# Basic Agent Demonstration
# Showcases the three core components: Model, Tools, Instructions

import os
import sys
from typing import Dict, Any

# Mock implementation for demonstration purposes
# In real implementation, you would use: from agents import Agent, function_tool, Runner, UserMessage

class MockAgent:
    """Mock implementation of OpenAI Agent for demonstration purposes."""
    
    def __init__(self, name: str, instructions: str, tools: list):
        self.name = name
        self.instructions = instructions
        self.tools = tools
        self.tool_registry = {tool.__name__: tool for tool in tools}
    
    def process_query(self, query: str) -> Dict[str, Any]:
        """Process a user query and return response with tool usage."""
        
        # Simple query routing based on keywords
        response_content = ""
        tools_used = []
        
        if "weather" in query.lower() and any(city in query.lower() for city in ["san francisco", "new york", "london", "tokyo"]):
            # Extract location
            for city in ["san francisco", "new york", "london", "tokyo"]:
                if city in query.lower():
                    if "forecast" in query.lower():
                        result = get_forecast(city.title())
                        tools_used.append("get_forecast")
                        response_content = f"Here's the forecast for {city.title()}: {result}. Pack accordingly for your trip!"
                    else:
                        result = get_weather(city.title())
                        tools_used.append("get_weather")
                        response_content = f"The current weather in {city.title()} is {result}. Perfect for outdoor activities!"
                    break
        else:
            response_content = "I can help you with weather information. Please ask about weather in San Francisco, New York, London, or Tokyo."
        
        return {
            "content": response_content,
            "tools_used": tools_used
        }

def get_weather(location: str) -> str:
    """Get current weather for a given location."""
    weather_data = {
        "San Francisco": "Sunny, 72°F",
        "New York": "Cloudy, 65°F", 
        "London": "Rainy, 58°F",
        "Tokyo": "Clear, 68°F"
    }
    
    return weather_data.get(location, "Weather data not available for this location")

def get_forecast(location: str, days: int = 3) -> str:
    """Get weather forecast for upcoming days."""
    forecasts = {
        "San Francisco": ["Sunny 75°F", "Partly Cloudy 73°F", "Sunny 76°F"],
        "New York": ["Rain 62°F", "Cloudy 67°F", "Sunny 70°F"],
        "London": ["Rain 55°F", "Overcast 60°F", "Partly Cloudy 63°F"],
        "Tokyo": ["Clear 70°F", "Sunny 72°F", "Partly Cloudy 69°F"]
    }
    
    forecast = forecasts.get(location, ["No forecast available"] * days)
    return f"{days}-day forecast: " + " | ".join(forecast[:days])

def create_weather_agent():
    """Create the weather agent with core components."""
    
    # Core Component 1: Instructions (explicit guidelines and guardrails)
    instructions = """You are a helpful weather agent. You can:
    1. Get current weather for any location
    2. Provide weather forecasts
    3. Give weather advice and recommendations
    
    Always be friendly and provide specific, actionable information.
    If asked about weather, use the available tools to get real data.
    Stay focused on weather-related queries only.
    """
    
    # Core Component 2: Tools (external functions the agent can use)
    tools = [get_weather, get_forecast]
    
    # Core Component 3: Model (would be LLM in real implementation)
    # In real implementation: Agent uses OpenAI's models for reasoning
    
    return MockAgent(
        name="Weather Agent",
        instructions=instructions,
        tools=tools
    )

def run_weather_demo():
    """Demonstrate basic agent functionality."""
    
    # Create the agent
    weather_agent = create_weather_agent()
    
    # Test scenarios demonstrating core concepts
    test_queries = [
        "What's the weather in San Francisco?",
        "Can you give me a 3-day forecast for London?", 
        "I'm planning a trip to New York tomorrow. What should I expect?",
        "What about Tokyo's weather?",
        "Tell me about the stock market"  # Off-topic query
    ]
    
    print("=== BASIC AGENT DEMONSTRATION ===")
    print("Showcasing: Model + Tools + Instructions")
    print("="*60)
    print()
    
    for i, query in enumerate(test_queries, 1):
        print(f"Query {i}: {query}")
        print("-" * 50)
        
        # Process query (in real implementation: Runner.run(agent, [UserMessage(query)]))
        response = weather_agent.process_query(query)
        
        print(f"Response: {response['content']}")
        print(f"Tools Used: {response['tools_used'] if response['tools_used'] else 'None'}")
        print()

def demonstrate_core_components():
    """Explain the three core components in detail."""
    
    print("=== CORE AGENT COMPONENTS BREAKDOWN ===")
    print()
    
    print("1. MODEL (LLM)")
    print("   • Powers reasoning and decision-making")
    print("   • Manages workflow execution") 
    print("   • Recognizes when workflow is complete")
    print("   • Can self-correct and handle failures")
    print()
    
    print("2. TOOLS (External Functions/APIs)")
    print("   • Data Tools: get_weather() - retrieve information")
    print("   • Action Tools: Could include send_alert(), update_database()")
    print("   • Orchestration Tools: Other agents as tools")
    print("   • Dynamically selected based on context")
    print()
    
    print("3. INSTRUCTIONS (Guidelines & Guardrails)")
    print("   • Define agent behavior and scope")
    print("   • Provide step-by-step procedures")
    print("   • Include edge case handling")
    print("   • Set safety boundaries and limitations")
    print()

def analyze_agent_behavior():
    """Analyze how the agent demonstrates key characteristics."""
    
    print("=== AGENT CHARACTERISTICS ANALYSIS ===")
    print()
    
    print("✓ INDEPENDENCE: Agent autonomously chooses tools and responses")
    print("✓ WORKFLOW MANAGEMENT: Completes entire user request end-to-end") 
    print("✓ DYNAMIC TOOL SELECTION: Chooses get_weather vs get_forecast based on query")
    print("✓ GUARDRAILS: Stays within weather domain, rejects off-topic queries")
    print("✓ CONTEXTUAL REASONING: Provides helpful advice beyond raw data")
    print()
    
    print("Contrast with Traditional Applications:")
    print("• Chatbot: Single turn, no workflow completion")
    print("• API: Fixed function calls, no contextual reasoning")  
    print("• Rule Engine: Rigid if-then logic, no adaptability")
    print()

if __name__ == "__main__":
    print("OpenAI Agent Building Guide - Basic Agent Demo")
    print("=" * 60)
    print()
    
    # Demonstrate core components
    demonstrate_core_components()
    
    # Run live demonstration
    run_weather_demo()
    
    # Analyze behavior
    analyze_agent_behavior()
    
    print("=== KEY TAKEAWAYS ===")
    print("• Agents = Model + Tools + Instructions working together")
    print("• Independence distinguishes agents from simple LLM apps")
    print("• Dynamic tool selection enables flexible problem solving") 
    print("• Clear instructions and guardrails ensure reliable behavior")
    print("• Start simple, then scale complexity as needed")
    print()
    print("Next: Try orchestration_demo.py for multi-agent patterns!")
