# Contributing

Thanks for helping keep this the best-curated Capella / Arcadia index anywhere. Read
this before opening a PR: the CI gates enforce most of it.

The fastest path: open an issue using the "Suggest a resource" form, or open a pull
request that edits `README.md` directly.

## 1. How to suggest a resource

- **Issue:** use the *Suggest a resource* form. Good for "I found this, you decide."
- **PR:** edit `README.md`, follow the entry format below, tick the PR checklist. CI
  link-checks your entry and lints the list.

## 2. Inclusion bar

An entry is accepted only if **all** hold:

1. **On-topic**: genuinely about Capella or the Arcadia method (not general MBSE only).
2. **Substantive**: it teaches, demonstrates, specifies, or provides something usable.
   Not a stub. Not pure vendor marketing.
3. **Live**: the link resolves right now.
4. **Not duplicative**: not already listed (see the canonical-URL rule, §6).
5. **Legally linkable**: publicly accessible. We **link**, we never re-host model files,
   PDFs, or proprietary content.

Tie-breakers (nice-to-have, not gates): has a real openable model (`has-model`),
recently updated, from a recognized source (Eclipse, Thales/Obeo, DLR, a university, an
established practitioner).

## 3. Entry format

One line per entry, **hyphen separator** (` - `, never an en/em dash: awesome-lint
rejects those), tags as **inline code spans inside the sentence before the terminal
period**, year parenthesized as the last token:

```text
- [Resource Name](https://example.com) - One-line factual description `Capella` `Arcadia` `tool` (2026).
```

- **Description:** factual, one line, **≤ 140 characters** (measured from the first
  character after ` - ` to the last character before the first tag, excluding the link
  markup and tags). No hype.
- **`has-model`** means: a **directly downloadable, non-paywalled** Capella model (an
  Eclipse model project with `.aird`) that opens in Capella. Screenshots, papers
  *describing* a model, and access-gated / request-only files **do not** qualify.

## 4. Tag vocabulary, cardinality & order

Tags appear in this fixed order, drawn **only** from this vocabulary:

`language → method → tool → has-model → type → spec/standard → paid → year`

| Axis | Cardinality | Values |
| --- | --- | --- |
| language | exactly 1 | `Capella` (native Capella viewpoints/metamodel, and Arcadia-method-only resources whose home is Capella) · `UAF` (UAF/UPDM through a Capella addon) · `SysML-general` (resources that primarily position Capella or Arcadia against SysML) |
| method | 0 or 1 | `Arcadia` |
| tool | 0 or more | `python4capella` · `py-capellambse` · `Capella-Studio` · `other-tool` |
| has-model | 0 or 1 | `has-model` |
| type | exactly 1 (dominant form) | `tutorial` · `course` · `book` · `paper` · `blog` · `video` · `tool` · `plugin` · `docs` · `case-study` |
| spec/standard | 0 or 1 | `standard` (use only after seed verifies the Arcadia standard id, e.g. AFNOR Z67-140, on the method page) |
| paid | 0 or 1 | `paid` |
| year | exactly 1 | `(YYYY)` (see §5) |

- `other-tool` graduates to its own tag only once ≥ 3 entries share it; update this
  table in the same change.
- For a normative standard document use `standard` and omit `paper`.

## 5. The year rule (`YYYY`)

`(YYYY)` = the year of the resource's **most recent author-published version**:

- a paper → its publication year;
- a repo → its latest tagged release, or the latest default-branch commit if untagged;
- a course → its current cohort year.

**Trivial edits (typo fixes) don't count.** Examples:

- A 2019 paper with a 2024 typo-fix commit → `(2019)`.
- A repo whose latest release tag is `v2.1` from 2023 → `(2023)`.

## 6. Canonical-URL rule (dedupe)

Before deciding "is this a duplicate", canonicalize both URLs: force `https`, lowercase
the host, strip a trailing slash, drop the query string and fragment unless they're
semantically required. If the canonical forms match, it's a duplicate.

Canonical hosts for official Capella material: `mbse-capella.org` (product home, Arcadia
method page, addons catalog, resources, Capella Days) and the `eclipse-capella` and
`labs4capella` GitHub orgs. Never list `arcadia-method.com` (DNS dead),
`capella.polarsys.org`, `projects.eclipse.org/projects/modeling.capella`, or the legacy
`eclipse.org/capella` / `eclipse.dev/capella` redirect paths.

## Editorial neutrality

This list is maintained by JG Systems Consulting Ltd., which sells commercial MBSE
consulting services, including Capella and Arcadia engagements. To keep it trustworthy:

- JGS-adjacent entries are listed by the **same inclusion bar** as everything else.
- Every JGS-adjacent entry sits next to **≥ 1 genuine competing/alternative entry**.
- **A superior competing resource is listed above a JGS-adjacent one.** Neutrality is
  enforced by this rule, not by tone.

> **Table of Contents:** the `## Contents` ToC is hand-maintained and lists only the
> top-level sections (a flat ToC keeps awesome-lint happy). If you add or rename a
> **top-level** section, update the ToC by hand; sub-sections are not listed. CI
> validates every ToC anchor resolves (lychee `--include-fragments anchor-only`).

## 8. Local link-check

No install needed. Check your changed links with Docker:

```sh
docker run --rm -v "$PWD:/d" -w /d lycheeverse/lychee --include-fragments anchor-only README.md
```

Or open a **draft PR** and let CI check it for you.

## 9. Maintenance cadence

The maintainers run a **quarterly sweep** (add new resources, prune rot), logged in
`CHANGELOG.md` with the date, and update the *Last full sweep* badge at the top of the
README each time. If it's been **> 6 months** since the last sweep, the badge flips to
"maintenance lapsed"; call it out in an issue.
