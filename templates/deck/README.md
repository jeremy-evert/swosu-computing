# Deck template

One self-contained HTML file. No build step, no outside scripts or fonts, works from a file, GitHub Pages, or a phone.
The Show Your Work lecture (`show-your-work/lecture/`) was made from this pattern.

## Make a deck
1. Copy `index.html` to `<topic>/lecture/index.html` (any folder that Pages serves).
2. Edit the `<title>` and description, then the `<section class="slide">` blocks. Keep `data-n` in order.
3. Put speaker notes in `<aside class="note">`. They show only when you press **N**.
4. Check links: `python3 templates/deck/check_links.py <topic>/lecture/index.html`.
5. Open it with `#3` on the end to jump to slide 3. Commit on a branch and open a PR.

## Keys
Arrows, Space, PageUp/PageDown, Home/End to move. **N** toggles notes. Swipe on a phone.

## Patterns in the template
Title, bullets (`.big`), three columns (`.three`, `.good`, `.bad`), prompt box (`.prompt`), question (`.ask`), table (`.lic`), link list (`.links`).
Colors are tokens on `:root`; dark mode follows the device.

## Handout
Print from the browser ("Save as PDF"). A print rule puts one slide per page. Check the result once before you rely on it.

## Rules for every deck
- No student names, quotes, grades, or transcript text. Protected material stays out.
- No host names, home paths, or secrets.
- Every link returns 200 (run the checker). Say what is not tested (projector, phone).
- Math-heavy decks need KaTeX. That is one pinned outside script, so only add it on purpose and say so in the PR.
