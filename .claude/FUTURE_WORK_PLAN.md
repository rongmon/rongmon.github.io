# Website Redesign - Future Work & Enhancements

**Last Updated:** December 2024
**Status:** Ready for Review & Discussion

---

## Summary

Website redesign is now in Phase 2. Phase 1 (core redesign) is complete with:
- ✅ New minimalist light theme homepage
- ✅ Dynamic news system
- ✅ Academics page with awards/CV
- ✅ Google Analytics integrated
- ✅ Publications list redesigned

This document tracks remaining work and improvements needed.

---

## Priority 1: Research Sub-Pages (CRITICAL)

**Current Status:** Research cards link to sub-pages that need proper content
**Files to Create/Update:**
- `/content/research/jwst/`
- `/content/research/ifu/`
- `/content/research/cgm/`
- `/content/research/fermi-bubbles/`
- `/content/research/galactic-outflows/`
- `/content/research/photometric-redshifts/`

**Each page should include:**
1. **Title & Overview** (what is this research area)
2. **Why It Matters** (scientific impact and importance)
3. **Our Approach** (methods, telescopes, techniques)
4. **Key Publications** (2-3 flagship papers with links)
5. **Team Members** (who works on this specific project)
6. **Visuals** (research images, diagrams, or figures)

**Suggested Structure Template:**
```markdown
---
title: "Research Area Name"
description: "Brief description"
---

# Research Area Title

## Overview
[2-3 sentences describing the research]

## Why It Matters
[Impact and scientific significance]

## Our Approach
[Methods, instruments, techniques used]

## Key Results & Publications
[2-3 papers with descriptions]

## The Team
[Team members working on this area]

## Related Resources
[Links to related pages, papers, news]
```

**Discussion Needed:** Content for each research page - you should provide the text/details

---

## Priority 2: Collaborators Page

**Current Status:** Does not exist
**File to Create:** `/content/collaborators/_index.md`

**Purpose:** Highlight national and international partnerships, strengthen credibility

**Suggested Content:**
- List of key collaborators (institutions)
- Brief collaboration descriptions
- Logos/links to partner institutions
- Collaborative projects

**Example Format:**
```
Collaborators include researchers at:
- MIT
- UC Berkeley
- ETH Zurich
- University of Wisconsin
- JPL
- STScI
[etc.]
```

**Discussion Needed:** Do you want this? If yes, who are key collaborators to highlight?

---

## Priority 3: Navigation/Menu Update

**Current Status:** ✅ COMPLETED - "Academics" now in main menu
- Replaced "About" with "Academics" in main navigation
- URL changed from `/about/` to `/academics/`
- Old `about.md` deleted
- Menu item updated in `config.toml`

**Next Steps (if needed):**
- Consider adding "Collaborators" to navigation if that page is created
- Verify all navigation links work and are discoverable

---

## Priority 4: CV/Document Management

**Current Status:** CV link points to external NC State profile
**File Consideration:** Create `/static/downloads/` directory for CV PDF

**Options:**
1. Keep linking to NC State profile (current approach)
2. Host CV PDF on site at `/static/downloads/CV_Bordoloi.pdf`
3. Both (CV on site + link to full profile)

**Discussion Needed:** Which approach do you prefer?

---

## Priority 5: Funding & Grants Page (OPTIONAL)

**Current Status:** Not present

**Purpose:** Show research funding, scale of operation, grant success

**Could Include:**
- Current/recent funded projects
- Funding agencies (NSF, NASA, etc.)
- Grant amounts
- Project timelines

**Discussion Needed:** Is this important to showcase? Would you like to add this?

---

## Priority 6: Teaching Page (OPTIONAL)

**Current Status:** Not present

**Purpose:** Highlight teaching contributions and mentorship

**Could Include:**
- Courses taught
- Course descriptions
- Mentoring approach
- Student outcomes

**Discussion Needed:** Important to include teaching? Would you like a dedicated page?

---

## Priority 7: Research Sub-Page Images

**Current Status:** Research cards have placeholder images

**Action Needed:** Ensure each research sub-page has appropriate visual content (diagrams, observations, plots)

**Files:** Store in `/static/images/`

**Discussion Needed:** Do you have images for each research area to include?

---

## Priority 8: Homepage Improvements (OPTIONAL)

**Current Status:** Homepage works well but could be enhanced

**Possible Enhancements:**
- Add "Key Discovery" or "Featured Research" highlight (1-2 flagship results)
- Add visual infographic showing research impact
- Add research stats (papers, students, grants)
- More visual storytelling

**Discussion Needed:** Would any of these enhancements appeal to you?

---

## Priority 9: SEO & Metadata

**Current Status:** Basic metadata present

**Could Improve:**
- Page descriptions (meta tags)
- Open Graph tags for social sharing
- Schema.org structured data for academic profile
- Sitemap optimization

**Discussion Needed:** How important is discoverability/SEO to you?

---

## Completed Phases

### Phase 1: Complete
- ✅ Homepage redesign with light theme
- ✅ News system (dynamic)
- ✅ Publications page (list format)
- ✅ People/Team page
- ✅ Research areas overview (cards)
- ✅ Code/Software page
- ✅ Press releases page
- ✅ Academics page (awards/CV)
- ✅ Google Analytics

---

## Next Steps

**Before Proceeding:**
1. Review this list and discuss priorities
2. Clarify content needs (especially research sub-pages)
3. Decide on optional sections (Collaborators, Teaching, Funding)
4. Gather materials (images, text, links)

**After Discussion:**
1. Implement research sub-pages with proper content
2. Add any other priority pages
3. Update navigation as needed
4. Refine styling/layout as needed
5. Final review and deployment

---

## Notes & Questions

- **Navigation:** Should "Academics" be in main menu or just linked from elsewhere?
- **Research Pages:** Who will write content for these? Do you have existing descriptions?
- **Images:** Do you have research diagrams, observation images, or publication figures to use?
- **Collaborators:** Is this important? Who are key partners to highlight?
- **Teaching:** Should teaching be more visible on the site?
- **Timeline:** What's the target completion date for all improvements?

---

**To Implement:** Review this with the user, discuss each section, gather content, then proceed with implementation.
