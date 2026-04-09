import re

index_file = r"c:\Users\salad507\Downloads\TALLER 2 ALLISON Y DANNA\ml-dashboard-copy\index.html"

with open(index_file, "r", encoding="utf-8") as f:
    content = f.read()

# We want to change the style of the injected sections to act like modals.
# They are currently: <section id="..." class="merged-model-section" style="padding-top: 80px;">
# We will replace them with:
# <div id="..." class="model-modal hidden">
#   <div class="modal-content">
#       <button class="close-modal">&times;</button>
#       <div class="modal-body"> ... </div>
#   </div>
# </div>

# Actually, an easier way is to just add a global CSS style for .merged-model-section and a close button inside each.
# Let's find each section start and inject a Close button.

def replace_section(m):
    id_name = m.group(1)
    return f'<section id="{id_name}" class="merged-model-section modal-overlay hidden">\n    <button class="close-modal-btn" onclick="closeModal(\'{id_name}\')"><i class="fa-solid fa-xmark"></i> CERRAR</button>\n    <div class="modal-scroll-content">'

content = re.sub(r'<section id="(section-[^"]+)" class="merged-model-section" style="padding-top: 80px;">', replace_section, content)
content = re.sub(r'(</section>\n<!-- FIN DE [^>]+ -->)', r'    </div>\n\1', content)

# Add CSS for modal
css = """
<style>
.modal-overlay {
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0,0,0,0.95);
    z-index: 9999;
    display: flex;
    flex-direction: column;
    overflow-y: auto;
    opacity: 1;
    transition: opacity 0.3s ease;
}
.modal-overlay.hidden {
    display: none;
    opacity: 0;
}
.close-modal-btn {
    position: fixed;
    top: 20px;
    right: 30px;
    background: rgba(255, 255, 255, 0.1);
    border: 1px solid rgba(255, 255, 255, 0.2);
    color: white;
    padding: 10px 20px;
    font-size: 1rem;
    border-radius: 30px;
    cursor: pointer;
    z-index: 10000;
    backdrop-filter: blur(10px);
    transition: 0.3s;
    font-family: 'Outfit', sans-serif;
    font-weight: bold;
}
.close-modal-btn:hover {
    background: #f43f5e;
    transform: scale(1.05);
}
.modal-scroll-content {
    width: 100%;
    margin: 0 auto;
    padding-bottom: 50px;
}
/* Prevent body scrolling when modal is open */
body.modal-open {
    overflow: hidden;
}
</style>
"""

if "<style>" not in content or "modal-overlay" not in content:
    content = content.replace("</head>", css + "\n</head>")

# Add JS logic to open/close
js_logic = """
<script>
    function openModal(id) {
        const modal = document.getElementById(id);
        if(modal) {
            modal.classList.remove('hidden');
            document.body.classList.add('modal-open');
        }
    }
    function closeModal(id) {
        const modal = document.getElementById(id);
        if(modal) {
            modal.classList.add('hidden');
            document.body.classList.remove('modal-open');
        }
    }
    
    document.addEventListener('DOMContentLoaded', () => {
        // Intercept nav links
        const links = document.querySelectorAll('a[href^="#section-"]');
        links.forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                const targetId = link.getAttribute('href').substring(1);
                openModal(targetId);
            });
        });
    });
</script>
"""

if "function openModal" not in content:
    content = content.replace("</body>", js_logic + "\n</body>")

with open(index_file, "w", encoding="utf-8") as f:
    f.write(content)

print("Modals converted!")
