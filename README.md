# Personal website (Quarto)

Source for <https://dariusmichienzi.github.io>.

## Edit locally

1. Install [Quarto](https://quarto.org/docs/get-started/).
2. `quarto preview` in this folder opens a live preview.
3. Pages are the `.qmd` files; styling is in `styles/`.

## Replace the Fe line profiles

The figure on the home and research pages reads three text files:

```
data/line-profiles/lamppost.txt
data/line-profiles/ring.txt
data/line-profiles/disc.txt
```

Each has two columns: energy (keV) and flux. Lines starting with `#` are ignored,
and each curve is normalised to its peak. To add a geometry, add a file and a
matching line in `_line-profile-figure.qmd`.

## Publish on GitHub Pages

1. Create a public repository named `DariusMichienzi.github.io` and push this folder to `main`.
2. In the repository: Settings → Pages → Source: **GitHub Actions**.
3. Every push to `main` re-renders and publishes the site (see `.github/workflows/publish.yml`).

The `_site/` folder is the rendered output and is not committed.
