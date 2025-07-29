# Visual Diagrams

This folder contains externalized Mermaid diagrams for the Agentic AI vs AI Agents concept.

## Diagram Files

### Mermaid Source Files
1. **[intelligence-spectrum.mmd](intelligence-spectrum.mmd)** - Shows the progression from Rule-Based Systems → AI Agents → Agentic AI
2. **[agentic-ai-architecture.mmd](agentic-ai-architecture.mmd)** - Detailed architecture of an Agentic AI thermostat system
3. **[agentic-cycle-flow.mmd](agentic-cycle-flow.mmd)** - The five-step agentic cycle: Perceive → Reflect → Plan → Execute → Learn

### SVG Rendered Files
1. **[intelligence-spectrum.svg](intelligence-spectrum.svg)** - Intelligence spectrum visualization (ready to display)
2. **[agentic-ai-architecture.svg](agentic-ai-architecture.svg)** - Agentic AI architecture (ready to display)
3. **[agentic-cycle-flow.svg](agentic-cycle-flow.svg)** - Agentic cycle flow (ready to display)

## How to View

### SVG Files (Recommended)
- **Direct Viewing**: Open `.svg` files directly in any web browser
- **Documentation**: Embed SVG files directly in markdown for universal compatibility
- **Print Ready**: SVG files are vector-based and scale perfectly for presentations
- **No Dependencies**: Work everywhere without requiring Mermaid extensions

### Mermaid Source Files (.mmd)
- **VS Code**: Install "Mermaid Preview" extension and open `.mmd` files
- **Online Editor**: Copy Mermaid code and paste into [Mermaid Live Editor](https://mermaid.live)
- **Editing**: Modify `.mmd` files and regenerate SVGs using `mmdc -i file.mmd -o file.svg`

## Diagram Types

All diagrams use Mermaid flowchart syntax with:
- Color-coded components for visual clarity
- Emoji icons for better identification
- Professional styling for documentation quality
- Interactive elements when rendered properly

## File Formats

- **`.mmd`**: Source Mermaid files for editing and version control
- **`.svg`**: Rendered vector graphics for universal display and embedding
- **Workflow**: Edit `.mmd` → Generate `.svg` → Embed in documentation

## Regenerating SVGs

To update SVG files after editing Mermaid source:
```bash
# Install Mermaid CLI (if not already installed)
npm install -g @mermaid-js/mermaid-cli

# Convert individual files
mmdc -i intelligence-spectrum.mmd -o intelligence-spectrum.svg
mmdc -i agentic-ai-architecture.mmd -o agentic-ai-architecture.svg
mmdc -i agentic-cycle-flow.mmd -o agentic-cycle-flow.svg

# Or convert all at once
for file in *.mmd; do mmdc -i "$file" -o "${file%.mmd}.svg"; done
```
