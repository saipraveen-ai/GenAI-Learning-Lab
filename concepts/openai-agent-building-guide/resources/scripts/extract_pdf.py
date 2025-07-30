#!/usr/bin/env python3
"""
Extract text content from OpenAI Agent Building Guide PDF
"""

import PyPDF2
import json

def extract_pdf_content(pdf_path, output_path):
    """Extract text from PDF and save to file"""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            total_pages = len(reader.pages)
            print(f'Total pages: {total_pages}')
            
            full_text = ""
            sections = []
            
            for page_num in range(total_pages):
                page = reader.pages[page_num]
                page_text = page.extract_text()
                
                sections.append({
                    "page": page_num + 1,
                    "content": page_text
                })
                
                full_text += f"\n=== PAGE {page_num + 1} ===\n"
                full_text += page_text
                full_text += "\n"
                
                print(f"Extracted page {page_num + 1}/{total_pages}")
            
            # Save full text
            with open(f"{output_path}_full.txt", 'w', encoding='utf-8') as f:
                f.write(full_text)
            
            # Save structured JSON
            with open(f"{output_path}_structured.json", 'w', encoding='utf-8') as f:
                json.dump(sections, f, indent=2, ensure_ascii=False)
            
            print(f"Content extracted and saved to {output_path}_full.txt and {output_path}_structured.json")
            return full_text
            
    except Exception as e:
        print(f'Error: {e}')
        return None

if __name__ == "__main__":
    content = extract_pdf_content("openai-agent-guide.pdf", "openai_agent_guide_content")
    if content:
        print("\n" + "="*50)
        print("EXTRACTION COMPLETE")
        print("="*50)
        # Print first 2000 characters as preview
        print("\nPREVIEW (first 2000 characters):")
        print("-" * 40)
        print(content[:2000] + "..." if len(content) > 2000 else content)
