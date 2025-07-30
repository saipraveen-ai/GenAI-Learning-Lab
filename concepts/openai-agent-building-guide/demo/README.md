# OpenAI Agent Building Guide - Demonstrations

This directory contains practical demonstrations of agent concepts, patterns, and safety mechanisms from the OpenAI Agent Building Guide.

## 🎯 Available Demonstrations

### 🤖 Core Agent Concepts
- **[basic_agent_demo.py](basic_agent_demo.py)**  
  *Basic agent implementation with tool integration and decision making*

### 🤝 Multi-Agent Orchestration
- **[orchestration_demo.py](orchestration_demo.py)**  
  *Manager Pattern vs Handoff Pattern comparison with working examples*

### 🛡️ Safety & Guardrails
- **[safety_guardrails_demo.py](safety_guardrails_demo.py)**  
  *Comprehensive 3-tier safety validation system demonstration*

### 🎯 Decision Framework
- **[workflow_decision_demo.py](workflow_decision_demo.py)**  
  *Interactive decision tree: When to build agents vs traditional automation*

### 🎮 Demo Runner
- **[run_all_demos.py](run_all_demos.py)**  
  *Execute all demonstrations in sequence with optional interactive mode*

## 🚀 Quick Start

### Run Individual Demos

```bash
# Basic agent concepts
python demo/basic_agent_demo.py

# Multi-agent orchestration patterns
python demo/orchestration_demo.py

# Safety guardrails system
python demo/safety_guardrails_demo.py

# Workflow decision framework (interactive)
python demo/workflow_decision_demo.py
```

### Run All Demos

```bash
# Run all demonstrations
python demo/run_all_demos.py

# Run with interactive prompts
python demo/run_all_demos.py --interactive
```
- Human intervention triggers

### 4. Advanced Orchestration (`advanced_orchestration_demo.py`)
- Decentralized agent handoff pattern
- Content creation workflow
- Research → Writing → Review pipeline

## Setup Instructions

1. **Install Dependencies**
   ```bash
   cd concepts/openai-agent-building-guide
   pip install -r requirements.txt
   ```

2. **Configure Environment**
   ```bash
   # Create .env file with your OpenAI API key
   echo "OPENAI_API_KEY=your-api-key-here" > .env
   ```

3. **Run Demonstrations**
   ```bash
   # Run individual demos
   python demo/basic_agent_demo.py
   python demo/orchestration_demo.py
   python demo/guardrails_demo.py
   python demo/advanced_orchestration_demo.py
   
   # Or run all demos
   python demo/run_all_demos.py
   ```

## Expected Outputs

Each demo script includes expected output examples in the documentation. The actual outputs may vary based on:
- OpenAI API model versions
- Real-time data (for weather examples)
- Random variations in LLM responses

## Key Learning Objectives

- **Understanding agent architecture**: See how Model + Tools + Instructions work together
- **Orchestration patterns**: Compare single-agent vs. multi-agent approaches
- **Safety implementation**: Observe guardrails protecting against various threats
- **Real-world applications**: Connect concepts to enterprise use cases

## Troubleshooting

### Common Issues

1. **API Key Errors**
   - Ensure OPENAI_API_KEY is set in environment or .env file
   - Verify API key has sufficient credits

2. **Import Errors**
   - Check that all dependencies are installed: `pip install -r requirements.txt`
   - Ensure you're using Python 3.8+

3. **Agent SDK Issues**
   - The agents-sdk is evolving rapidly; check for latest version
   - Some examples may need adjustment for SDK updates

### Getting Help

- Review the main documentation: [README.md](../README.md)
- Check the foundations: [FOUNDATIONS.md](../FOUNDATIONS.md)
- Examine working examples: [DEMONSTRATIONS.md](../DEMONSTRATIONS.md)
- Enterprise considerations: [APPLICATIONS.md](../APPLICATIONS.md)

## Contributing

To add new demonstrations:
1. Follow the existing naming pattern
2. Include comprehensive docstrings and comments
3. Provide expected output examples
4. Update this README with demo description
5. Test thoroughly before submitting
