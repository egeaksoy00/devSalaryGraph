![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)

![Recharts](https://img.shields.io/badge/Recharts-FF6384?style=for-the-badge)

![Papa Parse](https://img.shields.io/badge/Papa_Parse-4CAF50?style=for-the-badge)

![ETL Pipeline](https://img.shields.io/badge/ETL_Pipeline-6A1B9A?style=for-the-badge)

![Data Engineering](https://img.shields.io/badge/Data_Engineering-0A66C2?style=for-the-badge)

![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)

Update the existing “Türkiye Yazılımcı Maaşları” page in the current repository.

The page already exists at:

/yazilimcimaaslari/

Your task is to add:

1. A detailed “About This Project” section
2. A clear data-source and methodology disclaimer
3. A complete footer with my profiles, contact information, and the original data source

IMPORTANT DEPLOYMENT RESTRICTION

Do NOT deploy this project to Vercel.

Do NOT run:

- vercel
- vercel --prod
- npm run deploy
- any production deployment command
- git push
- automatic publishing workflows

Do not create a production deployment.

Only modify the local project files and validate the result locally.

Do not commit the changes unless I explicitly request it.

====================================================
GENERAL REQUIREMENTS
====================================================

Before editing:

1. Inspect the current implementation of the /yazilimcimaaslari/ page.
2. Preserve all existing charts, filters, data loading, interactions, SEO metadata, routes, and responsive behavior.
3. Match the page’s existing visual language.
4. Reuse existing layout, typography, spacing, colors, and component conventions where appropriate.
5. Do not introduce unnecessary dependencies.
6. Keep the entire visible page content in Turkish.
7. Do not fabricate technical claims or data-source details.
8. Do not alter the CSV data or analytical calculations.

The new content should feel integrated into the current page, not appended as an unrelated block.

====================================================
SECTION 1 — ABOUT THIS PROJECT
====================================================

Add a new section near the bottom of the page, after the charts and methodology content but before the footer.

Suggested section title:

“Proje Hakkında”

This section should explain how the project was created in a concise but technically credible way.

The content should communicate the following points:

- The original public survey data was obtained from the following GitHub repository:
  https://github.com/oncekiyazilimci/2026-yazilim-sektoru-maaslari

- The survey contains anonymous salary responses from 5,003 software professionals.

- The raw data was processed through a custom data pipeline.

- Python and pandas were used for extraction, cleaning, validation, transformation, currency normalization, aggregation, and generation of processed datasets.

- Separate aggregate datasets were created for:
  - salaries by software position
  - salaries by position and experience
  - salaries by company size and seniority

- Median salary was preferred over arithmetic mean because salary distributions can contain extreme values and outliers.

- The processed CSV datasets were then presented through an interactive web interface.

- React was used for the interface.

- Recharts was used for the interactive charts.

- Papa Parse was used to parse processed CSV files in the frontend.

- The project was designed as an end-to-end data engineering and data visualization project, covering the flow from raw data to a public-facing data product.

Do not present this as a long wall of text.

Use a clean editorial structure.

Possible layout:

- Short introductory paragraph
- A compact process timeline or step list
- A small technology list
- A highlighted source reference

Suggested process stages:

1. Veri Kaynağı
2. Veri Temizleme
3. Doğrulama ve Dönüştürme
4. Toplulaştırma
5. Görselleştirme

Use concise Turkish descriptions beneath each stage.

Example tone:

“Ham anket verileri Python ve pandas ile temizlendi, doğrulandı ve analiz için yeniden yapılandırıldı.”

Avoid exaggerated wording such as:

- tamamen kusursuz
- kesin sonuçlar
- Türkiye’nin en doğru maaş verisi
- sektörü eksiksiz temsil eder

====================================================
SECTION 2 — DATA SOURCE
====================================================

Add a visible source block inside or directly after the “Proje Hakkında” section.

Suggested heading:

“Veri Kaynağı”

Include:

“Bu projede kullanılan ham veriler, Önceki Yazılımcı tarafından yayımlanan açık GitHub deposundan alınmıştır.”

Create a clickable external link to:

https://github.com/oncekiyazilimci/2026-yazilim-sektoru-maaslari

Recommended link label:

“2026 Yazılım Sektörü Maaşları — GitHub”

External links must:

- open in a new tab
- use rel="noopener noreferrer"
- have a visible hover and keyboard focus state
- remain accessible

Clearly distinguish between:

- the original public dataset
- my own data processing, aggregation, analysis, and visualization work

Do not imply that I collected the original survey responses myself.

A suitable sentence would be:

“Anket verilerinin toplanması ve ilk yayımlanması kaynak depo sahibine aittir; veri temizleme, dönüştürme, toplulaştırma ve bu sayfadaki görselleştirme çalışmaları bu proje kapsamında gerçekleştirilmiştir.”

====================================================
SECTION 3 — DISCLAIMER
====================================================

Add a visually distinct but restrained disclaimer block.

Suggested title:

“Veri ve Yorumlama Notu”

The disclaimer should explain all of the following:

- The dataset comes from a publicly available third-party repository.
- The original data belongs to its respective publisher or contributors.
- This website is an independent analysis and visualization project.
- It is not officially affiliated with, endorsed by, or operated by the original repository owner.
- Survey participation was voluntary and anonymous.
- The results represent the survey participants and may not represent the entire Turkish software industry.
- Sample sizes differ by position, experience level, seniority, and company size.
- Segments with smaller sample sizes may be less representative.
- Salaries are presented for informational and analytical purposes only.
- The results should not be interpreted as guaranteed market salaries, employment advice, financial advice, or compensation commitments.
- Median values summarize the available survey responses and should be interpreted together with sample count.
- Any processing or interpretation errors may be reported using the contact email.

Use clear Turkish language.

Keep the disclaimer concise enough to remain readable.

Suggested copy direction:

“Bu sayfadaki sonuçlar gönüllü ve anonim anket yanıtlarının toplulaştırılmış analizidir. Veriler, Türkiye’deki tüm yazılım çalışanlarını eksiksiz biçimde temsil etmeyebilir. Özellikle düşük örneklemli segmentler yorumlanırken katılımcı sayısı dikkate alınmalıdır.”

Do not hide this information inside a tooltip or collapsed panel.

It must be visible on the page.

====================================================
SECTION 4 — FOOTER
====================================================

Add a complete footer at the bottom of the page.

The footer should visually match the rest of the salary page.

It should be responsive and readable on mobile.

Use semantic HTML:

<footer>

Recommended structure:

LEFT COLUMN

Project identity:

“Türkiye Yazılımcı Maaşları”

Short description:

“Türkiye’deki yazılım maaşlarını pozisyon, deneyim ve şirket büyüklüğüne göre inceleyen bağımsız veri analizi projesi.”

MIDDLE COLUMN

Heading:

“Bağlantılar”

Add:

- GitHub
- LinkedIn
- E-posta

Use the existing GitHub and LinkedIn URLs already present elsewhere in the portfolio repository.

Do not guess these URLs.

Search the existing project files and reuse the exact existing profile links.

The email must be:

egeaksoy@ug.bilkent.edu.tr

Create a mailto link:

mailto:egeaksoy@ug.bilkent.edu.tr

Suggested visible contact text:

“Herhangi bir soru, geri bildirim veya düzeltme için egeaksoy@ug.bilkent.edu.tr adresinden ulaşabilirsiniz.”

RIGHT COLUMN

Heading:

“Veri Kaynağı”

Add a clickable source link:

“Önceki Yazılımcı — 2026 Yazılım Sektörü Maaşları”

URL:

https://github.com/oncekiyazilimci/2026-yazilim-sektoru-maaslari

Add a short attribution:

“Ham anket verileri açık kaynak olarak yayımlanan bu depodan alınmıştır.”

BOTTOM ROW

Add:

- Dynamic current year
- My name
- A short independent-project notice

Example:

“© [CURRENT YEAR] Ege Aksoy. Bağımsız veri analizi ve görselleştirme projesi.”

Do not hardcode the year if the existing framework allows it to be generated dynamically.

====================================================
DESIGN REQUIREMENTS
====================================================

The new sections should preserve the current editorial and data-product style.

Use:

- generous spacing
- restrained typography
- soft borders
- subtle background contrast
- readable paragraph widths
- clear section hierarchy
- responsive grid layouts
- accessible link styles
- visible focus states

Avoid:

- oversized cards
- excessive icons
- bright gradients
- heavy shadows
- legal-document styling
- dense walls of text
- repeating the same source link too many times

The “About” section may use a process timeline, compact cards, or a structured grid, but it should remain visually lightweight.

The disclaimer should be noticeable without looking like an error alert.

====================================================
ACCESSIBILITY
====================================================

Ensure:

- proper heading hierarchy
- semantic section elements
- semantic footer element
- descriptive anchor text
- keyboard accessibility
- visible focus styles
- sufficient contrast
- external links are identifiable
- icons, if used, have accessible labels
- no meaning depends only on color

====================================================
SEO AND STRUCTURED CONTENT
====================================================

Preserve the existing SEO implementation.

Do not remove or overwrite:

- page title
- meta description
- canonical URL
- Open Graph metadata
- sitemap configuration
- trailing-slash routing

The new “About” and disclaimer text must be present in the rendered HTML so search engines can index it.

Do not render essential text only through canvas, tooltip, or client-only hover states.

If the project already uses structured data, update it only when appropriate and without breaking the existing schema.

====================================================
VALIDATION
====================================================

After implementation, validate locally:

1. The /yazilimcimaaslari/ page still loads correctly.
2. All four existing charts continue to work.
3. CSV data continues to load correctly.
4. Search, filters, comparison controls, and tooltips still work.
5. The About section appears above the footer.
6. The source repository link is correct.
7. GitHub and LinkedIn links reuse the exact URLs already present in the portfolio.
8. The email link opens the default mail client.
9. External links use target="_blank" and rel="noopener noreferrer".
10. The disclaimer is visible and readable.
11. The footer works correctly on desktop, tablet, and mobile.
12. No existing route or portfolio page is broken.
13. Run the appropriate local build and lint commands.
14. Resolve any errors introduced by the changes.

Do not deploy to Vercel.

Do not push to GitHub.

Do not create a Git commit.

At the end, provide a concise implementation report containing:

- files changed
- components added or updated
- local validation commands run
- build and lint results
- confirmation that no deployment, commit, or push was performed
