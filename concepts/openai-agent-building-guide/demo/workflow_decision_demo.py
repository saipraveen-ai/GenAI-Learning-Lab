#!/usr/bin/env python3
"""
Workflow Decision Framework Demo
===============================

Interactive decision tree to determine when to build agents vs traditional automation.
Demonstrates the decision framework with real-world scenarios and recommendations.

Requirements:
- Run from virtual environment: source venv/bin/activate
- Interactive CLI experience with scenario-based examples
"""

import asyncio
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional, Any

class AutomationType(Enum):
    TRADITIONAL = "traditional_automation"
    CHATBOT = "simple_chatbot"
    SINGLE_AGENT = "single_agent"
    MANAGER_PATTERN = "manager_pattern_multi_agent"
    HANDOFF_PATTERN = "handoff_pattern_multi_agent"
    HYBRID = "hybrid_approach"
    NOT_SUITABLE = "not_suitable"

@dataclass
class DecisionCriteria:
    well_defined_workflow: bool
    requires_dynamic_decisions: bool
    clear_success_criteria: bool
    involves_nlp: bool
    tolerates_variability: bool
    human_oversight_acceptable: bool
    multiple_interdependent_steps: bool
    needs_external_integration: bool
    mission_critical: bool
    comprehensive_guardrails_possible: bool
    multiple_users_concurrent: bool
    needs_specialized_expertise: bool
    needs_centralized_coordination: bool
    sequential_vs_parallel: str  # "sequential", "parallel", "mixed"

@dataclass
class Recommendation:
    automation_type: AutomationType
    confidence: float
    reasoning: List[str]
    implementation_steps: List[str]
    risks: List[str]
    success_metrics: List[str]
    real_world_examples: List[str]

class WorkflowDecisionEngine:
    def __init__(self):
        self.decision_tree = self._build_decision_tree()
    
    def _build_decision_tree(self) -> Dict[str, Any]:
        """Build the decision tree structure matching the diagram"""
        return {
            "start": {
                "question": "Is the workflow well-defined and deterministic?",
                "yes": "requires_dynamic",
                "no": "clear_success"
            },
            "requires_dynamic": {
                "question": "Does it require dynamic decision making?",
                "yes": "human_oversight",
                "no": "traditional"
            },
            "clear_success": {
                "question": "Can you define success criteria clearly?",
                "yes": "involves_nlp",
                "no": "not_suitable"
            },
            "human_oversight": {
                "question": "Is human oversight acceptable for edge cases?",
                "yes": "multiple_steps",
                "no": "traditional"
            },
            "involves_nlp": {
                "question": "Does it involve natural language understanding?",
                "yes": "tolerates_variability",
                "no": "traditional"
            },
            "tolerates_variability": {
                "question": "Can you tolerate some variability in outcomes?",
                "yes": "mission_critical",
                "no": "traditional"
            },
            "multiple_steps": {
                "question": "Are there multiple interdependent steps?",
                "yes": "external_integration",
                "no": "simple_chatbot"
            },
            "external_integration": {
                "question": "Do you need integration with external systems?",
                "yes": "multiple_users",
                "no": "simple_chatbot"
            },
            "mission_critical": {
                "question": "Is the task mission-critical?",
                "yes": "comprehensive_guardrails",
                "no": "single_agent"
            },
            "multiple_users": {
                "question": "Multiple users or concurrent workflows?",
                "yes": "specialized_expertise",
                "no": "single_agent"
            },
            "comprehensive_guardrails": {
                "question": "Can you implement comprehensive guardrails?",
                "yes": "single_agent",
                "no": "hybrid"
            },
            "specialized_expertise": {
                "question": "Need specialized expertise per workflow step?",
                "yes": "sequential_parallel",
                "no": "centralized_coordination"
            },
            "centralized_coordination": {
                "question": "Need centralized coordination and quality control?",
                "yes": "manager_pattern",
                "no": "single_agent"
            },
            "sequential_parallel": {
                "question": "Sequential workflow or parallel processing?",
                "sequential": "handoff_pattern",
                "parallel": "manager_pattern"
            }
        }
    
    async def evaluate_workflow(self, criteria: DecisionCriteria) -> Recommendation:
        """Evaluate workflow based on decision criteria"""
        
        # Navigate decision tree based on criteria
        current_node = "start"
        path = []
        
        while current_node in self.decision_tree:
            node = self.decision_tree[current_node]
            path.append(current_node)
            
            if current_node == "start":
                current_node = "requires_dynamic" if criteria.well_defined_workflow else "clear_success"
            elif current_node == "requires_dynamic":
                current_node = "human_oversight" if criteria.requires_dynamic_decisions else "traditional"
            elif current_node == "clear_success":
                current_node = "involves_nlp" if criteria.clear_success_criteria else "not_suitable"
            elif current_node == "human_oversight":
                current_node = "multiple_steps" if criteria.human_oversight_acceptable else "traditional"
            elif current_node == "involves_nlp":
                current_node = "tolerates_variability" if criteria.involves_nlp else "traditional"
            elif current_node == "tolerates_variability":
                current_node = "mission_critical" if criteria.tolerates_variability else "traditional"
            elif current_node == "multiple_steps":
                current_node = "external_integration" if criteria.multiple_interdependent_steps else "simple_chatbot"
            elif current_node == "external_integration":
                current_node = "multiple_users" if criteria.needs_external_integration else "simple_chatbot"
            elif current_node == "mission_critical":
                current_node = "comprehensive_guardrails" if criteria.mission_critical else "single_agent"
            elif current_node == "multiple_users":
                current_node = "specialized_expertise" if criteria.multiple_users_concurrent else "single_agent"
            elif current_node == "comprehensive_guardrails":
                current_node = "single_agent" if criteria.comprehensive_guardrails_possible else "hybrid"
            elif current_node == "specialized_expertise":
                current_node = "sequential_parallel" if criteria.needs_specialized_expertise else "centralized_coordination"
            elif current_node == "centralized_coordination":
                current_node = "manager_pattern" if criteria.needs_centralized_coordination else "single_agent"
            elif current_node == "sequential_parallel":
                if criteria.sequential_vs_parallel == "sequential":
                    current_node = "handoff_pattern"
                else:
                    current_node = "manager_pattern"
            else:
                break
        
        # Map final node to automation type
        automation_type_map = {
            "traditional": AutomationType.TRADITIONAL,
            "simple_chatbot": AutomationType.CHATBOT,
            "single_agent": AutomationType.SINGLE_AGENT,
            "manager_pattern": AutomationType.MANAGER_PATTERN,
            "handoff_pattern": AutomationType.HANDOFF_PATTERN,
            "hybrid": AutomationType.HYBRID,
            "not_suitable": AutomationType.NOT_SUITABLE
        }
        
        automation_type = automation_type_map.get(current_node, AutomationType.NOT_SUITABLE)
        
        return await self._generate_recommendation(automation_type, criteria, path)
    
    async def _generate_recommendation(self, automation_type: AutomationType, criteria: DecisionCriteria, path: List[str]) -> Recommendation:
        """Generate detailed recommendation based on automation type"""
        
        recommendations = {
            AutomationType.TRADITIONAL: {
                "confidence": 0.95,
                "reasoning": [
                    "Workflow is well-defined and deterministic",
                    "No dynamic decision making required",
                    "Traditional automation tools are sufficient",
                    "Lower complexity and maintenance overhead"
                ],
                "implementation_steps": [
                    "Map out exact workflow steps",
                    "Choose appropriate automation tool (RPA, scripts, APIs)",
                    "Implement error handling and monitoring",
                    "Test thoroughly with edge cases",
                    "Deploy with proper monitoring"
                ],
                "risks": [
                    "Brittle when requirements change",
                    "Limited adaptability to new scenarios",
                    "May require manual intervention for exceptions"
                ],
                "success_metrics": [
                    "Process completion rate > 95%",
                    "Error rate < 1%",
                    "Processing time reduction > 50%",
                    "Manual intervention rate < 5%"
                ],
                "real_world_examples": [
                    "Data backup scripts",
                    "Invoice processing pipelines",
                    "ETL data transformations",
                    "System monitoring alerts"
                ]
            },
            
            AutomationType.CHATBOT: {
                "confidence": 0.85,
                "reasoning": [
                    "Single-turn interactions sufficient",
                    "Natural language understanding needed",
                    "No complex workflow orchestration required",
                    "Simple Q&A or content generation focus"
                ],
                "implementation_steps": [
                    "Define conversation scope and intents",
                    "Create training data and response templates",
                    "Implement LLM integration",
                    "Add basic safety filters",
                    "Test with user scenarios"
                ],
                "risks": [
                    "Limited to single-turn interactions",
                    "Cannot handle complex multi-step workflows",
                    "May provide inconsistent responses"
                ],
                "success_metrics": [
                    "User satisfaction > 80%",
                    "Intent recognition accuracy > 90%",
                    "Response relevance score > 85%",
                    "Escalation rate < 10%"
                ],
                "real_world_examples": [
                    "FAQ chatbots",
                    "Content generation tools",
                    "Simple Q&A systems",
                    "Document summarization services"
                ]
            },
            
            AutomationType.SINGLE_AGENT: {
                "confidence": 0.80,
                "reasoning": [
                    "Multiple interdependent steps required",
                    "Dynamic decision making needed",
                    "Tool integration necessary",
                    "Manageable complexity for single agent"
                ],
                "implementation_steps": [
                    "Define agent capabilities and tools",
                    "Implement reasoning and planning logic",
                    "Create tool integration layer",
                    "Add comprehensive guardrails",
                    "Build monitoring and oversight systems"
                ],
                "risks": [
                    "Single point of failure",
                    "May become complex as requirements grow",
                    "Requires robust error handling"
                ],
                "success_metrics": [
                    "Task completion rate > 85%",
                    "User satisfaction > 85%",
                    "Response time < 30 seconds",
                    "Safety incident rate < 0.1%"
                ],
                "real_world_examples": [
                    "Customer service ticket routing",
                    "Research compilation tasks",
                    "Report generation workflows",
                    "Basic fraud detection systems"
                ]
            },
            
            AutomationType.MANAGER_PATTERN: {
                "confidence": 0.75,
                "reasoning": [
                    "Complex coordination requirements",
                    "Multiple specialized agents needed",
                    "Quality control and oversight critical", 
                    "Parallel processing beneficial"
                ],
                "implementation_steps": [
                    "Design manager agent architecture",
                    "Create specialized subordinate agents",
                    "Implement task delegation logic",
                    "Build quality review processes",
                    "Add comprehensive monitoring"
                ],
                "risks": [
                    "High complexity and coordination overhead",
                    "Manager agent becomes bottleneck",
                    "Difficult to debug multi-agent interactions"
                ],
                "success_metrics": [
                    "Overall workflow completion > 90%",
                    "Quality score > 95%",
                    "Resource utilization > 80%",
                    "Coordination efficiency > 85%"
                ],
                "real_world_examples": [
                    "Enterprise content creation workflows",
                    "Complex customer journey orchestration",
                    "Multi-step financial analysis",
                    "Comprehensive market research projects"
                ]
            },
            
            AutomationType.HANDOFF_PATTERN: {
                "confidence": 0.75,
                "reasoning": [
                    "Sequential workflow with high specialization",
                    "Each step requires domain expertise",
                    "Flexible routing decisions needed",
                    "Reduced coordination overhead preferred"
                ],
                "implementation_steps": [
                    "Design specialized agents for each step",
                    "Implement handoff decision logic",
                    "Create context preservation mechanisms",
                    "Add monitoring for handoff quality",
                    "Build failure recovery processes"
                ],
                "risks": [
                    "Context loss during handoffs",
                    "Difficult to maintain state consistency",
                    "Complex debugging across agent chain"
                ],
                "success_metrics": [
                    "End-to-end completion rate > 85%",
                    "Handoff success rate > 95%",
                    "Specialization quality > 90%",
                    "Average processing time meets SLA"
                ],
                "real_world_examples": [
                    "Multi-step fraud investigation",
                    "Complex technical support workflows",
                    "Research-to-publication pipelines",
                    "Advanced customer onboarding"
                ]
            },
            
            AutomationType.HYBRID: {
                "confidence": 0.70,
                "reasoning": [
                    "Mission-critical but insufficient guardrails",
                    "Human-in-the-loop required for safety",
                    "Agent assistance valuable but not autonomous",
                    "Gradual automation approach recommended"
                ],
                "implementation_steps": [
                    "Identify low-risk automation opportunities",
                    "Implement agent-assisted workflows",
                    "Create human approval processes",
                    "Build confidence through gradual expansion",
                    "Develop comprehensive safety measures"
                ],
                "risks": [
                    "Higher operational overhead",
                    "Potential for human bottlenecks",
                    "Complex approval workflows"
                ],
                "success_metrics": [
                    "Human productivity increase > 40%",
                    "Error reduction > 60%",
                    "Safety incident rate = 0",
                    "User satisfaction > 85%"
                ],
                "real_world_examples": [
                    "Medical diagnosis assistance",
                    "Financial advisory support",
                    "Legal document review",
                    "Safety-critical system monitoring"
                ]
            },
            
            AutomationType.NOT_SUITABLE: {
                "confidence": 0.90,
                "reasoning": [
                    "Requirements too undefined for automation",
                    "Success criteria unclear",
                    "Manual process needs refinement first",
                    "Premature for automation consideration"
                ],
                "implementation_steps": [
                    "Refine and document manual processes",
                    "Define clear success criteria",
                    "Gather process performance data",
                    "Identify potential automation points",
                    "Reassess when process stabilizes"
                ],
                "risks": [
                    "Wasted effort on premature automation",
                    "Poor user experience from unclear requirements",
                    "Technical debt from rushed implementation"
                ],
                "success_metrics": [
                    "Process documentation completeness",
                    "Success criteria clarity",
                    "Manual process consistency > 80%",
                    "Stakeholder requirement alignment"
                ],
                "real_world_examples": [
                    "Highly creative processes",
                    "Undefined business processes",
                    "Experimental workflows",
                    "Rapidly changing requirements"
                ]
            }
        }
        
        rec_data = recommendations[automation_type]
        
        return Recommendation(
            automation_type=automation_type,
            confidence=rec_data["confidence"],
            reasoning=rec_data["reasoning"],
            implementation_steps=rec_data["implementation_steps"],
            risks=rec_data["risks"],
            success_metrics=rec_data["success_metrics"],
            real_world_examples=rec_data["real_world_examples"]
        )

# Interactive Demo Functions
async def interactive_decision_demo():
    """Interactive workflow decision demo"""
    print("="*60)
    print("🎯 INTERACTIVE WORKFLOW DECISION DEMO")
    print("="*60)
    print("Let's walk through the decision framework with your specific use case!\n")
    
    engine = WorkflowDecisionEngine()
    
    # Collect user input for decision criteria
    print("Please answer the following questions about your workflow:\n")
    
    # Well-defined workflow
    well_defined = await _ask_yes_no("Is your workflow well-defined and deterministic?")
    
    # Dynamic decisions (only if well-defined)
    requires_dynamic = False
    if well_defined:
        requires_dynamic = await _ask_yes_no("Does it require dynamic decision making?")
    
    # Success criteria (only if not well-defined)
    clear_success = True
    if not well_defined:
        clear_success = await _ask_yes_no("Can you define success criteria clearly?")
        if not clear_success:
            print("\n🚫 Recommendation: Not suitable for automation yet.")
            print("   Focus on refining your process first!\n")
            return
    
    # Human oversight (only if dynamic decisions needed)
    human_oversight = False
    if requires_dynamic:
        human_oversight = await _ask_yes_no("Is human oversight acceptable for edge cases?")
    
    # NLP involvement
    involves_nlp = await _ask_yes_no("Does it involve natural language understanding?")
    
    # Variability tolerance
    tolerates_variability = True
    if involves_nlp:
        tolerates_variability = await _ask_yes_no("Can you tolerate some variability in outcomes?")
    
    # Mission critical
    mission_critical = False
    if tolerates_variability or not involves_nlp:
        mission_critical = await _ask_yes_no("Is the task mission-critical?")
    
    # Multiple steps
    multiple_steps = False
    if human_oversight or (not requires_dynamic and well_defined):
        multiple_steps = await _ask_yes_no("Are there multiple interdependent steps?")
    
    # External integration
    external_integration = False
    if multiple_steps:
        external_integration = await _ask_yes_no("Do you need integration with external systems?")
    
    # Multiple users
    multiple_users = False
    if external_integration or (not mission_critical and tolerates_variability):
        multiple_users = await _ask_yes_no("Multiple users or concurrent workflows?")
    
    # Comprehensive guardrails
    comprehensive_guardrails = False
    if mission_critical:
        comprehensive_guardrails = await _ask_yes_no("Can you implement comprehensive guardrails?")
    
    # Specialized expertise
    specialized_expertise = False
    if multiple_users:
        specialized_expertise = await _ask_yes_no("Need specialized expertise per workflow step?")
    
    # Centralized coordination
    centralized_coordination = False
    if not specialized_expertise and multiple_users:
        centralized_coordination = await _ask_yes_no("Need centralized coordination and quality control?")
    
    # Sequential vs parallel
    sequential_parallel = "sequential"
    if specialized_expertise:
        print("\nIs your workflow primarily:")
        print("1. Sequential (one step after another)")
        print("2. Parallel (multiple steps at once)")
        choice = input("Enter choice (1 or 2): ").strip()
        sequential_parallel = "sequential" if choice == "1" else "parallel"
    
    # Build criteria object
    criteria = DecisionCriteria(
        well_defined_workflow=well_defined,
        requires_dynamic_decisions=requires_dynamic,
        clear_success_criteria=clear_success,
        involves_nlp=involves_nlp,
        tolerates_variability=tolerates_variability,
        human_oversight_acceptable=human_oversight,
        multiple_interdependent_steps=multiple_steps,
        needs_external_integration=external_integration,
        mission_critical=mission_critical,
        comprehensive_guardrails_possible=comprehensive_guardrails,
        multiple_users_concurrent=multiple_users,
        needs_specialized_expertise=specialized_expertise,
        needs_centralized_coordination=centralized_coordination,
        sequential_vs_parallel=sequential_parallel
    )
    
    # Get recommendation
    recommendation = await engine.evaluate_workflow(criteria)
    
    # Display results
    await _display_recommendation(recommendation)

async def _ask_yes_no(question: str) -> bool:
    """Helper function to ask yes/no questions"""
    while True:
        answer = input(f"❓ {question} (y/n): ").strip().lower()
        if answer in ['y', 'yes']:
            return True
        elif answer in ['n', 'no']:
            return False
        else:
            print("   Please enter 'y' or 'n'")

async def _display_recommendation(recommendation: Recommendation) -> None:
    """Display the recommendation in a formatted way"""
    
    type_names = {
        AutomationType.TRADITIONAL: "Traditional Automation",
        AutomationType.CHATBOT: "Simple Chatbot/LLM",
        AutomationType.SINGLE_AGENT: "Single Agent",
        AutomationType.MANAGER_PATTERN: "Manager Pattern Multi-Agent",
        AutomationType.HANDOFF_PATTERN: "Handoff Pattern Multi-Agent",
        AutomationType.HYBRID: "Hybrid Human-Agent Approach",
        AutomationType.NOT_SUITABLE: "Not Suitable for Automation"
    }
    
    print("\n" + "="*60)
    print("📊 RECOMMENDATION RESULTS")
    print("="*60)
    
    print(f"🎯 Recommended Approach: {type_names[recommendation.automation_type]}")
    print(f"🔮 Confidence Level: {recommendation.confidence:.0%}")
    
    print(f"\n💡 Reasoning:")
    for reason in recommendation.reasoning:
        print(f"   • {reason}")
    
    print(f"\n🛠️ Implementation Steps:")
    for i, step in enumerate(recommendation.implementation_steps, 1):
        print(f"   {i}. {step}")
    
    print(f"\n⚠️ Risks to Consider:")
    for risk in recommendation.risks:
        print(f"   • {risk}")
    
    print(f"\n📈 Success Metrics:")
    for metric in recommendation.success_metrics:
        print(f"   • {metric}")
    
    print(f"\n🌍 Real-World Examples:")
    for example in recommendation.real_world_examples:
        print(f"   • {example}")

async def demo_predefined_scenarios():
    """Demo with predefined scenarios"""
    print("\n" + "="*60)
    print("📋 PREDEFINED SCENARIO DEMOS")
    print("="*60)
    
    engine = WorkflowDecisionEngine()
    
    scenarios = [
        {
            "name": "Customer Service Automation",
            "criteria": DecisionCriteria(
                well_defined_workflow=False,
                requires_dynamic_decisions=True,
                clear_success_criteria=True,
                involves_nlp=True,
                tolerates_variability=True,
                human_oversight_acceptable=True,
                multiple_interdependent_steps=True,
                needs_external_integration=True,
                mission_critical=False,
                comprehensive_guardrails_possible=True,
                multiple_users_concurrent=True,
                needs_specialized_expertise=False,
                needs_centralized_coordination=False,
                sequential_vs_parallel="sequential"
            )
        },
        {
            "name": "Financial Report Generation",
            "criteria": DecisionCriteria(
                well_defined_workflow=True,
                requires_dynamic_decisions=True,
                clear_success_criteria=True,
                involves_nlp=True,
                tolerates_variability=False,
                human_oversight_acceptable=True,
                multiple_interdependent_steps=True,
                needs_external_integration=True,
                mission_critical=True,
                comprehensive_guardrails_possible=True,
                multiple_users_concurrent=False,
                needs_specialized_expertise=False,
                needs_centralized_coordination=False,
                sequential_vs_parallel="sequential"
            )
        },
        {
            "name": "Data Backup System",
            "criteria": DecisionCriteria(
                well_defined_workflow=True,
                requires_dynamic_decisions=False,
                clear_success_criteria=True,
                involves_nlp=False,
                tolerates_variability=False,
                human_oversight_acceptable=False,
                multiple_interdependent_steps=False,
                needs_external_integration=False,
                mission_critical=False,
                comprehensive_guardrails_possible=False,
                multiple_users_concurrent=False,
                needs_specialized_expertise=False,
                needs_centralized_coordination=False,
                sequential_vs_parallel="sequential"
            )
        }
    ]
    
    for scenario in scenarios:
        print(f"\n📋 Scenario: {scenario['name']}")
        print("-" * 40)
        
        recommendation = await engine.evaluate_workflow(scenario["criteria"])
        
        type_names = {
            AutomationType.TRADITIONAL: "Traditional Automation",
            AutomationType.CHATBOT: "Simple Chatbot",
            AutomationType.SINGLE_AGENT: "Single Agent",
            AutomationType.MANAGER_PATTERN: "Manager Pattern",
            AutomationType.HANDOFF_PATTERN: "Handoff Pattern",
            AutomationType.HYBRID: "Hybrid Approach",
            AutomationType.NOT_SUITABLE: "Not Suitable"
        }
        
        print(f"Recommendation: {type_names[recommendation.automation_type]}")
        print(f"Confidence: {recommendation.confidence:.0%}")
        print(f"Key Reasoning: {recommendation.reasoning[0]}")

# Main execution
async def main():
    print("🎯 Workflow Decision Framework Demo")
    print("When to build agents vs traditional automation\n")
    
    print("Choose demo mode:")
    print("1. Interactive Decision Tree (recommended)")
    print("2. Predefined Scenarios")
    print("3. Both")
    
    choice = input("\nEnter choice (1, 2, or 3): ").strip()
    
    if choice in ["1", "3"]:
        await interactive_decision_demo()
    
    if choice in ["2", "3"]:
        await demo_predefined_scenarios()
    
    print("\n" + "="*60)
    print("✅ DECISION FRAMEWORK DEMO COMPLETED")
    print("="*60)
    print("Key Decision Principles:")
    print("• Start simple: Traditional automation for deterministic workflows")
    print("• Add intelligence: Agents for dynamic decision making")
    print("• Scale thoughtfully: Multi-agent only when complexity justifies it")
    print("• Prioritize safety: Comprehensive guardrails for critical systems")
    print("• Iterate gradually: Begin with low-risk implementations")

if __name__ == "__main__":
    asyncio.run(main())
