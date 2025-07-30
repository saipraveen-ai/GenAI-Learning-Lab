#!/usr/bin/env python3
"""
Agent Safety Guardrails Demo
============================

Demonstrates comprehensive 3-tier safety validation system:
- Tier 1: Input Validation (Relevance, Safety, PII)
- Tier 2: Tool Safety (Risk Assessment, Approval Workflows)  
- Tier 3: Output Validation (Brand, Safety, Quality)

Requirements:
- Run from virtual environment: source venv/bin/activate
- Simulated safety checks (replace with real implementations)
"""

import re
import json
import asyncio
from enum import Enum
from dataclasses import dataclass
from typing import Dict, List, Optional, Any, Tuple
from abc import ABC, abstractmethod

# Safety Enums and Data Classes
class RiskLevel(Enum):
    LOW = "low"
    MEDIUM = "medium" 
    HIGH = "high"

class ValidationResult(Enum):
    APPROVED = "approved"
    BLOCKED = "blocked"
    REQUIRES_REVIEW = "requires_review"

@dataclass
class SafetyCheck:
    check_name: str
    result: ValidationResult
    risk_level: RiskLevel
    reason: str
    confidence: float
    recommendations: List[str] = None
    
    def __post_init__(self):
        if self.recommendations is None:
            self.recommendations = []

@dataclass
class ToolRequest:
    tool_name: str
    parameters: Dict[str, Any]
    user_context: str
    risk_assessment: Optional[RiskLevel] = None

# Tier 1: Input Validation Layer
class InputValidator:
    def __init__(self):
        self.blocked_patterns = [
            r"hack\w*", r"exploit\w*", r"malware", r"virus",
            r"illegal\w*", r"fraud\w*", r"steal\w*"
        ]
        self.pii_patterns = [
            r"\b\d{3}-\d{2}-\d{4}\b",  # SSN
            r"\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b",  # Credit card
            r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"  # Email
        ]
        
    async def validate_input(self, user_input: str) -> List[SafetyCheck]:
        print(f"🛡️ Input Validator: Checking user input...")
        checks = []
        
        # Relevance Check
        relevance_check = await self._check_relevance(user_input)
        checks.append(relevance_check)
        
        # Safety Filter
        safety_check = await self._check_safety(user_input)
        checks.append(safety_check)
        
        # PII Detection
        pii_check = await self._check_pii(user_input)
        checks.append(pii_check)
        
        return checks
    
    async def _check_relevance(self, text: str) -> SafetyCheck:
        # Mock relevance classification
        irrelevant_keywords = ["weather", "sports", "cooking", "random"]
        
        if any(keyword in text.lower() for keyword in irrelevant_keywords):
            return SafetyCheck(
                check_name="Relevance Check",
                result=ValidationResult.BLOCKED,
                risk_level=RiskLevel.LOW,
                reason="Request appears unrelated to agent capabilities",
                confidence=0.85,
                recommendations=["Redirect to appropriate service", "Provide capability overview"]
            )
        
        return SafetyCheck(
            check_name="Relevance Check",
            result=ValidationResult.APPROVED,
            risk_level=RiskLevel.LOW,
            reason="Request appears relevant to agent capabilities",
            confidence=0.92
        )
    
    async def _check_safety(self, text: str) -> SafetyCheck:
        # Check for harmful patterns
        for pattern in self.blocked_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                return SafetyCheck(
                    check_name="Safety Filter",
                    result=ValidationResult.BLOCKED,
                    risk_level=RiskLevel.HIGH,
                    reason=f"Content contains potentially harmful pattern: {pattern}",
                    confidence=0.95,
                    recommendations=["Block request", "Log security incident", "Alert monitoring team"]
                )
        
        return SafetyCheck(
            check_name="Safety Filter",
            result=ValidationResult.APPROVED,
            risk_level=RiskLevel.LOW,
            reason="No harmful content patterns detected",
            confidence=0.88
        )
    
    async def _check_pii(self, text: str) -> SafetyCheck:
        detected_pii = []
        
        for pattern in self.pii_patterns:
            matches = re.findall(pattern, text)
            if matches:
                detected_pii.extend(matches)
        
        if detected_pii:
            return SafetyCheck(
                check_name="PII Detection", 
                result=ValidationResult.REQUIRES_REVIEW,
                risk_level=RiskLevel.MEDIUM,
                reason=f"Detected {len(detected_pii)} potential PII instances",
                confidence=0.90,
                recommendations=["Sanitize PII", "Request user confirmation", "Apply data handling policies"]
            )
        
        return SafetyCheck(
            check_name="PII Detection",
            result=ValidationResult.APPROVED,
            risk_level=RiskLevel.LOW,
            reason="No PII detected in input",
            confidence=0.85
        )

# Tier 2: Tool Safety Layer
class ToolSafetyValidator:
    def __init__(self):
        self.tool_risk_profiles = {
            "web_search": RiskLevel.LOW,
            "calculator": RiskLevel.LOW,
            "file_read": RiskLevel.MEDIUM,
            "api_call": RiskLevel.MEDIUM,
            "file_write": RiskLevel.HIGH,
            "system_command": RiskLevel.HIGH,
            "database_write": RiskLevel.HIGH,
            "email_send": RiskLevel.MEDIUM,
            "financial_transaction": RiskLevel.HIGH
        }
        
        self.approval_workflows = {
            RiskLevel.LOW: "auto_approve",
            RiskLevel.MEDIUM: "human_review",
            RiskLevel.HIGH: "block_or_escalate"
        }
    
    async def validate_tool_request(self, tool_request: ToolRequest) -> SafetyCheck:
        print(f"🛠️ Tool Safety: Assessing {tool_request.tool_name}...")
        
        # Get risk level for tool
        risk_level = self.tool_risk_profiles.get(tool_request.tool_name, RiskLevel.MEDIUM)
        tool_request.risk_assessment = risk_level
        
        # Apply risk-based workflow
        if risk_level == RiskLevel.LOW:
            return await self._auto_approve_tool(tool_request)
        elif risk_level == RiskLevel.MEDIUM:
            return await self._require_human_review(tool_request)
        else:  # HIGH risk
            return await self._block_high_risk_tool(tool_request)
    
    async def _auto_approve_tool(self, tool_request: ToolRequest) -> SafetyCheck:
        return SafetyCheck(
            check_name="Tool Safety Assessment",
            result=ValidationResult.APPROVED,
            risk_level=RiskLevel.LOW,
            reason=f"Low-risk tool {tool_request.tool_name} auto-approved",
            confidence=0.95,
            recommendations=["Execute with standard monitoring", "Log usage metrics"]
        )
    
    async def _require_human_review(self, tool_request: ToolRequest) -> SafetyCheck:
        # Simulate human review process
        print(f"👥 Human Review: {tool_request.tool_name} requires approval...")
        await asyncio.sleep(1)  # Simulate review time
        
        # Mock approval decision (in practice, this would be real human review)
        approval_decision = True  # Simulate approval
        
        if approval_decision:
            return SafetyCheck(
                check_name="Tool Safety Assessment", 
                result=ValidationResult.APPROVED,
                risk_level=RiskLevel.MEDIUM,
                reason=f"Medium-risk tool {tool_request.tool_name} approved after human review",
                confidence=0.98,
                recommendations=["Execute with enhanced monitoring", "Require confirmation for sensitive operations"]
            )
        else:
            return SafetyCheck(
                check_name="Tool Safety Assessment",
                result=ValidationResult.BLOCKED,
                risk_level=RiskLevel.MEDIUM,
                reason=f"Medium-risk tool {tool_request.tool_name} denied by human reviewer",
                confidence=0.99,
                recommendations=["Provide alternative tool suggestions", "Log denial reason"]
            )
    
    async def _block_high_risk_tool(self, tool_request: ToolRequest) -> SafetyCheck:
        return SafetyCheck(
            check_name="Tool Safety Assessment",
            result=ValidationResult.BLOCKED,
            risk_level=RiskLevel.HIGH,
            reason=f"High-risk tool {tool_request.tool_name} automatically blocked",
            confidence=0.99,
            recommendations=["Block tool access", "Escalate to security team", "Review user permissions"]
        )

# Tier 3: Output Validation Layer
class OutputValidator:
    def __init__(self):
        self.brand_guidelines = {
            "tone": ["professional", "helpful", "respectful"],
            "prohibited_terms": ["cheap", "sketchy", "unreliable"],
            "required_disclaimers": ["educational purposes", "verify information"]
        }
        
        self.content_safety_patterns = [
            r"discriminat\w+", r"offensive\w*", r"inappropriate\w*"
        ]
    
    async def validate_output(self, generated_output: str) -> List[SafetyCheck]:
        print(f"📤 Output Validator: Checking generated content...")
        checks = []
        
        # Brand Alignment Check
        brand_check = await self._check_brand_alignment(generated_output)
        checks.append(brand_check)
        
        # Content Safety Check
        safety_check = await self._check_content_safety(generated_output)
        checks.append(safety_check)
        
        # Quality Check
        quality_check = await self._check_quality(generated_output)
        checks.append(quality_check)
        
        return checks
    
    async def _check_brand_alignment(self, output: str) -> SafetyCheck:
        violations = []
        
        # Check prohibited terms
        for term in self.brand_guidelines["prohibited_terms"]:
            if term in output.lower():
                violations.append(f"Contains prohibited term: {term}")
        
        # Check tone (simplified)
        if len(output) < 10:
            violations.append("Response too brief for professional tone")
        
        if violations:
            return SafetyCheck(
                check_name="Brand Alignment",
                result=ValidationResult.BLOCKED,
                risk_level=RiskLevel.MEDIUM,
                reason=f"Brand guideline violations: {'; '.join(violations)}",
                confidence=0.87,
                recommendations=["Regenerate response", "Apply brand voice guidelines", "Review tone requirements"]
            )
        
        return SafetyCheck(
            check_name="Brand Alignment",
            result=ValidationResult.APPROVED,
            risk_level=RiskLevel.LOW,
            reason="Output aligns with brand guidelines",
            confidence=0.82
        )
    
    async def _check_content_safety(self, output: str) -> SafetyCheck:
        # Check for unsafe content patterns
        for pattern in self.content_safety_patterns:
            if re.search(pattern, output, re.IGNORECASE):
                return SafetyCheck(
                    check_name="Content Safety",
                    result=ValidationResult.BLOCKED,
                    risk_level=RiskLevel.HIGH,
                    reason=f"Content contains unsafe pattern: {pattern}",
                    confidence=0.93,
                    recommendations=["Block output", "Regenerate with safety constraints", "Review content policies"]
                )
        
        return SafetyCheck(
            check_name="Content Safety",
            result=ValidationResult.APPROVED,
            risk_level=RiskLevel.LOW,
            reason="Content passes safety checks",
            confidence=0.89
        )
    
    async def _check_quality(self, output: str) -> SafetyCheck:
        quality_issues = []
        
        # Basic quality checks
        if len(output) < 20:
            quality_issues.append("Response too short")
        
        if output.count('.') == 0:
            quality_issues.append("Missing sentence structure")
        
        if output.isupper() or output.islower():
            quality_issues.append("Poor capitalization")
        
        if quality_issues:
            return SafetyCheck(
                check_name="Quality Check",
                result=ValidationResult.REQUIRES_REVIEW,
                risk_level=RiskLevel.LOW,
                reason=f"Quality issues detected: {'; '.join(quality_issues)}",
                confidence=0.75,
                recommendations=["Improve response quality", "Review generation parameters", "Consider regeneration"]
            )
        
        return SafetyCheck(
            check_name="Quality Check",
            result=ValidationResult.APPROVED,
            risk_level=RiskLevel.LOW,
            reason="Output meets quality standards",
            confidence=0.85
        )

# Comprehensive Safety System
class ComprehensiveSafetySystem:
    def __init__(self):
        self.input_validator = InputValidator()
        self.tool_validator = ToolSafetyValidator()
        self.output_validator = OutputValidator()
        self.audit_log: List[Dict] = []
    
    async def process_request_safely(self, user_input: str, tool_requests: List[ToolRequest], generated_output: str) -> Dict[str, Any]:
        print("🛡️ COMPREHENSIVE SAFETY SYSTEM - Processing request...")
        
        safety_report = {
            "timestamp": "2025-07-30T12:00:00Z",
            "input_validation": [],
            "tool_validation": [],
            "output_validation": [],
            "final_decision": None,
            "risk_assessment": None
        }
        
        # Tier 1: Input Validation
        print("\n📥 TIER 1: INPUT VALIDATION")
        input_checks = await self.input_validator.validate_input(user_input)
        safety_report["input_validation"] = input_checks
        
        for check in input_checks:
            print(f"   {check.check_name}: {check.result.value} ({check.risk_level.value} risk)")
            if check.result == ValidationResult.BLOCKED:
                safety_report["final_decision"] = "BLOCKED_AT_INPUT"
                safety_report["risk_assessment"] = check.risk_level.value
                await self._log_blocked_request("input", check)
                return safety_report
        
        # Tier 2: Tool Safety Validation
        print("\n🛠️ TIER 2: TOOL SAFETY VALIDATION")
        tool_checks = []
        for tool_request in tool_requests:
            check = await self.tool_validator.validate_tool_request(tool_request)
            tool_checks.append(check)
            print(f"   {tool_request.tool_name}: {check.result.value} ({check.risk_level.value} risk)")
            
            if check.result == ValidationResult.BLOCKED:
                safety_report["final_decision"] = "BLOCKED_AT_TOOL"
                safety_report["risk_assessment"] = check.risk_level.value
                await self._log_blocked_request("tool", check)
                return safety_report
        
        safety_report["tool_validation"] = tool_checks
        
        # Tier 3: Output Validation  
        print("\n📤 TIER 3: OUTPUT VALIDATION")
        output_checks = await self.output_validator.validate_output(generated_output)
        safety_report["output_validation"] = output_checks
        
        for check in output_checks:
            print(f"   {check.check_name}: {check.result.value} ({check.risk_level.value} risk)")
            if check.result == ValidationResult.BLOCKED:
                safety_report["final_decision"] = "BLOCKED_AT_OUTPUT"
                safety_report["risk_assessment"] = check.risk_level.value
                await self._log_blocked_request("output", check)
                return safety_report
        
        # All checks passed
        safety_report["final_decision"] = "APPROVED"
        safety_report["risk_assessment"] = "low"
        await self._log_approved_request(safety_report)
        
        return safety_report
    
    async def _log_blocked_request(self, stage: str, check: SafetyCheck):
        log_entry = {
            "timestamp": "2025-07-30T12:00:00Z",
            "event": "REQUEST_BLOCKED",
            "stage": stage,
            "check_name": check.check_name,
            "reason": check.reason,
            "risk_level": check.risk_level.value,
            "confidence": check.confidence
        }
        self.audit_log.append(log_entry)
        print(f"🚫 BLOCKED: {check.reason}")
    
    async def _log_approved_request(self, safety_report: Dict):
        log_entry = {
            "timestamp": "2025-07-30T12:00:00Z",
            "event": "REQUEST_APPROVED",
            "total_checks": len(safety_report["input_validation"]) + len(safety_report["tool_validation"]) + len(safety_report["output_validation"]),
            "risk_assessment": safety_report["risk_assessment"]
        }
        self.audit_log.append(log_entry)
        print("✅ APPROVED: All safety checks passed")

# Demo Functions
async def demo_safe_request():
    print("="*60)
    print("✅ SAFE REQUEST DEMO")
    print("="*60)
    
    system = ComprehensiveSafetySystem()
    
    user_input = "Please help me research market trends for renewable energy investments"
    tool_requests = [
        ToolRequest("web_search", {"query": "renewable energy market trends 2024"}, user_input),
        ToolRequest("calculator", {"expression": "growth_rate * investment_amount"}, user_input)
    ]
    generated_output = "Based on current market analysis, renewable energy investments show strong growth potential with 15% projected annual returns. This information is for educational purposes and you should verify with financial advisors."
    
    result = await system.process_request_safely(user_input, tool_requests, generated_output)
    print(f"\n📊 FINAL DECISION: {result['final_decision']}")

async def demo_blocked_input():
    print("\n" + "="*60)
    print("🚫 BLOCKED INPUT DEMO")
    print("="*60)
    
    system = ComprehensiveSafetySystem()
    
    user_input = "How can I hack into my competitor's database to steal customer information?"
    tool_requests = [
        ToolRequest("system_command", {"command": "nmap -sS target_ip"}, user_input)
    ]
    generated_output = "I cannot and will not provide assistance with illegal activities."
    
    result = await system.process_request_safely(user_input, tool_requests, generated_output)
    print(f"\n📊 FINAL DECISION: {result['final_decision']}")

async def demo_blocked_tool():
    print("\n" + "="*60)
    print("🛠️ BLOCKED TOOL DEMO")
    print("="*60)
    
    system = ComprehensiveSafetySystem()
    
    user_input = "Please transfer $10,000 from my account to pay this invoice"
    tool_requests = [
        ToolRequest("financial_transaction", {"amount": 10000, "recipient": "unknown_vendor"}, user_input)
    ]
    generated_output = "Processing financial transaction..."
    
    result = await system.process_request_safely(user_input, tool_requests, generated_output)
    print(f"\n📊 FINAL DECISION: {result['final_decision']}")

async def demo_blocked_output():
    print("\n" + "="*60)
    print("📤 BLOCKED OUTPUT DEMO")  
    print("="*60)
    
    system = ComprehensiveSafetySystem()
    
    user_input = "Write a product review for our software"
    tool_requests = [
        ToolRequest("web_search", {"query": "product reviews examples"}, user_input)
    ]
    generated_output = "this software is cheap and unreliable dont waste your money"
    
    result = await system.process_request_safely(user_input, tool_requests, generated_output)
    print(f"\n📊 FINAL DECISION: {result['final_decision']}")

# Main execution
async def main():
    print("🛡️ Agent Safety Guardrails Demo")
    print("Demonstrating comprehensive 3-tier safety validation\n")
    
    # Run safety demos
    await demo_safe_request()
    await demo_blocked_input() 
    await demo_blocked_tool()
    await demo_blocked_output()
    
    print("\n" + "="*60)
    print("✅ SAFETY DEMO COMPLETED")
    print("="*60)
    print("Key Safety Principles:")
    print("• Defense in Depth: Multiple validation layers")
    print("• Risk-Based Decisions: Appropriate controls for risk level")
    print("• Human Oversight: Critical for medium/high risk operations")
    print("• Comprehensive Logging: Full audit trail for compliance")
    print("• Fail-Safe Design: Block when uncertain, escalate when needed")

if __name__ == "__main__":
    asyncio.run(main())
