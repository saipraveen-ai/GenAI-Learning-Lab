#!/usr/bin/env python3
"""
Multi-Agent Orchestration Patterns Demo
======================================

Demonstrates Manager Pattern vs Handoff Pattern for multi-agent coordination.
Shows how different patterns handle task delegation, coordination, and quality control.

Requirements:
- Run from virtual environment: source venv/bin/activate
- OpenAI API key in environment (mock implementation provided)
"""

import asyncio
import json
import time
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional, Any
from abc import ABC, abstractmethod

# Mock OpenAI Client (replace with real implementation)
class MockOpenAIClient:
    def __init__(self, api_key: str = "mock-key"):
        self.api_key = api_key
    
    async def chat_completions_create(self, model: str, messages: List[Dict], **kwargs):
        # Simulate API delay
        await asyncio.sleep(0.5)
        
        # Mock responses based on agent role
        last_message = messages[-1]["content"]
        
        if "research" in last_message.lower():
            return type('obj', (object,), {
                'choices': [type('obj', (object,), {
                    'message': type('obj', (object,), {
                        'content': f"Research findings: Based on analysis of {last_message[:50]}... [RESEARCH_DATA]"
                    })()
                })()]
            })()
        elif "analysis" in last_message.lower():
            return type('obj', (object,), {
                'choices': [type('obj', (object,), {
                    'message': type('obj', (object,), {
                        'content': f"Analysis results: The data shows key trends... [ANALYSIS_RESULTS]"
                    })()
                })()]
            })()
        elif "content" in last_message.lower():
            return type('obj', (object,), {
                'choices': [type('obj', (object,), {
                    'message': type('obj', (object,), {
                        'content': f"Content creation: Here's the structured content... [CONTENT_OUTPUT]"
                    })()
                })()]
            })()
        else:
            return type('obj', (object,), {
                'choices': [type('obj', (object,), {
                    'message': type('obj', (object,), {
                        'content': f"Processing: {last_message[:100]}... [COMPLETED]"
                    })()
                })()]
            })()

# Core Agent Framework
class AgentRole(Enum):
    MANAGER = "manager"
    RESEARCH = "research"
    ANALYSIS = "analysis"
    CONTENT = "content"
    COORDINATOR = "coordinator"

@dataclass
class Task:
    id: str
    description: str
    priority: int
    assigned_to: Optional[str] = None
    status: str = "pending"
    result: Optional[str] = None
    dependencies: List[str] = None
    
    def __post_init__(self):
        if self.dependencies is None:
            self.dependencies = []

class BaseAgent(ABC):
    def __init__(self, name: str, role: AgentRole, capabilities: List[str]):
        self.name = name
        self.role = role
        self.capabilities = capabilities
        self.client = MockOpenAIClient()
        self.task_history: List[Task] = []
    
    @abstractmethod
    async def process_task(self, task: Task) -> str:
        pass
    
    async def can_handle_task(self, task: Task) -> bool:
        # Simple capability matching
        return any(cap in task.description.lower() for cap in self.capabilities)

# Specialized Agent Implementations
class ResearchAgent(BaseAgent):
    def __init__(self, name: str = "ResearchBot"):
        super().__init__(name, AgentRole.RESEARCH, ["research", "data", "gather", "investigate"])
    
    async def process_task(self, task: Task) -> str:
        print(f"🔍 {self.name}: Starting research on '{task.description}'")
        
        messages = [
            {"role": "system", "content": "You are a research specialist. Gather comprehensive information."},
            {"role": "user", "content": f"Research task: {task.description}"}
        ]
        
        response = await self.client.chat_completions_create(
            model="gpt-4",
            messages=messages
        )
        
        result = response.choices[0].message.content
        task.result = result
        task.status = "completed"
        self.task_history.append(task)
        
        print(f"✅ {self.name}: Research completed - {result[:50]}...")
        return result

class AnalysisAgent(BaseAgent):
    def __init__(self, name: str = "AnalysisBot"):
        super().__init__(name, AgentRole.ANALYSIS, ["analysis", "analyze", "evaluate", "assess"])
    
    async def process_task(self, task: Task) -> str:
        print(f"📊 {self.name}: Analyzing '{task.description}'")
        
        messages = [
            {"role": "system", "content": "You are an analysis expert. Evaluate data and provide insights."},
            {"role": "user", "content": f"Analysis task: {task.description}"}
        ]
        
        response = await self.client.chat_completions_create(
            model="gpt-4",
            messages=messages
        )
        
        result = response.choices[0].message.content
        task.result = result
        task.status = "completed"
        self.task_history.append(task)
        
        print(f"✅ {self.name}: Analysis completed - {result[:50]}...")
        return result

class ContentAgent(BaseAgent):
    def __init__(self, name: str = "ContentBot"):
        super().__init__(name, AgentRole.CONTENT, ["content", "write", "create", "generate"])
    
    async def process_task(self, task: Task) -> str:
        print(f"✍️ {self.name}: Creating content for '{task.description}'")
        
        messages = [
            {"role": "system", "content": "You are a content creation specialist. Generate high-quality content."},
            {"role": "user", "content": f"Content task: {task.description}"}
        ]
        
        response = await self.client.chat_completions_create(
            model="gpt-4",
            messages=messages
        )
        
        result = response.choices[0].message.content
        task.result = result
        task.status = "completed"
        self.task_history.append(task)
        
        print(f"✅ {self.name}: Content created - {result[:50]}...")
        return result

# Manager Pattern Implementation
class ManagerAgent(BaseAgent):
    def __init__(self, name: str = "ManagerBot"):
        super().__init__(name, AgentRole.MANAGER, ["coordinate", "manage", "plan", "delegate"])
        self.subordinate_agents: List[BaseAgent] = []
        self.active_tasks: Dict[str, Task] = {}
    
    def add_subordinate(self, agent: BaseAgent):
        self.subordinate_agents.append(agent)
        print(f"👑 {self.name}: Added {agent.name} ({agent.role.value}) to team")
    
    async def process_task(self, task: Task) -> str:
        print(f"\n👑 {self.name}: Managing complex task - '{task.description}'")
        
        # Step 1: Break down the task
        subtasks = await self._break_down_task(task)
        
        # Step 2: Plan execution order
        execution_plan = await self._create_execution_plan(subtasks)
        
        # Step 3: Delegate and coordinate
        results = []
        for subtask in execution_plan:
            assigned_agent = await self._assign_task(subtask)
            if assigned_agent:
                result = await assigned_agent.process_task(subtask)
                results.append(result)
        
        # Step 4: Quality review and integration
        final_result = await self._integrate_results(results)
        
        print(f"✅ {self.name}: Task completed with integrated results")
        return final_result
    
    async def _break_down_task(self, task: Task) -> List[Task]:
        print(f"📋 {self.name}: Breaking down task into subtasks")
        
        # Mock task breakdown
        subtasks = [
            Task("sub1", f"Research phase: {task.description}", 1),
            Task("sub2", f"Analysis phase: {task.description}", 2, dependencies=["sub1"]),
            Task("sub3", f"Content creation: {task.description}", 3, dependencies=["sub2"])
        ]
        
        return subtasks
    
    async def _create_execution_plan(self, subtasks: List[Task]) -> List[Task]:
        print(f"🗓️ {self.name}: Creating execution plan")
        # Sort by priority and dependencies
        return sorted(subtasks, key=lambda t: t.priority)
    
    async def _assign_task(self, subtask: Task) -> Optional[BaseAgent]:
        # Find best agent for task
        for agent in self.subordinate_agents:
            if await agent.can_handle_task(subtask):
                subtask.assigned_to = agent.name
                print(f"📨 {self.name}: Assigned '{subtask.description[:30]}...' to {agent.name}")
                return agent
        return None
    
    async def _integrate_results(self, results: List[str]) -> str:
        print(f"🎭 {self.name}: Integrating all results")
        
        messages = [
            {"role": "system", "content": "Integrate multiple results into a coherent final output."},
            {"role": "user", "content": f"Integrate these results: {'; '.join(results[:2])}..."}
        ]
        
        response = await self.client.chat_completions_create(
            model="gpt-4",
            messages=messages
        )
        
        return f"INTEGRATED RESULT: {response.choices[0].message.content}"

# Handoff Pattern Implementation
class HandoffOrchestrator:
    def __init__(self):
        self.agents: List[BaseAgent] = []
        self.handoff_chain: List[str] = []
    
    def add_agent(self, agent: BaseAgent):
        self.agents.append(agent)
        print(f"🔄 HandoffOrchestrator: Added {agent.name} to handoff chain")
    
    async def process_with_handoff(self, initial_task: Task) -> str:
        print(f"\n🔄 HandoffOrchestrator: Starting handoff workflow for '{initial_task.description}'")
        
        current_task = initial_task
        results_chain = []
        
        for i, agent in enumerate(self.agents):
            if await agent.can_handle_task(current_task):
                print(f"🤝 Handing off to {agent.name} (Step {i+1})")
                
                result = await agent.process_task(current_task)
                results_chain.append(result)
                
                # Create next task based on current result
                if i < len(self.agents) - 1:
                    next_task = Task(
                        id=f"handoff_{i+1}",
                        description=f"Process result from {agent.name}: {result[:50]}...",
                        priority=1
                    )
                    current_task = next_task
                    print(f"🔄 Created next task for handoff chain")
        
        final_result = f"HANDOFF CHAIN COMPLETED: {len(results_chain)} steps processed"
        print(f"✅ HandoffOrchestrator: Workflow completed")
        return final_result

# Demo Functions
async def demo_manager_pattern():
    print("="*60)
    print("🎯 MANAGER PATTERN DEMO")
    print("="*60)
    
    # Create manager and subordinates
    manager = ManagerAgent("ProductManager")
    research_agent = ResearchAgent("MarketResearcher")
    analysis_agent = AnalysisAgent("DataAnalyst") 
    content_agent = ContentAgent("ContentWriter")
    
    # Build team
    manager.add_subordinate(research_agent)
    manager.add_subordinate(analysis_agent)
    manager.add_subordinate(content_agent)
    
    # Complex task requiring coordination
    complex_task = Task(
        id="market_report",
        description="Create comprehensive market report for Q4 product launch strategy",
        priority=1
    )
    
    # Execute with manager coordination
    result = await manager.process_task(complex_task)
    print(f"\n📊 FINAL RESULT: {result[:100]}...")

async def demo_handoff_pattern():
    print("\n" + "="*60)
    print("🔄 HANDOFF PATTERN DEMO")
    print("="*60)
    
    # Create orchestrator and agents
    orchestrator = HandoffOrchestrator()
    
    # Add agents in handoff sequence
    orchestrator.add_agent(ResearchAgent("InitialResearcher"))
    orchestrator.add_agent(AnalysisAgent("DeepAnalyzer"))
    orchestrator.add_agent(ContentAgent("FinalWriter"))
    
    # Sequential task
    sequential_task = Task(
        id="research_pipeline",
        description="Customer feedback analysis pipeline for product improvement recommendations",
        priority=1
    )
    
    # Execute with handoff pattern
    result = await orchestrator.process_with_handoff(sequential_task)
    print(f"\n📊 FINAL RESULT: {result[:100]}...")

async def demo_pattern_comparison():
    print("\n" + "="*60)
    print("⚖️ PATTERN COMPARISON")
    print("="*60)
    
    print("👑 MANAGER PATTERN - Best for:")
    print("  ✅ Complex coordination requirements")
    print("  ✅ Quality control and oversight needed")
    print("  ✅ Resource optimization")
    print("  ✅ Parallel task execution")
    print("  ✅ Consistent output quality")
    
    print("\n🔄 HANDOFF PATTERN - Best for:")
    print("  ✅ Sequential workflow specialization")  
    print("  ✅ High expertise per step")
    print("  ✅ Flexible routing decisions")
    print("  ✅ Reduced coordination overhead")
    print("  ✅ Natural workflow progression")
    
    print("\n📊 Performance Characteristics:")
    print("  Manager Pattern: Higher coordination overhead, better quality control")
    print("  Handoff Pattern: Lower latency, higher specialization, more autonomous")

# Main execution
async def main():
    print("🤖 Multi-Agent Orchestration Patterns Demo")
    print("Comparing Manager vs Handoff patterns for agent coordination\n")
    
    # Run demos
    await demo_manager_pattern()
    await demo_handoff_pattern()
    await demo_pattern_comparison()
    
    print("\n" + "="*60)
    print("✅ DEMO COMPLETED")
    print("="*60)
    print("Key Takeaways:")
    print("• Manager Pattern: Centralized control with quality oversight")
    print("• Handoff Pattern: Decentralized expertise with flexible routing")
    print("• Choose based on coordination needs and quality requirements")

if __name__ == "__main__":
    asyncio.run(main())
