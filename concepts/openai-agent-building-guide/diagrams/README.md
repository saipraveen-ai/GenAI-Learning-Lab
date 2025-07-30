# OpenAI Agent Building Guide - Diagrams

This directory contains visual representations of key concepts from the OpenAI Agent Building Guide, implemented as Mermaid diagrams with generated SVG files.

## 📋 Available Diagrams

### 🏗️ Core Architecture
- **[agent-architecture.mmd](agent-architecture.mmd)** / **[SVG](agent-architecture.svg)**  
  *Complete agent architecture showing components, safety layers, and orchestration patterns*

### 🤝 Orchestration Patterns  
- **[orchestration-patterns.mmd](orchestration-patterns.mmd)** / **[SVG](orchestration-patterns.svg)**  
  *Manager Pattern vs Handoff Pattern for multi-agent coordination*

### 🛡️ Safety & Security
- **[safety-guardrails.mmd](safety-guardrails.mmd)** / **[SVG](safety-guardrails.svg)**  
  *Comprehensive 3-tier safety validation and risk management system*

### 🎯 Decision Framework
- **[workflow-decision-tree.mmd](workflow-decision-tree.mmd)** / **[SVG](workflow-decision-tree.svg)**  
  *When to build agents vs traditional automation - complete decision tree*

## 🎨 Usage in Documentation

All diagrams are referenced as SVG files in the documentation:

```markdown
![Agent Architecture](diagrams/agent-architecture.svg)
![Orchestration Patterns](diagrams/orchestration-patterns.svg)
![Safety Guardrails](diagrams/safety-guardrails.svg)
![Decision Tree](diagrams/workflow-decision-tree.svg)
```

## 🔧 Regenerating SVGs

To regenerate all SVG files from Mermaid sources:

```bash
cd diagrams/
mmdc -i agent-architecture.mmd -o agent-architecture.svg
mmdc -i orchestration-patterns.mmd -o orchestration-patterns.svg  
mmdc -i safety-guardrails.mmd -o safety-guardrails.svg
mmdc -i workflow-decision-tree.mmd -o workflow-decision-tree.svg
```

## 📐 Diagram Design Principles

### Visual Hierarchy
- **🔵 Blue**: User interaction points
- **🟢 Green**: Safe operations and validation
- **🟡 Orange**: Tool operations and medium risk
- **🔴 Red**: Blocked operations and high risk
- **🟣 Purple**: Core agent logic and coordination
- **⚫ Gray**: External systems and infrastructure

### Flow Patterns
- **Solid arrows**: Primary workflow paths
- **Dotted arrows**: Monitoring and feedback loops
- **Labeled edges**: Decision criteria and conditions
- **Subgraphs**: Logical component groupings

### Content Strategy
- **Emojis**: Instant visual recognition
- **Multi-line labels**: Detailed context without clutter
- **Decision diamonds**: Clear branching logic
- **Color coding**: Consistent risk and component classification

---

*Generated from the OpenAI Agent Building Guide concept. Each diagram supports both educational understanding and practical implementation reference.*
