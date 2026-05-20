# Search Intent Notes

Checked: 2026-05-20.

These notes explain why the public README uses service-explicit naming instead
of a generic `local-seo` brand.

## Observed Query Patterns

Fresh search-result checks showed repeated RU/CIS phrasing around:

- `локальное SEO`
- `продвижение на Яндекс Картах`
- `продвижение в 2ГИС`
- `продвижение в Google Картах`
- `карточка организации`
- `геосервисы`
- `карты и справочники`
- `отзывы`, `рубрики`, `фото`, `филиалы`

Agent-skill discovery also needs English/platform terms:

- `Google Business Profile`
- `Google Maps`
- `Yandex Business`
- `Yandex Webmaster`
- `2GIS`
- `local SEO skill`
- `Claude Code SEO skill`
- `Codex skill`
- `OpenCode skill`
- `Cursor skill`

## Source Examples

- Topvisor local SEO guide result mentions Яндекс Карты, Google Maps, and 2GIS.
- SeoNews local SEO result frames the work as profile optimization for
  Яндекс Карты, Google Карты, and 2GIS.
- Multiple agency/service results frame the category as `продвижение на
  Яндекс Картах`, `продвижение в 2ГИС`, and `Google Карты`.
- Vercel `skills` docs describe `npx skills` as supporting OpenCode, Claude
  Code, Codex, Cursor, and many additional agents.

## README Implication

The public repo name should stay:

```text
google-yandex-2gis-local-seo-skill
```

That name is less elegant than `cis-local-seo-skill`, but it directly matches
how people search for the platforms.
