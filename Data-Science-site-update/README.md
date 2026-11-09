# Data Science – Course Page

Course website for Data Science, Dept. of Information Technology, JNTUGV-CEV.

## Files
- `index.html` – the course page
- `pdfs/` – the PDFs that the links on the page open in the browser
- `tools/build_comics.py` – rebuilds the comic PDFs from images

## 1. Turn on the view counter (one-time, about 2 minutes)
1. Sign up free at https://www.goatcounter.com and choose a site code (e.g. `jntugv-datascience`).
2. In GoatCounter go to **Settings → Site → "Allow adding visitor counts on your website"** and turn it on, then save.
3. Open `index.html`, find `var GOATCOUNTER_CODE = "";` near the bottom and put your code inside the quotes.
4. Commit/upload `index.html`. The "👁 Views" badge appears in the top bar.

Your GoatCounter dashboard also shows visits per day/country and how many times each PDF was opened or downloaded.

## 2. Add or change PDFs
- **Replace** (e.g. new notes): upload a PDF with the **same file name** to the `pdfs` folder (Add file → Upload files → Commit). The existing link then shows the new content. Press Ctrl+F5 if the old one still appears.
- **Add a new PDF**: upload it to `pdfs`, then add one line in the Quick Links section of `index.html`:
  `<li><a href="pdfs/Your-File.pdf" target="_blank" rel="noopener">Name shown on page</a></li>`

## Syllabus
The Syllabus link opens `pdfs/Syllabus.pdf`. Add your syllabus PDF to the `pdfs` folder with exactly that name.
(In Google Docs: File → Download → PDF Document, rename it `Syllabus.pdf`, then upload it.)

## Change the comic images
Each unit's comics are one PDF: `pdfs/Comics-Unit-1.pdf` … `Comics-Unit-5.pdf`.
1. Replace or add images in your local `comic designs/unit N images` folder (cover/infographic = any name; panels = `comic N_1.png`, `comic N_2.png` …).
2. Run `python tools/build_comics.py "comic designs" N` (N = unit number; leave it out to rebuild all). Needs `pip install pillow`.
3. Upload the new `pdfs/Comics-Unit-N.pdf` to GitHub (same name replaces the old one).
No Python? Combine the images into one PDF with any "JPG/PNG to PDF" tool and upload it with the same file name.

## Publish
Settings → Pages → Deploy from branch → `main` / root. The PDFs open publicly for everyone with the site link.
