# External Local SEO Skill Review

Checked: 2026-05-20.

Conclusion: do not import an external local SEO skill as-is for Google + Yandex
work. Use them only as idea sources.

## Candidates Found

- AgriciDaniel `claude-seo` / `seo-local`
  - URL: https://github.com/AgriciDaniel/claude-seo
  - Local skill URL:
    https://github.com/AgriciDaniel/claude-seo/blob/main/skills/seo-local/SKILL.md
  - Strengths: broad local SEO checklist, GBP/NAP/schema/reviews/location-page
    coverage, MIT metadata visible in skill frontmatter.
  - Reject as-is: Google-heavy, many ranking-factor claims and thresholds, no
    Yandex/Kazakhstan operating path, and not strict enough about verified facts
    versus generated recommendations.

- Local Falcon `local-visibility-skill`
  - URL: https://github.com/local-falcon/local-visibility-skill
  - Strengths: MIT license, strong geo-grid / AI visibility / GBP analysis
    framing, useful for Local Falcon customers.
  - Reject as-is: vendor-specific, MCP/subscription-oriented, AI visibility scope
    broader than local business safety, no Yandex workflow.

- Horosheff `google-yandex-seo-skill`
  - URL: https://github.com/Horosheff/google-yandex-seo-skill
  - Strengths: MIT, Google/Yandex page-auditor orientation, local parser, no
    paid APIs in the quick pass.
  - Use only as supplemental page-audit inspiration. It is not a full
    local-business listing/GBP/Yandex Business operating skill and does not
    replace the safety gates in `local-seo`.

- Garrett Smith `localseoskills`
  - URL: https://github.com/garrettjsmith/localseoskills
  - Strengths: local SEO oriented, open repo.
  - Reject as-is for current need: larger plugin/package structure, not a small
    Codex skill to drop into this environment, no confirmed Yandex/Kazakhstan
    safety model in the quick pass.

## Adoption Rule

Before importing any future local SEO skill:

1. Inspect `SKILL.md`, scripts, install hooks, package files, and any network/API
   behavior.
2. Confirm license.
3. Confirm no secret/cookie/token exfiltration.
4. Confirm it does not encourage fake reviews, fake locations, keyword stuffing,
   scraped owner accounts, or bypassing verification.
5. Confirm it covers Yandex or can be safely limited to Google-only use.
6. Prefer a small local skill plus project scripts over a broad external plugin.
