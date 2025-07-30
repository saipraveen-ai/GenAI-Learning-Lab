# Resources for OpenAI Agent Building Guide

This directory contains auxiliary files, scripts, and source materials used in the development of the OpenAI Agent Building Guide concept.

## Directory Structure

```
resources/
├── README.md              # This file
├── extraction/            # PDF content extraction results
│   ├── openai-agent-guide.pdf
│   ├── openai_agent_guide_content_full.txt
│   └── openai_agent_guide_content_structured.json
└── scripts/               # Utility scripts
    ├── extract_pdf.py
    └── generate_svgs.sh
```

## 📄 Extraction Files

### `openai-agent-guide.pdf`
- **Source**: OpenAI's official "A Practical Guide to Building Agents"
- **Pages**: 34 pages of comprehensive agent building guidance
- **Content**: Enterprise-focused best practices from customer deployments

### `openai_agent_guide_content_full.txt`
- **Purpose**: Complete text extraction from the PDF
- **Format**: Plain text with page separators
- **Usage**: Source material for concept documentation

### `openai_agent_guide_content_structured.json`
- **Purpose**: Structured extraction with page-by-page organization
- **Format**: JSON array with page objects
- **Usage**: Programmatic access to content by page

## 🛠️ Scripts

### `extract_pdf.py`
- **Purpose**: Extract text content from PDF files
- **Dependencies**: PyPDF2
- **Usage**: `python extract_pdf.py`
- **Output**: Generates both .txt and .json files

### `generate_svgs.sh`
- **Purpose**: Generate SVG files from Mermaid diagrams
- **Dependencies**: mermaid-cli (mmdc)
- **Usage**: `./generate_svgs.sh` (from diagrams directory)
- **Output**: Creates .svg files for each .mmd diagram

## 🔄 Workflow

The typical workflow for using these resources:

1. **Content Extraction**: Use `extract_pdf.py` to process source PDFs
2. **Documentation Creation**: Reference extracted content for concept development
3. **Diagram Generation**: Use `generate_svgs.sh` to create SVG visualizations
4. **Integration**: Reference SVGs in documentation (not Mermaid code)

## 📋 Dependencies

### Python Dependencies (extract_pdf.py)
```bash
pip install PyPDF2 python-dotenv
```

### System Dependencies (generate_svgs.sh)
```bash
# Install mermaid-cli
npm install -g @mermaid-js/mermaid-cli

# Or using Homebrew
brew install mermaid-cli
```

## 🔒 File Management

### What's Tracked in Git
- ✅ Scripts (extract_pdf.py, generate_svgs.sh)
- ✅ Generated content (.txt, .json files)
- ✅ Generated SVGs (.svg files)
- ✅ Source PDFs (when appropriate for documentation)

### Best Practices
- Keep extraction results for reproducibility
- Version control both source (.mmd) and generated (.svg) files
- Document any manual modifications to extracted content
- Use scripts for consistent generation across environments

## 🚀 Usage Examples

### Extract Content from New PDF
```bash
cd resources/scripts
python extract_pdf.py /path/to/new-document.pdf
```

### Generate All Diagram SVGs
```bash
cd ../../diagrams
../resources/scripts/generate_svgs.sh
```

### Verify Content Structure
```bash
# Check extracted content
head -n 20 resources/extraction/openai_agent_guide_content_full.txt

# Check JSON structure
jq '.[:3]' resources/extraction/openai_agent_guide_content_structured.json
```

---

*This resources directory supports the [OpenAI Agent Building Guide](../README.md) concept development and maintenance.*
