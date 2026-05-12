import os
import json

def bundle():
    manual_dir = r"C:\Users\proje\source\repos\Teste\manual"
    output_file = os.path.join(manual_dir, "manual_viewer", "manual_content.js")
    
    manual_data = {}
    
    for root, dirs, files in os.walk(manual_dir):
        if "manual_viewer" in root:
            continue
            
        for file in files:
            if file.endswith(".md"):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, manual_dir).replace("\\", "/")
                
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    manual_data[rel_path] = content
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"const manualData = {json.dumps(manual_data, ensure_ascii=False)};")
    
    print(f"Bundle created successfully with {len(manual_data)} files.")

if __name__ == "__main__":
    bundle()
