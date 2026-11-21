# -*- coding: utf-8 -*-
"""Static build for the Asiimwe Derick personal-brand platform.
Run:  python3 build.py
Keeps one design system, one header/footer, one content model.
"""
import json, html, os

BASE = "https://asiimwe3.github.io/derick-personal-website/"
EMAIL = "derickasiimwe849@gmail.com"
WA = "https://wa.me/256762306675"
YEAR = 2026

NAV = [
    ("about.html", "About"),
    ("ventures.html", "Ventures"),
    ("projects.html", "Projects"),
    ("writing.html", "Writing"),
    ("vision.html", "Vision"),
    ("contact.html", "Contact"),
]
MORE = [
    ("journey.html", "Journey &amp; experience"),
    ("skills.html", "Skills &amp; CV"),
    ("impact.html", "Impact &amp; leadership"),
    ("speaking.html", "Speaking &amp; media"),
    ("gallery.html", "Gallery &amp; life"),
    ("services.html", "Services &amp; collaboration"),
    ("investors.html", "For investors"),
    ("mediakit.html", "Media kit &amp; archive"),
    ("assistant.html", "Ask Derick AI"),
    ("sitemap.html", "Site map"),
]

def head(slug, title, desc, extra_ld=None, og_type="website"):
    url = BASE + ("" if slug == "index.html" else slug)
    ld = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": "Asiimwe Derick",
        "alternateName": "Derick",
        "jobTitle": "Social entrepreneur, Founder of DeryCode Technologies, CEO of Sageco Evergreen",
        "url": BASE,
        "image": BASE + "assets/hoodie-laptop.webp",
        "email": EMAIL,
        "address": {"@type": "PostalAddress", "addressLocality": "Kyenjojo", "addressCountry": "UG"},
        "sameAs": ["https://github.com/asiimwe3", "https://derycode.online"],
        "worksFor": [
            {"@type": "Organization", "name": "DeryCode Technologies", "url": "https://derycode.online"},
            {"@type": "Organization", "name": "Sageco Evergreen", "url": "https://sageco-evergreen.vercel.app/"},
        ],
        "knowsAbout": ["social entrepreneurship", "software development", "real estate technology", "impact investing", "offline-first software"],
        "birthDate": "2006-01-09",
        "birthPlace": {"@type": "Place", "name": "Kyenjojo, Uganda"},
    }
    blocks = [json.dumps(ld)]
    if extra_ld:
        blocks += [json.dumps(x) for x in extra_ld]
    ld_html = "".join('<script type="application/ld+json">%s</script>' % b for b in blocks)
    return f'''<!doctype html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#ffffff">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="Asiimwe Derick">
<meta name="robots" content="index,follow,max-image-preview:large">
<link rel="canonical" href="{url}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Asiimwe Derick">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}assets/hoodie-laptop.webp">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<link rel="icon" href="assets/hoodie-laptop-sq.webp" type="image/webp">
<link rel="apple-touch-icon" href="assets/hoodie-laptop-sq.webp">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css?v=10">
<link rel="stylesheet" href="assets/site.css?v=7">
{ld_html}
<script src="assets/site.js?v=4" defer></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="header">
 <a class="brand" href="index.html"><img src="assets/hoodie-laptop-sq.webp" alt="Asiimwe Derick" class="brand-pic" width="38" height="38"> Derick<span>.</span></a>
 <nav id="primaryNav">
  {"".join(f'<a href="{u}">{t}</a>' for u,t in NAV)}
  <div class="nav-more"><button type="button" aria-expanded="false">More ▾</button>
   <div class="drop">{"".join(f'<a href="{u}">{t}</a>' for u,t in MORE)}</div>
  </div>
  <a class="nav-cta" href="contact.html">Say hello</a>
 </nav>
 <div class="tools">
  <button class="icon-btn" data-search-open type="button" aria-label="Search this site"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg></button>
  <button class="icon-btn" id="themeBtn" type="button" aria-label="Switch colour theme"><svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg></button>
  <button class="menu" type="button" aria-label="Toggle navigation" aria-expanded="false"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg></button>
 </div>
</header>

<div class="search-wrap" id="searchWrap" role="dialog" aria-modal="true" aria-label="Search">
 <div class="searchbox">
  <input id="searchInput" type="search" placeholder="Search pages, projects, writing, sections…" aria-label="Search">
  <p class="hint">Press <b>/</b> to open search anywhere. Esc closes.</p>
  <div id="searchResults"></div>
 </div>
</div>

<main id="main">
'''

def foot():
    quick = [("about.html","About"),("journey.html","Journey"),("ventures.html","Ventures"),("projects.html","Projects"),("skills.html","Skills &amp; CV")]
    work = [("writing.html","Writing"),("vision.html","Vision"),("impact.html","Impact"),("speaking.html","Speaking"),("gallery.html","Gallery")]
    more = [("investors.html","Investors"),("services.html","Services"),("mediakit.html","Media kit"),("assistant.html","Ask Derick AI"),("sitemap.html","Site map")]
    return f'''</main>
<footer class="foot">
 <div class="wrap foot-grid">
  <div>
   <a class="brand" href="index.html" style="margin-bottom:14px"><img src="assets/hoodie-laptop-sq.webp" alt="Asiimwe Derick" class="brand-pic" width="38" height="38"> Derick<span>.</span></a>
   <p>Asiimwe Derick, social entrepreneur from Kyenjojo, Uganda. Founder of DeryCode Technologies and CEO of Sageco Evergreen. Building for people, at scale.</p>
   <p><a href="mailto:{EMAIL}">{EMAIL}</a><br><a href="{WA}" target="_blank" rel="noopener">WhatsApp 0762 306 675</a></p>
  </div>
  <div><h4>Profile</h4>{"".join(f'<a href="{u}">{t}</a>' for u,t in quick)}</div>
  <div><h4>Work</h4>{"".join(f'<a href="{u}">{t}</a>' for u,t in work)}</div>
  <div><h4>More</h4>{"".join(f'<a href="{u}">{t}</a>' for u,t in more)}
   <a href="privacy.html">Privacy</a><a href="terms.html">Terms</a><a href="disclaimer.html">Disclaimer</a></div>
 </div>
 <div class="wrap foot-btm">
  <span>© <span id="year">{YEAR}</span> Asiimwe Derick. All rights reserved.</span>
  <span>Built by <a href="https://derycode.online" target="_blank" rel="noopener" style="display:inline">DeryCode Technologies</a> · <a href="{WA}" target="_blank" rel="noopener" style="display:inline">Need a site like this? WhatsApp 0762 306 675</a></span>
 </div>
</footer>
</body>
</html>
'''

def page_head_block(slug_label, crumb, kicker, h1, lead, toc=None):
    t = f'<div class="wrap crumbs"><a href="index.html">Home</a><span>/</span>{crumb}</div>' if crumb else ''
    toc_html = ''
    if toc:
        toc_html = '<div class="toc">' + "".join(f'<a href="#{i}">{l}</a>' for i,l in toc) + '</div>'
    return f'''{t}
<section class="page-head wrap">
 <p class="eyebrow"><i></i> {kicker}</p>
 <h1>{h1}</h1>
 <p class="lead">{lead}</p>
 {toc_html}
</section>
'''

def section(sid, kicker, title, body, band=False, wrap=True):
    cls = "section band" if band else "section"
    inner_open = '<div class="wrap">' if band else ''
    inner_close = '</div>' if band else ''
    k = f'<p class="kicker">{kicker}</p>' if kicker else ''
    t = f'<h2>{title}</h2>' if title else ''
    return f'''<section class="{cls}" id="{sid}">
 {inner_open}{k}
 {t}
 {body}
 {inner_close}
</section>
'''

def cards(items, wide_first=False):
    out = []
    for i,(tag,title,desc,link,label) in enumerate(items):
        cls = "card wide" if (wide_first and i==0) else "card"
        tag_h = f'<span class="tag">{tag}</span>' if tag else ''
        link_h = f'<a class="more" href="{link}">{label or "Read more"} →</a>' if link else ''
        if link and not label:
            out.append(f'<a class="{cls}" href="{link}">{tag_h}<h3>{title}</h3><p>{desc}</p></a>')
        else:
            out.append(f'<div class="{cls}">{tag_h}<h3>{title}</h3><p>{desc}</p>{link_h}</div>')
    return '<div class="cards">' + "".join(out) + '</div>'

def stats(items):
    return '<div class="stat-row">' + "".join(f'<div class="stat-box"><b>{n}</b><span>{l}</span></div>' for n,l in items) + '</div>'

def timeline(items):
    return '<div class="timeline">' + "".join(
        f'<div class="tl-item"><b class="when">{w}</b><h3>{t}</h3><p>{d}</p></div>' for w,t,d in items) + '</div>'

def prose(paras):
    return '<div class="prose">' + "".join(paras) + '</div>'

def edit(title, note):
    return f'<div class="edit"><b>Editable placeholder</b><p><strong>{title}.</strong> {note}</p></div>'

def acc(items):
    return "".join(f'<details class="acc"><summary>{q}</summary><p>{a}</p></details>' for q,a in items)

def chips(items):
    return "".join(f'<span class="chip">{i}</span>' for i in items)

def cta(title, text, primary=("contact.html","Start a conversation"), secondary=None):
    sec = f'<a class="btn ghost" href="{secondary[0]}">{secondary[1]}</a>' if secondary else ''
    return f'''<div class="cta-band">
 <h2>{title}</h2><p>{text}</p>
 <div class="btn-row"><a class="btn" href="{primary[0]}">{primary[1]}</a>{sec}</div>
</div>'''

PAGES = []   # (slug, title, desc, keys, html_body)

def add(slug, title, desc, keys, body):
    PAGES.append((slug, title, desc, keys, body))

# ============================== HOME ==============================
home = page_head_block("Home", "", "KYENJOJO, UGANDA",
  "I'm Derick.<br><em>I build for people.</em>",
  "A young social entrepreneur born in Fort Portal, western Uganda. Founder of DeryCode Technologies, CEO of Sageco Evergreen, and building more ventures than one page can hold. Many businesses, one purpose: to change people's lives and turn that change into mass social impact.")
home += f'''
<section class="section wrap" style="padding-top:10px">
 <div class="two">
  <div>
   <p class="lead">Born 9 January 2006, in Fort Portal. Twenty years old, still finishing school. Running several ventures in the hours school leaves me, and telling you that plainly because it is the constraint I actually build under.</p>
   <p class="roles" style="margin-top:18px">FOUNDER · DERYCODE TECHNOLOGIES <span>|</span> CEO · SAGECO EVERGREEN <span>|</span> AND MORE VENTURES</p>
   <div class="btn-row" style="justify-content:flex-start;margin-top:22px">
    <a class="btn" href="about.html">Read my story</a>
    <a class="btn ghost" href="assets/derick-asiimwe-cv.pdf" download>Download CV</a>
   </div>
  </div>
  <figure class="avatar-fig"><img class="avatar" src="assets/hoodie-laptop.webp" alt="Derick in a black DeryCode hoodie working on his laptop" width="720" height="720"></figure>
 </div>
</section>
'''


home += '''<section class="section wrap" style="padding-top:0">
 <div class="quotes">
  <blockquote>Smart people are doubted at the start. <em>Results do the talking.</em></blockquote>
  <blockquote>Nobody funds a dream. <em>They fund evidence.</em></blockquote>
  <blockquote>Build like a billionaire. <em>Serve like a servant.</em></blockquote>
 </div>
</section>'''

home += section("explore", "EXPLORE", "One place for<br><em>everything I do.</em>",
  cards([
   ("Profile","About &amp; biography","Who I am, where I come from, what I believe and the philosophy behind the work.","about.html","Read about me"),
   ("Track record","Journey &amp; experience","The timeline, career profile, work experience and the milestones so far.","journey.html","See the journey"),
   ("Capability","Skills &amp; CV","What I actually build with, plus the CV in PDF and a printable version.","skills.html","See skills"),
   ("Companies","Ventures &amp; portfolio","DeryCode, Sageco Evergreen, and the products and startups around them.","ventures.html","Explore ventures"),
   ("Evidence","Projects &amp; case studies","Live sites, platforms, open-source work, experiments and client results.","projects.html","Browse projects"),
   ("Purpose","Impact &amp; leadership","Mentorship, youth empowerment, community development and social impact.","impact.html","See the impact"),
   ("Thinking","Writing &amp; insights","Technology, business, leadership and ideas, written plainly.","writing.html","Read the writing"),
   ("Direction","Vision &amp; goals","1, 5, 10 and 20 year goals, Vision 2030, and the path from builder to investor.","vision.html","See the vision"),
   ("Voice","Speaking &amp; media","Talks, interviews, press and the media kit for organisers and journalists.","speaking.html","Speaking &amp; media"),
   ("Work with me","Services &amp; collaboration","Consulting, builds, partnerships and what working together looks like.","services.html","Services"),
   ("For investors","Investment opportunities","Open to angel and strategic investors in both companies, with impact and return.","investors.html","For investors"),
   ("Life","Gallery &amp; interests","Photos, travel, books, habits and the human side of the work.","gallery.html","Gallery"),
  ]))

home += section("mission-home", "MISSION", "To change people's lives.<br><em>At scale.</em>", f'''
<div class="prose">
 <p>I didn't start a company because I wanted a company. I started because I kept meeting people working hard inside broken systems: families paying too much for software they can't use, buyers who can't verify land before handing over savings, shop owners keeping stock in their heads.</p>
 <p>So I build tools that work where people actually are: offline when the internet is down, priced for small businesses, supported long after launch. And I lead companies that treat people as the point, not the by-product.</p>
 <p class="mission-line">One life improved is a story. Millions is a generation changed. My mission is the millions.</p>
</div>
<p style="margin-top:18px"><a class="btn ghost" href="about.html#mission">Read the full mission, vision and values</a></p>
''', band=True)

home += section("ventures-home", "WHAT I LEAD", "The ventures<br><em>I lead.</em>", f'''
<div class="cards">
 <a class="card" href="ventures.html#derycode"><span class="tag">Founder</span><h3>DeryCode Technologies</h3><p>Software for Ugandan businesses that has to survive real conditions: weak internet, small budgets, no IT department. Offline-first systems and websites, built and supported by the person who wrote the code.</p><span class="more">derycode.online ↗</span></a>
 <a class="card" href="ventures.html#sageco"><span class="tag">CEO</span><h3>Sageco Evergreen</h3><p>A property platform built to stop the fear in buying land: verified listings, GPS boundaries, escrow-protected payments and eco-smart development.</p><span class="more">The platform ↗</span></a>
</div>
<p class="side" style="color:var(--muted);font-size:14.5px">Also building <a href="ventures.html#products">Elite Members, DeryAccount, DeryCode Search, Spin &amp; Win, BuildCalc UG and Voice IDE</a>, plus client platforms across hospitality, property, retail and health.</p>
''')

home += section("writing-home", "LATEST THINKING", "Writing it down<br><em>as I learn it.</em>", cards([
  ("Technology","Why Ugandan software has to work offline first","Most software assumes fast internet and a card. Most Ugandan businesses have neither. Here is how I build for that reality.","article-offline-first.html","Read"),
  ("Business","Software, land and stocks: three roads to wealth","Comparing the three vehicles honestly: ceilings, liquidity, control, and how I stack them.","article-software-land-stocks.html","Read"),
  ("Business","The fear in buying land, and what technology can do about it","Land disputes are not only a legal problem. They are an information problem, and information can be engineered.","article-land-trust.html","Read"),
  ("Youth","You do not need permission to build","A note to young people in western Uganda who are waiting for a degree, a job or a title before they start.","article-youth-tech.html","Read"),
]), band=True)
home += '<div class="wrap" style="padding-bottom:10px"><p><a class="btn ghost" href="writing.html">All writing</a></p></div>'

home += section("photos-home", "MOMENTS", "Some moments<br><em>from my days.</em>", '''
<div class="gallery">
 <figure><img src="assets/standing.webp" alt="Derick standing outdoors in Kyenjojo"><figcaption>Kyenjojo, home ground</figcaption></figure>
 <figure><img src="assets/rooftop.webp" alt="Derick on a rooftop in Fort Portal"><figcaption>Site visits and city rooftops</figcaption></figure>
 <figure><img src="assets/terrace.webp" alt="Derick on a terrace during a work session"><figcaption>Between meetings</figcaption></figure>
 <figure><img src="assets/hoodie-laptop-sq.webp" alt="Derick in a DeryCode hoodie with his laptop"><figcaption>DeryCode hoodie, always working</figcaption></figure>
</div>
<p style="margin-top:18px"><a class="btn ghost" href="gallery.html">More photos and life</a></p>
''')

home += f'''<section class="section wrap">
 {cta("Invest in what we're building.",
  "DeryCode Technologies and Sageco Evergreen are open to angel and strategic investors who want commercial returns and measurable social impact in the same deal. Both companies are early stage and already operating.",
  ("investors.html","See the opportunity"), ("contact.html","Talk to me"))}
</section>'''

add("index.html", "Asiimwe Derick | Social entrepreneur, founder &amp; CEO",
    "Asiimwe Derick, young social entrepreneur in Uganda, founder of DeryCode Technologies and CEO of Sageco Evergreen. Biography, ventures, projects, writing, vision and how to get in touch.",
    "home derick uganda entrepreneur founder derycode sageco", home)

# ============================== ABOUT ==============================
about = page_head_block("About", '<a href="about.html">About</a>', "01 / PROFILE",
  "The person behind<br><em>the work.</em>",
  "Biography, story, identity, philosophy and values. No titles without the reasoning behind them.",
  [("biography","Biography"),("story","My story"),("identity","Identity &amp; brand"),("philosophy","Philosophy &amp; manifesto"),("mission","Mission, vision &amp; values"),("education","Education &amp; learning")])

about += section("biography", "BIOGRAPHY", "Who I am", f'''
<div class="prose">
 <p><strong>Asiimwe Derick</strong> is a social entrepreneur from Kyenjojo, in western Uganda, born on 9 January 2006. He is the founder of <a href="ventures.html#derycode">DeryCode Technologies</a>, a software company building offline-first systems and websites for Ugandan businesses, and the CEO of <a href="ventures.html#sageco">Sageco Evergreen</a>, a property platform built around verified listings, GPS boundaries and escrow-protected payments.</p>
 <p>He is twenty years old and still completing school, running both companies in the hours that school leaves him. He states that constraint plainly because it shapes how he works: small teams, fast shipping, and systems designed for unreliable power, weak internet and small budgets, because those are the conditions he builds in.</p>
 <p>His work sits at the meeting point of two problems he kept meeting personally: businesses that cannot afford or operate the software sold to them, and families who lose savings to land deals they cannot verify. Both are information problems before they are legal or technical ones, and both can be engineered against.</p>
 <p>He writes in public, publishes his numbers, and is open to angel and strategic investors in both companies. His stated long-term ambition, <a href="vision.html">Vision 2040</a>, is to move from building companies to investing in the people building Africa's future.</p>
</div>
<div class="stat-row">
 <div class="stat-box"><b>2006</b><span>Born 9 January, Kyenjojo, Uganda</span></div>
 <div class="stat-box"><b>2</b><span>Companies founded or led</span></div>
 <div class="stat-box"><b>59</b><span>Live websites and apps built</span></div>
 <div class="stat-box"><b>5</b><span>Sectors served</span></div>
</div>
''')

about += section("story", "MY STORY", "How this started", f'''
<div class="prose">
 <p>It started with watching people work hard inside systems that were not built for them. In Kyenjojo, that looks like a shop owner who knows every item in his head because the software costs more than his margin, a family that has paid for land twice because the first proof was a paper in a drawer, a student with no record of what he has actually learned.</p>
 <p>The first response was technical: learn to build, then build the thing that is missing. That is how DeryCode Technologies began, writing websites and business systems for local companies, then keeping them running long after launch, because a small business with no IT department cannot absorb a handover that ends in a broken invoice.</p>
 <p>The second response was structural. Software alone does not fix a market where the buyer cannot verify what they are buying. That is why Sageco Evergreen exists: to put verification, boundaries and payment protection into the same place, so trust becomes a product feature rather than a favour.</p>
 <p>He is honest that both companies are early. The point of publishing the story this way is that the work is checkable: live sites, live listings, real clients, real numbers.</p>
</div>
{edit("Add your personal turning points", "This section is written from public facts about your work. Add two or three personal moments (the first computer, the first client, the first loss) with dates, and the story becomes unmistakably yours.")}
''')

about += section("identity", "IDENTITY &amp; BRAND", "What the name stands for", f'''
<div class="prose">
 <p><strong>Name:</strong> Asiimwe Derick. Publicly, Derick. <strong>Positioning:</strong> a young Ugandan builder who ships and publishes his numbers, not a motivational speaker. <strong>Promise:</strong> tools that work where people actually are, and deals done on transparency.</p>
 <p><strong>Voice:</strong> plain, specific, unexaggerated. Short sentences. Numbers over adjectives. He would rather be trusted than impressive. <strong>Visual identity:</strong> warm amber on deep navy, Space Grotesk for headings, DM Sans for text, generous white space and photography that shows the work rather than stock imagery.</p>
 <p><strong>What he refuses:</strong> inflated claims, invented credentials, and the habit of selling African founders a dream instead of a product.</p>
</div>
<p>{chips(["Amber #F2B44A","Navy #0B0F17","Space Grotesk","DM Sans","Trust over hype","Show the work"])}</p>
<p><a class="btn ghost" href="mediakit.html">Brand assets, bios and media kit</a></p>
''', band=True)

about += section("philosophy", "PHILOSOPHY &amp; MANIFESTO", "What I actually believe", f'''
<div class="prose">
 <blockquote>Character before titles. The business changes; what you are does not.</blockquote>
 <p><strong>1. Build where the need is greatest.</strong> The interesting problem is not in the market that already has eleven solutions. It is with the shop owner, the farmer and the family buying land.</p>
 <p><strong>2. Offline is a feature, not a limitation.</strong> Software that needs perfect conditions is software for someone else's country.</p>
 <p><strong>3. Price for the person you claim to serve.</strong> If the tool costs more than the problem, it is not a solution.</p>
 <p><strong>4. Publish the numbers.</strong> Claims should be checkable. Live links, real listings, real clients.</p>
 <p><strong>5. Support is part of the product.</strong> A launch is the middle of the job, not the end.</p>
 <p><strong>6. Open doors behind you.</strong> Every chance to pull someone up is part of the work, not charity around it.</p>
 <p><strong>7. Stay a student.</strong> Ask why before how, and keep asking after you are the one leading.</p>
</div>
''')

about += section("mission", "MISSION, VISION &amp; VALUES", "The frame everything hangs on", f'''
<div class="prose">
 <h3>Mission</h3>
 <p>To change people's lives at scale: build tools and companies that improve how ordinary people work, buy, learn and own, and make that improvement reachable by millions rather than dozens.</p>
 <h3>Vision</h3>
 <p>Vision 2040: from builder to global investor. Build companies that make money and help people, learn how capital flows, then put capital behind African founders solving African problems. <a href="vision.html">Read the full vision and roadmap</a>.</p>
 <h3>Values</h3>
</div>
<div class="cards">
 <div class="card"><span class="tag">01</span><h3>Integrity</h3><p>My word is the product. If I promise it, I deliver it, even when it costs me.</p></div>
 <div class="card"><span class="tag">02</span><h3>Service</h3><p>Success that leaves people behind isn't success. Impact is measured in lives changed, not numbers raised.</p></div>
 <div class="card"><span class="tag">03</span><h3>Courage</h3><p>Start where the need is greatest, not where it's easiest to look good.</p></div>
 <div class="card"><span class="tag">04</span><h3>Curiosity</h3><p>I ask why before how, and I stay a student even as I lead.</p></div>
 <div class="card"><span class="tag">05</span><h3>Patience</h3><p>I'm building things that should outlast me. That means choosing the slow, honest path.</p></div>
 <div class="card"><span class="tag">06</span><h3>Generosity</h3><p>Open doors behind me. Every chance I get, I want to pull someone else up.</p></div>
</div>
''', band=True)

about += section("education", "EDUCATION &amp; LEARNING", "School, and everything after it", f'''
<div class="prose">
 <p>Formal education is in progress: he is completing school while running several ventures. The rest of his learning is public and checkable in the work itself, software engineering, product design, payments, property verification and the commercial side of running a company.</p>
</div>
{edit("Add your schools and qualifications", "Add your school name, level and expected completion year, plus any certificates or courses (for example programming, accounting or business programmes). This is the one section of the site that must come from you, not from inference.")}
<div class="cards">
 <div class="card"><span class="tag">Learning</span><h3>Self-taught engineering</h3><p>Web and software development learned by shipping: HTML, CSS, JavaScript, React and Next.js, Python, Postgres and Supabase, deployment on Vercel and GitHub Pages.</p></div>
 <div class="card"><span class="tag">Learning</span><h3>Business by operating</h3><p>Pricing, client care, payroll of trust and the discipline of running several ventures: learned in the market rather than in a classroom.</p></div>
 <div class="card"><span class="tag">Learning</span><h3>Always next</h3><p>Currently deepening: AI systems, payments infrastructure, property law basics for product design, and investor communication.</p></div>
</div>
''')

add("about.html", "About Asiimwe Derick | Biography, story, philosophy and values",
    "Biography of Asiimwe Derick: born 9 January 2006 in Kyenjojo, Uganda. Founder of DeryCode Technologies, CEO of Sageco Evergreen. His story, identity, philosophy, mission, vision and values.",
    "about biography story philosophy manifesto values mission vision identity education", about)

# ============================== JOURNEY ==============================
journey = page_head_block("Journey", '<a href="journey.html">Journey</a>', "02 / TRACK RECORD",
  "The road so far,<br><em>in order.</em>",
  "Timeline, career profile, work experience and the milestones that can be checked rather than claimed.",
  [("timeline","Timeline"),("career","Career profile"),("experience","Work experience"),("milestones","Milestones &amp; achievements")])

journey += section("timeline", "TIMELINE", "My journey", f'''
<div class="prose"><p>Milestones are listed with dates where they are known. Anything marked <strong>[year]</strong> needs your exact date, and that is deliberate: no invented history on a page people use to judge you.</p></div>
{timeline([
 ("9 January 2006","Born in Kyenjojo, western Uganda","Home ground. The place that shaped the problems he went on to build against: land, small trade, unreliable infrastructure."),
 ("School years","Learning, then learning to build","Formal schooling continues today, alongside self-taught software engineering: HTML, CSS, JavaScript, then React, Next.js, Python and databases."),
 ("[year]","First paid websites","The beginning of DeryCode: websites and simple business systems for local companies, delivered and then supported."),
 ("[year]","DeryCode Technologies","Founded as a software company: offline-first systems, websites, AI tools and digital work for Ugandan businesses."),
 ("2026","Sageco Evergreen platform","A property platform built around verified listings, GPS boundaries, escrow-protected payments and eco-smart development, led as CEO."),
 ("2026","59 live sites and apps","A portfolio of live client and product sites across property, hospitality, education, retail, health and agriculture."),
 ("Next","Vision 2030 and Vision 2040","From building companies to investing in the people building Africa's future. <a href='vision.html'>The roadmap</a>."),
])}
{edit("Confirm the two dates marked [year]", "Tell me the year you started DeryCode and the year you delivered your first paid website, and I will lock them into the timeline.")}
''')

journey += section("career", "CAREER &amp; PROFESSIONAL PROFILE", "What I do professionally", f'''
<div class="prose">
 <p>Derick works as a founder and operator, not a consultant on the side. Professionally he runs several ventures at once: one that builds software for other businesses, and one that uses software to fix a market he grew up watching fail.</p>
 <p><strong>Founder &amp; CEO, DeryCode Technologies.</strong> Leads product, engineering and client delivery: websites, offline-first business systems, AI tooling and digital presence for Ugandan businesses. Responsible for scoping, pricing, building, deploying and supporting.</p>
 <p><strong>CEO, Sageco Evergreen.</strong> Leads a property platform: verified listings, GPS-verified boundaries, escrow-protected payments, digital land passports and fractional investment features. Responsible for product direction, partner relationships and operating discipline.</p>
 <p><strong>Working style.</strong> Small teams, direct communication, ship then improve, publish the numbers, and stay reachable after launch.</p>
</div>
<div class="stat-row">
 <div class="stat-box"><b>2</b><span>Executive roles held simultaneously</span></div>
 <div class="stat-box"><b>59</b><span>Live products and client sites delivered</span></div>
 <div class="stat-box"><b>5</b><span>Sectors: property, hospitality, education, retail, agriculture</span></div>
 <div class="stat-box"><b>1</b><span>Country: Uganda, building for African markets</span></div>
</div>
''', band=True)

journey += section("experience", "WORK EXPERIENCE", "Where the work has been done", f'''
{timeline([
 ("Present","DeryCode Technologies — Founder &amp; CEO","Building and supporting websites, business systems and AI tools for Ugandan businesses. Client work spans hospitality (Relie Motel, Tropical Gardens Hotel), machinery retail (Nuwe Rugaba), electronics (Steady Company), property (Sageco), health (Peters Medicare), beauty (Posh Healing Parlour), education and community organisations."),
 ("Present","Sageco Evergreen — CEO","Running a property platform with verified listings, GPS boundaries, escrow payments, land passports and fractional investment. Live platform, paid viewings and investor conversations."),
 ("Present","Product builder — own products","Elite Members, DeryAccount, DeryCode Search, Spin &amp; Win, BuildCalc UG, School Sync Manager, Visit Fort Portal and Voice IDE: products built, deployed and maintained."),
 ("Ongoing","Mentorship and youth work","Supporting young people in western Uganda into technology, and building free tools and sites for community organisations."),
])}
{edit("Add employment or attachment history", "If you have worked for anyone else, or held a formal attachment, add it here with the organisation, role and dates. If everything has been your own companies, delete this block.")}
''')

journey += section("milestones", "MILESTONES &amp; ACHIEVEMENTS", "What is checkable today", f'''
{cards([
 ("Statistics","59 live websites and apps","Built, deployed and running across Uganda: client platforms, product sites and experiments. Each one is a link you can open.","projects.html","See the projects"),
 ("Statistics","63 verified property listings","Live on Sageco Evergreen with GPS boundaries and escrow-protected payment flows, plus paid viewing bookings.","ventures.html#sageco","See the platform"),
 ("Achievement","Several ventures before twenty-one","Founder of some, CEO of another, all operating rather than planned, all built in Uganda.","ventures.html","Explore the ventures"),
 ("Achievement","A platform that protects savings","Sageco Evergreen turns land verification, boundaries and payment protection into product features rather than promises.","article-land-trust.html","Read the thinking"),
])}
{edit("Add awards, certificates and recognition", "List any awards, competitions, scholarships, press mentions or certificates with the year and the awarding body. If none yet, this block can stay empty or be removed: the statistics above already carry the page.")}
''', band=True)

add("journey.html", "Journey &amp; experience | Asiimwe Derick",
    "Asiimwe Derick's journey, career profile, work experience and milestones: several ventures, 59 live websites and apps, and the timeline from Fort Portal to Sageco Evergreen.",
    "journey timeline career experience work milestones achievements", journey)

# ============================== SKILLS & CV ==============================
skills = page_head_block("Skills &amp; CV", '<a href="skills.html">Skills &amp; CV</a>', "03 / CAPABILITY",
  "What I build with,<br><em>and what I've shipped.</em>",
  "Skills listed against evidence rather than adjectives, with the CV available as PDF or printable page.",
  [("skills","Skills &amp; expertise"),("evidence","Evidence"),("cv","CV download")])

skills += section("skills", "SKILLS &amp; EXPERTISE", "Capability, grouped", f'''
<div class="cards">
 <div class="card"><span class="tag">Engineering</span><h3>Web &amp; software</h3><p>HTML, CSS, JavaScript, React, Next.js, Python, REST APIs, static and server-rendered sites, progressive web apps, performance and accessibility basics.</p></div>
 <div class="card"><span class="tag">Engineering</span><h3>Data &amp; backend</h3><p>PostgreSQL, Supabase (auth, row-level security, storage, policies), data modelling, migrations and API design.</p></div>
 <div class="card"><span class="tag">Engineering</span><h3>Deployment &amp; operations</h3><p>Vercel, GitHub Pages, Git and GitHub workflows, DNS and custom domains, environment configuration, uptime and post-launch support.</p></div>
 <div class="card"><span class="tag">AI</span><h3>AI systems</h3><p>LLM integration into products, prompt and knowledge-base design, on-site assistants, search relevance and offline-first AI tooling.</p></div>
 <div class="card"><span class="tag">Payments</span><h3>Money movement</h3><p>PesaPal integration, mobile money flows, escrow logic, subscriptions and reconciliation reporting.</p></div>
 <div class="card"><span class="tag">Product</span><h3>Product &amp; design</h3><p>Problem discovery with local businesses, information architecture, interface design, mobile-first layouts and copy that sells without exaggerating.</p></div>
 <div class="card"><span class="tag">Business</span><h3>Company building</h3><p>Pricing, client delivery, partnership development, team leadership and investor communication.</p></div>
 <div class="card"><span class="tag">Growth</span><h3>Digital marketing &amp; SEO</h3><p>Technical SEO, structured data, local search, Google Business Profile work, content strategy and outreach.</p></div>
</div>
''')

skills += section("evidence", "EVIDENCE", "Skills, with receipts", f'''
<div class="table-wrap"><table>
<tr><th>Skill</th><th>Where you can see it</th></tr>
<tr><td>Full-stack web development</td><td>59 live sites and apps, including <a href="projects.html">client platforms and products</a></td></tr>
<tr><td>Offline-first product design</td><td><a href="ventures.html#products">DeryAccount</a>, accounting built to work without reliable internet</td></tr>
<tr><td>Property technology</td><td><a href="ventures.html#sageco">Sageco Evergreen</a>: verified listings, GPS boundaries, escrow, land passports</td></tr>
<tr><td>Payments</td><td>PesaPal and mobile money flows running in production on client and product sites</td></tr>
<tr><td>AI integration</td><td><a href="projects.html#platforms">DeryCode Search</a> with 10 modes and 22 sources, plus on-site assistants</td></tr>
<tr><td>Technical SEO</td><td>Structured data, sitemaps and local search work across the portfolio</td></tr>
<tr><td>Search engineering</td><td><a href="projects.html#platforms">DeryCode Search</a> relevance scoring and multi-source synthesis</td></tr>
</table></div>
''', band=True)

skills += section("cv", "CV / RÉSUMÉ", "Take the CV with you", f'''
<div class="prose">
 <p>The CV is kept to one page: roles, companies, capability and contact. Download the PDF, or open the printable page if you would rather read it in the browser or print a copy.</p>
</div>
<div class="btn-row" style="justify-content:flex-start">
 <a class="btn" href="assets/derick-asiimwe-cv.pdf" download>Download CV (PDF)</a>
 <a class="btn ghost" href="cv.html">Printable CV page</a>
 <a class="btn ghost" href="mailto:{EMAIL}?subject=CV%20request">Request by email</a>
</div>
{edit("Keep the CV current", "The PDF is generated from this site's facts. When you add schools, certificates or new roles, ask for a regeneration and the PDF updates with the site.")}
''')

add("skills.html", "Skills, expertise and CV | Asiimwe Derick",
    "Asiimwe Derick's skills and expertise: full-stack web development, offline-first product design, property technology, payments, AI integration, SEO and company building. Download the CV.",
    "skills expertise cv resume developer nextjs python supabase payments ai seo", skills)

# ============================== PRINTABLE CV ==============================
cv = page_head_block("CV", '<a href="cv.html">Printable CV</a>', "CURRICULUM VITAE",
  "Asiimwe Derick",
  "Founder &amp; CEO, DeryCode Technologies · CEO, Sageco Evergreen · Kyenjojo, Uganda")
cv += f'''
<section class="section wrap" style="padding-top:0">
 <div class="btn-row" style="justify-content:flex-start;margin-bottom:26px">
  <a class="btn" href="assets/derick-asiimwe-cv.pdf" download>Download PDF</a>
  <button class="btn ghost" onclick="window.print()" type="button">Print this page</button>
 </div>
 <div class="prose">
  <h3>Profile</h3>
  <p>Social entrepreneur from Kyenjojo, Uganda. Founder of DeryCode Technologies (offline-first software and websites for Ugandan businesses) and CEO of Sageco Evergreen (property platform with verified listings, GPS boundaries and escrow payments). Twenty years old, completing school while running both companies.</p>
  <h3>Experience</h3>
  <p><strong>Founder &amp; CEO, DeryCode Technologies</strong> · present<br>Leads product, engineering and delivery of websites, business systems and AI tools. 59 live sites and apps across property, hospitality, education, retail, health and agriculture.</p>
  <p><strong>CEO, Sageco Evergreen</strong> · present<br>Leads a property platform: verified listings, GPS-verified boundaries, escrow-protected payments, digital land passports and fractional investment features.</p>
  <p><strong>Product builder</strong> · present<br>Elite Members, DeryAccount, DeryCode Search, Spin &amp; Win, BuildCalc UG, School Sync Manager, Visit Fort Portal, Voice IDE.</p>
  <h3>Skills</h3>
  <p>JavaScript, React, Next.js, Python, PostgreSQL and Supabase, REST APIs, Vercel, GitHub, PesaPal and mobile money integration, technical SEO, AI integration, product design, company operations.</p>
  <h3>Education</h3>
  <p>School in progress, Kyenjojo. Self-taught software engineering and business operations. <em>[Add school name, level and completion year.]</em></p>
  <h3>Contact</h3>
  <p>{EMAIL} · WhatsApp 0762 306 675 · {BASE}</p>
 </div>
</section>
'''
add("cv.html", "Asiimwe Derick — Curriculum Vitae",
    "Printable CV for Asiimwe Derick: founder of DeryCode Technologies, CEO of Sageco Evergreen. Experience, skills, education and contact, with PDF download.",
    "cv resume curriculum vitae derick asiimwe", cv)

# ============================== VENTURES ==============================
vent = page_head_block("Ventures", '<a href="ventures.html">Ventures</a>', "04 / BUSINESSES",
  "The ventures.<br><em>A portfolio behind them.</em>",
  "The businesses he leads, the startups and products around them, and the sectors he is moving into next.",
  [("derycode","DeryCode Technologies"),("sageco","Sageco Evergreen"),("products","Products &amp; startups"),("sectors","Real estate &amp; agriculture")])

vent += section("derycode", "FOUNDER", "DeryCode Technologies", f'''
<div class="prose">
 <p>DeryCode Technologies builds software for Ugandan businesses that has to survive real conditions: weak internet, small budgets, no IT department. The company writes websites, offline-first business systems, AI tools and digital campaigns, then keeps them running after launch.</p>
 <p><strong>Why it exists:</strong> most software sold in Uganda is priced and designed for a different economy. It assumes fast internet, card payments and someone on staff to administer it. DeryCode builds the opposite: light, resilient, affordable, supported.</p>
 <p><strong>What it delivers:</strong> business websites and booking systems, offline-first accounting and records, payment integration through PesaPal and mobile money, technical SEO, and AI assistants embedded in the product.</p>
 <p><strong>Who it serves:</strong> hotels and lodges, property companies, machinery and retail shops, clinics, schools, community organisations and event businesses.</p>
</div>
<div class="btn-row" style="justify-content:flex-start"><a class="btn" href="https://derycode.online" target="_blank" rel="noopener">derycode.online ↗</a><a class="btn ghost" href="services.html">Work with DeryCode</a></div>
''')

vent += section("sageco", "CEO", "Sageco Evergreen", f'''
<div class="prose">
 <p>Sageco Evergreen is a property platform built to remove the fear from buying land in Uganda. Instead of a listing and a phone number, every property carries verification, GPS boundaries, a digital land passport and a payment path protected by escrow.</p>
 <p><strong>The problem it attacks:</strong> families lose savings to land they cannot verify. Proof lives in drawers, boundaries live in memory, and the buyer carries all the risk. That is an information failure, and information failures can be engineered against.</p>
 <p><strong>What is live:</strong> 63 verified property listings, GPS-verified boundaries, escrow-protected milestones, paid viewings, fractional investment features, an Android app, and a PesaPal payment rail in production.</p>
 <p><strong>Where it is going:</strong> verified inventory at scale, broker partnerships, and land transactions that a first-time buyer can complete without a lawyer holding their hand.</p>
</div>
<div class="btn-row" style="justify-content:flex-start"><a class="btn" href="https://sageco-evergreen.vercel.app" target="_blank" rel="noopener">Open the platform ↗</a><a class="btn ghost" href="investors.html">Investor information</a></div>
''', band=True)

vent += section("products", "STARTUP PORTFOLIO", "Products built and running", cards([
 ("Social","Elite Members","An exclusive social platform for creators, entrepreneurs and professionals, built around a premium, invite-driven community rather than an open feed.","https://elitemembers.base44.app","Open Elite Members"),
 ("Finance","DeryAccount","Simple, offline-first business accounting for Ugandan shops: sales, stock and records that survive a bad connection.","https://deryaccount.vercel.app","Open DeryAccount"),
 ("Search","DeryCode Search","A multi-mode search engine: AI, web, images, news, code, books, maps, deep web and video, with 10 modes across 22 sources.","projects.html#search","See how it works"),
 ("Productivity","BuildCalc UG","A construction materials calculator for Ugandan builders: quantities, costs and estimates without a spreadsheet.","https://asiimwe3.github.io/buildcalc-ug/","Open BuildCalc"),
 ("Education","School Sync Manager","School fees and student records for Ugandan schools, built for bursars who work offline.","projects.html#education","See the project"),
 ("Tourism","Visit Fort Portal","A destination guide to Fort Portal: attractions, lakes, culture and trip planning for visitors.","https://asiimwe3.github.io/fort-portal-tourism/","Open the guide"),
 ("AI","Voice IDE","An editor you can code in by talking: voice-first programming for people who think faster than they type.","https://asiimwe3.github.io/derycode-voice-ide/","Try Voice IDE"),
 ("Promotions","Spin &amp; Win","A promotional spin-to-win product for businesses. Currently held back from paid operation pending written licensing guidance.","projects.html#spin","Read the status"),
]))

vent += section("sectors", "SECTORS", "Where the portfolio is heading", f'''
<div class="cards">
 <div class="card"><span class="tag">Real estate</span><h3>Property &amp; land</h3><p>Sageco Evergreen is the anchor: verified listings, escrow, land passports, fractional investment. The next step is inventory and broker partnerships that make verification the default in western Uganda.</p></div>
 <div class="card"><span class="tag">Agriculture</span><h3>Agribusiness</h3><p>Tools for farmers and agri-traders: record keeping, input costing and market access. <em>[Add the specific agriculture venture or pilot you are running, if one exists.]</em></p></div>
 <div class="card"><span class="tag">Technology</span><h3>Software &amp; AI</h3><p>DeryCode is the delivery arm: offline-first systems, AI assistants and search, sold to businesses that need working tools rather than demos.</p></div>
</div>
{cta("Building something that fits this portfolio?", "If you are building in property, agriculture or small-business software in Uganda, and you want a partner who ships, start a conversation.", ("contact.html","Talk to Derick"), ("investors.html","Investor information"))}
''', band=True)

add("ventures.html", "Ventures &amp; portfolio | Asiimwe Derick",
    "DeryCode Technologies and Sageco Evergreen, plus the product portfolio: Elite Members, DeryAccount, DeryCode Search, BuildCalc UG, School Sync Manager, Visit Fort Portal and Voice IDE.",
    "ventures companies derycode sageco portfolio startups products real estate agriculture", vent)

# ============================== PROJECTS ==============================
proj = page_head_block("Projects", '<a href="projects.html">Projects</a>', "05 / EVIDENCE",
  "Things I built,<br><em>still running.</em>",
  "Platforms, products, client work, open source and experiments. Every item links to something live where one exists.",
  [("platforms","Platforms &amp; products"),("clients","Client work"),("cases","Case studies"),("opensource","Open source"),("research","Research &amp; experiments")])

proj += section("platforms", "SOFTWARE &amp; PRODUCT PORTFOLIO", "Platforms and products", f'''
<div id="search"></div>
{cards([
 ("Platform","Sageco Evergreen","Property platform with verified listings, GPS boundaries, escrow payments, land passports, fractional investment, an AI broker and an Android app. Live with 63 listings and a production PesaPal rail.","https://sageco-evergreen.vercel.app","Open platform"),
 ("Search","DeryCode Search","A search engine with 10 modes across 22 sources, including AI answers, deep-web indexes, academic sources and code search. Relevance-scored synthesis rather than raw links.","https://github.com/asiimwe3","View on GitHub"),
 ("Finance","DeryAccount","Offline-first accounting for small businesses, with subscription checkout running through PesaPal.","https://deryaccount.vercel.app","Open DeryAccount"),
 ("Social","Elite Members","An exclusive community platform for creators and professionals.","https://elitemembers.base44.app","Open Elite Members"),
 ("AI","Voice IDE","Voice-first code editor: write software by talking, for people who think faster than they type.","https://asiimwe3.github.io/derycode-voice-ide/","Try Voice IDE"),
 ("Utility","BuildCalc UG","Construction materials calculator for Ugandan builders.","https://asiimwe3.github.io/buildcalc-ug/","Open BuildCalc"),
])}
<div id="education"></div>
<div id="spin"></div>
<div class="cards">
 <div class="card"><span class="tag">Education</span><h3>School Sync Manager</h3><p>Fees and student records for Ugandan schools, designed for bursars working with unreliable internet and paper backups.</p><span class="more">Product in the DeryCode portfolio</span></div>
 <div class="card"><span class="tag">Promotions</span><h3>Spin &amp; Win</h3><p>A promotional spin-to-win product. Paid operation is paused deliberately: Uganda's Lotteries and Gaming Act treats paid promotional competitions as licensable, so it stays offline until the regulator confirms the position in writing. The engineering is done; the compliance call is not.</p><span class="more">Held pending licensing guidance</span></div>
 <div class="card"><span class="tag">Tourism</span><h3>Visit Fort Portal</h3><p>A destination guide to Fort Portal: parks, crater lakes, culture and trip planning, built to send visitors to local businesses.</p><a class="more" href="https://asiimwe3.github.io/fort-portal-tourism/" target="_blank" rel="noopener">Open the guide ↗</a></div>
</div>
''')

proj += section("clients", "CLIENT WORK", "Sites built for real businesses", f'''
<div class="prose"><p>Client platforms delivered through DeryCode Technologies. Each one is live, supported, and built around what the business actually needed rather than a template.</p></div>
{cards([
 ("Hospitality","Relie Motel, Fort Portal","Website, room showcase, direct WhatsApp booking and a 12-language, 9-currency front end for a 26-room motel. Includes an operator outreach system and a reputation recovery plan.","https://reliemotel.com","Open the site"),
 ("Hospitality","Tropical Gardens Hotel","Hotel and events site for a Kyenjojo property: rooms, conference and wedding gardens, restaurant, and a PesaPal payment path.","https://tropicalgardenshotelkyenjojo.com","Open the site"),
 ("Retail","Nuwe Rugaba Machinery","Machinery retailer in Fort Portal: a six-category catalogue with product pages, WhatsApp quote flow and structured data for search.","https://nuwerugabamachinary.com","Open the site"),
 ("Retail","Steady Company (U) Ltd","Phone distributor and electronics retailer in Fort Portal.","https://steadycompanyltd.com","Open the site"),
 ("Hospitality","Bagu Legacy Homes","Homestay accommodation in Fort Portal, positioned on comfort and local hosting.","https://bagulegacyhomes.online","Open the site"),
 ("Services","Brazil Plumbing Center","Plumbing services company with a clear service and booking path.","https://brazilplumbingcenter.online","Open the site"),
 ("Health","Peters Medicare Services","Clinic in Kyenjojo: services, hours and contact.","https://petersmedicare.online","Open the site"),
 ("Wellness","Posh Healing Parlour","Spa and healing parlour: treatments and booking.","projects.html","In the portfolio"),
])}

''')

proj += section("cases", "CASE STUDIES", "Three, in detail", f'''
<div class="cards">
 <div class="card wide"><span class="tag">Case study · Property</span><h3>Sageco Evergreen: making verification a product feature</h3>
 <p><strong>Problem.</strong> Land buyers in Uganda carry all the risk: proof in drawers, boundaries in memory, payment before verification.</p>
 <p><strong>Build.</strong> A platform where each listing carries GPS-verified boundaries, a digital land passport, escrow milestones and a paid viewing path, with an AI broker answering buyer questions and an Android app for field use.</p>
 <p><strong>Result.</strong> Live with 63 listings, working payments, and a security model rebuilt so the public key can read and submit but never modify or delete records.</p>
 <a class="more" href="https://sageco-evergreen.vercel.app" target="_blank" rel="noopener">Open the platform ↗</a></div>
 <div class="card wide"><span class="tag">Case study · Hospitality</span><h3>Relie Motel: from a Google pin to a booking channel</h3>
 <p><strong>Problem.</strong> No website, no rates published, bookings only by phone, and a 3.8-star rating contradicted by guests describing five-star service.</p>
 <p><strong>Build.</strong> A multilingual, multi-currency site with direct WhatsApp booking and zero commission, plus a delivery document analysing 289 reviews, a tour-operator outreach pack and a 339-contact licensed operator list.</p>
 <p><strong>Result.</strong> A direct booking channel that costs nothing per reservation, and a reputation plan aimed at 4.3 stars within two quarters.</p>
 <a class="more" href="https://reliemotel.com" target="_blank" rel="noopener">Open the site ↗</a></div>
 <div class="card wide"><span class="tag">Case study · Retail</span><h3>Nuwe Rugaba Machinery: turning one page into seven doors</h3>
 <p><strong>Problem.</strong> A single-page site with one keyword, a Maps listing whose hours read as opening at midnight, and a misspelled domain that dead-ended correct-spelling traffic.</p>
 <p><strong>Build.</strong> Six category pages (pumps, generators, construction, welding, farm machinery, spares) with product structured data, FAQ schema, WhatsApp quote flows, a category grid on the homepage, a rebuilt sitemap and clean URLs.</p>
 <p><strong>Result.</strong> Seven indexable pages instead of one, each targeting what buyers actually search.</p>
 <a class="more" href="https://nuwerugabamachinary.com" target="_blank" rel="noopener">Open the site ↗</a></div>
</div>
''', band=True)

proj += section("opensource", "OPEN SOURCE", "Code in public", f'''
<div class="prose"><p>Repositories are public where they can be: the sites themselves, the search engine, the calculators and the experiments. The GitHub profile is the raw index.</p></div>
<div class="cards">
 <div class="card"><span class="tag">GitHub</span><h3>25+ public repositories</h3><p>Static sites, Next.js applications, tools and experiments, all publicly readable and forkable.</p><a class="more" href="https://github.com/asiimwe3" target="_blank" rel="noopener">github.com/asiimwe3 ↗</a></div>
 <div class="card"><span class="tag">Search</span><h3>DeryCode Search</h3><p>Multi-source search with relevance scoring, intent detection and deep-web indexes.</p><a class="more" href="https://github.com/asiimwe3" target="_blank" rel="noopener">View repository ↗</a></div>
 <div class="card"><span class="tag">Tools</span><h3>BuildCalc UG</h3><p>Open construction calculator for Ugandan builders and quantity surveyors.</p><a class="more" href="https://asiimwe3.github.io/buildcalc-ug/" target="_blank" rel="noopener">Open tool ↗</a></div>
</div>
''')

proj += section("research", "RESEARCH &amp; EXPERIMENTS", "Things being tested", f'''
<div class="cards">
 <div class="card"><span class="tag">AI</span><h3>Voice-first programming</h3><p>Voice IDE explores a simple question: if someone can describe software out loud, should they need a keyboard to build it? Useful for builders with limited typing speed or literacy in English syntax.</p></div>
 <div class="card"><span class="tag">AI</span><h3>Offline-capable assistants</h3><p>Can a business assistant stay useful when the connection drops? Experiments in local knowledge bases and graceful degradation.</p></div>
 <div class="card"><span class="tag">Property</span><h3>Digital land passports</h3><p>Verifiable records attached to a plot: GPS, ownership history, documents. Researching how far a passport can go before it needs legal weight behind it.</p></div>
 <div class="card"><span class="tag">Payments</span><h3>Escrow for small transactions</h3><p>Milestone-based release of funds against verified visits. The hard part is not the code, it is the trust model around it.</p></div>
</div>
{cta("Want the detail behind any project?", "Happy to walk you through the architecture, the numbers or the mistakes. Ask for the project you care about.", ("contact.html","Ask about a project"), ("assistant.html","Ask Derick AI"))}
''')

add("projects.html", "Projects, products and case studies | Asiimwe Derick",
    "Projects and case studies: Sageco Evergreen, DeryCode Search, DeryAccount, Elite Members, Voice IDE, plus client work for hotels, retailers and clinics across Uganda.",
    "projects portfolio products client work case studies open source research sageco derycode", proj)

# ============================== IMPACT ==============================
imp = page_head_block("Impact", '<a href="impact.html">Impact</a>', "06 / PURPOSE",
  "The point is<br><em>people.</em>",
  "Leadership, mentorship, social impact, community development and youth empowerment: the part of the work that is not on an invoice.",
  [("leadership","Leadership"),("mentorship","Mentorship"),("social","Social impact"),("community","Community"),("youth","Youth empowerment")])

imp += section("leadership", "LEADERSHIP", "How I lead", f'''
<div class="prose">
 <p>Leadership here means several ventures running at once, with small teams and no layer to hide behind. It means setting direction, doing the work, and staying reachable after launch, because the person who wrote the code is also the person who answers the phone.</p>
 <p><strong>What that looks like in practice:</strong> plain communication, decisions made in the open, and a bias to shipping something working rather than describing something perfect. Mistakes are named early: on Sageco Evergreen, a database permission model that would have let a stranger delete real bookings was found and rebuilt before launch, not after.</p>
 <p><strong>What he is learning:</strong> delegation, hiring, and the discipline of saying no to work that does not serve the mission.</p>
</div>
''')

imp += section("mentorship", "MENTORSHIP", "Bringing people with me", f'''
<div class="prose">
 <p>Mentorship in western Uganda rarely looks like a programme. It looks like a young person with a laptop asking how to get their first client. Derick's approach is practical: show the work, share the numbers, and help with the specific next step rather than a motivational speech.</p>
 <p>He is building <a href="ventures.html#products">tools that lower the entry cost</a> for beginners, a voice-first editor for people who think faster than they type, and calculators that remove the maths barrier to trade work.</p>
</div>
{edit("Add your mentorship record", "Add the number of young people you currently mentor, any programme or group you support, and one concrete outcome you are proud of. A named example beats any adjective.")}
''', band=True)

imp += section("social", "SOCIAL IMPACT", "Impact that is measurable", f'''
<div class="cards">
 <div class="card"><span class="tag">Access</span><h3>Software priced for small business</h3><p>DeryCode builds systems that a shop in Kyenjojo can afford and run without an IT department. Affordable software is the difference between a business keeping records and losing them.</p></div>
 <div class="card"><span class="tag">Protection</span><h3>Land savings protected</h3><p>Sageco Evergreen exists so a family can verify what they are buying before they hand over savings: GPS boundaries, land passports, escrow.</p></div>
 <div class="card"><span class="tag">Skills</span><h3>Digital skills in the region</h3><p>Showing young people in Fort Portal and Kyenjojo that software work is available from home, not only in Kampala.</p></div>
 <div class="card"><span class="tag">Local economy</span><h3>Local businesses online</h3><p>Hotels, clinics, hardware shops and homestays given a real web presence, which turns search traffic into customers for the local economy.</p></div>
</div>
{edit("Add your impact numbers", "Add anything measurable: businesses served, jobs created, students trained, free sites built for community organisations. If you keep a simple count, this page becomes evidence.")}
''')

imp += section("community", "COMMUNITY DEVELOPMENT", "Where I come from", f'''
<div class="prose">
 <p>Fort Portal and Kyenjojo are home. The businesses there are the first clients, the first case studies and the first beneficiaries: hotels, clinics, hardware shops, homestays and community organisations that needed a real web presence and could not afford an agency in Kampala.</p>
 <p>He also builds for community organisations, including work for the <a href="https://western-youth-tech-foundation.vercel.app" target="_blank" rel="noopener">Western Youth Tech Foundation</a> and a free destination guide to <a href="https://asiimwe3.github.io/fort-portal-tourism/" target="_blank" rel="noopener">Visit Fort Portal</a> that sends visitors to local businesses.</p>
</div>
''', band=True)

imp += section("youth", "YOUTH EMPOWERMENT", "For the ones coming after", f'''
<div class="prose">
 <blockquote>You do not need permission to build. You need a problem you care about and the discipline to finish something small.</blockquote>
 <p>The message he gives young people in western Uganda is the one his own record demonstrates: start before you are ready, ship something real, publish it, and let the work answer the questions about your age.</p>
</div>
<div class="btn-row" style="justify-content:flex-start">
 <a class="btn" href="article-youth-tech.html">Read: You do not need permission to build</a>
 <a class="btn ghost" href="contact.html">Invite me to speak</a>
</div>
''')

add("impact.html", "Impact, leadership and youth empowerment | Asiimwe Derick",
    "Leadership, mentorship, social impact, community development and youth empowerment work by Asiimwe Derick in Fort Portal and Kyenjojo, Uganda.",
    "impact leadership mentorship social community youth empowerment uganda", imp)

# ============================== WRITING ==============================
writ = page_head_block("Writing", '<a href="writing.html">Writing</a>', "07 / THINKING",
  "Writing it down<br><em>as I learn it.</em>",
  "Technology, business, leadership and ideas. Short, plain, and written from the work rather than around it.",
  [("tech","Technology"),("business","Business &amp; entrepreneurship"),("leadership","Leadership &amp; life"),("ideas","Ideas &amp; future")])

writ += section("tech", "TECHNOLOGY ARTICLES", "Building software for Uganda", f'''
{cards([
 ("Technology","Why Ugandan software has to work offline first","Most software assumes fast internet and a card. Most Ugandan businesses have neither. How to design for the conditions that actually exist.","article-offline-first.html","Read the article"),
 ("Technology","What a search engine taught me about relevance","Building a multi-source search tool: why ten sources beat one, and why the ranking is harder than the crawling.","writing.html","Coming next"),
 ("Technology","Payments are a product decision","PesaPal, mobile money and the difference between a checkout that converts and one that loses the sale.","writing.html","Coming next"),
])}
''')

writ += section("business", "BUSINESS &amp; ENTREPRENEURSHIP", "Building companies here", f'''
{cards([
 ("Business","The fear in buying land, and what technology can do about it","Land disputes are an information problem before they are a legal one, and information problems can be engineered.","article-land-trust.html","Read the article"),
 ("Business","Software, land and stocks: three roads to wealth","Comparing the three vehicles honestly: ceilings, liquidity, control, and how I stack them as a young entrepreneur with billion-scale ambition.","article-software-land-stocks.html","Read the essay"),
 ("Business","Why I stopped selling subscriptions to a marketplace with no buyers","A pricing lesson from Sageco Evergreen: liquidity first, subscriptions later.","writing.html","Coming next"),
 ("Business","Commission beats subscription when trust is the product","What tour operators and brokers taught me about distribution in Uganda.","writing.html","Coming next"),
])}
''', band=True)

writ += section("leadership", "LEADERSHIP &amp; LIFE LESSONS", "What running things teaches", f'''
{cards([
 ("Youth","You do not need permission to build","A note to young people in western Uganda waiting for a degree, a job or a title before they start.","article-youth-tech.html","Read the article"),
 ("Leadership","Character before titles","Why I would rather be trusted than impressive, and what that costs in practice.","about.html#philosophy","Read the manifesto"),
 ("Leadership","Running several ventures while still in school","The honest version of the constraint: what gets dropped, what cannot, and how to protect the work that matters.","journey.html","See the journey"),
])}
''')

writ += section("ideas", "IDEAS &amp; FUTURE INNOVATIONS", "What I think comes next", f'''
<div class="cards">
 <div class="card"><span class="tag">Idea</span><h3>Voice as the next interface</h3><p>If software can be described out loud, the number of people who can build with it multiplies. Voice-first development is an accessibility story before it is a productivity one.</p></div>
 <div class="card"><span class="tag">Idea</span><h3>Verification as infrastructure</h3><p>Land, goods, qualifications, businesses: whoever makes verification cheap and portable unlocks the transactions everyone else avoids.</p></div>
 <div class="card"><span class="tag">Idea</span><h3>Offline-first AI</h3><p>An assistant that keeps working when the connection drops is worth more in Uganda than a smarter one that needs 5G.</p></div>
 <div class="card"><span class="tag">Idea</span><h3>Patient capital for African founders</h3><p>The investor he wants to become: patient, transparent, and useful beyond the cheque. <a href="vision.html">Vision 2040</a>.</p></div>
</div>
{edit("Publish on a schedule", "Pick one slot a week and keep it. The three published pieces are linked above; the marked items are ready to be written next.")}
''', band=True)

add("writing.html", "Writing: technology, business and leadership | Asiimwe Derick",
    "Articles by Asiimwe Derick on technology in Uganda, business and entrepreneurship, leadership and ideas: offline-first software, land verification and youth in tech.",
    "writing blog articles insights technology business leadership ideas", writ)

# ---------------------------- ARTICLE 1 ----------------------------
a1 = page_head_block("Article", '<a href="writing.html">Writing</a><span>/</span>Technology', "TECHNOLOGY · ESSAY",
  "Why Ugandan software<br><em>has to work offline first.</em>",
  "Most software sold here assumes fast internet, a card and someone on staff to administer it. Most Ugandan businesses have none of those things. Designing for that reality is not a compromise, it is the product.")
a1 += f'''<section class="section wrap"><div class="prose">
 <p>Walk into a shop in Kyenjojo and watch what happens when the internet drops. The till still works because it is a book. The stock still counts because it is in the owner's head. The business keeps running because it never depended on a connection in the first place.</p>
 <p>Then watch the same shop try a cloud point-of-sale system sold to them by someone in Kampala. It works beautifully until the line drops, and then it is a very expensive paperweight with a login screen.</p>
 <h3>The assumption nobody states</h3>
 <p>Most software is designed against an implicit checklist: reliable electricity, reliable broadband, a bank card, an English-speaking administrator, and someone who can debug a sync error. In much of Uganda, one or more of those is missing on any given day.</p>
 <p>When a product fails here, the usual explanation is "the market is not ready". That is almost always wrong. The product was not ready for the market.</p>
 <h3>What offline-first actually means</h3>
 <p>Offline-first is not a feature you bolt on. It changes the architecture: the local device is the source of truth, and the network is an optimisation. Concretely, that means three decisions.</p>
 <ul>
  <li><strong>Local writes always succeed.</strong> A sale, a stock count, a student payment records immediately on the device and syncs when it can.</li>
  <li><strong>Conflicts are resolved by rules, not by asking the user.</strong> A shopkeeper should never be shown a merge dialogue. The system decides, and logs what it decided.</li>
  <li><strong>The interface tells the truth about state.</strong> "Saved on this phone, waiting to sync" is honest. A spinner that never resolves is not.</li>
 </ul>
 <h3>Price is part of the design</h3>
 <p>The second assumption is money. If software costs more than the problem it solves, it is not a solution; it is a subscription the business will cancel in month three. Pricing for the person you claim to serve means pricing against their margin, not against a competitor's list price.</p>
 <h3>Support is the last mile</h3>
 <p>A handover that ends with a link is not a handover. Small businesses do not have an IT department, so the person who built the system has to be reachable after launch. That is not generosity; it is what makes the sale real.</p>
 <h3>The result</h3>
 <p>When you get this right, the technology disappears into the business. The owner keeps records they can trust, the numbers are available when a loan officer asks, and nobody has to explain what a sync conflict is. That is what <a href="ventures.html#derycode">DeryCode</a> builds, and it is why <a href="ventures.html#products">DeryAccount</a> was designed around the connection dropping rather than assuming it will not.</p>
 <blockquote>Software that needs perfect conditions is software for someone else's country.</blockquote>
 <p><a class="btn ghost" href="writing.html">Back to all writing</a></p>
</div></section>
'''
add("article-offline-first.html", "Why Ugandan software has to work offline first | Asiimwe Derick",
    "Most software assumes fast internet and a card. Most Ugandan businesses have neither. How to design software for the conditions that actually exist, by Asiimwe Derick.",
    "offline first software uganda derycode design architecture small business", a1, )

# ---------------------------- ARTICLE 2 ----------------------------
a2 = page_head_block("Article", '<a href="writing.html">Writing</a><span>/</span>Business', "BUSINESS · ESSAY",
  "The fear in buying land,<br><em>and what technology can do about it.</em>",
  "Land disputes are not only a legal problem. They are an information problem, and information problems can be engineered against.")
a2 += '''<section class="section wrap"><div class="prose">
 <p>Ask anyone in western Uganda about buying land and you will hear the same sentence: "You have to be careful." That sentence is doing a lot of work. It is carrying the cost of a system where the buyer holds almost all the risk.</p>
 <h3>What the buyer cannot see</h3>
 <ul>
  <li>Whether the seller actually owns the land, and whether anyone else has a claim on it</li>
  <li>Where the boundary really runs, as opposed to where the seller says it runs</li>
  <li>Whether the same plot has already been sold to someone else</li>
  <li>Whether the money will move before or after verification</li>
 </ul>
 <p>None of that is a legal mystery. It is missing information, delivered late and unevenly, which is exactly the kind of problem software is good at.</p>
 <h3>Three things technology can do</h3>
 <p><strong>1. Make verification visible.</strong> A listing that carries a GPS-verified boundary and a document record turns a verbal claim into something a buyer can inspect before paying.</p>
 <p><strong>2. Put payment behind the evidence.</strong> Escrow changes the order of operations: money is committed, but released against milestones rather than against a promise.</p>
 <p><strong>3. Give the plot a history.</strong> A digital land passport, with boundaries, ownership history and documents attached, makes the next sale cheaper than this one, because the evidence already exists.</p>
 <h3>What technology cannot do</h3>
 <p>It cannot replace a title registry, a surveyor or a court. Anyone selling you a platform that claims to is selling you something else. What a platform can do is make the honest transaction easier than the dishonest one, which is the only durable way to change behaviour.</p>
 <p>That is the design brief behind <a href="ventures.html#sageco">Sageco Evergreen</a>: verified listings, GPS boundaries, escrow-protected payments and land passports in one place, so trust becomes a feature of the product rather than a favour from the seller.</p>
 <blockquote>The goal is not a clever platform. The goal is a family that does not lose its savings twice.</blockquote>
 <p><a class="btn ghost" href="writing.html">Back to all writing</a></p>
</div></section>
'''
add("article-land-trust.html", "The fear in buying land, and what technology can do about it | Asiimwe Derick",
    "Land disputes in Uganda are an information problem before they are a legal one. How verification, GPS boundaries, escrow and land passports change the risk for buyers.",
    "land buying uganda verification escrow gps boundaries sageco property", a2)

# ---------------------------- ARTICLE 3 ----------------------------
a3 = page_head_block("Article", '<a href="writing.html">Writing</a><span>/</span>Youth', "YOUTH · NOTE",
  "You do not need<br><em>permission to build.</em>",
  "A note to young people in western Uganda who are waiting for a degree, a job or a title before they start.")
a3 += '''<section class="section wrap"><div class="prose">
 <p>I am twenty. I am still in school. I run several ventures in the hours that school leaves me. I am not telling you that to impress you; I am telling you because the usual advice, wait until you are qualified, is the reason a lot of good builders never start.</p>
 <h3>Nobody is coming to appoint you</h3>
 <p>There is no committee that decides when you are ready. The first client does not check your certificate; they check whether the thing works. The first customer does not care how old you are; they care whether you answered the phone.</p>
 <h3>Start with something small and real</h3>
 <p>Not a startup. A shop that needs a price list. A school that needs a fees record. A hotel that needs a page with rooms and a phone number. Small, real, finished work compounds in a way that a plan never does.</p>
 <h3>Publish the evidence</h3>
 <p>Put the work where people can see it. A live link beats a claim. When I say 59 sites are running, you can open them. That is the whole trick: make your record checkable, and the conversation about your age ends quickly.</p>
 <h3>Learn the boring parts</h3>
 <p>Payments, support, records, permissions. The interesting part of building is the idea. The durable part is the maintenance, and maintenance is where trust is earned.</p>
 <h3>Open the door behind you</h3>
 <p>When you get your first client, help someone else get theirs. That is how a region gets a technology industry instead of one lucky person.</p>
 <blockquote>You need a problem you care about, and the discipline to finish something small.</blockquote>
 <p><a class="btn ghost" href="writing.html">Back to all writing</a> <a class="btn ghost" href="impact.html">Youth and mentorship work</a></p>
</div></section>
'''
add("article-youth-tech.html", "You do not need permission to build | Asiimwe Derick",
    "A note to young people in western Uganda waiting for a degree, a job or a title before they start building: start with something small and real, and publish the evidence.",
    "youth uganda young builders entrepreneurship advice start", a3)

# ---------------------------- ARTICLE 4: software, land, stocks ----------------------------
a4 = page_head_block("Article", '<a href="writing.html">Writing</a><span>/</span>Business', "BUSINESS · ESSAY",
  "Software, land<br><em>and stocks.</em>",
  "Three roads a young entrepreneur can take to serious wealth, compared honestly, and how I stack them.")
a4 += '''<section class="section wrap"><div class="prose">
 <p>I am twenty. I want to reach a scale that people raise an eyebrow at. So I have to be honest about the three vehicles in front of me: software, real estate and stocks. Each one builds wealth in a completely different way, and confusing them is how young people lose money.</p>
 <h3>Software: the highest ceiling, the fastest clock</h3>
 <p>A product can serve a hundred customers or a million with roughly the same code. Margins are high, distribution is cheap and the asset keeps working while you sleep. Of the three, it is the only one where a person with no capital can start with nothing but a laptop.</p>
 <p>The catch is that software has no intrinsic value. It is worth what customers pay for it, and nobody pays for a demo. Every month you are re-earning the right to exist. That is why I obsess over clients who renew, not launches that trend.</p>
 <h3>Real estate: the slowest, the most solid, the most borrowed-against</h3>
 <p>Land does not pivot. It does not need a marketing budget. In Uganda it appreciates, it produces rent, and a bank will lend against it in a way no bank will lend against my code. It is also the asset ordinary families trust, which is exactly why fraud thrives in it.</p>
 <p>The catch is liquidity: you cannot sell a plot on a Tuesday to make payroll, and a bad title can destroy a lifetime of savings. That is the reason Sageco Evergreen exists, verification and escrow are the product, not a feature.</p>
 <h3>Stocks: the most liquid, the least control</h3>
 <p>Stocks ask the least of my time and give the least of my control. I can enter and exit in minutes, and compounding quietly does the work. For a young person, it is the most forgiving place to learn how capital behaves, because mistakes are cheap and reversible.</p>
 <p>The catch is that you own a fraction of decisions other people make. It can build wealth, but it will not build a builder. It is a place for money to wait without sleeping.</p>
 <h3>How I stack them</h3>
 <p>Software gives me cash flow and ownership. Real estate gives me security and leverage. Stocks give me liquidity and patience. None of them is a shortcut, and any one of them alone will cap you: a coder with no assets stays a coder, a landlord with no cash flow is trapped, and a trader with no business never learns to build.</p>
 <p>Stacked and compounded over twenty years, from Fort Portal, that is how an ambitious young entrepreneur reaches billionaire scale without gambling everything on one bet.</p>
 <blockquote>Smart people are doubted at the start. Results do the talking.</blockquote>
 <p class="muted">This is how I think about building, not financial advice.</p>
 <p><a class="btn ghost" href="writing.html">Back to all writing</a> <a class="btn ghost" href="investors.html">For investors</a></p>
</div></section>
'''
add("article-software-land-stocks.html", "Software, land and stocks: three roads to wealth | Asiimwe Derick",
    "Comparing software, real estate and stocks as wealth vehicles for a young African entrepreneur with billion-scale ambition: ceilings, liquidity, control and how Derick stacks all three.",
    "software vs real estate vs stocks wealth young entrepreneur uganda investing ambition", a4)

# ============================== VISION ==============================
vis = page_head_block("Vision", '<a href="vision.html">Vision</a>', "08 / DIRECTION",
  "From builder to<br><em>global investor.</em>",
  "Goals, the 1 to 20 year roadmap, Vision 2030 and the financial journey behind Vision 2040. A direction, not a claim.",
  [("now","Where I am"),("roadmap","Roadmap"),("v2030","Vision 2030"),("v2040","Vision 2040"),("money","Financial journey")])

vis += section("now", "WHERE I AM", "The starting point, honestly", f'''
<div class="prose">
 <p>Several ventures operating, one of them with paying customers and a live payment rail, 59 sites and apps built, and a school timetable to work around. Early stage, not paper stage.</p>
 <p>The gap between here and Vision 2040 is not ambition. It is capital, team and time, in that order.</p>
</div>
<div class="stat-row">
 <div class="stat-box"><b>2</b><span>Companies operating today</span></div>
 <div class="stat-box"><b>59</b><span>Live products and sites built</span></div>
 <div class="stat-box"><b>63</b><span>Verified property listings live</span></div>
 <div class="stat-box"><b>2040</b><span>The year the vision points at</span></div>
</div>
''')

vis += section("roadmap", "ROADMAP", "1, 5, 10 and 20 years", f'''
{timeline([
 ("1 year — 2027","Make both companies pay properly","Sageco Evergreen with verified inventory at scale and broker partnerships; DeryCode with recurring support contracts rather than one-off builds. Close the first outside investment round."),
 ("5 years — 2031","Build the operating machine","A team that runs delivery without him in every detail, a property platform that is the default verified route to land in western Uganda, and a portfolio of small-business software with recurring revenue."),
 ("10 years — 2036","From operator to allocator","Start investing in other founders while still operating: small cheques, real mentorship, and a track record of returns that is not a story about potential."),
 ("20 years — 2046","Global investor, African focus","Capital deployed across Africa and beyond, with a portfolio of companies solving the problems he grew up inside. The investor he needed when he started."),
])}
''', band=True)

vis += section("v2030", "VISION 2030", "The next checkpoint", f'''
<div class="prose">
 <p>By 2030 the goal is simple to state and hard to do: <strong>verification and affordable software become normal in western Uganda, because his companies made them normal.</strong></p>
 <ul>
  <li>A property platform where a first-time buyer can complete a verified purchase without a middleman holding their hand</li>
  <li>Hundreds of small businesses running software they own, can afford and can operate offline</li>
  <li>A team of Ugandan engineers and operators earning from work that did not exist here five years earlier</li>
  <li>An investment record, not an investment ambition</li>
 </ul>
</div>
{edit("Add your Vision 2030 numbers", "Put specific targets against each line: listings verified, businesses served, jobs created, revenue. Specific targets are what make a vision checkable.")}
''')

vis += section("v2040", "VISION 2040", "The long direction", f'''
<div class="prose">
 <p>My long-term ambition is to work as an investor on the world stage, backing the people who build. I want to earn my way to that table: build companies that actually make money and actually help people, learn how capital flows, then put that capital behind African founders solving African problems. Patient money, trusted partnerships, deals done on transparency.</p>
 <p>I want to be the investor I needed when I was starting out. Vision 2040 is a direction, not a claim: a commitment to keep learning, keep building and keep lifting others as I grow.</p>
</div>
''', band=True)

vis += section("money", "FINANCIAL &amp; WEALTH-BUILDING JOURNEY", "How the money is meant to work", f'''
<div class="prose">
 <p>The plan is unglamorous: earn from software, reinvest into products that compound, avoid debt that assumes growth he cannot control, and keep the companies able to pay their own bills before chasing capital.</p>
 <p><strong>Three rules he works by:</strong> price work honestly, keep costs small enough to survive a bad quarter, and never let a client's project depend on money he does not have yet.</p>
</div>
{edit("Add the numbers when you are ready", "Revenue, reinvestment, savings and the first investment target. Publishing this is optional, but if you want to be taken seriously as an investor, a track record of your own capital discipline is the strongest evidence you can show.")}
<div class="cards">
 <div class="card"><span class="tag">Income</span><h3>Software delivery</h3><p>Client builds and support contracts through DeryCode, the base that funds everything else.</p></div>
 <div class="card"><span class="tag">Compounding</span><h3>Products with recurring revenue</h3><p>Subscriptions and transaction fees from products like DeryAccount and Sageco, which grow without a new client each month.</p></div>
 <div class="card"><span class="tag">Allocation</span><h3>Investing in founders</h3><p>The long game: small cheques into companies he understands, with the discipline learned from building his own.</p></div>
</div>
''')

add("vision.html", "Vision, goals and roadmap to 2040 | Asiimwe Derick",
    "Asiimwe Derick's vision: 1, 5, 10 and 20 year goals, Vision 2030, Vision 2040, and the financial journey from builder to global investor.",
    "vision goals roadmap 2030 2040 investor wealth plan", vis)

# ============================== SPEAKING ==============================
spk = page_head_block("Speaking", '<a href="speaking.html">Speaking &amp; media</a>', "09 / VOICE",
  "On stage,<br><em>on record.</em>",
  "Speaking topics, interviews, press and the media kit. Everything an organiser or journalist needs in one place.",
  [("topics","Speaking topics"),("events","Events"),("press","Press &amp; interviews")])

spk += section("topics", "SPEAKING", "What I talk about", f'''
<div class="cards">
 <div class="card"><span class="tag">Technology</span><h3>Software for the conditions that exist</h3><p>Offline-first design, pricing for small businesses, and why products built for Silicon Valley fail in Kyenjojo.</p></div>
 <div class="card"><span class="tag">Business</span><h3>Building before you are ready</h3><p>Running several ventures at twenty: what it takes, what it costs, and the discipline of shipping something finished.</p></div>
 <div class="card"><span class="tag">Property</span><h3>Trust as infrastructure</h3><p>How verification, GPS boundaries and escrow change the risk of buying land in Uganda.</p></div>
 <div class="card"><span class="tag">Youth</span><h3>The case for building from home</h3><p>Why technology work can happen in Fort Portal, not only Kampala, and what young people need to start.</p></div>
 <div class="card"><span class="tag">AI</span><h3>AI where the connection drops</h3><p>What useful AI looks like in markets with unreliable power and data, and what to ignore.</p></div>
 <div class="card"><span class="tag">Investing</span><h3>Patient capital for African founders</h3><p>What he looks for as a founder, and the investor he intends to become.</p></div>
</div>
<p><a class="btn" href="mailto:{EMAIL}?subject=Speaking%20invitation">Invite me to speak</a></p>
''')

spk += section("events", "EVENTS", "Where I've spoken", f'''
{edit("Add your events", "List each event with the date, the host organisation, the audience and the topic. Even two or three entries turn this page from an offer into a record. Until then, this section states availability rather than history.")}
<div class="prose">
 <p><strong>Available for:</strong> university and school talks, founder and startup events, business association meetings, technology meetups, youth programmes and panel discussions. In person across Uganda, or remote.</p>
 <p><strong>Formats:</strong> 20 to 40 minute keynote, panel contribution, workshop on shipping software in low-resource settings, or a fireside conversation.</p>
</div>
''', band=True)

spk += section("press", "MEDIA &amp; PRESS", "Interviews and coverage", f'''
{edit("Add press coverage", "Add links to any article, radio segment, podcast or interview that mentions you or your companies. If there is none yet, keep this page as the invitation and remove the placeholder before publishing widely.")}
<div class="prose">
 <p><strong>For journalists:</strong> short and long bios, photography and company facts are in the <a href="mediakit.html">media kit</a>. Direct enquiries to <a href="mailto:{EMAIL}?subject=Media%20enquiry">{EMAIL}</a>.</p>
</div>
''')

add("speaking.html", "Speaking, media and press | Asiimwe Derick",
    "Speaking topics, event appearances, interviews and press for Asiimwe Derick: technology in Uganda, building young, land verification and youth in tech.",
    "speaking events talks media press interviews journalist", spk)

# ============================== GALLERY ==============================
gal = page_head_block("Gallery", '<a href="gallery.html">Gallery &amp; life</a>', "10 / LIFE",
  "The human<br><em>side of the work.</em>",
  "Photos, travel, interests, habits and the books that shaped the thinking.",
  [("photos","Photos"),("travel","Travel &amp; experiences"),("interests","Interests &amp; lifestyle"),("growth","Personal development"),("books","Books &amp; resources")])

gal += section("photos", "GALLERY", "Photos", f'''
<div class="gallery">
 <figure><img src="assets/hoodie-laptop.webp" alt="Derick working on his laptop in a DeryCode hoodie" loading="lazy"><figcaption>Working, most days</figcaption></figure>
 <figure><img src="assets/standing.webp" alt="Derick standing outdoors in Kyenjojo" loading="lazy"><figcaption>Kyenjojo, home ground</figcaption></figure>
 <figure><img src="assets/rooftop.webp" alt="Derick on a rooftop in Fort Portal" loading="lazy"><figcaption>Fort Portal rooftops</figcaption></figure>
 <figure><img src="assets/terrace.webp" alt="Derick on a terrace during a work session" loading="lazy"><figcaption>Between meetings</figcaption></figure>
</div>
{edit("Add video and more photos", "Add site visits, client launches, events and short clips. Photos of real work outperform posed portraits for trust, and they are the easiest content to keep current.")}
''')

gal += section("travel", "TRAVEL &amp; EXPERIENCES", "Where the work has taken me", f'''
<div class="prose">
 <p>Most travel is work travel: client sites, deliveries and meetings across western Uganda, from Kyenjojo and Fort Portal to Kampala. The places that shaped him most are the ones he did not have to travel to: the trading centres, the farms and the land deals that became the case studies.</p>
</div>
{edit("Add your travels", "Places you have been, and one line on what each one changed about how you think. This is optional but humanising.")}
''', band=True)

gal += section("interests", "PERSONAL INTERESTS &amp; LIFESTYLE", "Outside the work", f'''
<div class="cards">
 <div class="card"><span class="tag">Interest</span><h3>Building things that run</h3><p>Side projects are the hobby: calculators, search tools, editors. The line between work and play is thin.</p></div>
 <div class="card"><span class="tag">Interest</span><h3>Technology and AI</h3><p>Reading about and testing new models, tools and interfaces, mostly to answer one question: does this help someone here?</p></div>
 <div class="card"><span class="tag">Interest</span><h3>Property and land</h3><p>Not abstract: how land is priced, verified and developed in western Uganda.</p></div>
 <div class="card"><span class="tag">Interest</span><h3>Football and community</h3><p>Local football, and the informal networks where business actually gets done.</p></div>
</div>
{edit("Correct these interests", "These are drawn from your work. Replace or add what is actually true for you: music, faith, sport, cooking, photography, whatever it is.")}
''')

gal += section("growth", "PERSONAL DEVELOPMENT &amp; PRODUCTIVITY", "How I work", f'''
<div class="prose">
 <p><strong>Time:</strong> school hours are fixed, so the business hours are early mornings, evenings and weekends. That constraint forces prioritisation: one or two things per day, finished.</p>
 <p><strong>Tools:</strong> a laptop, a phone, Git, Vercel, Supabase, and a notes system that survives interruption.</p>
 <p><strong>Rules:</strong> ship something visible each week, write down decisions, and never let a client wait without an update.</p>
</div>
''', band=True)

gal += section("books", "BOOKS &amp; LEARNING RESOURCES", "What shaped the thinking", f'''
{edit("Add your real reading list", "List the books, courses and people that actually shaped how you build. Five honest entries beat fifty recommendations, and readers trust specificity.")}
<div class="prose">
 <p>The learning is mostly practical: documentation, source code, and the businesses themselves. Formal reading clusters around company building, capital and product design.</p>
</div>
''')

add("gallery.html", "Gallery, travel and interests | Asiimwe Derick",
    "Photos, travel and experiences, personal interests, productivity habits and learning resources: the human side of Asiimwe Derick's work in Uganda.",
    "gallery photos travel interests lifestyle books learning habits", gal)

# ============================== SERVICES ==============================
svc = page_head_block("Services", '<a href="services.html">Services</a>', "11 / WORK WITH ME",
  "What working<br><em>together looks like.</em>",
  "Services, consulting, collaboration and partnerships. Clear scopes, honest pricing, and work that keeps running after launch.",
  [("services","Services"),("services","Services"),("consult","Consulting"),("partner","Collaboration"),("proof","Testimonials")])

svc += section("services", "SERVICES &amp; CONSULTING", "What I do for clients", f'''
<div class="cards">
 <div class="card"><span class="tag">Build</span><h3>Websites that earn</h3><p>Fast, mobile-first sites for hotels, shops, clinics and services: room and product pages, direct booking or ordering, payments, and technical SEO so the site is found. Delivered by DeryCode.</p><a class="more" href="https://derycode.online" target="_blank" rel="noopener">derycode.online ↗</a></div>
 <div class="card"><span class="tag">Build</span><h3>Offline-first business systems</h3><p>Records, stock, invoicing and accounting that keep working when the connection drops, priced for small businesses rather than enterprises.</p></div>
 <div class="card"><span class="tag">Build</span><h3>AI inside the product</h3><p>Assistants and search that answer real customer questions, trained on your own content rather than the open internet.</p></div>
 <div class="card"><span class="tag">Consult</span><h3>Digital presence audit</h3><p>What is stopping customers finding you: search visibility, Maps listing, speed, structure, and the small technical faults that quietly cost sales.</p></div>
 <div class="card"><span class="tag">Consult</span><h3>Property and payment technology</h3><p>Verification flows, escrow logic, mobile money and PesaPal integration, designed with the compliance question asked early.</p></div>
 <div class="card"><span class="tag">Consult</span><h3>Growth for hospitality and retail</h3><p>Direct booking instead of commission, tour operator outreach, review recovery and local search, the work that turns a website into bookings.</p></div>
</div>
<p><a class="btn" href="mailto:{EMAIL}?subject=Project%20enquiry">Start a project enquiry</a> <a class="btn ghost" href="{WA}" target="_blank" rel="noopener">WhatsApp 0762 306 675</a></p>
''')

svc += '<div id="consult"></div>'
svc += section("partner", "COLLABORATION &amp; PARTNERSHIPS", "Who I want to work with", f'''
<div class="cards">
 <div class="card"><span class="tag">Partners</span><h3>Tour operators and travel</h3><p>Accommodation partners for Kibale and Fort Portal itineraries, and digital work for lodges that want direct bookings.</p></div>
 <div class="card"><span class="tag">Partners</span><h3>Brokers and land professionals</h3><p>Verified inventory for Sageco Evergreen, and partnerships that make verification the default in western Uganda.</p></div>
 <div class="card"><span class="tag">Partners</span><h3>Schools and training institutions</h3><p>Software for fees and records, plus practical sessions for students learning to build.</p></div>
 <div class="card"><span class="tag">Partners</span><h3>Funders and investors</h3><p>Angel and strategic investors who want returns and measurable impact in the same deal. <a href="investors.html">Details</a>.</p></div>
</div>
''', band=True)

svc += section("proof", "TESTIMONIALS &amp; RECOMMENDATIONS", "What clients say", f'''
{edit("Add client testimonials", "Ask three clients for two sentences each: the problem, and what changed. Quote them with name, business and town. This section is deliberately empty rather than invented, because fake testimonials are the fastest way to lose the trust the rest of the site is built to earn.")}
<div class="prose"><p>Until those arrive, the evidence is the work itself: <a href="projects.html#cases">three detailed case studies</a> with live links, and <a href="projects.html#clients">every client site</a> open for inspection.</p></div>
''')

add("services.html", "Services, consulting and collaboration | Asiimwe Derick",
    "Websites, offline-first business systems, AI integration and digital presence consulting through DeryCode Technologies, plus partnership and collaboration options.",
    "services consulting websites offline software ai partnership collaboration", svc)

# ============================== INVESTORS ==============================
inv = page_head_block("Investors", '<a href="investors.html">For investors</a>', "12 / CAPITAL",
  "Invest in what<br><em>we're building.</em>",
  "DeryCode Technologies and Sageco Evergreen are open to angel and strategic investors who want commercial returns and measurable social impact in the same deal.",
  [("thesis","The opportunity"),("numbers","Numbers"),("ask","What I'm looking for"),("contact-inv","Talk to me")])

inv += section("thesis", "THE OPPORTUNITY", "The ventures, one thesis", f'''
<div class="cards">
 <div class="card"><span class="tag">DeryCode Technologies</span><h3>Software for the businesses everyone else ignores</h3><p>Offline-first systems and websites for Ugandan small businesses, sold at a price the market can pay and supported after launch. Recurring support contracts and products like DeryAccount sit on top of a delivery business that already has clients.</p></div>
 <div class="card"><span class="tag">Sageco Evergreen</span><h3>Trust as a product in a $ billions land market</h3><p>Verified listings, GPS boundaries, escrow-protected payments, land passports and fractional investment. Live with 63 listings, a production payment rail and paid viewings already running.</p></div>
</div>
<div class="prose">
 <p><strong>The shared thesis:</strong> in markets with weak infrastructure, the winner is whoever makes the honest transaction the easy one. Verification for land, affordability for software. Both are unglamorous, defensible, and hard to copy without being on the ground.</p>
</div>
''')

inv += section("numbers", "NUMBERS", "Where things stand", f'''
<div class="stat-row">
 <div class="stat-box"><b>59</b><span>Live sites and apps built and running</span></div>
 <div class="stat-box"><b>63</b><span>Verified property listings live</span></div>
 <div class="stat-box"><b>2</b><span>Companies operating</span></div>
 <div class="stat-box"><b>5</b><span>Sectors served</span></div>
</div>
{edit("Add financial detail for serious conversations", "Revenue, growth, unit economics and the round size belong in the deck, not on a public page. Keep this page as the door, and send the numbers directly.")}
''', band=True)

inv += section("ask", "WHAT I'M LOOKING FOR", "The ask, stated plainly", f'''
<div class="prose">
 <p>I'm opening DeryCode Technologies and Sageco Evergreen to angel and strategic investors who want commercial returns and measurable social impact in the same deal. Both companies are early stage and already operating, not ideas on paper.</p>
 <p><strong>Beyond money, what helps:</strong> distribution (property, hospitality and retail networks), operating experience in payments or property, and patience measured in years rather than quarters.</p>
 <p><strong>What you get:</strong> direct access to the founder, published numbers, and a partner who has already built and shipped 59 live products.</p>
</div>
<div class="btn-row" style="justify-content:flex-start">
 <a class="btn" href="mailto:{EMAIL}?subject=Investing%20in%20DeryCode%20and%20Sageco%20Evergreen">Request the deck</a>
 <a class="btn ghost" href="contact.html">Talk to me first</a>
</div>
''')

inv += section("contact-inv", "NEXT STEP", "How to start", f'''
<div class="prose"><p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> with a line about your focus, or WhatsApp 0762 306 675. I answer personally, and I will tell you plainly if the fit is wrong.</p></div>
''', band=True)

add("investors.html", "Investment opportunities | DeryCode Technologies and Sageco Evergreen",
    "Asiimwe Derick is open to angel and strategic investors in DeryCode Technologies and Sageco Evergreen: the thesis, the numbers, and how to request the deck.",
    "investors investment angel funding deck derycode sageco capital", inv)

# ============================== CONTACT ==============================
con = page_head_block("Contact", '<a href="contact.html">Contact</a>', "13 / SAY HELLO",
  "Start a<br><em>conversation.</em>",
  "Business, partnership, media or investment: pick the route that fits and it reaches him directly.",
  [("routes","Ways to reach me"),("inquiries","Inquiry types"),("socials","Social &amp; community"),("newsletter","Newsletter"),("qr","QR &amp; sharing")])

con += section("routes", "CONTACT", "Direct lines", f'''
<div class="cards">
 <div class="card"><span class="tag">Email</span><h3>{EMAIL}</h3><p>The best route for anything detailed. Answered personally, usually within a day.</p><a class="more" href="mailto:{EMAIL}">Send an email →</a></div>
 <div class="card"><span class="tag">WhatsApp</span><h3>0762 306 675</h3><p>Fastest for quick questions, quotes and anything time-sensitive.</p><a class="more" href="{WA}" target="_blank" rel="noopener">Open WhatsApp →</a></div>
 <div class="card"><span class="tag">Location</span><h3>Kyenjojo, Uganda</h3><p>Working across Fort Portal, Kyenjojo and Kampala. Remote work welcome.</p><span class="more">East Africa Time (EAT, UTC+3)</span></div>
</div>
''')

con += section("inquiries", "INQUIRY TYPES", "Pick the right door", f'''
<div class="cards">
 <div class="card"><span class="tag">Business</span><h3>Business inquiry</h3><p>A website, software build, support contract or digital audit through DeryCode.</p><a class="more" href="mailto:{EMAIL}?subject=Business%20inquiry">Email business inquiry →</a></div>
 <div class="card"><span class="tag">Partnership</span><h3>Partnership inquiry</h3><p>Property inventory, travel and hospitality partnerships, distribution or reseller conversations.</p><a class="more" href="mailto:{EMAIL}?subject=Partnership%20inquiry">Email partnership inquiry →</a></div>
 <div class="card"><span class="tag">Media</span><h3>Media &amp; speaking</h3><p>Interviews, press, podcasts, panels and event invitations.</p><a class="more" href="mailto:{EMAIL}?subject=Media%20or%20speaking%20inquiry">Email media inquiry →</a></div>
 <div class="card"><span class="tag">Investment</span><h3>Investment inquiry</h3><p>Angel or strategic investment in DeryCode Technologies and Sageco Evergreen.</p><a class="more" href="mailto:{EMAIL}?subject=Investing%20in%20DeryCode%20and%20Sageco%20Evergreen">Email investor inquiry →</a></div>
</div>
''', band=True)

con += section("socials", "SOCIAL MEDIA &amp; COMMUNITY", "Where else to find me", f'''
<p>{chips(["GitHub","LinkedIn","WhatsApp","DeryCode.online","Sageco Evergreen"])}</p>
<div class="cards">
 <div class="card"><span class="tag">Code</span><h3>GitHub</h3><p>25+ public repositories: sites, tools and experiments.</p><a class="more" href="https://github.com/asiimwe3" target="_blank" rel="noopener">github.com/asiimwe3 ↗</a></div>
 <div class="card"><span class="tag">Company</span><h3>DeryCode Technologies</h3><p>Software, AI and websites for Ugandan businesses.</p><a class="more" href="https://derycode.online" target="_blank" rel="noopener">derycode.online ↗</a></div>
 <div class="card"><span class="tag">Company</span><h3>Sageco Evergreen</h3><p>Verified property platform: land, homes and commercial space.</p><a class="more" href="https://sageco-evergreen.vercel.app" target="_blank" rel="noopener">Open the platform ↗</a></div>
</div>
{edit("Add your LinkedIn and social profiles", "Add the exact URLs for LinkedIn, X, Instagram, Facebook and TikTok. They also belong in the schema in the page head so search engines tie the profiles to this site.")}
''')

con += section("newsletter", "NEWSLETTER", "Occasional notes, no noise", f'''
<div class="prose"><p>One email when there is something worth saying: a new article, a company milestone, or a lesson from a build. No schedule for its own sake.</p></div>
<form action="mailto:{EMAIL}" method="post" enctype="text/plain" style="max-width:560px;margin-top:14px">
 <label for="nlEmail" style="display:block;font-size:13px;color:var(--muted);margin-bottom:8px">Your email</label>
 <div style="display:flex;gap:10px;flex-wrap:wrap">
  <input id="nlEmail" name="email" type="email" required placeholder="you@example.com" style="flex:1;min-width:220px;background:var(--card);border:1px solid var(--line);border-radius:11px;color:var(--ink);padding:13px 15px;font-size:15px">
  <button class="btn" type="submit">Subscribe</button>
 </div>
 <p style="font-size:12.5px;color:var(--muted);margin-top:10px">This form opens your mail app and sends the request to Derick directly. When a mailing provider is connected, it will subscribe you automatically instead.</p>
</form>
''', band=True)

con += section("qr", "QR &amp; DIGITAL PROFILE", "Share this page in person", f'''
<div class="qrcard">
 <img src="assets/qr-site.png" alt="QR code linking to this personal website" width="170" height="170">
 <div>
  <h3 style="margin:0 0 8px">Scan to open this site</h3>
  <p style="color:var(--muted);margin:0 0 12px;max-width:52ch">Print it on a card, put it on a slide, or show it at a meeting. It opens this site, which is the single place with the biography, ventures, projects and contact routes.</p>
  <a class="btn ghost" href="assets/qr-site.png" download>Download QR code</a>
 </div>
</div>
''')

add("contact.html", "Contact Asiimwe Derick | Business, partnership, media and investment",
    "Contact Asiimwe Derick directly: email, WhatsApp, business inquiries, partnership inquiries, media and speaking requests, social profiles, newsletter and QR code.",
    "contact email whatsapp inquiry business partnership media investment newsletter qr", con)

# ============================== MEDIA KIT ==============================
mk = page_head_block("Media kit", '<a href="mediakit.html">Media kit</a>', "14 / FOR PRESS",
  "Everything you need<br><em>to write about me.</em>",
  "Approved bios, photography, brand assets, QR code, and the public archive of documents.",
  [("bios","Bios"),("assets","Photos &amp; brand"),("archive","Archive &amp; documents")])

mk += section("bios", "BIOS", "Copy and paste", f'''
<div class="prose">
 <h3>One line (25 words)</h3>
 <p>Asiimwe Derick is a Ugandan social entrepreneur, founder of DeryCode Technologies and CEO of Sageco Evergreen, building software and verified land transactions for African markets.</p>
 <h3>Short bio (60 words)</h3>
 <p>Asiimwe Derick is a social entrepreneur from Kyenjojo, Uganda, born in 2006. He founded DeryCode Technologies, which builds offline-first software and websites for Ugandan businesses, and leads Sageco Evergreen, a property platform using verified listings, GPS boundaries and escrow-protected payments. He has delivered 59 live sites and apps and is open to angel and strategic investors.</p>
 <h3>Long bio (150 words)</h3>
 <p>Asiimwe Derick is a Ugandan social entrepreneur from Kyenjojo in the west of the country. He is the founder of DeryCode Technologies, a software company building offline-first business systems, websites and AI tools for businesses that work without reliable internet or large budgets, and the CEO of Sageco Evergreen, a property platform designed to remove the fear from buying land through verified listings, GPS-verified boundaries, escrow-protected payments and digital land passports. Born in January 2006, he runs both companies while completing school, and has delivered 59 live websites and applications across property, hospitality, education, retail, health and agriculture. His stated mission is to change lives at scale, and his long-term ambition, Vision 2040, is to move from building companies to investing in the founders building Africa's future.</p>
</div>
''')

mk += section("assets", "PHOTOS &amp; BRAND", "Approved assets", f'''
<div class="gallery">
 <figure><img src="assets/hoodie-laptop.webp" alt="Derick working on a laptop" loading="lazy"><figcaption><a href="assets/hoodie-laptop.webp" download>hoodie-laptop.webp</a></figcaption></figure>
 <figure><img src="assets/standing.webp" alt="Derick standing outdoors" loading="lazy"><figcaption><a href="assets/standing.webp" download>standing.webp</a></figcaption></figure>
 <figure><img src="assets/rooftop.webp" alt="Derick on a rooftop" loading="lazy"><figcaption><a href="assets/rooftop.webp" download>rooftop.webp</a></figcaption></figure>
 <figure><img src="assets/terrace.webp" alt="Derick on a terrace" loading="lazy"><figcaption><a href="assets/terrace.webp" download>terrace.webp</a></figcaption></figure>
</div>
<p style="margin-top:16px">{chips(["Amber #F2B44A","Navy #0B0F17","Cream #F3EFE7","Space Grotesk","DM Sans"])}</p>
<div class="qrcard" style="margin-top:18px">
 <img src="assets/qr-site.png" alt="QR code for this website" width="170" height="170">
 <div><h3 style="margin:0 0 8px">QR code</h3><p style="color:var(--muted);margin:0 0 12px">For print, slides and business cards. Opens this website.</p><a class="btn ghost" href="assets/qr-site.png" download>Download QR</a></div>
</div>
''', band=True)

mk += section("archive", "PERSONAL DIGITAL ARCHIVE &amp; PUBLIC DOCUMENTS", "The record", f'''
<div class="cards">
 <div class="card"><span class="tag">Document</span><h3>Curriculum vitae</h3><p>The current CV, one page, in PDF.</p><a class="more" href="assets/derick-asiimwe-cv.pdf" download>Download CV →</a></div>
 <div class="card"><span class="tag">Archive</span><h3>Live project index</h3><p>Every public project, with links that can be checked today.</p><a class="more" href="projects.html">Open the index →</a></div>
 <div class="card"><span class="tag">Archive</span><h3>Company facts</h3><p>DeryCode Technologies and Sageco Evergreen, in plain language.</p><a class="more" href="ventures.html">Read the ventures →</a></div>
</div>
{edit("Add documents you want public", "Certificates, company registration documents, pitch decks or reports you are willing to publish. Each one you add becomes a permanent, linkable record, which is how a personal brand becomes verifiable.")}
''')

add("mediakit.html", "Media kit, bios and brand assets | Asiimwe Derick",
    "Approved bios in three lengths, photography, brand colours, QR code and public archive for journalists, event organisers and partners writing about Asiimwe Derick.",
    "media kit press bios photos brand assets qr archive documents journalist", mk)

# ============================== ASSISTANT ==============================
asst = page_head_block("Ask Derick AI", '<a href="assistant.html">Ask Derick AI</a>', "15 / ASSISTANT",
  "Ask me<br><em>anything on this site.</em>",
  "An assistant that answers from this website only: biography, companies, projects, vision, skills and how to get in touch. No account, no waiting, and it works on a slow connection.")
asst += f'''<section class="section wrap" style="padding-top:0">
 <div class="chat">
  <div id="chatLog" aria-live="polite">
   <div class="msg ai">Hello. I answer questions about Derick using this website: his biography, DeryCode Technologies, Sageco Evergreen, projects, vision, skills, writing and contact routes. What would you like to know?</div>
  </div>
  <div class="sugg">
   <button type="button" data-ask="Who is Asiimwe Derick?">Who is he?</button>
   <button type="button" data-ask="What companies does he run?">His companies</button>
   <button type="button" data-ask="What projects has he built?">Projects</button>
   <button type="button" data-ask="Is he open to investors?">Investors</button>
   <button type="button" data-ask="How do I contact him?">Contact</button>
  </div>
  <form id="chatForm">
   <input id="chatInput" type="text" placeholder="Ask about Derick, his work, or how to reach him…" aria-label="Your question" autocomplete="off">
   <button class="btn" type="submit">Ask</button>
  </form>
 </div>
 <p style="color:var(--muted);font-size:13px;margin-top:14px">This assistant runs entirely in your browser against the content of this site. It does not send your question anywhere, and it will say so when it does not know.</p>
</section>
'''
add("assistant.html", "Ask Derick AI | Asiimwe Derick",
    "Ask questions about Asiimwe Derick and get answers from this website: biography, companies, projects, vision, skills and contact routes.",
    "assistant ai chat ask questions derick", asst)

# ============================== SITE MAP ==============================
SITEMAP_GROUPS = [
 ("Profile", [("index.html","Home"),("about.html","About &amp; biography"),("journey.html","Journey &amp; experience"),("skills.html","Skills &amp; CV"),("cv.html","Printable CV")]),
 ("Work", [("ventures.html","Ventures &amp; portfolio"),("projects.html","Projects &amp; case studies"),("services.html","Services &amp; collaboration"),("investors.html","For investors")]),
 ("Thinking", [("writing.html","Writing"),("article-offline-first.html","Why Ugandan software has to work offline first"),("article-land-trust.html","The fear in buying land"),("article-youth-tech.html","You do not need permission to build"),("vision.html","Vision &amp; roadmap")]),
 ("People", [("impact.html","Impact &amp; leadership"),("speaking.html","Speaking &amp; media"),("gallery.html","Gallery &amp; life"),("mediakit.html","Media kit &amp; archive")]),
 ("Utility", [("contact.html","Contact"),("assistant.html","Ask Derick AI"),("sitemap.html","Site map"),("privacy.html","Privacy policy"),("terms.html","Terms of use"),("disclaimer.html","Disclaimer")]),
]
sm_body = page_head_block("Site map", '<a href="sitemap.html">Site map</a>', "SITE MAP",
  "Every page,<br><em>one list.</em>",
  "The complete structure of this site. Nothing hidden, nothing orphaned.")
for gname, items in SITEMAP_GROUPS:
    sm_body += section(gname.lower(), gname.upper(), gname, '<div class="cards">' + "".join(
        f'<a class="card" href="{u}"><h3>{t}</h3></a>' for u,t in items) + '</div>')
add("sitemap.html", "Site map | Asiimwe Derick",
    "Complete site map for the personal website of Asiimwe Derick: profile, work, thinking, impact, media and contact pages.",
    "sitemap all pages index navigation", sm_body)

# ============================== LEGAL ==============================
priv = page_head_block("Privacy", '<a href="privacy.html">Privacy</a>', "LEGAL",
  "Privacy policy", "What this site collects, what it does not, and how to have your data removed.")
priv += '''<section class="section wrap"><div class="prose">
 <p><strong>Last updated:</strong> 21 November 2026</p>
 <h3>What this site collects</h3>
 <p>This is a static website. It does not set advertising cookies, does not use third-party tracking pixels, and does not build a profile of you. There is no login and no account.</p>
 <ul>
  <li><strong>No server-side logs are controlled by this site.</strong> It is hosted on GitHub Pages, which may keep standard technical logs under its own policy.</li>
  <li><strong>Local visit counts.</strong> The site stores a simple page-visit count in your own browser's local storage. It never leaves your device and can be cleared by clearing site data.</li>
  <li><strong>Theme preference.</strong> Your light or dark choice is stored in your browser only.</li>
  <li><strong>Search and the assistant</strong> run entirely in your browser against a file on this site. Your questions are not sent anywhere.</li>
 </ul>
 <h3>When you contact me</h3>
 <p>If you email or message, I receive what you send: your name, address and message. I use it to reply and keep it only as long as the conversation or the working relationship requires. I do not sell or share contact data.</p>
 <h3>Newsletter</h3>
 <p>The newsletter form opens your own email app and sends a subscription request to me directly. No third-party mailing system receives your address until one is connected, and if that changes this page will say which provider is used.</p>
 <h3>Your rights</h3>
 <p>You can ask what personal data I hold about you, ask for a copy, or ask for it to be deleted. Email <a href="mailto:derickasiimwe849@gmail.com">derickasiimwe849@gmail.com</a> and it will be handled.</p>
 <h3>Children</h3>
 <p>This site is not directed at children under 13 and does not knowingly collect their data.</p>
 <h3>Changes</h3>
 <p>If this policy changes, the date above changes with it.</p>
</div></section>
'''
add("privacy.html", "Privacy policy | Asiimwe Derick",
    "Privacy policy for the personal website of Asiimwe Derick: no advertising cookies, no third-party tracking, local-only analytics, and how to request deletion of your data.",
    "privacy policy data cookies gdpr", priv)

terms = page_head_block("Terms", '<a href="terms.html">Terms</a>', "LEGAL",
  "Terms of use", "The rules for using this website and the limits of what it promises.")
terms += '''<section class="section wrap"><div class="prose">
 <p><strong>Last updated:</strong> 21 November 2026</p>
 <h3>Using this site</h3>
 <p>This website is provided for information about Asiimwe Derick, his companies and his work. You may read it, quote it with attribution, and link to any page.</p>
 <h3>Accuracy</h3>
 <p>Content is written in good faith and kept as current as practical. Figures such as project counts are accurate at the time of writing and change as work continues. Nothing here is a binding offer, a guarantee of results, or financial, legal or investment advice.</p>
 <h3>Intellectual property</h3>
 <p>The text and photography on this site belong to Asiimwe Derick unless stated otherwise. Company names and logos belong to their respective owners. Do not republish substantial portions without permission.</p>
 <h3>Third-party links</h3>
 <p>Links to other websites are provided for convenience. Those sites are governed by their own terms, and I am not responsible for their content.</p>
 <h3>Limitation of liability</h3>
 <p>The site is provided as is. To the extent permitted by law, I am not liable for any loss arising from use of the site or reliance on its content.</p>
 <h3>Governing law</h3>
 <p>These terms are governed by the laws of Uganda.</p>
 <h3>Contact</h3>
 <p>Questions about these terms: <a href="mailto:derickasiimwe849@gmail.com">derickasiimwe849@gmail.com</a>.</p>
</div></section>
'''
add("terms.html", "Terms of use | Asiimwe Derick",
    "Terms of use for the personal website of Asiimwe Derick: permitted use, accuracy, intellectual property, third-party links and limitation of liability.",
    "terms of use legal conditions", terms)

disc = page_head_block("Disclaimer", '<a href="disclaimer.html">Disclaimer</a>', "LEGAL",
  "Disclaimer", "What this site is, and what it is not.")
disc += '''<section class="section wrap"><div class="prose">
 <p><strong>Last updated:</strong> 21 November 2026</p>
 <h3>No investment advice</h3>
 <p>Nothing on this website is an offer to sell securities or a solicitation to invest. Descriptions of DeryCode Technologies and Sageco Evergreen are informational. Any investment discussion happens separately, in writing, with full disclosure of risk, and early-stage companies can lose all invested capital.</p>
 <h3>No legal, financial or property advice</h3>
 <p>Content about land, verification, escrow and property transactions explains how a platform is designed. It is not legal advice and does not replace a lawyer, surveyor or the land registry. Always verify independently before any property transaction.</p>
 <h3>Forward-looking statements</h3>
 <p>Vision 2030, Vision 2040, goals and roadmaps are ambitions, not forecasts or promises. They describe direction and intent, and they will change as circumstances change.</p>
 <h3>Company mentions</h3>
 <p>Client names and links are used to describe work delivered. Their inclusion does not imply endorsement of this site or of any other service.</p>
 <h3>Regulated products</h3>
 <p>Promotional or gaming-style products are not operated where a licence or written regulatory guidance is required. Where a product is paused for that reason, this site says so rather than implying it is live.</p>
 <h3>Contact</h3>
 <p>If something on this site looks wrong or out of date, tell me: <a href="mailto:derickasiimwe849@gmail.com">derickasiimwe849@gmail.com</a>.</p>
</div></section>
'''
add("disclaimer.html", "Disclaimer | Asiimwe Derick",
    "Disclaimer for Asiimwe Derick's website: no investment, legal or property advice, forward-looking statements are ambitions not forecasts, and regulated products are paused where required.",
    "disclaimer legal investment advice risk", disc)

# ============================== RENDER ==============================
def render():
    written = []
    for slug, title, desc, keys, body in PAGES:
        html_doc = head(slug, title, desc) + body + foot()
        open(slug, "w", encoding="utf-8").write(html_doc)
        written.append(slug)
    # 404
    nf = head("404.html", "Page not found | Asiimwe Derick", "That page does not exist on this site. Use the site map or search to find what you were looking for.")
    nf += page_head_block("404", "", "404", "That page<br><em>is not here.</em>", "The link may be old, or the address may have a typo. Search the site, or start from the pages below.")
    nf += section("links", "TRY THESE", "Most visited", cards([
        ("Profile","About &amp; biography","Who he is, where he comes from, what he believes.","about.html","Read"),
        ("Evidence","Projects &amp; case studies","Live work you can open and check.","projects.html","Browse"),
        ("Thinking","Writing","Technology, business, leadership and ideas.","writing.html","Read"),
        ("Contact","Contact","Email, WhatsApp and inquiry routes.","contact.html","Get in touch"),
    ]))
    nf += foot()
    open("404.html","w",encoding="utf-8").write(nf)

    # search + assistant index
    idx = []
    for slug, title, desc, keys, body in PAGES:
        clean_title = title.split("|")[0].strip().replace("&amp;","&")
        idx.append({"title": clean_title, "desc": desc[:150], "url": slug, "keys": keys})
    extra = [
        {"title":"Mission, vision and values","desc":"The frame everything hangs on: mission at scale, Vision 2040 and six values.","url":"about.html#mission","keys":"mission vision values"},
        {"title":"Philosophy and manifesto","desc":"Seven beliefs behind the work, from offline-first to publishing numbers.","url":"about.html#philosophy","keys":"philosophy manifesto beliefs"},
        {"title":"Timeline","desc":"Birth in Kyenjojo, school, DeryCode, Sageco Evergreen and what comes next.","url":"journey.html#timeline","keys":"timeline history dates"},
        {"title":"Case studies","desc":"Sageco Evergreen, Relie Motel and Nuwe Rugaba in detail.","url":"projects.html#cases","keys":"case study results"},
        {"title":"Client work","desc":"Hotels, retailers, clinics and homestays with live links.","url":"projects.html#clients","keys":"clients portfolio websites"},
        {"title":"Vision 2030","desc":"The next checkpoint and what has to be true by then.","url":"vision.html#v2030","keys":"vision 2030 goals"},
        {"title":"Vision 2040","desc":"From builder to global investor, in his own words.","url":"vision.html#v2040","keys":"2040 investor future"},
        {"title":"Speaking topics","desc":"Six talks for universities, founder events and panels.","url":"speaking.html#topics","keys":"speaking talks keynote"},
        {"title":"Media kit bios","desc":"25, 60 and 150 word approved bios plus photos and QR.","url":"mediakit.html#bios","keys":"bio press kit"},
        {"title":"Investment thesis","desc":"The ventures, one thesis, and how to request the deck.","url":"investors.html#thesis","keys":"invest thesis deck"},
        {"title":"Download CV","desc":"One-page PDF curriculum vitae.","url":"assets/derick-asiimwe-cv.pdf","keys":"cv resume pdf download"},
    ]
    idx += extra
    json.dump(idx, open("assets/site-index.json","w",encoding="utf-8"), indent=1, ensure_ascii=False)

    # xml sitemap
    pages = [s for s,_,_,_,_ in PAGES] + ["404.html"]
    prio = {"index.html":"1.0"}
    xml = ['<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for s in pages:
        if s == "404.html": continue
        loc = BASE + ("" if s=="index.html" else s)
        xml.append(f'  <url><loc>{loc}</loc><lastmod>2026-11-21</lastmod><changefreq>monthly</changefreq><priority>{prio.get(s,"0.8")}</priority></url>')
    xml.append('</urlset>')
    open("sitemap.xml","w",encoding="utf-8").write("\n".join(xml)+"\n")

    open("robots.txt","w").write("User-agent: *\nAllow: /\n\nSitemap: %ssitemap.xml\n" % BASE)
    print("pages written:", len(written)+1)
    for w in written: print("  ", w)

if __name__ == "__main__":
    render()
