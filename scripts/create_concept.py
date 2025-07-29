#!/usr/bin/env python3
"""
New Concept Creator Script

This script creates a new concept folder with optimized structure:
- Single README.md with complete documentation
- No redundant files (insights.md, resources/ folder)
- Follows the "minimal, complete documentation" principle
"""

import os
import sys
from datetime import datetime
import argparse

def create_concept_folder(concept_name, source_url=None):
    """Create a new concept folder with optimized template structure."""
    
    # Sanitize concept name for folder
    folder_name = concept_name.lower().replace(" ", "-").replace("_", "-")
    concept_path = f"concepts/{folder_name}"
    
    # Create main concept directory only
    os.makedirs(concept_path, exist_ok=True)
    
    # Read template
    with open("templates/concept-template.md", "r") as f:
        template_content = f.read()
    
    # Replace placeholders
    content = template_content.replace("[Concept Name]", concept_name)
    content = content.replace("[URL]", source_url or "TBD")
    content = content.replace("[Date]", datetime.now().strftime("%Y-%m-%d"))
    
    # Create README.md (single source of truth)
    with open(f"{concept_path}/README.md", "w") as f:
        f.write(content)
    
    print(f"✅ Created concept folder: {concept_path}")
    print(f"📁 Optimized Structure:")
    print(f"   └── README.md  # Complete concept documentation")
    print(f"\n💡 Next Steps:")
    print(f"   • Add demo/ folder if practical implementation needed")
    print(f"   • All insights go directly in README.md")
    print(f"   • No separate resources - use Sources section in README")
    
    return concept_path

def main():
    parser = argparse.ArgumentParser(description="Create a new AI concept exploration folder")
    parser.add_argument("concept_name", help="Name of the AI concept to explore")
    parser.add_argument("--url", help="Source URL for the concept")
    
    args = parser.parse_args()
    
    # Change to project root if needed
    if not os.path.exists("concepts"):
        print("❌ Please run this script from the GenAI-Learning-Lab root directory")
        sys.exit(1)
    
    concept_path = create_concept_folder(args.concept_name, args.url)
    
    print(f"\n🚀 Ready to start exploring '{args.concept_name}'!")
    print(f"📝 Edit {concept_path}/README.md to begin documentation")
    print(f"🎯 Remember: All content goes in README.md - no separate files needed")

if __name__ == "__main__":
    main()
