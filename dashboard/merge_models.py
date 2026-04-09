import os
import re

base_dir = r"c:\Users\salad507\Downloads\TALLER 2 ALLISON Y DANNA\ml-dashboard-copy"
index_file = os.path.join(base_dir, "index.html")

# Read index.html
with open(index_file, "r", encoding="utf-8") as f:
    index_content = f.read()

# Define models to merge
models = [
    {"file": "modelo-xg.html", "id": "section-xg", "href_target": "modelo-xg.html"},
    {"file": "match-predictor.html", "id": "section-match", "href_target": "match-predictor.html"},
    {"file": "clustering.html", "id": "section-clustering", "href_target": "clustering.html"},
    {"file": "random-forest.html", "id": "section-rf", "href_target": "random-forest.html"}
]

merged_html = ""

for model in models:
    file_path = os.path.join(base_dir, model["file"])
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Extract everything inside <main class="content-detail"> ... </main>
    match = re.search(r'<main class="content-detail">(.*?)</main>', content, re.DOTALL)
    if match:
        main_content = match.group(1)
        # Wrap it in a section with the ID
        merged_html += f'\n<!-- INICIO DE {model["file"]} -->\n<section id="{model["id"]}" class="merged-model-section" style="padding-top: 80px;">\n{main_content}\n</section>\n<!-- FIN DE {model["file"]} -->\n'
        
        # Update nav links in index.html
        # E.g. href="modelo-xg.html" target="_blank" -> href="#section-xg"
        # We need to handle variations though. 
        index_content = index_content.replace(f'href="{model["href_target"]}" target="_blank"', f'href="#{model["id"]}"')
        index_content = index_content.replace(f'href="{model["href_target"]}"', f'href="#{model["id"]}"')
        

# Find where to inject in index_content. We will inject right before the JS includes at the bottom.
# E.g., right before <!-- JS -->
insertion_point = "    <!-- JS -->"
if insertion_point in index_content:
    index_content = index_content.replace(insertion_point, merged_html + "\n" + insertion_point)
else:
    # fallback, right before </body>
    index_content = index_content.replace("</body>", merged_html + "\n</body>")

with open(index_file, "w", encoding="utf-8") as f:
    f.write(index_content)

print("Merged all models into index.html successfully.")
