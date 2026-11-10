# Swarn Chatterjee academic website

Static GitHub Pages website in UGA red (#BA0C2F), black, white and light gray.

## Publish
1. Upload **all** files and directories (including `.github`) to a GitHub repository named `YOURUSERNAME.github.io`.
2. In repository Settings > Pages choose Deploy from a branch, `main`, `/ (root)`.
3. The photo is `assets/swarn-chatterjee.jpg`; the downloadable CV is `assets/Swarn_Chatterjee_CV.pdf`.

## Google Scholar citation metrics
The verified Google Scholar profile is `https://scholar.google.com/citations?user=GyPrRgcAAAAJ&hl=en`. Google Scholar does not offer a straightforward public browser API for this purpose, and GitHub Pages cannot safely store a private API key. The website therefore reads `data/scholar-metrics.json`, updated by a daily GitHub Actions job via the third-party SerpAPI Google Scholar Author API.

1. Register with SerpAPI (https://serpapi.com/), obtain an API key, and check your plan's request allowance.
2. In GitHub repository Settings > Secrets and variables > Actions > New repository secret, add `SERPAPI_KEY`. Never put the key in HTML or JavaScript.
3. Go to Actions > Update Google Scholar metrics > Run workflow for the first synchronization. Enable Actions and scheduled workflows as necessary.
4. The site displays a clear unavailable state until the first successful update. If a request fails, the last successful snapshot is preserved. GitHub scheduled runs can be delayed, so this is daily synchronized data, not a real-time live feed.

## Research profile links
- Google Scholar: verified profile ID `GyPrRgcAAAAJ`
- Scopus: verified author ID `26532233700`
- ORCID: currently points to ORCID name search, **not** an unverified personal identifier. Replace it with your exact ORCID profile URL once confirmed.

## Local preview
Run `python -m http.server 8000` from the website folder and open `http://localhost:8000`.
