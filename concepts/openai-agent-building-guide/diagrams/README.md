# Diagrams for OpenAI Agent Building Guide

This directory contains architectural diagrams and visualizations for the OpenAI Agent Building Guide concepts.

## Available Diagrams

### 1. Agent Architecture (`agent-architecture.mmd`)
- Core components: Model, Tools, Instructions
- Component interactions and relationships
- Data flow visualization

### 2. Orchestration Patterns (`orchestration-patterns.mmd`)
- Single-agent vs multi-agent systems
- Manager pattern architecture
- Decentralized handoff pattern

### 3. Guardrails Framework (`guardrails-framework.mmd`)
- Safety layers and protection mechanisms
- Input validation flow
- Risk assessment workflow

### 4. Production Deployment (`production-architecture.mmd`)
- Enterprise deployment architecture
- Monitoring and observability
- Scaling and redundancy patterns

## Viewing Diagrams

### VS Code with Mermaid Extension
1. Install "Mermaid Preview" extension
2. Open `.mmd` files and use preview mode
3. Live editing with real-time preview

### Online Mermaid Editor
1. Copy diagram code from `.mmd` files
2. Paste into [Mermaid Live Editor](https://mermaid.live/)
3. View and export diagrams

### Command Line
```bash
# Install mermaid-cli
npm install -g @mermaid-js/mermaid-cli

# Generate SVG from mermaid
mmdc -i diagram.mmd -o diagram.svg
```

## Diagram Standards

All diagrams follow these conventions:
- **Blue**: Core agent components
- **Green**: Safe/approved paths
- **Red**: Blocked/dangerous paths  
- **Yellow**: Warning/attention areas
- **Gray**: External systems/infrastructure

## Contributing

When adding new diagrams:
1. Use descriptive filenames
2. Include YAML frontmatter for metadata
3. Follow the color conventions
4. Add description to this README
5. Test rendering in multiple viewers
