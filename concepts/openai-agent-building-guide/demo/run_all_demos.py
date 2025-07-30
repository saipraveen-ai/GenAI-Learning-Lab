#!/usr/bin/env python3
"""
Run All Demonstrations Script
============================

Executes all OpenAI Agent Building Guide demonstrations in sequence.
Provides both automated and interactive modes for comprehensive learning.

Requirements:
- Run from virtual environment: source venv/bin/activate
- All demo files must be in the same directory
"""

import sys
import subprocess
import os
import argparse
from pathlib import Path
from typing import List, Tuple

def run_demo(demo_name: str, demo_file: str, interactive: bool = False) -> bool:
    """Run a single demonstration script."""
    print(f"\n{'='*80}")
    print(f"🎯 RUNNING: {demo_name}")
    print(f"{'='*80}")
    
    if interactive:
        proceed = input(f"\nPress Enter to run {demo_name} (or 's' to skip): ").strip().lower()
        if proceed == 's':
            print(f"⏭️ Skipped: {demo_name}")
            return True
    
    try:
        # Get the directory of this script
        demo_dir = Path(__file__).parent
        demo_path = demo_dir / demo_file
        
        if demo_path.exists():
            print(f"📂 Executing: {demo_file}")
            
            result = subprocess.run([sys.executable, str(demo_path)], 
                                  capture_output=True, text=True, cwd=demo_dir)
            
            if result.returncode == 0:
                print(result.stdout)
                if result.stderr:
                    print("⚠️ Warnings:", result.stderr)
                print(f"✅ {demo_name} completed successfully!")
                
                if interactive:
                    input("\nPress Enter to continue to next demo...")
                
                return True
            else:
                print(f"❌ {demo_name} failed with return code {result.returncode}")
                print("📤 STDOUT:", result.stdout)
                print("📤 STDERR:", result.stderr)
                return False
        else:
            print(f"⚠️ Demo file not found: {demo_file}")
            print("   This demo may not be implemented yet.")
            return False
            
    except Exception as e:
        print(f"❌ Error running {demo_name}: {str(e)}")
        return False

def get_demo_list() -> List[Tuple[str, str, str]]:
    """Get list of available demonstrations."""
    return [
        (
            "Basic Agent Implementation",
            "basic_agent_demo.py",
            "Core agent concepts: Model + Tools + Instructions with decision making"
        ),
        (
            "Multi-Agent Orchestration Patterns",
            "orchestration_demo.py", 
            "Manager Pattern vs Handoff Pattern comparison with specialized agents"
        ),
        (
            "Safety Guardrails System", 
            "safety_guardrails_demo.py",
            "3-tier safety validation: Input → Tool → Output with comprehensive monitoring"
        ),
        (
            "Workflow Decision Framework",
            "workflow_decision_demo.py",
            "Interactive decision tree: When to build agents vs traditional automation"
        )
    ]

def check_environment():
    """Check if the environment is properly set up."""
    print("🔍 ENVIRONMENT CHECK")
    print("="*50)
    
    # Check Python version
    python_version = sys.version_info
    print(f"🐍 Python Version: {python_version.major}.{python_version.minor}.{python_version.micro}")
    
    if python_version < (3, 7):
        print("⚠️ Warning: Python 3.7+ recommended for async/await support")
    
    # Check for virtual environment
    venv_active = hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)
    if venv_active:
        print("✅ Virtual environment: Active")
    else:
        print("⚠️ Virtual environment: Not detected (recommended to activate)")
    
    # Check current directory
    current_dir = Path.cwd()
    demo_dir = Path(__file__).parent
    print(f"📂 Current directory: {current_dir}")
    print(f"📂 Demo directory: {demo_dir}")
    
    # Check for demo files
    demos = get_demo_list()
    missing_demos = []
    
    for demo_name, demo_file, _ in demos:
        demo_path = demo_dir / demo_file
        if demo_path.exists():
            print(f"✅ Found: {demo_file}")
        else:
            print(f"❌ Missing: {demo_file}")
            missing_demos.append(demo_file)
    
    if missing_demos:
        print(f"\n⚠️ Warning: {len(missing_demos)} demo files are missing")
        print("   Some demonstrations may be skipped")
    
    print()

def print_demo_overview():
    """Print overview of all available demonstrations."""
    print("📋 DEMONSTRATION OVERVIEW")
    print("="*50)
    
    demos = get_demo_list()
    
    for i, (demo_name, demo_file, description) in enumerate(demos, 1):
        print(f"\n{i}. {demo_name}")
        print(f"   📄 File: {demo_file}")
        print(f"   📝 Description: {description}")
    
    print(f"\n📊 Total Demonstrations: {len(demos)}")
    print()

def run_specific_demo():
    """Allow user to run a specific demo."""
    demos = get_demo_list()
    
    print("🎯 SELECT SPECIFIC DEMO")
    print("="*50)
    
    for i, (demo_name, demo_file, description) in enumerate(demos, 1):
        print(f"{i}. {demo_name}")
    
    print(f"{len(demos) + 1}. Run All Demos")
    print("0. Exit")
    
    while True:
        try:
            choice = int(input(f"\nEnter choice (0-{len(demos) + 1}): "))
            
            if choice == 0:
                print("👋 Goodbye!")
                return
            elif choice == len(demos) + 1:
                run_all_demos(interactive=True)
                return
            elif 1 <= choice <= len(demos):
                demo_name, demo_file, _ = demos[choice - 1]
                success = run_demo(demo_name, demo_file, interactive=True)
                if success:
                    print(f"\n🎉 {demo_name} completed successfully!")
                else:
                    print(f"\n💥 {demo_name} encountered issues")
                return
            else:
                print(f"Please enter a number between 0 and {len(demos) + 1}")
                
        except ValueError:
            print("Please enter a valid number")

def run_all_demos(interactive: bool = False):
    """Run all demonstrations in sequence."""
    demos = get_demo_list()
    
    print("🚀 RUNNING ALL DEMONSTRATIONS")
    print("="*50)
    
    if interactive:
        print("Interactive mode: You'll be prompted before each demo")
    else:
        print("Automated mode: All demos will run in sequence")
    
    print(f"Total demos to run: {len(demos)}\n")
    
    results = []
    
    for demo_name, demo_file, description in demos:
        print(f"\n📋 Next: {demo_name}")
        print(f"📝 {description}")
        
        success = run_demo(demo_name, demo_file, interactive)
        results.append((demo_name, success))
    
    # Summary
    print("\n" + "="*80)
    print("📊 DEMONSTRATION SUMMARY")
    print("="*80)
    
    successful = sum(1 for _, success in results if success)
    total = len(results)
    
    print(f"✅ Successful: {successful}/{total}")
    print(f"❌ Failed: {total - successful}/{total}")
    
    print("\nDetailed Results:")
    for demo_name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"   {status} - {demo_name}")
    
    if successful == total:
        print("\n🎉 All demonstrations completed successfully!")
        print("You now have hands-on experience with:")
        print("• Basic agent implementation patterns")
        print("• Multi-agent orchestration strategies") 
        print("• Comprehensive safety and guardrails")
        print("• Decision frameworks for automation")
    else:
        print(f"\n⚠️ {total - successful} demonstration(s) had issues")
        print("Check the output above for troubleshooting guidance")

def main():
    """Main entry point with argument parsing."""
    parser = argparse.ArgumentParser(
        description="Run OpenAI Agent Building Guide demonstrations",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run_all_demos.py                 # Run all demos automatically
  python run_all_demos.py --interactive   # Run with interactive prompts
  python run_all_demos.py --specific      # Choose specific demo to run
  python run_all_demos.py --overview      # Show demo overview only
        """
    )
    
    parser.add_argument('--interactive', '-i', action='store_true',
                       help='Run in interactive mode with prompts')
    parser.add_argument('--specific', '-s', action='store_true',
                       help='Select a specific demo to run')
    parser.add_argument('--overview', '-o', action='store_true',
                       help='Show demo overview and exit')
    parser.add_argument('--no-env-check', action='store_true',
                       help='Skip environment check')
    
    args = parser.parse_args()
    
    print("🤖 OpenAI Agent Building Guide - Complete Demonstration Suite")
    print("="*80)
    print()
    
    # Environment check
    if not args.no_env_check:
        check_environment()
    
    # Demo overview
    if args.overview:
        print_demo_overview()
        sys.exit(0)
    
    print_demo_overview()
    
    # Run specific demo
    if args.specific:
        run_specific_demo()
        sys.exit(0)
    
    # Run all demos
    run_all_demos(interactive=args.interactive)
    
    print("\n" + "="*80)
    print("🎓 LEARNING COMPLETE")
    print("="*80)
    print("Next steps:")
    print("• Review the documentation in README.md, FOUNDATIONS.md, etc.")
    print("• Examine the diagram visualizations in diagrams/")
    print("• Explore the resources/ directory for source materials")
    print("• Try modifying the demo code for your own use cases")
    print("• Check out the APPLICATIONS.md for enterprise implementation guidance")

if __name__ == "__main__":
    main()
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
