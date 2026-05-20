# Google/Yandex Local SEO Guardrails

Checked: 2026-05-20.

## Google Official Sources

- Google Business Profile local ranking: complete and accurate profile data,
  verification, current hours, review responses, photos/videos; ranking factors
  are relevance, distance, and prominence. No paid/requested ranking override.
  Source: https://support.google.com/business/answer/7091
- Google Business Profile representation rules: eligible businesses need a real
  customer-facing location or customer travel; business names must reflect the
  real-world name; address/service area must be accurate; virtual offices and
  keyword-stuffed address/name fields are not allowed; service-area businesses
  may need to hide residential addresses.
  Source: https://support.google.com/business/answer/3038177
- Google Business Profile eligibility and agency conduct: manage only eligible
  real businesses with owner authorization; do not claim profiles without
  consent, block ownership transfer, or make unrealistic claims.
  Source: https://support.google.com/business/answer/13763036
- Business details in Search: claim and verify GBP, verify site ownership in
  Search Console, provide contact/social/official details, and use structured
  data to clarify business information.
  Source: https://developers.google.com/search/docs/appearance/establish-business-details
- LocalBusiness structured data: use LocalBusiness or a specific subtype with
  visible, accurate name, address, phone, URL, opening hours, geo, reviews only
  when applicable, and validate with Rich Results Test / URL Inspection.
  Source: https://developers.google.com/search/docs/appearance/structured-data/local-business
- Structured data policies: markup must represent the main visible content, not
  be hidden, misleading, spammy, or irrelevant. Correct markup does not
  guarantee rich results.
  Source: https://developers.google.com/search/docs/appearance/structured-data/sd-policies
- Search spam policies: block doorway city pages, scaled low-value pages,
  cloaking, sneaky redirects, keyword stuffing, link spam, and other manipulative
  patterns. Local pages must provide real location-specific value.
  Source: https://developers.google.com/search/docs/essentials/spam-policies
- Sitemap/indexing guidance: sitemaps are discovery hints, not indexing
  guarantees. `lastmod` should reflect significant page updates, and repeated
  recrawl requests do not force faster crawling.
  Sources: https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview,
  https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl

## Yandex Official Sources

- Yandex Business quick start: adding a company is free; company ownership must
  be confirmed; online-only businesses should use city/region instead of a fake
  street address.
  Source: https://yandex.ru/support/business-priority/ru/add-company/add-org
- Yandex Business data/moderation: business data, edits, photos, posts, and
  responses can require moderation; address checks may require real evidence.
  Sources: https://yandex.ru/support/business-priority/ru/manage/data,
  https://yandex.ru/support/business-priority/ru/add-company/info-terms,
  https://yandex.ru/support/business-priority/ru/moderation/moderation-address
- Yandex site/social rules: profile contacts and site data must match the
  official company data. Use the same scheme/www variant between Business and
  Webmaster where possible.
  Source: https://yandex.ru/support/business-priority/ru/add-company/rules-site
- Yandex address rules: use factual client-facing addresses, avoid legal/postal
  addresses that are not real public locations, and avoid duplicate cards.
  Source: https://yandex.ru/support/business-priority/ru/add-company/rules-address
- Yandex reviews: owner replies are moderated, often around three days; one
  reply per review; use personal helpful replies rather than boilerplate only.
  Source: https://yandex.ru/support/business-priority/ru/manage/reviews
- Yandex regionality: regionality can affect geo-dependent queries; it is based
  on actual company/site evidence and does not exclude a site from other
  regions when relevant.
  Source: https://yandex.ru/support/webmaster/ru/site-geography/site-region
- Yandex snippets: titles/descriptions are influenced by page text, title/meta,
  schema, Market data, and links; they are not fully controlled by the site.
  Source: https://yandex.ru/support/webmaster/ru/search-results/title-and-description
- Yandex Organization/Place schema: use supported Organization/Place-derived
  schema fields such as name, URL, address, telephone, geo, location, and
  openingHours to mirror verified facts.
  Source: https://yandex.ru/support/webmaster/ru/supported-schemas/address-organization
- Yandex Product schema: only mark up real visible product/offer data with price
  and ISO currency when present. Kazakh and Russian page languages are supported
  for relevant snippets.
  Source: https://yandex.ru/support/webmaster/ru/supported-schemas/goods-prices
- Yandex discovery: use sitemaps and IndexNow where appropriate; YML feeds are
  relevant for goods/services, not a generic replacement for organization-card
  ownership.
  Sources: https://yandex.ru/support/webmaster/ru/indexing-options/sitemap,
  https://yandex.ru/support/webmaster/ru/indexing-options/index-now,
  https://yandex.ru/support/business-priority/ru/manage/price-list

## Secondary Practitioner Context

Use these only for prioritization, not compliance:

- Whitespark local ranking factors reports emphasize GBP category, reviews,
  proximity, on-page service/location pages, citations, and links.
  Source: https://whitespark.ca/local-search-ranking-factors/
- BrightLocal local ranking/review guides are useful for review and local
  algorithm context, especially consumer review behavior.
  Source: https://www.brightlocal.com/learn/google-local-algorithm-and-ranking-factors/
- LocalU checklists are useful as implementation reminders, not policy.
  Source: https://localu.org/

Reject any recommendation from practitioner material if it conflicts with
Google/Yandex policy, visible business facts, or owner approval requirements.
