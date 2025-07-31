#!/usr/bin/env python3
"""
Translation Manager Demo
======================

Demonstrates Manager Pattern with specialized translation agents.
Shows how a central manager coordinates multiple specialized agents.

Requirements:
- Mock implementation provided for demonstration
"""

import asyncio
from dataclasses import dataclass
from typing import List, Dict

# Mock Agent Framework for Translation Demo
class MockTranslationClient:
    def __init__(self):
        self.translations = {
            "spanish": {
                "Hello, how are you today?": "Hola, ¿cómo estás hoy?",
                "Good morning, have a great day!": "¡Buenos días, que tengas un gran día!",
                "The weather is beautiful today": "El clima está hermoso hoy"
            },
            "french": {
                "Hello, how are you today?": "Bonjour, comment allez-vous aujourd'hui?",
                "Good morning, have a great day!": "Bonjour, passez une excellente journée!",
                "The weather is beautiful today": "Le temps est magnifique aujourd'hui"
            },
            "italian": {
                "Hello, how are you today?": "Ciao, come stai oggi?",
                "Good morning, have a great day!": "Buongiorno, buona giornata!",
                "The weather is beautiful today": "Il tempo è bellissimo oggi"
            }
        }
    
    async def translate(self, text: str, language: str) -> str:
        await asyncio.sleep(0.3)  # Simulate API delay
        return self.translations.get(language, {}).get(text, f"[{language.upper()} TRANSLATION: {text}]")

class TranslationAgent:
    def __init__(self, name: str, language: str):
        self.name = name
        self.language = language
        self.client = MockTranslationClient()
    
    async def translate(self, text: str) -> str:
        print(f"🌍 {self.name}: Translating '{text}' to {self.language.title()}")
        
        result = await self.client.translate(text, self.language)
        
        print(f"✅ {self.name}: Translation complete - '{result}'")
        return result

class TranslationManager:
    def __init__(self):
        self.agents = {
            "spanish": TranslationAgent("SpanishBot", "spanish"),
            "french": TranslationAgent("FrenchBot", "french"), 
            "italian": TranslationAgent("ItalianBot", "italian")
        }
        self.available_languages = list(self.agents.keys())
    
    async def process_request(self, request: str) -> Dict[str, str]:
        print(f"\n👑 TranslationManager: Processing request - '{request}'")
        
        # Parse request to identify text and target languages
        text, languages = self._parse_request(request)
        
        print(f"📝 TranslationManager: Text to translate - '{text}'")
        print(f"🎯 TranslationManager: Target languages - {languages}")
        
        # Coordinate translations
        results = {}
        for lang in languages:
            if lang in self.agents:
                translation = await self.agents[lang].translate(text)
                results[lang] = translation
        
        print(f"✅ TranslationManager: All translations completed")
        return results
    
    def _parse_request(self, request: str) -> tuple[str, List[str]]:
        """Parse user request to extract text and target languages."""
        request_lower = request.lower()
        
        # Extract text (simplified - looks for quotes or common patterns)
        if "'" in request:
            text_start = request.find("'") + 1
            text_end = request.find("'", text_start)
            text = request[text_start:text_end]
        else:
            # Fallback for demo
            text = "Hello, how are you today?"
        
        # Identify requested languages
        languages = []
        if "spanish" in request_lower:
            languages.append("spanish")
        if "french" in request_lower:
            languages.append("french")
        if "italian" in request_lower:
            languages.append("italian")
            
        # Handle "all languages" requests
        if "all" in request_lower and "languages" in request_lower:
            languages = self.available_languages.copy()
        
        # Default fallback
        if not languages:
            languages = ["spanish"]
            
        return text, languages

async def run_translation_demo():
    """Demonstrate translation service with Manager pattern."""
    
    print("🌍 TRANSLATION MANAGER DEMONSTRATION")
    print("Manager Pattern: Central coordinator with specialized agents")
    print("="*60)
    
    manager = TranslationManager()
    
    test_scenarios = [
        "Translate 'Hello, how are you today?' to Spanish and French",
        "I need 'Good morning, have a great day!' in all three languages", 
        "Translate 'The weather is beautiful today' to Italian only"
    ]
    
    for i, scenario in enumerate(test_scenarios, 1):
        print(f"\n📋 Scenario {i}: {scenario}")
        print("-" * 50)
        
        results = await manager.process_request(scenario)
        
        print(f"\n📊 Results:")
        for language, translation in results.items():
            print(f"  {language.title()}: {translation}")
        
        print("\n" + "="*60)

async def main():
    print("🤖 Multi-Agent Translation Service Demo")
    print("Demonstrating Manager Pattern with specialized translation agents\n")
    
    await run_translation_demo()
    
    print("\n✅ DEMO COMPLETED")
    print("\nKey Concepts Demonstrated:")
    print("• Manager Pattern: Central coordination agent")
    print("• Specialized Agents: Each agent handles one language")
    print("• Tool Functions: Manager uses tools to access agent capabilities")
    print("• Request Parsing: Manager interprets complex user requests") 
    print("• Result Coordination: Manager presents unified results")

if __name__ == "__main__":
    asyncio.run(main())
