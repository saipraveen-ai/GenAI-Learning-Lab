#!/bin/bash
# SVG Generation Script for OpenAI Agent Building Guide Diagrams
# Usage: Run from project root or diagrams directory
#   From project root: ./resources/scripts/generate_svgs.sh
#   From diagrams: ../../resources/scripts/generate_svgs.sh

set -e  # Exit on any error

echo "🎨 Generating SVG files from Mermaid diagrams..."
echo "=================================================="

# Function to generate SVG from Mermaid file
generate_svg() {
    local mmd_file="$1"
    local svg_file="${mmd_file%.mmd}.svg"
    
    if [[ -f "$mmd_file" ]]; then
        echo "📐 Generating: $mmd_file → $svg_file"
        mmdc -i "$mmd_file" -o "$svg_file"
        
        if [[ -f "$svg_file" ]]; then
            local size=$(du -h "$svg_file" | cut -f1)
            echo "✅ Success: $svg_file ($size)"
        else
            echo "❌ Failed: $svg_file"
            return 1
        fi
    else
        echo "⚠️  Not found: $mmd_file"
    fi
    echo ""
}

# Check if mermaid-cli is installed
if ! command -v mmdc &> /dev/null; then
    echo "❌ Error: mermaid-cli not found!"
    echo ""
    echo "Install with: npm install -g @mermaid-js/mermaid-cli"
    echo "Or using Homebrew: brew install mermaid-cli"
    exit 1
fi

# Find the diagrams directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
PROJECT_ROOT="$(dirname "$(dirname "$SCRIPT_DIR")")"
DIAGRAMS_DIR="$PROJECT_ROOT/diagrams"

if [[ ! -d "$DIAGRAMS_DIR" ]]; then
    echo "❌ Error: Cannot find diagrams directory at $DIAGRAMS_DIR"
    exit 1
fi

cd "$DIAGRAMS_DIR"
echo "📁 Working directory: $(pwd)"
echo ""

# Generate SVGs for all defined diagrams
generate_svg "agent-architecture.mmd"
generate_svg "orchestration-patterns.mmd" 
generate_svg "safety-guardrails.mmd"
generate_svg "workflow-decision-tree.mmd"

# List all generated SVGs
echo "📊 Generated SVG files:"
echo "======================"
if ls *.svg 1> /dev/null 2>&1; then
    for svg in *.svg; do
        local size=$(du -h "$svg" | cut -f1)
        echo "  📄 $svg ($size)"
    done
else
    echo "  (No SVG files found)"
fi

echo ""
echo "🎯 Next steps:"
echo "  1. Commit both .mmd and .svg files to git"
echo "  2. Reference SVGs in documentation instead of embedding Mermaid code"
echo "  3. Test SVG rendering in your target platforms"
echo ""
echo "✨ SVG generation complete!"
