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
- `оформить карточку организации`
- `ведение карточек`
- `Яндекс Справочник`
- `карточка компании в 2ГИС`
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

- 34web local SEO result frames visibility around geoservices such as Яндекс
  Карты, Google Карты, 2GIS, Авито, and Яндекс Услуги:
  https://34web.ru/blog/professionalnaya-nastroyka-lokalnogo-seo-po-11-osnovnym-pravilam/
- Topvisor local SEO guide result mentions Яндекс Карты, Google Maps, and 2GIS:
  https://journal.topvisor.com/ru/practice/local-seo-guide/
- SeoNews local SEO result frames the work as profile optimization for Яндекс
  Карты, Google Карты, and 2GIS:
  https://m.seonews.ru/analytics/lokalnoe-seo-prodvigaem-kompaniyu-na-geoservisakh-svoimi-rukami/
- RocketData frames map promotion as work across geoservices, directories, and
  related local surfaces:
  https://rocketdata.ru/blog/5-instrumentov-dlya-prodvizheniya-biznesa-na-kartakh-v-novoy-realnosti
- Service pages in the search results explicitly use combinations like
  `продвижение на Яндекс.Картах, Google и 2ГИС`.
- `npx skills --help` lists `-a, --agent`, `-s, --skill`, `--all`,
  `--copy`, project installs, global installs, and JSON listing; the README
  install block uses those verified flags.

## README Implication

The public repo name should stay:

```text
google-yandex-2gis-local-seo-skill
```

That name is less elegant than `cis-local-seo-skill`, but it directly matches
how people search for the platforms.
