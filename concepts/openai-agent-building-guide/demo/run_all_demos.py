#!/usr/bin/env python3
"""
Run All Demonstrations Script
Executes all OpenAI Agent Building Guide demonstrations in sequence
"""

import sys
import subprocess
import os
from pathlib import Path

def run_demo(demo_name: str, demo_file: str):
    """Run a single demonstration script."""
    print(f"\n{'='*80}")
    print(f"RUNNING: {demo_name}")
    print(f"{'='*80}")
    
    try:
        # Get the directory of this script
        demo_dir = Path(__file__).parent
        demo_path = demo_dir / demo_file
        
        if demo_path.exists():
            result = subprocess.run([sys.executable, str(demo_path)], 
                                  capture_output=True, text=True, cwd=demo_dir)
            
            if result.returncode == 0:
                print(result.stdout)
                if result.stderr:
                    print("Warnings:", result.stderr)
                print(f"✅ {demo_name} completed successfully!")
            else:
                print(f"❌ {demo_name} failed with return code {result.returncode}")
                print("STDOUT:", result.stdout)
                print("STDERR:", result.stderr)
        else:
            print(f"⚠️ Demo file not found: {demo_file}")
            print("This demo may not be implemented yet.")
            
    except Exception as e:
        print(f"❌ Error running {demo_name}: {str(e)}")

def main():
    """Run all demonstrations in sequence."""
    
    print("OpenAI Agent Building Guide - Complete Demonstration Suite")
    print("="*80)
    print()
    print("This script runs all available demonstrations to showcase:")
    print("• Basic agent implementation (Model + Tools + Instructions)")
    print("• Multi-agent orchestration patterns") 
    print("• Guardrails and safety mechanisms")
    print("• Advanced workflow automation")
    print()
    
    # Check if we're in the right directory
    current_dir = Path.cwd()
    if not (current_dir.name == "demo" or "demo" in str(current_dir)):
        print("⚠️ Please run this script from the demo directory:")
        print("cd concepts/openai-agent-building-guide/demo")
        print("python run_all_demos.py")
        return
    
    # Define demonstrations to run
    demonstrations = [
        ("Basic Agent Implementation", "basic_agent_demo.py"),
        ("Multi-Agent Orchestration", "orchestration_demo.py"),
        ("Guardrails and Safety", "guardrails_demo.py"),
        ("Advanced Workflows", "advanced_orchestration_demo.py")
    ]
    
    # Run each demonstration
    for demo_name, demo_file in demonstrations:
        run_demo(demo_name, demo_file)
        
        # Pause between demos for readability
        input(f"\nPress Enter to continue to next demo...")
    
    # Summary
    print(f"\n{'='*80}")
    print("DEMONSTRATION SUITE COMPLETE")
    print(f"{'='*80}")
    print()
    print("🎯 What you've seen:")
    print("• Single-agent systems with dynamic tool selection")
    print("• Manager pattern for coordinating specialized agents")  
    print("• Comprehensive guardrail implementation")
    print("• Decentralized agent handoff workflows")
    print()
    print("📚 Next Steps:")
    print("• Review the documentation: ../README.md")
    print("• Study the foundations: ../FOUNDATIONS.md") 
    print("• Explore enterprise applications: ../APPLICATIONS.md")
    print("• Build your own agent using these patterns!")
    print()
    print("🚀 Ready to implement agents in your organization?")
    print("• Start with simple, well-defined use cases")
    print("• Implement comprehensive guardrails from day one")
    print("• Monitor performance and iterate based on real usage")
    print("• Scale gradually from single-agent to multi-agent systems")

if __name__ == "__main__":
    main()
