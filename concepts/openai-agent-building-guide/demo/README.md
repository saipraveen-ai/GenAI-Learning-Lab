# Demo Scripts for OpenAI Agent Building Guide

This directory contains working demonstrations of the concepts covered in the OpenAI Agent Building Guide.

## Available Demonstrations

### 1. Basic Agent Demo (`basic_agent_demo.py`)
- Single-agent weather system
- Demonstrates core components: Model, Tools, Instructions
- Shows dynamic tool selection and workflow execution

### 2. Orchestration Demo (`orchestration_demo.py`)
- Multi-agent translation service
- Manager pattern implementation
- Specialized agent coordination

### 3. Guardrails Demo (`guardrails_demo.py`)
- Comprehensive safety mechanisms
- Input validation and filtering
- Tool-level safety checks
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
