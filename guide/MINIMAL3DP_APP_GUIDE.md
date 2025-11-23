# minimal3dp.com Application Development Guide

**Version:** 2.0
**Last Updated:** November 12, 2025
**Purpose:** Unified deployment, SEO, and monetization strategy for all minimal3dp.com applications
**Based on:** Proven patterns from minimal3dp.com Hugo site (5k+ YouTube subscribers, multiple tools)

---

## 🎯 Mission Statement & Brand Identity

**Primary Identity:** minimal3dp.com is the **central hub** for Mike Wilson's 3D printing ecosystem.

Build a portfolio of high-quality, free 3D printing tools under the `minimal3dp.com` brand. Each tool should:
- Solve a specific user problem exceptionally well
- Generate passive revenue through Amazon affiliate links
- Drive traffic through SEO and **YouTube integration** (Channel: UCM_8Mv-0S1LnnJpRJLjahaw)
- Maintain consistent branding and **cross-link back to minimal3dp.com**
- Strengthen the minimal3dp.com brand authority (not dilute it)

**Core Brand Pillars:**
1. **minimal3dp.com** - The home base (Hugo static site, Vercel-hosted)
2. **YouTube Channel** - Video content, tutorials, reviews (5,000+ subscribers)
3. **Tool Suite** - Free calculators and utilities (hosted on main site or subdomains)
4. **Educational Content** - Blog posts, Klipper guides, calibration tutorials
5. **Community** - Discord, GitHub, social media presence

**Brand Voice:** Technical but accessible, helpful not condescending, community-focused

---

## 📐 Architecture Standards

### Domain Strategy

**Root Domain:** `minimal3dp.com` ⭐ **PRIMARY BRAND IDENTITY**
- **Purpose:** Main marketing site, portfolio page, blog, tutorials, reviews
- **Technology:** Hugo Static Site Generator (v0.152.2 + Docsy theme)
- **Hosting:** Vercel (migrating from Hostinger)
- **Repository:** `minimal3dp/minimal3dp.github.io`
- **Current Features:**
  - FDM Cost Calculator (integrated tool)
  - Klipper Calibration Guides (comprehensive tutorials)
  - Blog (3D printing news, tips, reviews)
  - Product Reviews (affiliate revenue)
  - Tools Section (calculator suite)
- **Traffic:** Primary SEO target, main entry point for all users
- **Revenue:** Amazon Associates (tag: mwf064-20), potential consultation services

**YouTube Channel:** `youtube.com/channel/UCM_8Mv-0S1LnnJpRJLjahaw` ⭐ **CONTENT ENGINE**
- **Subscribers:** 5,000+ (growing)
- **Strategy:** Every video drives traffic back to minimal3dp.com
- **Content Types:** Tutorials, reviews, calibration guides, tool demos
- **Cross-Promotion:** All videos link to tools/guides on minimal3dp.com
- **Video Descriptions:** Include tool links, affiliate products, blog post references
- **Pinned Comments:** Direct links to relevant calculators/guides

**Subdomain Strategy:** One app = One subdomain (OPTIONAL, use sparingly)
```
minimal3dp.com ⭐                   → Main site (Hugo) - KEEP TRAFFIC HERE
├── blog posts                     → Integrated into main site
├── /tools/                        → Calculator suite (integrated)
├── /klipper-calibration/          → Tutorial hub (integrated)
└── /projects/                     → Build logs (integrated)

FUTURE Subdomains (only if tool becomes large standalone app):
├── settings.minimal3dp.com        → OrcaSlicer Expert Assistant
├── api.minimal3dp.com             → Shared API backend
└── [other specialized tools]      → Only if traffic justifies separation
```

**✅ RECOMMENDED: Keep Tools on Main Domain**
- **Why:** SEO authority stays with minimal3dp.com (not diluted across subdomains)
- **Example:** `minimal3dp.com/tools/fdm-cost-calculator` (current, working well)
- **Benefit:** All tool traffic benefits main domain's SEO
- **Exception:** Only use subdomain if tool becomes a major standalone product (10k+ monthly users)

**Why Prioritize Main Domain?**
- ✅ Centralized SEO authority (all backlinks boost main domain)
- ✅ Single brand identity (not confusing multiple subdomains)
- ✅ Hugo's fast performance handles multiple tools easily
- ✅ Easier cross-linking (all internal links)
- ✅ YouTube drives traffic to one destination
- ✅ Users recognize minimal3dp.com brand
- ✅ Affiliate revenue concentrated on main domain

### Technology Stack

**Main Site (minimal3dp.com):**
- **Hugo Static Site Generator** v0.152.2 Extended
  - **Theme:** Docsy v0.12.0 (via Hugo modules)
  - **Why Hugo:** 90-100 PageSpeed score, 2-5x faster than WordPress, zero maintenance
  - **Build:** `hugo --gc --minify` (automated via Vercel)
  - **Content:** Markdown files (Git-versioned, portable)
  - **Strengths:** Fast, secure, no database, excellent SEO performance
- **Hosting:** Vercel (migrating from Hostinger)
  - Automatic HTTPS, GitHub auto-deploy, Edge CDN
  - 60-90% faster TTFB vs traditional hosting
  - Free tier sufficient for current traffic

**New Tools/Apps (if needed):**
- **Static HTML/JS:** Best for simple tools (Tailwind CSS recommended)
- **Hugo Shortcodes:** Integrate tools directly into main site (RECOMMENDED)
- **Next.js:** For complex apps needing SSR/SSG
- **Python + Flask:** For data-heavy tools
- **Vue/React:** For interactive calculators

**Hosting for All Applications:** Vercel (Hobby - Free Tier)
- Automatic HTTPS
- GitHub auto-deploy
- Edge CDN (global performance)
- Unlimited bandwidth (within fair use)
- Zero configuration

**Backend (Future):**
- **Serverless Functions:** Python or Node.js on Vercel
- **Shared API:** `api.minimal3dp.com` for common services (if needed)
- **Database:** PostgreSQL (Vercel Postgres) or MongoDB Atlas

### Repository Structure

**Option A: Monorepo** (Recommended for 5+ apps)
```
minimal3dp-apps/
├── apps/
│   ├── orcaslicer/
│   ├── filament/
│   └── calc/
├── packages/
│   ├── ui-components/
│   └── shared-utils/
└── turbo.json
```

**Option B: Individual Repos** (Current - Good for 1-3 apps)
```
minimal3dp/orcaslicer-assistant
minimal3dp/filament-database
minimal3dp/print-calculator
```

---

## 🚀 Deployment Checklist

Use this checklist for **every new app or significant content update** you deploy.

### Phase 0: Hugo Content Development (Main Site)

For content on minimal3dp.com (blog posts, tutorials, calculators):

- [ ] **Create Content from Archetype**
  ```bash
  # Use appropriate archetype
  hugo new blog/posts/my-post.md
  hugo new projects/3d-printers/reviews/my-review.md
  ```

- [ ] **Write in Markdown with Shortcodes**
  - Use `{{< amazon-product "B0XXXXXX" >}}` for affiliate links
  - Use `{{< youtube "VIDEO_ID" >}}` for video embeds
  - Use `{{< cta type="youtube" >}}` for calls-to-action
  - Use `{{< alert type="info" >}}` for callout boxes

- [ ] **Add Front Matter**
  - Title, description, date, categories, tags
  - Featured image (1200x630px for OG image)
  - Draft status (set `draft: false` when ready)

- [ ] **Test Locally**
  ```bash
  hugo server -D --disableFastRender
  # Visit http://localhost:1313
  ```

- [ ] **Build and Deploy**
  ```bash
  git add .
  git commit -m "Add new post: [title]"
  git push origin main
  # Vercel auto-deploys in ~2 minutes
  ```

### Phase 1: Initial Setup (30 minutes) - New Tools Only

Only needed for **standalone tools** (if not using Hugo shortcodes):

- [ ] **Create GitHub Repository**
  - Name: `<app-name>` (lowercase, hyphens)
  - Description: One-sentence summary
  - Add README.md with project overview
  - Initialize with main branch

- [ ] **Choose URL Path**
  - **RECOMMENDED:** `/tools/<app-name>` on minimal3dp.com (Hugo shortcode/static page)
  - **Alternative:** `<app>.minimal3dp.com` subdomain (only if tool gets 10k+ monthly users)
  - Keep it short, descriptive, keyword-focused
  - Examples: `/tools/fdm-calculator`, `/tools/shrinkage`, `/klipper-calibration/flow-calibration`

- [ ] **Deploy to Vercel (if standalone)**
  - Connect GitHub repository
  - Framework: Select appropriate preset (or "Other" for static)
  - Root directory: `./`
  - Build command: (depends on framework, or blank for static HTML)
  - Output directory: (depends on framework, or `./` for static HTML)
  - Click "Deploy"

- [ ] **Configure Custom Domain (if standalone)**
  - In Vercel: Settings → Domains → Add domain
  - Enter: `<app>.minimal3dp.com`
  - Copy CNAME record: `cname.vercel-dns.com`
  - Add DNS record at domain registrar:
    ```
    Type:   CNAME
    Name:   <app>
    Value:  cname.vercel-dns.com.
    TTL:    3600
    ```
  - Wait 5-15 minutes for DNS propagation
  - Verify HTTPS certificate (auto-provisioned)

### Phase 2: SEO Foundation (60 minutes)

- [ ] **Optimize Page Title**
  - Format: `<Primary Keyword> - <Brand> | <Secondary Keyword>`
  - Example: `Best Slicer Settings for 3D Printing - OrcaSlicer Expert Assistant`
  - Include 1-2 target keywords
  - Keep under 60 characters

- [ ] **Write Meta Description**
  - Length: 150-160 characters
  - Include primary keyword in first 50 characters
  - List key features or benefits
  - Include call-to-action
  - Example: `Get expert 3D printing settings for 28 materials. Free tool optimized for strength, speed, quality, and accuracy. PLA, PETG, ABS, Nylon, PEEK, and more.`

- [ ] **Add Meta Keywords**
  - 5-10 targeted keywords
  - Include variations and long-tail phrases
  - Example: `3d printing, slicer settings, orcaslicer, pla settings, petg settings, bambu lab`

- [ ] **Add Schema.org Structured Data**
  - Type: `WebApplication` (for tools) or `Article` (for guides)
  - Include: name, description, keywords, applicationCategory
  - JSON-LD format in `<head>` section
  ```json
  {
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "OrcaSlicer Expert Assistant",
    "description": "Free tool for 3D printing slicer settings",
    "applicationCategory": "UtilitiesApplication",
    "keywords": "3d printing, slicer settings, orcaslicer"
  }
  ```

- [ ] **Add Open Graph Tags** (Social Sharing)
  ```html
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://<app>.minimal3dp.com/">
  <meta property="og:title" content="<App Name>">
  <meta property="og:description" content="<Description>">
  <meta property="og:image" content="https://<app>.minimal3dp.com/og-image.png">
  ```

- [ ] **Add Twitter Card Tags**
  ```html
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:url" content="https://<app>.minimal3dp.com/">
  <meta name="twitter:title" content="<App Name>">
  <meta name="twitter:description" content="<Description>">
  <meta name="twitter:image" content="https://<app>.minimal3dp.com/og-image.png">
  ```

- [ ] **Create OG Image**
  - Dimensions: 1200x630 pixels
  - Format: PNG (preferred) or JPG
  - File size: <300KB
  - Content: App name, key benefit, branding
  - Tool: Canva (use "Facebook Post" template)
  - Save as: `/og-image.png` in project root

- [ ] **Create sitemap.xml**
  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
      <loc>https://<app>.minimal3dp.com/</loc>
      <lastmod>2025-11-12</lastmod>
      <changefreq>weekly</changefreq>
      <priority>1.0</priority>
    </url>
  </urlset>
  ```

- [ ] **Create robots.txt**
  ```
  User-agent: *
  Allow: /

  Sitemap: https://<app>.minimal3dp.com/sitemap.xml
  ```

- [ ] **Submit to Google Search Console**
  - Go to: https://search.google.com/search-console
  - Add property: `https://<app>.minimal3dp.com`
  - Verify ownership (HTML file or meta tag)
  - Submit sitemap: `sitemap.xml`
  - Monitor weekly: impressions, clicks, position

- [ ] **Add FAQ Section**
  - 5-10 common questions related to your target keyword
  - Answer format: conversational, helpful, 2-3 sentences
  - Include Schema.org FAQ markup for rich snippets
  - Place prominently on page (not hidden in footer)

### Phase 3: Branding & Navigation (30 minutes)

**For Hugo Site Content (minimal3dp.com):**
- [ ] **Navigation is Automatic** - Docsy theme handles this
- [ ] **Add Internal Links** - Link to related posts, tutorials, tools
- [ ] **Add YouTube Videos** - Use `{{< youtube "VIDEO_ID" >}}` shortcode
- [ ] **Add Affiliate Links** - Use `{{< amazon-product "ASIN" >}}` shortcode
- [ ] **Add CTAs** - Use `{{< cta type="youtube" >}}` or `{{< cta type="email" >}}` shortcodes
- [ ] **Footer Links** - Configured in `hugo.toml` under `[params.links]`

**For Standalone Tools (if applicable):**
- [ ] **Add Header Navigation**
  ```html
  <nav class="main-nav">
    <a href="https://minimal3dp.com">← minimal3dp</a>
    <a href="https://minimal3dp.com/tools">All Tools</a>
    <a href="https://youtube.com/channel/UCM_8Mv-0S1LnnJpRJLjahaw">YouTube</a>
  </nav>
  ```

- [ ] **Add Footer Links**
  - Link to main site: `minimal3dp.com`
  - Link to other tools
  - Social media links (YouTube, Twitter, GitHub)
  - Ko-fi or donation link
  - Privacy policy (if collecting data)

- [ ] **Add YouTube Channel Link**
  - Prominent placement in header
  - Text: "Watch on YouTube" or "Video Guide"
  - Link: `https://youtube.com/channel/UCM_8Mv-0S1LnnJpRJLjahaw`
  - Include auto-subscribe button where relevant

- [ ] **Add Canonical URL**
  ```html
  <link rel="canonical" href="https://<app>.minimal3dp.com">
  ```
  (For Hugo pages, this is automatic)

### Phase 4: Analytics Setup (30 minutes)

**For Hugo Site (minimal3dp.com):**
- [ ] **Google Analytics 4 Already Configured**
  - Measurement ID: `G-VQ8RPWC2MK` (in `hugo.toml`)
  - Automatically tracks all pages

- [ ] **Add Custom Events** (in shortcodes)
  ```javascript
  // Already included in affiliate/YouTube shortcodes
  gtag('event', 'click_affiliate_link', {
    'product_id': '{{ .Get 0 }}',
    'link_text': 'View on Amazon'
  });

  gtag('event', 'video_play', {
    'video_id': '{{ .Get 0 }}',
    'video_title': 'Tutorial Video'
  });
  ```

- [ ] **Set Up Goals in GA4**
  - Affiliate link clicks
  - YouTube video plays
  - Newsletter signups
  - Tool interactions
  - Scroll depth (75%, 100%)

**For Standalone Tools (if applicable):**
- [ ] **Set Up Google Analytics 4**
  - Create GA4 property: `<App Name>`
  - Get Measurement ID: `G-XXXXXXXXXX`
  - Add GA4 script to `<head>`:
  ```html
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-XXXXXXXXXX');
  </script>
  ```

- [ ] **Configure Cross-Domain Tracking** (if linking to other apps)
  ```javascript
  gtag('config', 'G-XXXXXXXXXX', {
    'linker': {
      'domains': ['minimal3dp.com', '<app>.minimal3dp.com']
    }
  });
  ```

- [ ] **Track Custom Events**
  - Button clicks
  - Form submissions
  - Tool usage (calculations, selections, etc.)
  - Affiliate link clicks
  - External link clicks

- [ ] **Set Up Conversions**
  - Define primary conversion (tool usage, download, etc.)
  - Mark event as "Key Event" in GA4
  - Track conversion funnel

### Phase 5: YouTube Integration (30 minutes)

**For All Content (Main Site and Tools):**

- [ ] **Embed YouTube Videos**
  - **Hugo shortcode:** `{{< youtube "VIDEO_ID" >}}` (auto-responsive, privacy-enhanced)
  - **Standalone tools:** Use YouTube iframe API
  - Include tutorial/demo videos in every tool page
  - Add auto-subscribe button after video playback

- [ ] **Update YouTube Channel Description**
  - Add link to new content/tool
  - Format: `🔧 <TOOL/POST NAME>: https://minimal3dp.com/tools/<name>`
  - Brief description of content/tool's purpose
  - Keep minimal3dp.com as primary link

- [ ] **Update YouTube Channel Links**
  - YouTube Studio → Customization → Basic Info → Links
  - Primary link: `https://minimal3dp.com` (always)
  - Secondary links: Top tools, blog, Discord
  - Custom link for new major tools

- [ ] **Update Video Descriptions (Template)**
  ```
  ━━━━━━━━━━━━━━━━━━━━━
  🔧 FREE TOOLS & RESOURCES
  ━━━━━━━━━━━━━━━━━━━━━

  📖 Blog Post: https://minimal3dp.com/blog/posts/<slug>
  🧮 Calculator: https://minimal3dp.com/tools/fdm-cost-calculator
  📚 Klipper Guides: https://minimal3dp.com/klipper-calibration

  🏠 Main Site: https://minimal3dp.com
  💬 Discord: [link]

  ━━━━━━━━━━━━━━━━━━━━━
  🛒 GEAR I USE (Affiliate Links)
  ━━━━━━━━━━━━━━━━━━━━━

  [Use amazon-product shortcode links here]

  As an Amazon Associate I earn from qualifying purchases.
  ```

- [ ] **Cross-Promote in Videos**
  - Mention new content/tools in video
  - Show tool usage on screen
  - Add YouTube cards at 30%, 60%, 90% timestamps
  - Pin comment with link to minimal3dp.com
  - Add end screen with subscribe button + minimal3dp.com link

- [ ] **Create Companion Video (for major tools)**
  - Title format: `<Target Keyword> - Free Tool Tutorial`
  - Optimize for target SEO keyword
  - Show tool usage step-by-step
  - Include affiliate product recommendations
  - Link to minimal3dp.com in description, pinned comment, cards, end screen

- [ ] **Add Video Embeds to Blog Posts**
  - Every blog post should have related YouTube video
  - Use `{{< youtube "VIDEO_ID" >}}` shortcode
  - Place video near top of post (after intro paragraph)
  - Include text CTA: "Watch the video version of this guide"

---

## 💰 Monetization Strategy

### Amazon Affiliate Implementation (Hugo-Based)

**Prerequisites:**
- Amazon Associates account: https://affiliate-program.amazon.com
- Affiliate tag: `mwf064-20` (ALWAYS use this across ALL content)
- Hugo shortcode: `amazon-product.html` (see RECOMMENDATIONS.md for full code)

#### Hugo Shortcode Method (Recommended)

**Use Case:** Blog posts, reviews, tutorials on minimal3dp.com

**Implementation:**

1. **Create `/data/affiliate-products.yaml`:**
```yaml
# Organized by category
filaments:
  BXXXXXXX1:
    title: "eSUN PLA+ Filament"
    rating: 4.6
    reviews: 12453
    price: "$19.99"
    image: "https://m.media-amazon.com/images/I/..."
    description: "High-quality PLA+ with excellent layer adhesion"

printers:
  BXXXXXXX2:
    title: "Creality Ender 3 V3"
    rating: 4.5
    reviews: 8932
    price: "$289.99"
    image: "https://m.media-amazon.com/images/I/..."
    description: "Best budget 3D printer for beginners"
```

2. **Use in Blog Posts/Reviews:**
```markdown
---
title: "Best PLA Filaments for 3D Printing"
---

## Top Pick: eSUN PLA+

{{< amazon-product "BXXXXXXX1" >}}

This filament is my go-to for...

## Budget Option

{{< amazon-product "BXXXXXXX3" >}}
```

3. **Shortcode Auto-Handles:**
- Affiliate tag (`mwf064-20`) automatically appended
- GA4 click tracking (`affiliate_click` event)
- Disclosure text ("As an Amazon Associate...")
- Responsive card design with image, rating, price
- "View on Amazon" button

**Benefits:**
- One data file = update products site-wide
- Consistent styling across all pages
- Auto-tracking of clicks in GA4
- SEO-friendly (proper rel="sponsored" tags)

#### Static Product Recommendations (Standalone Tools)

**Use Case:** Simple standalone tools with known product recommendations

**Implementation:**
1. Create JSON file with product data:
```json
{
  "material_name": {
    "products": [
      {
        "name": "Product Name",
        "asin": "B0XXXXXXXX",
        "price": "$25.99",
        "reason": "Why this product is recommended"
      }
    ]
  }
}
```

2. Generate affiliate links:
```
https://www.amazon.com/dp/<ASIN>?tag=mwf064-20
```

3. Display recommendations contextually:
   - After user makes a selection
   - Related to user's inputs
   - Sidebar or bottom section

**Tracking Static Links:**
```javascript
// Track affiliate link clicks in GA4
document.addEventListener('click', function(e) {
    if (e.target.closest('a[rel*="sponsored"]')) {
        const link = e.target.closest('a');
        const productName = link.getAttribute('data-product-name');

        gtag('event', 'affiliate_click', {
            'event_category': 'Affiliate',
            'event_label': productName,
            'value': 1
        });
    }
});
```

#### Dynamic PA-API Integration (Phase 2 - Advanced)

**Use Case:** Tools needing real-time pricing, reviews, or product search

**Requirements:**
- Amazon Product Advertising API (PA-API) credentials
- Python serverless function on Vercel
- Redis or in-memory caching

**API Endpoints:**
```
GET /api/products?keyword=<keyword>&category=<category>
GET /api/product/<asin>
```

**Environment Variables (Vercel):**
```
PAAPI_ACCESS_KEY = <Your PA-API Access Key>
PAAPI_SECRET_KEY = <Your PA-API Secret Key>
PAAPI_ASSOCIATE_TAG = mwf064-20
PAAPI_REGION = us-east-1
PAAPI_HOST = webservices.amazon.com
CACHE_TTL = 3600
```

**Caching Strategy:**
- Cache product data for 1 hour
- Fallback to static data if API fails
- Rate limit: 1 request/second (PA-API limit)

**Implementation:** See `TODO.md` Phases 11-14 in OrcaSlicer Assistant for full PA-API roadmap

### Revenue Expectations

**Static Affiliate System:**
- Week 1: $5-10/month
- Month 1: $15-25/month
- Month 3: $40-60/month
- Month 6: $80-120/month

**With PA-API (Dynamic):**
- More products → More clicks → Higher revenue
- Expected: 1.5-2× static system revenue
- Month 6: $120-200/month
- Month 12: $200-400/month

**Revenue Multiplier Per App:**
- Each app = additional revenue stream
- 3 apps = 3× revenue potential
- Cross-linking boosts all apps' traffic

### Best Practices

✅ **Do:**
- Recommend products you genuinely believe in
- Explain WHY you recommend each product
- Disclose affiliate relationship: "As an Amazon Associate, I earn from qualifying purchases"
- Use `rel="noopener noreferrer sponsored"` on links
- Test products before recommending (if possible)

❌ **Don't:**
- Recommend products just for commissions
- Use deceptive practices (fake urgency, false claims)
- Hide affiliate disclosure
- Spam users with excessive ads
- Violate Amazon Associates terms

**Compliance:**
- Add disclosure: "This site contains affiliate links. We may earn a commission if you purchase through these links at no extra cost to you."
- Use `rel="sponsored"` attribute on affiliate links
- Follow FTC guidelines for affiliate marketing
- Comply with Amazon Associates Program Policies

---

## 🎯 SEO Strategy Template

### Keyword Research Process (Hugo Content-Focused)

**For Each New Blog Post, Tutorial, or Tool Page:**

1. **Identify Primary Keyword** (1-3 keywords)
   - What problem does your content solve?
   - What would users search for?
   - Use Google Autocomplete for ideas
   - Check YouTube Analytics "Trends" tab for video ideas
   - Check Google Search Console "Queries" for existing traffic

2. **Find Secondary Keywords** (5-10 keywords)
   - Variations of primary keyword
   - Related questions (use "People Also Ask" in Google)
   - Long-tail phrases
   - Tool: Ubersuggest, Google Keyword Planner (free), Ahrefs (paid)
   - YouTube search suggestions

3. **Analyze Competition**
   - Google your primary keyword
   - Check top 10 results
   - Identify gaps: What are they missing?
   - Your advantage: Free tools, interactive calculators, video tutorials, comprehensive guides

**Example: Flow Calibration Guide (minimal3dp.com)**
- **Primary:** "best slicer settings for 3d printing"
- **Secondary:** "orcaslicer settings", "pla settings 3d printing", "petg settings", "slicer settings guide", "3d print optimization"
- **Advantage:** Interactive tool vs static blog posts, 28 materials vs 5-10 materials

### Content Strategy

**On-Page Content:**
- H1: Primary keyword (exact match or close variation)
- H2-H3: Secondary keywords, questions
- First paragraph: Primary keyword in first 50 words
- Body: Natural keyword usage (don't stuff)
- Alt text: Describe images with keywords
- Internal links: Link to related tools/pages

**FAQ Section:**
- Answer 5-10 common questions
- Use question format in H3 tags: "What are the best..."
- Natural, helpful answers
- Include Schema.org FAQ markup

**Material/Topic Landing Pages:** (For content-heavy tools)
- Create dedicated pages for high-traffic topics
- Example: `/materials/pla`, `/materials/petg`
- Optimize each page for specific keyword
- Internal linking between related pages

### Link Building Strategy

**Internal Linking:**
- Link from main site (`minimal3dp.com`) to all apps
- Link between related apps
- Breadcrumb navigation
- Footer links on all pages

**External Backlinks:**
- **Reddit:** Share tool in r/3Dprinting, r/BambuLab, r/ender3 (helpful, not spammy)
- **Forums:** 3DPrintBoardPro, Prusa forums, Bambu forum
- **YouTube:** Video descriptions, pinned comments
- **Guest Posts:** Write for All3DP, 3DPrintBeginner
- **Open Source:** Contribute to OrcaSlicer, link to tool in discussions

**Social Media:**
- Twitter: Share tool launches, updates
- Reddit: Helpful responses with tool link
- Facebook Groups: 3D printing communities
- Discord: Bambu Lab, OrcaSlicer servers

### Technical SEO (Hugo-Specific)

- [ ] **Mobile-Friendly:** Hugo + Docsy theme is fully responsive (auto-configured)
- [ ] **Fast Loading:** Hugo generates static HTML (90-100 PageSpeed score)
  - Use `hugo --gc --minify` for production builds
  - Optimize images with Hugo's imgproc shortcode
  - Enable caching in `hugo.toml` (see RECOMMENDATIONS.md)
- [ ] **HTTPS:** Auto-configured with Vercel
- [ ] **Structured Data:** Use `schema-article.html` partial (see RECOMMENDATIONS.md)
  - Automatically generates JSON-LD for blog posts
  - Include FAQ schema for guides
  - Product schema for review posts
- [ ] **Sitemap:** Auto-generated by Hugo at `/sitemap.xml`
- [ ] **Canonical URLs:** Auto-configured by Hugo theme
- [ ] **Internal Linking:** Use Hugo `related-posts.html` partial (see RECOMMENDATIONS.md)
  - Auto-generates related content links
  - Improves site structure and crawlability
- [ ] **Image Optimization:**
  - Use Hugo imgproc: `{{< imgproc "image.jpg" Resize "800x" >}}`
  - Compress before upload (TinyPNG, Squoosh)
  - Use WebP where supported
- [ ] **Core Web Vitals:** Monitor in Google Search Console
  - Hugo static sites typically score 95-100
  - Ensure images have width/height attributes
  - Use preload for critical CSS/fonts

### Hugo SEO Enhancements (Quick Wins)

- [ ] **Enable Hugo SEO Params** (in `hugo.toml`):
```toml
[params]
  description = "Free 3D printing tools, tutorials, and calculators"
  images = ["og-image.png"]

[params.social]
  twitter = "minimal3dp"
  youtube = "UCM_8Mv-0S1LnnJpRJLjahaw"
  github = "minimal3dp"
```

- [ ] **Front Matter Optimization** (every post):
```yaml
---
title: "Flow Calibration Guide"
description: "Step-by-step guide to calibrate flow rate for perfect 3D prints"
date: 2025-01-15
categories: ["Klipper", "Calibration"]
tags: ["flow-rate", "3d-printing", "klipper", "tuning"]
featured_image: "images/flow-calibration.jpg"
draft: false
---
```

- [ ] **Use Hugo Shortcodes for SEO**:
  - `{{< amazon-product >}}` - Adds proper affiliate link structure
  - `{{< youtube >}}` - Privacy-enhanced YouTube embeds
  - `{{< cta >}}` - Call-to-action boxes with GA4 tracking
  - `{{< alert >}}` - Callout boxes for key info
  - See RECOMMENDATIONS.md for full shortcode implementations

### SEO Success Metrics (minimal3dp.com)

**Week 1 (After Vercel Migration):**
- Site indexed in Google Search Console
- 500-1,000 impressions
- Core Web Vitals: All green

**Month 1:**
- 5,000+ impressions
- 250+ clicks
- Page 2-3 ranking for target keywords
- 10+ backlinks

**Month 2:**
- 15,000+ impressions
- 750+ clicks
- Page 1 (top 10) ranking for 3-5 keywords
- 25+ backlinks

**Month 3:**
- 30,000+ impressions
- 1,500+ clicks
- Top 5 ranking for primary keywords
- 50+ backlinks
- YouTube traffic: 500+ referrals

**Month 6:**
- 75,000+ impressions
- 3,500+ clicks
- Top 3 ranking for 10+ keywords
- 150+ backlinks
- YouTube traffic: 2,000+ referrals
- Affiliate revenue: $80-120/month

**Month 12:**
- 150,000+ impressions
- 8,000+ clicks
- #1 ranking for 20+ keywords
- 500+ backlinks
- YouTube traffic: 5,000+ referrals
- Affiliate revenue: $200-400/month

---

## 📺 YouTube Integration Strategy

### Channel Structure

**Main Channel:** youtube.com/channel/UCM_8Mv-0S1LnnJpRJLjahaw (5,000+ subscribers)

**Content Engine Strategy:**
- YouTube drives traffic to minimal3dp.com
- Every video links to relevant blog post/tool
- Blog posts embed YouTube videos
- Symbiotic relationship: Video → Blog → Affiliate → Revenue

**Content Types:**
1. **Tool Tutorials:** How to use each minimal3dp.com tool (FDM calculator, Klipper guides)
2. **Calibration Guides:** Flow, pressure advance, input shaping, etc.
3. **Product Reviews:** 3D printers, filaments, accessories (with affiliate links)
4. **Comparison Videos:** "Cura vs OrcaSlicer vs PrusaSlicer"
5. **Project Walkthroughs:** Using tools in real projects
6. **Tips & Tricks:** Quick wins for 3D printing

### Video SEO

**Title Format:**
```
<Target Keyword> - <Secondary Keyword> (<Year>)
```
Example: `Klipper Flow Calibration - Perfect 3D Prints Every Time (2025)`

**Description Template:**
```
<Hook - What viewer will learn in 1-2 sentences>

<Chapters/Timestamps>
0:00 - Intro
1:00 - Why Flow Calibration Matters
3:00 - Using the Free Calculator
6:00 - Step-by-Step Process
...

━━━━━━━━━━━━━━━━━━━━━
🔧 FREE TOOLS & RESOURCES
━━━━━━━━━━━━━━━━━━━━━

📖 Full Written Guide: https://minimal3dp.com/klipper-calibration/flow-calibration
🧮 Flow Calculator: https://minimal3dp.com/klipper-calibration/flow-calibration#calculator
🏠 All Tools: https://minimal3dp.com/tools

━━━━━━━━━━━━━━━━━━━━━
🛒 GEAR I USE (Affiliate Links)
━━━━━━━━━━━━━━━━━━━━━

[Product Name]: https://amzn.to/XXXXX
[Product Name]: https://amzn.to/XXXXX

As an Amazon Associate I earn from qualifying purchases.

━━━━━━━━━━━━━━━━━━━━━

<Full video description, additional tips, troubleshooting>

💬 Join the Community:
Discord: [link]
GitHub: github.com/minimal3dp

#3dprinting #klipper #flowcalibration #calibration
```

**Tags (10-15):**
- Primary keyword (e.g., "flow calibration")
- Secondary keywords (e.g., "klipper tuning", "3d print quality")
- Material names (PLA, PETG, ABS)
- Slicer names (OrcaSlicer, Cura, PrusaSlicer, Klipper)
- Brand names (Bambu Lab, Prusa, Creality, Voron)

**Thumbnail:**
- Bold text: Primary keyword or benefit
- High contrast colors
- Include branding element
- Face (if applicable) for higher CTR
- 1280x720 pixels

### Cross-Promotion

**In Videos:**
- Mention tool in intro: "Link in description"
- Show tool on screen while explaining
- End screen: Add link to tool (custom URL)
- Cards: Link to tool at relevant moments

**Pinned Comments:**
```
📌 FREE TOOL: <APP NAME>

👉 https://<app>.minimal3dp.com

<Brief description of what tool does>

---

## 📝 Medium.com Cross-Posting Strategy

### Why Use Medium?

**Benefits:**
- **Expanded Reach:** Medium has 100M+ monthly readers
- **Built-in Audience:** Tap into Medium's recommendation algorithm
- **Backlinks:** All Medium posts link back to minimal3dp.com
- **SEO:** Canonical tags prevent duplicate content penalties
- **Authority:** Medium posts rank well in Google (domain rating 95+)
- **Monetization:** Medium Partner Program ($5-50/article for high performers)

**Your Profile:** https://medium.com/@minimal3dp

### Hugo → Medium Workflow

#### Option 1: Manual Cross-Posting (Recommended - Best Control)

**Process:**
1. Publish on minimal3dp.com first (establish ownership)
2. Wait 24-48 hours for Google to index
3. Copy content to Medium
4. Add canonical URL pointing to original
5. Add call-to-action linking to minimal3dp.com

**Implementation:**

1. **Write and Publish on Hugo Site:**
```bash
hugo new blog/posts/my-post.md
# Write content
hugo server -D  # Preview
# Set draft: false
git commit -am "Add new post"
git push  # Auto-deploys to Vercel
```

2. **Wait for Google Indexing:**
- Check Google Search Console: URL Inspection tool
- Confirm URL is indexed (usually 24-48 hours)

3. **Cross-Post to Medium:**
- Go to https://medium.com/new-story
- Copy Markdown content from Hugo
- Paste into Medium editor
- Format images (reupload if needed)
- Add canonical URL (see below)
- Add intro paragraph with CTA

4. **Set Canonical URL (Critical for SEO):**
```
Medium Editor → Story Settings (three dots menu) → Advanced Settings → Canonical URL

Enter: https://minimal3dp.com/blog/posts/my-post
```

**This tells Google:** "This is a republished version. The original is on minimal3dp.com."

5. **Add Medium-Specific Elements:**

**Intro Paragraph (before original content):**
```
Originally published at minimal3dp.com: https://minimal3dp.com/blog/posts/my-post

For interactive calculators, video tutorials, and more free tools, visit minimal3dp.com.

━━━━━━━━━━━━━━━━━━━━━
```

**End CTA (after original content):**
```
━━━━━━━━━━━━━━━━━━━━━

👉 Read the full guide with interactive tools: https://minimal3dp.com/blog/posts/my-post

🎥 Watch the video version: https://youtube.com/watch?v=VIDEO_ID

🔧 Free 3D Printing Tools: https://minimal3dp.com/tools

💬 Join our community on Discord: [link]

📧 Subscribe to our newsletter for more 3D printing tips: [link]
```

6. **Choose Publication (Optional):**
- Submit to relevant Medium publications:
  - "Towards Data Science" (for technical content)
  - "Better Programming" (for code/tools)
  - "3D Printing" publications
- Increases reach but reduces control

7. **Add Tags (5 max):**
- Primary keyword (e.g., "3D Printing")
- Secondary keywords ("Klipper", "Flow Calibration")
- Material/brand names ("PLA", "Bambu Lab")

8. **Publish on Medium:**
- Publish immediately or schedule
- Share on Twitter, Discord, LinkedIn

#### Option 2: Automated Cross-Posting (Advanced - Requires Setup)

**Tools Available:**

**A. Medium API + GitHub Actions (Free, Most Control)**

Create `.github/workflows/medium-crosspost.yml`:
```yaml
name: Cross-post to Medium

on:
  push:
    branches: [main]
    paths:
      - 'content/blog/posts/**'

jobs:
  crosspost:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          pip install requests python-frontmatter markdown2

      - name: Cross-post to Medium
        env:
          MEDIUM_TOKEN: ${{ secrets.MEDIUM_TOKEN }}
        run: python .github/scripts/crosspost-medium.py
```

Create `.github/scripts/crosspost-medium.py`:
```python
import os
import requests
import frontmatter
import markdown2
from pathlib import Path

MEDIUM_TOKEN = os.environ['MEDIUM_TOKEN']
SITE_URL = 'https://minimal3dp.com'

def get_changed_posts():
    # Get recently modified posts
    # Implementation details...
    pass

def convert_hugo_to_medium(post_path):
    # Read Hugo markdown
    with open(post_path, 'r') as f:
        post = frontmatter.load(f)

    # Convert to HTML
    content_html = markdown2.markdown(post.content)

    # Get canonical URL from front matter
    slug = Path(post_path).parent.name
    canonical_url = f"{SITE_URL}/blog/posts/{slug}"

    # Add intro and CTA
    intro = f'<p><em>Originally published at <a href="{canonical_url}">minimal3dp.com</a></em></p><hr>'
    cta = f'''<hr>
    <p>👉 <a href="{canonical_url}">Read the full guide with interactive tools</a></p>
    <p>🔧 <a href="{SITE_URL}/tools">Free 3D Printing Tools</a></p>
    '''

    full_content = intro + content_html + cta

    return {
        'title': post['title'],
        'content': full_content,
        'canonicalUrl': canonical_url,
        'tags': post.get('tags', [])[:5],  # Medium allows max 5 tags
        'publishStatus': 'draft'  # Or 'public' for auto-publish
    }

def post_to_medium(data):
    # Get user ID
    me_response = requests.get(
        'https://api.medium.com/v1/me',
        headers={'Authorization': f'Bearer {MEDIUM_TOKEN}'}
    )
    user_id = me_response.json()['data']['id']

    # Create post
    response = requests.post(
        f'https://api.medium.com/v1/users/{user_id}/posts',
        headers={
            'Authorization': f'Bearer {MEDIUM_TOKEN}',
            'Content-Type': 'application/json'
        },
        json=data
    )

    return response.json()

# Main execution
changed_posts = get_changed_posts()
for post in changed_posts:
    medium_data = convert_hugo_to_medium(post)
    result = post_to_medium(medium_data)
    print(f"Posted to Medium: {result['data']['url']}")
```

**Setup Requirements:**
1. Get Medium Integration Token: https://medium.com/me/settings/security
2. Add token to GitHub Secrets: `MEDIUM_TOKEN`
3. Configure workflow to trigger on new posts
4. Test with draft posts first

**Pros:**
- Fully automated on git push
- Maintains canonical URLs
- Consistent formatting
- Free (runs on GitHub Actions)

**Cons:**
- Requires Python scripting knowledge
- Medium API has rate limits (publish status may be "draft" only)
- Images need special handling (reupload to Medium or use absolute URLs)
- Less control over final formatting

**B. Zapier/Make.com (Paid, No-Code)**

**Workflow:**
1. RSS Trigger: New post on minimal3dp.com/blog/index.xml
2. Delay: 48 hours (for Google indexing)
3. Medium Action: Create draft post
4. Manual review and publish

**Pros:**
- No coding required
- Visual workflow builder
- Reliable

**Cons:**
- Costs $20-30/month
- Still requires manual review
- Limited customization

**C. IFTTT (Simple but Limited)**

- Free tier available
- RSS → Medium integration
- Very basic, no canonical URL support
- **Not recommended** (no SEO control)

#### Option 3: Hybrid Approach (Best of Both Worlds)

**Recommended Setup:**

1. **Automated Draft Creation:**
   - Use GitHub Actions to auto-create Medium drafts
   - Set `publishStatus: 'draft'`
   - Notification sent when draft ready

2. **Manual Review & Publish:**
   - Review formatting on Medium
   - Adjust images if needed
   - Add any Medium-specific enhancements
   - Publish manually

3. **Tracking:**
   - Add UTM parameters to all links:
     ```
     https://minimal3dp.com/tools?utm_source=medium&utm_medium=referral&utm_campaign=cross-post
     ```
   - Track Medium referral traffic in GA4

### Content Selection Strategy

**What to Cross-Post:**

✅ **High-Quality Tutorials:**
- Klipper calibration guides
- 3D printing troubleshooting
- How-to guides
- Best practices

✅ **Product Reviews:**
- Printer reviews
- Filament comparisons
- Tool comparisons

✅ **Long-Form Content (1,500+ words):**
- Medium algorithm favors depth
- Better chance of curation

✅ **Evergreen Content:**
- Content that stays relevant
- Not time-sensitive news

❌ **Don't Cross-Post:**
- Short posts (<800 words)
- Time-sensitive news
- Pure product listings
- Tool pages (keep exclusive to minimal3dp.com)

### Medium SEO Best Practices

1. **Canonical URLs Always:**
   - Every Medium post should have canonical URL pointing to minimal3dp.com
   - This gives minimal3dp.com the SEO credit

2. **Strategic Linking:**
   - Link to minimal3dp.com in intro and conclusion
   - Link to specific tools/calculators throughout
   - Use descriptive anchor text

3. **Image Optimization:**
   - High-quality images (Medium compresses heavily)
   - Add alt text in Hugo (copy to Medium)
   - Include diagrams and screenshots

4. **Engagement:**
   - Respond to Medium comments
   - Engage with readers
   - Higher engagement = more recommendations

5. **Publications:**
   - Submit best content to relevant Medium publications
   - Increases reach 5-10x
   - Maintains your byline and links

### Medium Monetization

**Medium Partner Program:**
- $5/month membership required to join
- Earn based on reading time from members
- Typical earnings: $5-50/article for niche content
- Top articles: $100-500/month

**Strategy:**
- Cross-posted content earns passive income
- Doesn't compete with Amazon Associates (both can coexist)
- Additional revenue stream from same content

### Success Metrics

**Track Monthly:**
- Medium views
- Medium reads (full read-through)
- Medium followers gained
- Clicks to minimal3dp.com from Medium (GA4 referral traffic)
- Medium Partner Program earnings (if enrolled)

**Goals:**

**Month 1:**
- 5-10 cross-posts
- 500-1,000 views
- 50-100 followers
- 50+ clicks to minimal3dp.com

**Month 3:**
- 20-30 cross-posts
- 3,000-5,000 views
- 300-500 followers
- 300+ clicks to minimal3dp.com

**Month 6:**
- 40-60 cross-posts
- 10,000-20,000 views
- 1,000+ followers
- 1,000+ clicks to minimal3dp.com
- $20-50/month Medium earnings (if enrolled)

### Recommended Workflow (Pragmatic)

**Week 1-2: Manual Testing**
1. Cross-post 3-5 existing Hugo posts manually
2. Set canonical URLs correctly
3. Track referral traffic in GA4
4. Measure engagement (views, reads, clicks)

**Week 3-4: Optimize Process**
1. Create templates for intro/CTA
2. Document workflow (screenshot tutorial)
3. Decide if automation worth effort

**Month 2+: Scale or Automate**
- If manual works well: Continue (15 min per post)
- If volume increases: Implement GitHub Actions automation
- If budget allows: Use Zapier for convenience

**Ideal Cadence:**
- Publish on minimal3dp.com first
- Cross-post to Medium 48 hours later
- 1-2 cross-posts per week
- Focus on best-performing Hugo content



Perfect for <use cases>!
```

**Video Series Ideas:**

1. **"Klipper Calibration" Series** - One video per calibration type (flow, pressure advance, input shaping, etc.)
2. **"Tool Tutorial" Series** - Deep dive on each minimal3dp.com tool (FDM calculator, shrinkage calculator)
3. **"Product Review" Series** - Honest reviews with affiliate links (printers, filaments, accessories)
4. **"Common Problems" Series** - Troubleshooting guides (under-extrusion, warping, stringing)
5. **"Project Showcase" Series** - Using tools in real projects (functional prints, mods, builds)
6. **"Comparison" Series** - Compare materials, slicers, printers (PLA vs PETG, Ender 3 vs Prusa)

### YouTube → Blog Cross-Promotion

- **Every video should link to a blog post** on minimal3dp.com
- **Every blog post should embed the video** using `{{< youtube >}}` shortcode
- Pin comment with minimal3dp.com link on every video
- Add YouTube cards at 30%, 60%, 90% timestamps
- End screen: Subscribe button + minimal3dp.com link
- Video description: Always include minimal3dp.com as primary link

### Content Production Schedule

**Goal:** 1 video per week = 4 videos/month

**Weekly Workflow:**
1. **Monday:** Plan video topic (align with blog post)
2. **Tuesday-Wednesday:** Film video
3. **Thursday:** Edit video
4. **Friday:** Write blog post (with video embed)
5. **Saturday:** Publish video + blog post together
6. **Sunday:** Promote on socials, Discord, Twitter

---

## 🔄 Cross-Linking Strategy (Hugo Site-Focused)

### Main Site (`minimal3dp.com`) - Internal Linking

**1. Use Hugo `related-posts.html` Partial** (see RECOMMENDATIONS.md):
```markdown
<!-- At end of every blog post -->
{{< related-posts >}}
```
- Auto-generates related content based on tags/categories
- Improves internal linking structure
- Increases time on site

**2. Manual Internal Links in Content:**
```markdown
For more details, see our [Flow Calibration Guide](/klipper-calibration/flow-calibration).

Looking for a complete solution? Try our [FDM Cost Calculator](/tools/m3dp-fdm-cost-calculator).

Check out our [3D Printer Reviews](/projects/3d-printers/reviews) for recommendations.
```

**3. Tools Page** (`/tools/_index.md`):
```markdown
---
title: "Free 3D Printing Tools"
---

## Calculators

- [FDM Cost Calculator](/tools/m3dp-fdm-cost-calculator) - Calculate filament cost, time, energy
- [Shrinkage Calculator](/tools/m3dp-shrinkage-calculator) - Account for material shrinkage

## Klipper Calibration

- [Flow Calibration](/klipper-calibration/flow-calibration)
- [Pressure Advance](/klipper-calibration/pressure-advance)
- [Input Shaping](/klipper-calibration/input-shaping)
- [All Guides](/klipper-calibration)
```

**4. Navigation Menu** (configured in `hugo.toml`):
```toml
[[menu.main]]
  name = "Blog"
  url = "/blog"
  weight = 10

[[menu.main]]
  name = "Tools"
  url = "/tools"
  weight = 20

[[menu.main]]
  name = "Klipper Calibration"
  url = "/klipper-calibration"
  weight = 30

[[menu.main]]
  name = "Projects"
  url = "/projects"
  weight = 40

[[menu.main]]
  name = "YouTube"
  url = "https://youtube.com/channel/UCM_8Mv-0S1LnnJpRJLjahaw"
  weight = 50
```

### Standalone Tools (if applicable) - External Linking

**Standard Header Navigation:**
```html
<nav class="main-nav">
  <a href="https://minimal3dp.com" class="logo">minimal3dp</a>

  <div class="nav-links">
    <a href="https://minimal3dp.com/tools">All Tools</a>
    <a href="https://minimal3dp.com/blog">Blog</a>
    <a href="https://youtube.com/channel/UCM_8Mv-0S1LnnJpRJLjahaw">YouTube</a>
  </div>
</nav>
```

**Standard Footer Links:**
```html
<footer>
  <div class="footer-content">
    <div class="footer-section">
      <h4>minimal3dp Tools</h4>
      <ul>
        <li><a href="https://minimal3dp.com/tools/m3dp-fdm-cost-calculator">FDM Calculator</a></li>
        <li><a href="https://minimal3dp.com/klipper-calibration">Klipper Guides</a></li>
        <li><a href="https://minimal3dp.com/tools">All Tools</a></li>
      </ul>
    </div>

    <div class="footer-section">
      <h4>Resources</h4>
      <ul>
        <li><a href="https://youtube.com/channel/UCM_8Mv-0S1LnnJpRJLjahaw">YouTube Channel</a></li>
        <li><a href="https://minimal3dp.com/blog">Blog</a></li>
        <li><a href="https://minimal3dp.com/projects">Projects</a></li>
      </ul>
    </div>

    <div class="footer-section">
      <h4>Connect</h4>
      <ul>
        <li><a href="https://github.com/minimal3dp">GitHub</a></li>
        <li><a href="https://ko-fi.com/J3J41MTJUB">Support Us</a></li>
      </ul>
    </div>
  </div>

  <div class="footer-disclaimer">
    <p>As an Amazon Associate, we earn from qualifying purchases.</p>
    <p>&copy; 2025 minimal3dp. All rights reserved.</p>
  </div>
</footer>
```

### Related Tools Section (Within Blog Posts)

**Use Hugo Shortcode or Markdown:**
<section class="related-tools">
  <h3>You Might Also Like</h3>

  <div class="tool-cards">
    <a href="https://filament.minimal3dp.com">
      <strong>Filament Database</strong>
      <span>Compare 100+ filament specs</span>
    </a>

    <a href="https://calc.minimal3dp.com">
      <strong>Print Calculator</strong>
      <span>Estimate time, cost, and material</span>
    </a>
  </div>
</section>
```

---

## 📊 Analytics & Monitoring (Hugo Site + YouTube)

### Weekly Review (15 minutes)

**Google Analytics 4 (minimal3dp.com):**
- [ ] Check total users, sessions, pageviews (Goal: +10-20% weekly in first 3 months)
- [ ] Review top pages (Which content is resonating?)
- [ ] Check affiliate click events (`affiliate_click`, `product_view`)
- [ ] Identify traffic sources:
  - Organic search (goal: 50-60%)
  - YouTube referrals (goal: 20-30%)
  - Social (Discord, Twitter)
  - Direct
- [ ] Monitor bounce rate (goal: <60%, Hugo sites typically 40-50%)
- [ ] Check average session duration (goal: >2 min, Hugo sites often 3-4 min)
- [ ] Review custom events:
  - Video plays (`video_play`)
  - Tool interactions (`calculator_use`, `form_submit`)
  - Newsletter signups (`email_signup`)

**Google Search Console (minimal3dp.com):**
- [ ] Total impressions (trending up? Goal: +20-30% monthly)
- [ ] Total clicks (trending up? Goal: +25-35% monthly)
- [ ] Average CTR (goal: 5%+, blog posts often 6-8%)
- [ ] Average position (goal: improving weekly)
- [ ] Top queries:
  - Ranking for target keywords?
  - Any unexpected keywords? (Create content around them)
- [ ] Top pages:
  - Which pages get most impressions?
  - Which need optimization (high impressions, low clicks)?
- [ ] Coverage issues:
  - Any indexing errors?
  - All pages indexed?
- [ ] Core Web Vitals:
  - All metrics green? (Hugo typically scores 95-100)

**YouTube Analytics:**
- [ ] Views this week (goal: +10-15% weekly)
- [ ] Watch time (goal: >50% average view duration)
- [ ] Subscribers gained (goal: +50-100/month)
- [ ] Top videos (which topics resonate?)
- [ ] Traffic sources:
  - YouTube search
  - Suggested videos
  - External (minimal3dp.com embeds)
- [ ] Click-through rate on cards/end screens
- [ ] Clicks to minimal3dp.com (goal: 5-10% of views)

**Amazon Associates:**
- [ ] Total clicks (goal: 50-100/week initially, 200+/week at scale)
- [ ] Conversion rate (orders / clicks) (goal: 3-6%)
- [ ] Earnings this week (goal: $20-50/week at scale)
- [ ] Best-performing products (double down on winners)
- [ ] Which pages drive most clicks? (create similar content)

### Monthly Review (30 minutes)

**Performance Analysis:**
- [ ] Compare to last month:
  - Users: +X% (goal: +20-40% in growth phase)
  - Sessions: +X%
  - Pageviews: +X%
  - Affiliate revenue: +X% (goal: +30-50% monthly)
- [ ] Identify growth trends:
  - Which content types perform best? (tutorials, reviews, calculators)
  - Which traffic sources growing fastest?
  - Which keywords driving most traffic?
- [ ] Top-performing content:
  - Top 10 pages by traffic
  - Top 5 pages by conversions (affiliate clicks)
  - Top 3 YouTube videos by views
- [ ] Best traffic sources:
  - Organic search %
  - YouTube referrals %
  - Social/Discord %
- [ ] Conversion funnel analysis:
  - Homepage → Blog → Affiliate click
  - YouTube → Blog → Tool → Affiliate click
  - Search → Tool → Affiliate click

**SEO Progress:**
- [ ] Keyword rankings:
  - Top 10 keywords: Improved or declined?
  - How many keywords in positions 1-3? (goal: 5+ by month 3)
  - How many keywords in positions 1-10? (goal: 20+ by month 6)
- [ ] New keywords ranking:
  - Any unexpected keywords?
  - Create content to capitalize on accidental wins
- [ ] Backlinks gained:
  - Check Google Search Console → Links
  - Quality of linking domains (DR 40+)
  - Anchor text diversity
- [ ] Domain authority:
  - Use Moz or Ahrefs free tools
  - Goal: DR 20+ by month 6, DR 40+ by month 12

**Content Optimization:**
- [ ] High bounce rate pages (>70%):
  - Improve content quality
  - Add internal links
  - Add video embeds
  - Add affiliate products
- [ ] Low CTR pages (<3% in GSC):
  - Rewrite title (add primary keyword, number, year)
  - Rewrite meta description (add CTA, benefits)
- [ ] High impressions, low clicks:
  - Page is ranking but not compelling
  - Update title/description to improve CTR
- [ ] Low conversion pages:
  - Add more affiliate products
  - Improve product recommendations
  - Add comparison tables
- [ ] Best-performing pages:
  - Create similar content (if it works, do more)
  - Update with fresh info (keep it current)
  - Add YouTube video embed if missing

**Competitive Analysis:**
- [ ] Google your primary keywords:
  - Where do you rank? (Position X)
  - Who ranks above you?
- [ ] Check top 3 competitors:
  - What topics do they cover?
  - What's their content quality?
  - How many backlinks do they have?
  - What can you do better?
- [ ] Identify content gaps:
  - Topics competitors cover that you don't
  - Questions in "People Also Ask" you haven't answered
  - Keywords competitors rank for that you don't
  - Create content to fill these gaps

### Key Performance Indicators (KPIs)

**Traffic Metrics (minimal3dp.com + YouTube):**
- Monthly unique users (website)
- Monthly pageviews (website)
- YouTube views
- YouTube watch time
- Average session duration (website: goal 2-4 min)
- Pages per session (goal: 2.5+)
- Bounce rate (goal: <60%)

**SEO Metrics (minimal3dp.com):**
- Keyword rankings (track top 10 keywords)
- Organic search traffic % (goal: 50-60%)
- Impressions in Google Search (goal: +20-30% monthly)
- Click-through rate (CTR) (goal: 5%+)
- Backlinks (goal: +10-20/month)
- Domain rating (goal: DR 40+ by month 12)

**Revenue Metrics (Amazon Associates):**
- Affiliate clicks (goal: 200+/week at scale)
- Affiliate conversion rate (goal: 3-6%)
- Monthly earnings (goal: $200-400/month by month 12)
- Revenue per 1,000 visitors (goal: $10-20)
- Best-performing products (track top 10)
- Revenue per 1000 visitors (RPM)

**Engagement Metrics:**
- Tool usage rate (% of visitors who use tool)
- Return visitor rate
- Social shares
- YouTube referral traffic

---

## 🚀 Launch Checklist

Use this checklist for **every new app launch**.

### Pre-Launch (1 week before)

- [ ] **Feature Complete:** Core functionality works flawlessly
- [ ] **Mobile Tested:** Responsive on phone, tablet, desktop
- [ ] **Browser Tested:** Chrome, Safari, Firefox, Edge
- [ ] **SEO Complete:** All meta tags, Schema.org, OG image
- [ ] **Analytics Installed:** GA4 tracking verified
- [ ] **Affiliate Links Ready:** Products selected, links tested
- [ ] **Cross-Links Added:** Header, footer navigation
- [ ] **Performance Optimized:** Images compressed, fast loading
- [ ] **Vercel Deployed:** Custom domain configured, HTTPS working

### Launch Day

- [ ] **Deploy to Production:** Final commit, Vercel auto-deploys
- [ ] **Submit to Google Search Console:** Sitemap submitted
- [ ] **Update Main Site:** Add tool to portfolio page
- [ ] **Update YouTube:** Channel description, links
- [ ] **Social Media Announcement:**
  - Twitter: "Launching <Tool Name>! Free 3D printing tool..."
  - Reddit: r/3Dprinting, r/BambuLab (helpful post, not spammy)
  - Discord: OrcaSlicer, Bambu Lab servers
- [ ] **Update Video Descriptions:** Add tool link to relevant videos
- [ ] **Pin Comment:** Pin comment with tool link on popular videos
- [ ] **Verify GA4 Tracking:** Check Realtime reports

### Post-Launch (First Week)

- [ ] **Monitor Daily:** Check for errors, user feedback
- [ ] **Fix Bugs:** Address any issues quickly
- [ ] **Gather Feedback:** Reddit comments, YouTube comments, Discord
- [ ] **Iterate:** Small improvements based on feedback
- [ ] **Create Content:** Blog post, video tutorial (if planned)
- [ ] **Monitor Rankings:** Check Google Search Console daily
- [ ] **Engage Community:** Respond to comments, questions

### First Month

- [ ] **Analyze Data:** GA4 reports, Search Console, Amazon Associates
- [ ] **Optimize Content:** Improve based on user behavior
- [ ] **Expand Features:** Add nice-to-haves based on feedback
- [ ] **Create More Content:** Additional blog posts, videos
- [ ] **Build Backlinks:** Reddit, forums, guest posts
- [ ] **Plan Next App:** Start developing next tool in portfolio

---

## 🎨 Branding Guidelines

### Visual Identity

**Logo/Brand:**
- Brand name: `minimal3dp`
- Tagline: "Free 3D Printing Tools" or "Tools for Makers"
- Design style: Clean, minimal, technical
- Color palette: Blue/teal (tech), white/gray (minimal)

**Typography:**
- Headings: Bold, sans-serif (Inter, Roboto, Tailwind default)
- Body: Regular, readable (system fonts)
- Code: Monospace (for technical content)

**Color Scheme:**
- Primary: Blue (#3B82F6) - action, links
- Secondary: Teal (#14B8A6) - accents
- Background: Dark gray (#1F2937) or white
- Text: Light gray (#E5E7EB) on dark, dark on light
- Success: Green (#10B981)
- Warning: Yellow (#F59E0B)
- Error: Red (#EF4444)

### Voice & Tone

**Brand Voice:**
- Helpful, not condescending
- Technical but accessible
- Enthusiastic about 3D printing
- Honest about trade-offs
- Community-focused

**Writing Style:**
- Short sentences (10-15 words average)
- Active voice: "Select your material" not "Material should be selected"
- Second person: "You can..." not "Users can..."
- Conversational but professional
- Use examples, not just theory

**Examples:**

✅ **Good:**
> "Select your material and print goal. We'll recommend the perfect settings for your project."

❌ **Bad:**
> "The user should proceed to select the material type and desired optimization parameters to receive algorithmically-determined configuration values."

### User Experience Principles

1. **Clarity:** Make it obvious what the tool does
2. **Simplicity:** Minimal clicks to get value
3. **Speed:** Fast loading, instant results
4. **Mobile-First:** Design for phones, enhance for desktop
5. **Accessibility:** Readable text, good contrast, keyboard navigation
6. **Consistency:** Same patterns across all apps
7. **Helpful:** Explain WHY, not just WHAT
8. **Trust:** Disclose affiliates, be honest about limitations

---

## 🛠️ Development Best Practices

### Code Quality

- [ ] **DRY (Don't Repeat Yourself):** Extract shared components
- [ ] **Comments:** Explain WHY, not WHAT
- [ ] **Naming:** Descriptive variable/function names
- [ ] **Error Handling:** Graceful failures, user-friendly messages
- [ ] **Validation:** Client-side and server-side (if applicable)
- [ ] **Security:** Sanitize inputs, use HTTPS, environment variables for secrets

### Performance

- [ ] **Image Optimization:** Compress, lazy load, WebP format
- [ ] **Code Splitting:** Load only what's needed
- [ ] **Caching:** Browser caching, CDN, API response caching
- [ ] **Minification:** Minify CSS/JS for production
- [ ] **Lazy Loading:** Defer non-critical resources

### Testing

- [ ] **Manual Testing:** Click every button, test every input
- [ ] **Mobile Testing:** Real devices, not just browser DevTools
- [ ] **Browser Testing:** Chrome, Safari, Firefox, Edge
- [ ] **Error Scenarios:** What happens if API fails? No internet?
- [ ] **Accessibility Testing:** Screen reader, keyboard navigation

### Git Workflow

**Branch Strategy:**
- `main`: Production-ready code
- `develop`: Development branch
- `feature/<name>`: New features
- `bugfix/<name>`: Bug fixes

**Commit Messages:**
```
<type>: <short summary>

<longer description if needed>

Examples:
feat: Add material search filter
fix: Resolve mobile navigation bug
docs: Update deployment guide
style: Improve button hover states
```

**Deployment:**
- Push to `main` → Auto-deploy to Vercel
- Preview deployments for feature branches
- Test on preview URL before merging

---

## 📈 Growth Strategy

### Months 1-3: Foundation

**Focus:** Launch, SEO foundation, initial traffic

- [ ] Deploy first 1-2 apps
- [ ] Optimize for target keywords
- [ ] Submit to Google Search Console
- [ ] Create 5-10 YouTube videos
- [ ] Build initial backlinks (Reddit, forums)
- [ ] Monitor analytics weekly
- [ ] Iterate based on feedback

**Goals:**
- 1,000+ monthly visitors per app
- Page 2-3 ranking for primary keyword
- $40-60/month revenue per app

### Months 4-6: Growth

**Focus:** More apps, more content, better rankings

- [ ] Deploy 2-3 additional apps
- [ ] Create material landing pages
- [ ] Publish 10-20 YouTube videos
- [ ] Guest post on 3D printing blogs
- [ ] Expand affiliate products
- [ ] Optimize conversion funnels

**Goals:**
- 5,000+ monthly visitors per app
- Page 1 (top 10) ranking for primary keywords
- $80-120/month revenue per app

### Months 7-12: Scale

**Focus:** Dominate keywords, expand portfolio, maximize revenue

- [ ] Deploy 5+ apps total
- [ ] Rank #1-3 for primary keywords
- [ ] 20,000+ monthly visitors per app
- [ ] Dynamic PA-API integration
- [ ] Premium features (optional)
- [ ] Partnerships with filament brands

**Goals:**
- 20,000+ monthly visitors per app
- Top 3 ranking for multiple keywords
- $200-400/month revenue per app
- $1,000-2,000/month total revenue

### Year 2+: Monetization Expansion

**Additional Revenue Streams:**
- Sponsored content (filament brand partnerships)
- Premium features ($5-10/month subscriptions)
- Consulting/coaching services
- Merchandise (branded tools, accessories)
- Affiliate expansion (printers, accessories, not just filament)

---

## 📋 Case Study: OrcaSlicer Expert Assistant

### Pre-Launch Improvements (November 2025)

**Context:** Preparing for YouTube launch video, identified 4 critical UI/UX improvements with SEO focus.

#### 1. Featured YouTube Badge
**Problem:** No visual connection between tool and YouTube channel
**Solution:** Added prominent red badge at top of page
**Implementation:**
- Positioned after Ko-fi button for high visibility
- Red color (#DC2626) for brand recognition
- Link includes `?sub_confirmation=1` for direct subscribe
- GA4 tracking: `youtube_featured_click` event

**Impact:** Drives YouTube traffic, builds credibility, cross-promotes content

#### 2. How to Use Section
**Problem:** First-time users had no guidance on tool functionality
**Solution:** Added collapsible "How to Use" section with 3-step instructions
**Implementation:**
- Collapsible design (doesn't clutter interface)
- SEO-optimized content with target keywords
- 3-step process: Select Material → Adjust Priorities → Get Recommendations
- Pro tips section for advanced users
- Link to companion YouTube video
- GA4 tracking: `how_to_use_expanded` event

**Impact:** Reduces bounce rate, improves user experience, adds SEO content

#### 3. Enhanced Generate Button
**Problem:** No feedback during generation, no validation, generic text
**Solution:** Comprehensive button enhancement
**Implementation:**
- Updated text: "🎯 Get Expert Recommendations" (more descriptive)
- Material validation with alert if no material selected
- Loading state: "⏳ Generating Recommendations..." while processing
- Button reset after recommendations complete
- Auto-scroll to results after generation
- GA4 tracking: `generate_recommendations` event with material/slider data

**Impact:** Better UX, prevents errors, tracks user behavior

#### 4. Reset Sliders Button
**Problem:** Users had to manually adjust all 4 sliders back to default
**Solution:** One-click reset button
**Implementation:**
- Secondary button styling (gray, smaller)
- Positioned below main generate button
- Resets all sliders to 50% (balanced)
- Updates all percentage displays
- Hides strength type selector
- Visual feedback: "✓ Reset Complete" for 1.5 seconds
- GA4 tracking: `sliders_reset` event

**Impact:** Improves experimentation, reduces friction

#### 5. Footer CTA
**Problem:** No engagement opportunity at bottom of page
**Solution:** Comprehensive footer with multiple CTAs
**Implementation:**
- YouTube subscribe CTA with 40-video social proof
- Ko-fi support link
- Version info and copyright
- SEO keywords embedded
- GA4 tracking: `footer_youtube_subscribe` and `footer_kofi_support` events

**Impact:** Captures bottom-of-page engagement, provides multiple conversion paths

### Key Learnings

1. **User Guidance is Critical:** Even simple tools need instructions
2. **Loading States Matter:** Users need feedback during processing
3. **Validation Prevents Frustration:** Check inputs before processing
4. **Visual Feedback Builds Trust:** Show users their actions succeeded
5. **Cross-Promotion Works:** Multiple touchpoints to YouTube/support
6. **Track Everything:** GA4 events provide valuable behavior insights
7. **SEO in UI:** Every new element is an opportunity for keywords

### Before/After Metrics (To Be Measured)

**Expected Improvements:**
- Bounce rate: 65% → 45% (How to Use section reduces confusion)
- Average session: 1:30 → 2:30 (better engagement)
- Generate button clicks: +20% (clearer CTA, better guidance)
- YouTube traffic: +30% (multiple promotion points)
- Affiliate clicks: +15% (longer sessions, more engaged users)

---

## 🆘 Common Issues & Solutions

### DNS/Deployment Issues

**Problem:** DNS not propagating
- **Solution:** Wait 15 minutes for CNAME, 24 hours for nameservers. Check https://www.whatsmydns.net/

**Problem:** HTTPS not working
- **Solution:** Vercel auto-provisions SSL, wait 5-10 minutes after DNS is verified

**Problem:** Site showing 404
- **Solution:** Check that `index.html` exists in root (or rename your HTML file)

### SEO Issues

**Problem:** Not appearing in Google after 1 week
- **Solution:** Submit sitemap in Google Search Console, verify indexing

**Problem:** Low CTR (<2%)
- **Solution:** Improve meta description, make it compelling and keyword-rich

**Problem:** High bounce rate (>70%)
- **Solution:** Improve page speed, make value proposition clearer, improve UX

### Analytics Issues

**Problem:** GA4 not tracking
- **Solution:** Check Measurement ID, verify script in `<head>`, test in Realtime view

**Problem:** Affiliate clicks not tracked
- **Solution:** Check event listener code, verify `gtag` function exists, test manually

### Revenue Issues

**Problem:** Clicks but no conversions
- **Solution:** Review product selection (wrong products?), check link format, verify tag `mwf064-20`

**Problem:** Low click-through rate on affiliate links
- **Solution:** Improve product presentation, add more context (WHY recommend), better placement

---

## 📚 Resources & References

### Vercel Documentation
- **Getting Started:** https://vercel.com/docs
- **Custom Domains:** https://vercel.com/docs/concepts/projects/domains
- **Environment Variables:** https://vercel.com/docs/concepts/projects/environment-variables

### SEO Resources
- **Google Search Console:** https://search.google.com/search-console
- **Google Keyword Planner:** https://ads.google.com/home/tools/keyword-planner/
- **Ubersuggest (Free):** https://neilpatel.com/ubersuggest/
- **Schema.org Documentation:** https://schema.org/

### Amazon Associates
- **Associates Central:** https://affiliate-program.amazon.com
- **Program Policies:** https://affiliate-program.amazon.com/help/operating/agreement
- **Product Linking:** https://affiliate-program.amazon.com/help/node/topic/GP38PJ6EUR6PFBEC

### Analytics
- **Google Analytics 4:** https://analytics.google.com
- **GA4 Documentation:** https://support.google.com/analytics/answer/9304153

### YouTube
- **YouTube Studio:** https://studio.youtube.com
- **YouTube SEO Guide:** https://backlinko.com/youtube-seo

### Development Tools
- **Tailwind CSS:** https://tailwindcss.com
- **Canva (Free):** https://canva.com
- **Figma (Free):** https://figma.com

---

## 🎯 AI Agent Instructions

**When using this guide to help develop a new minimal3dp.com application:**

1. **Read this entire document first** to understand the architecture, strategy, and standards.

2. **Follow the checklist sequentially:**
   - Phase 1: Deployment
   - Phase 2: SEO
   - Phase 3: Branding
   - Phase 4: Analytics
   - Phase 5: YouTube

3. **Customize for the specific app:**
   - Research target keywords for this app's niche
   - Identify appropriate affiliate products
   - Create app-specific content (FAQ, descriptions)

4. **Maintain consistency:**
   - Use same affiliate tag: `mwf064-20`
   - Follow subdomain naming convention
   - Use standard header/footer templates
   - Match branding guidelines

5. **Verify integrations:**
   - GA4 Measurement ID is correct
   - Affiliate links include tag
   - Cross-links point to correct URLs
   - DNS records are accurate

6. **Test thoroughly:**
   - Mobile responsiveness
   - All interactive features
   - Analytics tracking (use Realtime view)
   - Affiliate link tracking

7. **Document app-specific details:**
   - Create app README with specific features
   - Update TODO.md with app roadmap
   - Note any deviations from standard template

8. **Launch following checklist:**
   - Pre-launch verification
   - Launch day tasks
   - Post-launch monitoring

**Key Principle:** This guide is a starting point. Adapt as needed, but maintain consistency across the minimal3dp.com portfolio.

---

## 📝 Version History

- **v1.1 (2025-11-12):** Added Case Study section documenting OrcaSlicer Assistant pre-launch improvements (Featured YouTube badge, How to Use section, Enhanced Generate button, Reset Sliders button, Footer CTA)
- **v1.0 (2025-11-12):** Initial guide created based on OrcaSlicer Assistant deployment experience

---

**This is a living document.** Update it as you learn best practices, encounter new scenarios, or optimize the workflow.

**Questions?** Review the Resources section above or consult the specific app's documentation (README.md, TODO.md, SEO_STRATEGY.md).

🚀 **Happy Building!**
