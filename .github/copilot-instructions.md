<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

This repository is a structured course on AI/ML/Gen AI/Agents. Please assist in generating content related to:
- Large Language Models (LLMs)
- Multi-Agent Systems
- Agentic Architecture
- Design Patterns
- Real-World Projects
- MCP Servers

Focus on practical applications, hands-on projects, and educational resources.

## 📚 Documentation Structure Pattern for Concepts

When creating or organizing concept documentation, follow this proven 4-file structure:

### **README.md** (Navigation Hub - ~150 lines)
- Overview and learning objectives
- Clear navigation to all focused documents
- Quick comparison tables
- Live demonstration instructions
- Project structure and learning path
- **Purpose**: Entry point and roadmap

### **FOUNDATIONS.md** (Core Concepts - ~200-300 lines)
- Key definitions and characteristics  
- Technical spectrum and classifications
- Critical distinctions and comparisons
- Visual architecture diagrams
- Theoretical frameworks and testing scenarios
- **Purpose**: Deep conceptual understanding

### **DEMONSTRATIONS.md** (Practical Examples - ~300-400 lines)
- Working code examples and experiments
- Complete execution outputs and results
- Questions & answers from real scenarios
- Validation frameworks and testing
- Live implementation demonstrations
- **Purpose**: Hands-on learning and validation

### **APPLICATIONS.md** (Real-World Context - ~200-300 lines)
- Industry applications and use cases
- Scenario handling demonstrations  
- Research insights and key takeaways
- Strategic implementation guidance
- Future directions and related concepts
- **Purpose**: Practical application and broader context

### **Supporting Structure**
```
concept-name/
├── README.md              # Navigation hub (~150 lines)
├── FOUNDATIONS.md         # Core concepts (~200-300 lines)
├── DEMONSTRATIONS.md      # Practical examples (~300-400 lines)  
├── APPLICATIONS.md        # Real-world context (~200-300 lines)
├── diagrams/             # Visual architecture diagrams (.svg files)
├── demo/                 # Working code examples
└── requirements.txt      # Dependencies (if applicable)
```

### **Content Organization Principles**
- **Preserve all content**: Never lose information during reorganization
- **Clear cross-references**: Each document links to related sections
- **Progressive learning**: README → FOUNDATIONS → DEMONSTRATIONS → APPLICATIONS
- **Self-contained sections**: Each file serves a specific learning purpose
- **Visual elements**: Include diagrams, tables, and code examples
- **Executable demos**: Provide working code that users can run

### **Example Cross-Reference Pattern**
```markdown
---
*Part of: [Concept Name](README.md)*  
*Previous: [FOUNDATIONS.md](FOUNDATIONS.md) | Next: [APPLICATIONS.md](APPLICATIONS.md)*
```

This structure transforms lengthy monolithic documentation into focused, navigable learning resources while preserving comprehensive coverage of complex topics.