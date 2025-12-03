#!/usr/bin/env python3
"""
Script de conversion Markdown vers PDF
Utilise markdown2 pour le parsing et génère un HTML puis PDF via Chrome/Chromium
"""

import subprocess
import sys
import os
from pathlib import Path
import tempfile
import shutil

def install_if_missing(package):
    """Installe un package pip si nécessaire"""
    try:
        __import__(package.replace('-', '_'))
    except ImportError:
        print(f"Installation de {package}...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package, '-q'])

# Installer markdown2
install_if_missing('markdown2')
import markdown2

# CSS pour un rendu professionnel
CSS_STYLE = """
@page {
    size: A4;
    margin: 2cm;
}

@media print {
    h1 { page-break-before: always; }
    h1:first-of-type { page-break-before: avoid; }
    pre, table, blockquote { page-break-inside: avoid; }
    h2, h3 { page-break-after: avoid; }
}

* {
    box-sizing: border-box;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.6;
    color: #24292e;
    max-width: 100%;
    padding: 20px;
    background: white;
}

h1 {
    color: #1a1a2e;
    font-size: 26pt;
    border-bottom: 3px solid #0366d6;
    padding-bottom: 12px;
    margin-top: 40px;
    margin-bottom: 20px;
}

h1:first-of-type {
    text-align: center;
    font-size: 30pt;
    margin-top: 60px;
    border-bottom: none;
}

h2 {
    color: #24292e;
    font-size: 18pt;
    border-bottom: 1px solid #e1e4e8;
    padding-bottom: 8px;
    margin-top: 30px;
    margin-bottom: 15px;
}

h3 {
    color: #0366d6;
    font-size: 14pt;
    margin-top: 25px;
    margin-bottom: 10px;
}

h4 {
    color: #586069;
    font-size: 12pt;
    margin-top: 20px;
}

p {
    margin: 12px 0;
    text-align: justify;
}

code {
    background-color: rgba(27, 31, 35, 0.05);
    padding: 3px 6px;
    border-radius: 4px;
    font-family: 'SF Mono', Monaco, 'Courier New', monospace;
    font-size: 10pt;
    color: #e01e5a;
}

pre {
    background-color: #1e1e1e;
    color: #d4d4d4;
    padding: 16px;
    border-radius: 8px;
    overflow-x: auto;
    font-size: 9.5pt;
    line-height: 1.5;
    margin: 16px 0;
    border: 1px solid #30363d;
}

pre code {
    background-color: transparent;
    color: inherit;
    padding: 0;
    font-size: inherit;
}

blockquote {
    border-left: 4px solid #0366d6;
    margin: 16px 0;
    padding: 12px 20px;
    background-color: #f6f8fa;
    border-radius: 0 6px 6px 0;
}

blockquote p {
    margin: 0;
}

blockquote strong {
    color: #0366d6;
}

/* Blockquote variants based on emoji */
blockquote:has(strong:contains("Tip")),
blockquote:has(strong:contains("tip")) {
    border-left-color: #28a745;
    background-color: #f0fff4;
}

blockquote:has(strong:contains("Attention")),
blockquote:has(strong:contains("Warning")) {
    border-left-color: #ffc107;
    background-color: #fffbf0;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 16px 0;
    font-size: 10pt;
    border: 1px solid #e1e4e8;
    border-radius: 6px;
    overflow: hidden;
}

th {
    background: linear-gradient(180deg, #0366d6 0%, #0256b9 100%);
    color: white;
    padding: 12px 15px;
    text-align: left;
    font-weight: 600;
    font-size: 10pt;
}

td {
    padding: 10px 15px;
    border-bottom: 1px solid #e1e4e8;
    vertical-align: top;
}

tr:nth-child(even) {
    background-color: #f6f8fa;
}

tr:last-child td {
    border-bottom: none;
}

ul, ol {
    margin: 12px 0;
    padding-left: 28px;
}

li {
    margin: 6px 0;
}

li > ul, li > ol {
    margin: 4px 0;
}

hr {
    border: none;
    border-top: 1px solid #e1e4e8;
    margin: 30px 0;
}

/* Checkbox styling for task lists */
input[type="checkbox"] {
    margin-right: 8px;
    transform: scale(1.2);
}

a {
    color: #0366d6;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

strong {
    color: #24292e;
    font-weight: 600;
}

em {
    color: #586069;
}

/* Special styling for warning blocks */
blockquote p:first-child strong:first-child {
    display: inline-block;
    margin-bottom: 4px;
}

/* Footer styling */
body > p:last-of-type {
    text-align: center;
    color: #586069;
    font-style: italic;
    margin-top: 40px;
    padding-top: 20px;
    border-top: 1px solid #e1e4e8;
}
"""

def find_chrome():
    """Trouve le chemin de Chrome/Chromium"""
    chrome_paths = [
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '/Applications/Chromium.app/Contents/MacOS/Chromium',
        '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser',
        shutil.which('google-chrome'),
        shutil.which('chromium'),
        shutil.which('chromium-browser'),
    ]

    for path in chrome_paths:
        if path and os.path.exists(path):
            return path

    return None

def convert_md_to_pdf(input_path: str, output_path: str = None):
    """
    Convertit un fichier Markdown en PDF

    Args:
        input_path: Chemin du fichier Markdown
        output_path: Chemin du fichier PDF de sortie (optionnel)
    """
    input_file = Path(input_path)

    if not input_file.exists():
        print(f"Erreur: Le fichier {input_path} n'existe pas")
        sys.exit(1)

    if output_path is None:
        output_path = str(input_file.with_suffix('.pdf'))

    print(f"Lecture de {input_path}...")

    # Lire le contenu Markdown
    with open(input_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    print("Conversion Markdown -> HTML...")

    # Convertir en HTML avec extras
    html_content = markdown2.markdown(
        md_content,
        extras=[
            'tables',
            'fenced-code-blocks',
            'code-friendly',
            'cuddled-lists',
            'target-blank-links',
            'task_list',
            'header-ids'
        ]
    )

    # Créer le document HTML complet
    full_html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formation ChatGPT - Exercices Pratiques</title>
    <style>
{CSS_STYLE}
    </style>
</head>
<body>
{html_content}
</body>
</html>"""

    # Trouver Chrome
    chrome_path = find_chrome()

    if chrome_path:
        print(f"Utilisation de Chrome: {chrome_path}")

        # Créer un fichier HTML temporaire
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False, encoding='utf-8') as f:
            f.write(full_html)
            temp_html = f.name

        try:
            # Utiliser Chrome headless pour générer le PDF
            cmd = [
                chrome_path,
                '--headless',
                '--disable-gpu',
                '--no-sandbox',
                '--disable-software-rasterizer',
                f'--print-to-pdf={output_path}',
                '--no-pdf-header-footer',
                temp_html
            ]

            print("Génération du PDF avec Chrome...")
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)

            if os.path.exists(output_path):
                print(f"PDF généré avec succès: {output_path}")
                return output_path
            else:
                print("Erreur Chrome:", result.stderr)
                raise Exception("Chrome n'a pas pu générer le PDF")

        finally:
            # Nettoyer le fichier temporaire
            os.unlink(temp_html)
    else:
        # Fallback: sauvegarder le HTML
        html_output = str(Path(output_path).with_suffix('.html'))
        with open(html_output, 'w', encoding='utf-8') as f:
            f.write(full_html)
        print(f"Chrome non trouvé. HTML généré: {html_output}")
        print("Pour convertir en PDF, ouvrez le fichier HTML dans un navigateur et imprimez en PDF.")
        return html_output

if __name__ == "__main__":
    # Fichier par défaut
    script_dir = Path(__file__).parent
    default_input = script_dir / "EXERCICES-CHATGPT.md"

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = str(default_input)

    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    convert_md_to_pdf(input_file, output_file)
