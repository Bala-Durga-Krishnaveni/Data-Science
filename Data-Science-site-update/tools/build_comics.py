"""Rebuilds pdfs/Comics-Unit-N.pdf from the comic images.

Folder layout expected (same as your project):
    comic designs/unit 1 images/*.png   (also unit 2 ... unit 5)
Inside each unit folder:
    - any image that is NOT named like "comic 1_3.png" is used as the first page (cover/infographic)
    - images named "comic <unit>_<number>.png" follow in number order (1, 2, 3 ... 10)

Usage (needs Python and Pillow:  pip install pillow):
    python tools/build_comics.py "comic designs"            # rebuilds all units into pdfs/
    python tools/build_comics.py "comic designs" 3          # rebuilds only unit 3
"""
import glob, os, re, sys
from PIL import Image

Image.MAX_IMAGE_PIXELS = None
src = sys.argv[1] if len(sys.argv) > 1 else "comic designs"
only = sys.argv[2] if len(sys.argv) > 2 else None
out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "pdfs")

def natural(path):
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", os.path.basename(path))]

for unit in range(1, 6):
    if only and str(unit) != only:
        continue
    files = [f for ext in ("png", "jpg", "jpeg") for f in glob.glob(os.path.join(src, f"unit {unit} images", f"*.{ext}"))]
    if not files:
        print(f"Unit {unit}: no images found, skipped")
        continue
    panel = lambda f: re.search(r"comic \d+_\d+", os.path.basename(f), re.I)
    ordered = [f for f in files if not panel(f)] + sorted([f for f in files if panel(f)], key=natural)
    pages = []
    for f in ordered:
        im = Image.open(f).convert("RGB")
        if im.width > 1600:
            im = im.resize((1600, round(im.height * 1600 / im.width)), Image.LANCZOS)
        pages.append(im)
    out = os.path.join(out_dir, f"Comics-Unit-{unit}.pdf")
    pages[0].save(out, save_all=True, append_images=pages[1:], quality=82, resolution=150)
    print(f"Unit {unit}: {len(pages)} pages -> {out}")
