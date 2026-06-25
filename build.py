#!/usr/bin/env python3
# A La Cart Charcuterie Co. - mockup generator (3 themes + 12-post blog)
# Single-process build. Customer-facing: no em dashes, her real photos, real reviews.
import os, html, shutil

ROOT = os.path.expanduser("~/site-work/alacart-mockups")
IMG = "assets/img/real"

# ----------------------------------------------------------------------------- DATA
BIZ = dict(
    name="A La Cart Charcuterie Co.",
    tagline="Mobile charcuterie, grazing tables, and cart catering for Lawrence and Kansas City.",
    phone_display="(913) 217-5908",
    phone_raw="+19132175908",
    email="hello@alacartcharcuterieco.com",
    city="Lawrence, KS",
    areas=["Lawrence", "Lecompton", "Eudora", "Baldwin City", "Overland Park", "Olathe", "Kansas City", "Topeka", "De Soto", "Leawood"],
)
SOCIAL = dict(
    facebook="https://www.facebook.com/profile.php?id=61576221921489",
    google="https://search.google.com/local/reviews?placeid=ChIJtdudUadnv4cRxcH9MTJodZs",
    yelp="https://www.yelp.com/biz/a-la-cart-charcuterie-lawrence",
)

# semantic image map -> real files
P = {
    "hero_cart": f"{IMG}/cart_at_wedding.jpg",
    "cart2": f"{IMG}/cart_at_wedding_2.jpg",
    "trailer": f"{IMG}/wedding_trailer.jpg",
    "owner": f"{IMG}/blob-bf5ded7.png",
    "box_big": f"{IMG}/fb_122149932296874064_2048x1513.jpg",
    "board_round": f"{IMG}/fb_122148158648874064_2045x2048.jpg",
    "cups_trio": f"{IMG}/fb_122158624262874064_2048x1536.jpg",
    "cup_wine": f"{IMG}/fb_122140420256874064_1536x2048.jpg",
    "cups_close": f"{IMG}/fb_122140420280874064_1536x2048.jpg",
    "boxes_clam": f"{IMG}/fb_122162304050874064_1536x2048.jpg",
    "crackers": f"{IMG}/fb_122164717466874064_1536x2048.jpg",
    "boxes_holiday": f"{IMG}/fb_122164717478874064_2048x1536.jpg",
}

SERVICES = [
    dict(name="Grazing Tables", price="from $15 / guest", img="board_round",
         blurb="Our showpiece. A lavish, hand built spread of cured meats, artisan cheeses, fresh and dried fruit, nuts, honey, and house touches, styled on site for weddings and larger celebrations."),
    dict(name="Charcuterie Boards", price="from $15 / guest", img="box_big",
         blurb="The classic, elevated. Beautifully arranged boards sized for dinner parties, showers, and intimate gatherings, finished with salami roses and seasonal garnish."),
    dict(name="Boxes and Cups", price="from $12 / guest", img="cups_trio",
         blurb="Individually portioned charcuterie cups and grab and go boxes, perfect for cocktail hours, corporate orders, and stress free hosting."),
    dict(name="The Charcuterie Cart", price="from $10 / guest + cart fee", img="hero_cart",
         blurb="Our signature mobile cart rolls into your venue under a striped umbrella, a living centerpiece guests gather around all evening."),
    dict(name="The Charcuterie Trailer", price="custom quote", img="trailer",
         blurb="A vintage converted trailer turned charcuterie bar, dressed with florals and string lights. The wow factor for weddings and outdoor events."),
    dict(name="Add Ons and Custom", price="custom quote", img="crackers",
         blurb="Cracker and fig spread trays, sandwich add ons, dietary requests, and fully custom builds. Tell us the occasion and we design around it."),
]

REVIEWS = [
    dict(name="Gilbert Montano", src="Google", url=SOCIAL["google"], stars=5,
         text="If you are in need of a wow factor this is your place. Rebecca came through on time as promised and the presentation was amazing."),
    dict(name="Kyrie L.", src="Google", url=SOCIAL["google"], stars=5,
         text="The best charcuterie box hands down. Each one is different, with meats, cheeses, chocolates, jellies, cookies, fresh fruit, and flowers. She listens to her customers and the food is always fresh and delicious. I 100% recommend to everyone."),
    dict(name="Cindy Penzler", src="Google", url=SOCIAL["google"], stars=5,
         text="Unbelievable. Thank you so much for the beautiful, innovative, and most importantly, delicious charcuterie boxes. The selections were fresh and diverse, making the choices fun and conversational."),
    dict(name="Jennifer K.", src="Yelp", url=SOCIAL["yelp"], stars=5,
         text="This charcuterie company was the highlight of our party. The setup was absolutely beautiful and the food was fresh, delicious, and perfectly curated. It made hosting so easy and truly elevated the entire event."),
    dict(name="Cheryl Hutchison", src="Google", url=SOCIAL["google"], stars=5,
         text="Absolutely fantastic. Everything was perfect, and she goes above and beyond with suggestions, helpfulness, and creativity. A definite 10 star all the way around."),
    dict(name="Mollee Fanello", src="Facebook", url=SOCIAL["facebook"], stars=5,
         text="One of the most thoughtful and delicious surprises I have ever gotten. Everything was beautifully arranged and clearly crafted with care. Elegant, gift worthy, and unforgettable."),
    dict(name="Joe Stellwagon", src="Google", url=SOCIAL["google"], stars=5,
         text="A great addition to the usual vendors at the Kaw Valley wine event. The kit was perfect for the event and plenty for two people. A unique, Lawrence based vendor worth seeking out."),
]

FAQS = [
    ("How far in advance should I book?", "For weddings and large grazing tables we recommend two to four weeks. Boxes and cups can often be arranged with shorter notice. Popular weekends fill quickly in spring, summer, and fall."),
    ("How much charcuterie do I need?", "A grazing table or board is typically planned at one generous serving per guest as an appetizer, or more if it is the main feature. We help you size every order to your headcount."),
    ("What areas do you serve?", "We are based in Lawrence and serve the surrounding towns plus the Greater Topeka and Kansas City metros, including Overland Park, Olathe, Leawood, and De Soto. Travel beyond Lawrence may include a small fee."),
    ("Can you accommodate dietary needs?", "Yes. We regularly build around gluten free, vegetarian, and other preferences. Tell us when you inquire and we design the spread accordingly."),
    ("Do you set up on site?", "Grazing tables, the cart, and the trailer are styled on site by Rebecca. Boxes and cups are delivered ready to serve."),
]

# 12 blog posts - SEO targeted to her keyword gaps (KC metro, weddings, cart rental, grazing tables)
BLOG = [
 dict(slug="grazing-tables-kansas-city", cat="Grazing Tables", thumb="board_round", inline=["box_big","hero_cart"],
   title="Grazing Tables in Kansas City: What to Expect When You Book One",
   excerpt="From headcount to styling, here is how a grazing table comes together for a Kansas City celebration.",
   body=[
     "A grazing table is the centerpiece guests remember. Instead of a single board, it is a flowing, abundant spread built right on your table, layered with cured meats, artisan cheeses, fresh and dried fruit, nuts, honey, crackers, and seasonal touches.",
     "For Kansas City and Lawrence events, we plan the table around your guest count and the role it plays. As a cocktail hour feature it reads as one generous serving per guest. As the main event, we build it larger and richer so it carries the room.",
     "Everything is styled on site. Rebecca arrives, dresses the table, and arranges each element so it looks effortless and photographs beautifully. All you do is point your guests toward it.",
   ]),
 dict(slug="wedding-charcuterie-cart-grazing-table", cat="Weddings", thumb="hero_cart", inline=["trailer","cups_trio"],
   title="Wedding Charcuterie: How a Cart or Grazing Table Elevates Your Reception",
   excerpt="Cocktail hour is where a wedding finds its rhythm. Here is how charcuterie sets the tone.",
   body=[
     "Cocktail hour sets the mood for the whole reception. A charcuterie cart or grazing table gives guests something beautiful to gather around while photos wrap up, and it turns the food itself into part of the decor.",
     "Our branded cart rolls in under a striped umbrella and becomes a living centerpiece. For a softer, vintage look, the converted charcuterie trailer dresses up with florals and string lights and becomes a backdrop guests line up to photograph.",
     "We coordinate with your planner and venue on timing and placement so the spread is ready the moment cocktail hour begins, styled to match your colors and season.",
   ]),
 dict(slug="charcuterie-cups-wedding-cocktail-hour", cat="Weddings", thumb="cups_close", inline=["cup_wine","cups_trio"],
   title="Charcuterie Cups: The Perfect Wedding Cocktail Hour Bite",
   excerpt="Individually portioned, easy to hold, and endlessly photogenic. Why cups shine at weddings.",
   body=[
     "Charcuterie cups are individually portioned servings of meats, cheeses, fruit, and a sweet finish, built tall and garnished so each one is its own little work of art. Guests can grab one in a hand that is already holding a drink.",
     "They are ideal for cocktail hour and standing receptions where a full table is not practical. They also pair beautifully with a mini bottle of wine for a welcome favor guests will remember.",
     "Because each cup is portioned, they make catering headcounts simple and keep service clean and effortless from start to finish.",
   ]),
 dict(slug="how-much-charcuterie-do-i-need", cat="Planning", thumb="box_big", inline=["board_round"],
   title="How Much Charcuterie Do I Need? A Simple Per Guest Guide",
   excerpt="The most common question we hear. A quick, honest guide to sizing your order.",
   body=[
     "The right amount depends on one thing: is charcuterie the appetizer, or the meal? As an appetizer before dinner, plan roughly one generous serving per guest. As the main feature of a party, plan closer to two to three servings per guest.",
     "For cups and boxes the math is easy, since each one is a single portion. For grazing tables and boards we scale the size of the spread to your headcount so nothing runs short and the table still looks full at the end of the night.",
     "When in doubt, tell us your guest count and the occasion. We have sized hundreds of events and will recommend the right build so you are never guessing.",
   ]),
 dict(slug="vintage-charcuterie-trailer-lawrence", cat="The Trailer", thumb="trailer", inline=["hero_cart"],
   title="Our Vintage Charcuterie Trailer: A Showstopper for Lawrence Events",
   excerpt="A converted trailer turned charcuterie bar, and why it steals the show.",
   body=[
     "Some details make guests reach for their phones the second they see them. Our vintage converted trailer, restyled as a charcuterie bar, is one of them. Dressed with florals, greenery, and warm string lights, it becomes the visual anchor of an outdoor event.",
     "Inside, it serves the same beautifully built charcuterie our boards and cups are known for. Outside, it doubles as a photo moment and a talking point that ties your whole setup together.",
     "The trailer is perfect for weddings, milestone parties, and outdoor gatherings around Lawrence and the Greater Topeka and Kansas City metros where you want a centerpiece guests will not forget.",
   ]),
 dict(slug="charcuterie-boxes-corporate-gifting-lawrence", cat="Boxes", thumb="boxes_clam", inline=["boxes_holiday","crackers"],
   title="Charcuterie Boxes for Corporate Events and Gifting in Lawrence",
   excerpt="Individual boxes make client gifts and office events simple, polished, and memorable.",
   body=[
     "Individually packaged charcuterie boxes are an easy way to make a strong impression. For corporate orders they solve the logistics of serving a group, since every box is portioned, sealed, and ready to hand out.",
     "As a client or employee gift, a beautifully styled box says more than a generic basket. Each one is arranged with the same care as our larger spreads, finished with fresh fruit, chocolate, and seasonal accents.",
     "We handle bulk orders for offices and events across Lawrence and Kansas City, and we can coordinate delivery so everything arrives fresh and on schedule.",
   ]),
 dict(slug="charcuterie-wine-pairing-guide", cat="Pairings", thumb="cup_wine", inline=["board_round"],
   title="Charcuterie and Wine Pairing: Simple Rules That Always Work",
   excerpt="You do not need to be a sommelier. A few easy pairings make any spread sing.",
   body=[
     "Great pairings come down to balance. A crisp white like Chardonnay cuts through rich, soft cheeses and lighter cured meats, which is why it is a favorite alongside our cups and boxes.",
     "For bolder boards with aged cheeses and peppery salami, a medium red holds its own. And a touch of something sparkling makes the whole table feel like a celebration.",
     "The simplest rule of all: pair what you enjoy. We build our spreads to play well with a wide range of wines so you can pour what your guests love and let the food do the rest.",
   ]),
 dict(slug="graduation-party-grazing-table-lawrence", cat="Local Events", thumb="box_big", inline=["cups_trio"],
   title="Planning a Graduation Party in Lawrence? Add a Grazing Table",
   excerpt="Open house season is busy. A grazing table feeds a crowd and looks incredible doing it.",
   body=[
     "Graduation open houses bring a steady flow of guests across a few hours, which is exactly the kind of event a grazing table is built for. It stays beautiful and abundant from the first guest to the last.",
     "Instead of refilling trays all afternoon, you get one styled spread that anchors the room and frees you to actually enjoy the party. Guests serve themselves whenever they arrive.",
     "We book Lawrence area graduations through the spring and early summer. Reserve your date early, since open house weekends are some of the busiest of the year.",
   ]),
 dict(slug="holiday-charcuterie-boxes-gifting", cat="Seasonal", thumb="boxes_holiday", inline=["boxes_clam"],
   title="Holiday Charcuterie Boxes: Hosting and Gifting Made Easy",
   excerpt="The season of gatherings and gifts. Let a styled box do the heavy lifting.",
   body=[
     "The holidays are full of hosting, drop ins, and gifts that need to feel personal. A seasonal charcuterie box covers all three, styled with festive touches, chocolates, and a window that shows off the spread before it is even opened.",
     "For hosts, a box or two means the appetizer is handled and looks like you fussed for hours. For gifting, it is a present that feels thoughtful and tastes even better than it looks.",
     "Holiday boxes are limited and book fast. We open seasonal ordering early so Lawrence and Kansas City clients can reserve before the calendar fills.",
   ]),
 dict(slug="what-makes-a-great-charcuterie-board", cat="Behind the Scenes", thumb="board_round", inline=["box_big","crackers"],
   title="What Makes a Great Charcuterie Board: A Behind the Scenes Look",
   excerpt="Abundance, contrast, and a little artistry. Inside how each board comes together.",
   body=[
     "A great board is built in layers. It starts with anchors of cheese and folded or rosed meats, then fills with fruit, nuts, crackers, and sweet bites until there is no empty space left. Abundance is the whole point.",
     "Contrast is what makes it beautiful. Soft against crunchy, sweet against savory, bright fruit against deep cured reds. The eye travels the board and finds something new at every turn.",
     "The finishing touches are the difference. Salami roses, a sprig of rosemary, a drizzle of honey. Small details, done by hand, are what turn good ingredients into something guests photograph before they taste.",
   ]),
 dict(slug="charcuterie-cart-rental-kansas-city", cat="The Cart", thumb="hero_cart", inline=["cart2","cups_trio"],
   title="Charcuterie Cart Rental for Kansas City Weddings and Parties",
   excerpt="A mobile cart that rolls into your venue and becomes the centerpiece of the night.",
   body=[
     "Our charcuterie cart is a mobile, fully styled spread on wheels. It rolls into your venue under a striped umbrella, loaded with trays of meats, cheeses, fruit, and accompaniments, and becomes a centerpiece guests gather around all evening.",
     "For Kansas City and Lawrence weddings and parties, the cart blends catering and decor into one. It serves a crowd, looks stunning in photos, and gives your event a focal point without taking up a permanent table.",
     "We bring the cart to venues across the metro. Reach out with your date, location, and headcount and we will tailor the build to your event.",
   ]),
 dict(slug="meet-rebecca-a-la-cart-story", cat="Our Story", thumb="owner", inline=["hero_cart","board_round"],
   title="Meet Rebecca: The Story Behind A La Cart Charcuterie Co.",
   excerpt="A Lawrence, Kansas based maker whose attention to detail has guests talking long after the event.",
   body=[
     "A La Cart Charcuterie Co. began with a simple belief: that food can be beautiful, generous, and personal all at once. Rebecca is the artist behind every spread, and her eye for detail is what customers mention again and again.",
     "From a single charcuterie box to a full wedding grazing table, she builds each order by hand and styles it on site, treating presentation as seriously as the ingredients. Guests do not just eat the spread, they remember it.",
     "Based in Lawrence and serving the Greater Topeka and Kansas City metros, A La Cart has grown through word of mouth and five star reviews, one beautifully built table at a time.",
   ]),
]

STAR = "★"
def stars(n): return STAR * n

def img_tag(key, alt, cls="", prefix=""):
    return f'<img src="{prefix}{P[key]}" alt="{html.escape(alt)}" loading="lazy" class="{cls}">'

# ----------------------------------------------------------------------------- CSS
BASE_CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:var(--body);color:var(--ink);background:var(--bg);line-height:1.65;-webkit-font-smoothing:antialiased}
h1,h2,h3,h4{font-family:var(--display);font-weight:var(--dw,600);line-height:1.1;color:var(--ink)}
a{color:inherit;text-decoration:none}
img{display:block;max-width:100%}
.wrap{max-width:1180px;margin:0 auto;padding:0 24px}
.eyebrow{font-family:var(--body);text-transform:uppercase;letter-spacing:.28em;font-size:.72rem;font-weight:600;color:var(--accent)}
.btn{display:inline-block;padding:14px 30px;border-radius:var(--radius);background:var(--accent);color:var(--on-accent);font-family:var(--body);font-weight:600;letter-spacing:.02em;font-size:.95rem;transition:transform .2s,box-shadow .2s;border:1px solid var(--accent)}
.btn:hover{transform:translateY(-2px);box-shadow:0 12px 30px var(--shadow)}
.btn.ghost{background:transparent;color:var(--ink);border:1px solid var(--line)}
.btn.ghost:hover{background:var(--soft)}
section{padding:96px 0}
.sec-head{max-width:680px;margin:0 auto 56px;text-align:center}
.sec-head h2{font-size:clamp(2rem,4vw,3rem);margin:14px 0}
.sec-head p{color:var(--muted);font-size:1.08rem}
/* NAV */
header.nav{position:sticky;top:0;z-index:50;background:var(--nav-bg);backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.nav .wrap{display:flex;align-items:center;justify-content:space-between;height:78px}
.brand{display:flex;flex-direction:column;line-height:1}
.brand .script{font-family:var(--script);font-size:1.9rem;color:var(--accent);line-height:.9}
.brand .sub{font-family:var(--display);letter-spacing:.18em;text-transform:uppercase;font-size:.62rem;color:var(--muted);margin-top:3px}
.nav nav{display:flex;gap:30px;align-items:center}
.nav nav a{font-family:var(--body);font-size:.93rem;font-weight:500;color:var(--ink);opacity:.82}
.nav nav a:hover{opacity:1;color:var(--accent)}
.nav .navcta{padding:10px 22px;border-radius:var(--radius);background:var(--accent);color:var(--on-accent);font-weight:600}
@media(max-width:860px){.nav nav a:not(.navcta){display:none}}
/* HERO */
.hero{position:relative;min-height:88vh;display:flex;align-items:center;overflow:hidden}
.hero .bg{position:absolute;inset:0}
.hero .bg img{width:100%;height:100%;object-fit:cover}
.hero .scrim{position:absolute;inset:0;background:var(--hero-scrim)}
.hero .inner{position:relative;z-index:2;max-width:680px;color:var(--hero-ink)}
.hero h1{font-size:clamp(2.6rem,6vw,4.6rem);color:var(--hero-ink);margin:18px 0 20px}
.hero p.lede{font-size:1.25rem;color:var(--hero-ink);opacity:.92;margin-bottom:34px;max-width:560px}
.hero .eyebrow{color:var(--hero-accent)}
.hero .cta-row{display:flex;gap:16px;flex-wrap:wrap}
.hero .btn.ghost{color:var(--hero-ink);border-color:var(--hero-ink)}
.badge-row{position:absolute;bottom:26px;z-index:2;display:flex;gap:24px;align-items:center;color:var(--hero-ink);font-family:var(--body);font-size:.86rem;opacity:.9}
.badge-row b{color:var(--hero-accent)}
/* INTRO */
.intro{display:grid;grid-template-columns:1.1fr .9fr;gap:64px;align-items:center}
.intro .txt h2{font-size:clamp(1.9rem,3.5vw,2.7rem);margin:14px 0 18px}
.intro .txt p{color:var(--muted);margin-bottom:16px;font-size:1.06rem}
.intro .pic{position:relative}
.intro .pic img{width:100%;border-radius:var(--radius-lg);box-shadow:0 30px 60px var(--shadow)}
.intro .pic .tag{position:absolute;bottom:-22px;left:-22px;background:var(--accent);color:var(--on-accent);padding:18px 24px;border-radius:var(--radius);font-family:var(--display);font-size:1.05rem;box-shadow:0 16px 36px var(--shadow)}
@media(max-width:820px){.intro{grid-template-columns:1fr;gap:40px}.intro .pic .tag{left:16px}}
/* SERVICES */
.svc-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:28px}
.svc{background:var(--card);border:1px solid var(--line);border-radius:var(--radius-lg);overflow:hidden;transition:transform .25s,box-shadow .25s}
.svc:hover{transform:translateY(-6px);box-shadow:0 24px 50px var(--shadow)}
.svc .ph{aspect-ratio:4/3;overflow:hidden}
.svc .ph img{width:100%;height:100%;object-fit:cover;transition:transform .5s}
.svc:hover .ph img{transform:scale(1.06)}
.svc .body{padding:26px 24px 30px}
.svc h3{font-size:1.4rem;margin-bottom:8px}
.svc .price{font-family:var(--body);color:var(--accent);font-weight:600;font-size:.9rem;letter-spacing:.02em;margin-bottom:12px}
.svc p{color:var(--muted);font-size:.97rem}
@media(max-width:860px){.svc-grid{grid-template-columns:1fr 1fr}}
@media(max-width:560px){.svc-grid{grid-template-columns:1fr}}
/* REVIEWS CAROUSEL */
.reviews{background:var(--soft)}
.marquee{overflow:hidden;position:relative;-webkit-mask-image:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent);mask-image:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent)}
.track{display:flex;gap:24px;width:max-content;animation:scroll var(--marquee-speed,110s) linear infinite}
.marquee:hover .track{animation-play-state:paused}
@keyframes scroll{from{transform:translateX(0)}to{transform:translateX(-50%)}}
.rev{flex:0 0 380px;background:var(--card);border:1px solid var(--line);border-radius:var(--radius-lg);padding:30px 28px;display:flex;flex-direction:column;transition:box-shadow .25s,transform .25s}
.rev:hover{box-shadow:0 20px 44px var(--shadow);transform:translateY(-4px)}
.rev .stars{color:var(--gold);letter-spacing:3px;font-size:1.05rem;margin-bottom:12px}
.rev .txt{color:var(--ink);font-size:1rem;line-height:1.6;flex:1}
.rev .ft{display:flex;align-items:center;justify-content:space-between;margin-top:20px;padding-top:16px;border-top:1px solid var(--line)}
.rev .who{font-family:var(--display);font-weight:600}
.rev .src{font-family:var(--body);font-size:.74rem;text-transform:uppercase;letter-spacing:.12em;color:var(--accent);display:flex;align-items:center;gap:6px}
.rev .src:hover{text-decoration:underline}
/* GALLERY */
.gal{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.gal a{overflow:hidden;border-radius:var(--radius);aspect-ratio:1}
.gal img{width:100%;height:100%;object-fit:cover;transition:transform .5s}
.gal a:hover img{transform:scale(1.08)}
.gal a.tall{grid-row:span 2;aspect-ratio:auto}
@media(max-width:760px){.gal{grid-template-columns:1fr 1fr}}
/* AREAS */
.areas{background:var(--accent);color:var(--on-accent);text-align:center}
.areas h2{color:var(--on-accent)}
.areas .chips{display:flex;flex-wrap:wrap;gap:12px;justify-content:center;margin-top:26px}
.areas .chips span{border:1px solid var(--on-accent);opacity:.9;padding:8px 18px;border-radius:999px;font-family:var(--body);font-size:.9rem}
/* BLOG TEASER + INDEX */
.posts{display:grid;grid-template-columns:repeat(3,1fr);gap:30px}
.post{background:var(--card);border:1px solid var(--line);border-radius:var(--radius-lg);overflow:hidden;display:flex;flex-direction:column;transition:transform .25s,box-shadow .25s}
.post:hover{transform:translateY(-6px);box-shadow:0 24px 50px var(--shadow)}
.post .ph{aspect-ratio:16/10;overflow:hidden}
.post .ph img{width:100%;height:100%;object-fit:cover;transition:transform .5s}
.post:hover .ph img{transform:scale(1.06)}
.post .body{padding:24px;display:flex;flex-direction:column;flex:1}
.post .cat{font-family:var(--body);font-size:.7rem;text-transform:uppercase;letter-spacing:.16em;color:var(--accent);font-weight:700;margin-bottom:10px}
.post h3{font-size:1.25rem;line-height:1.25;margin-bottom:10px}
.post p{color:var(--muted);font-size:.95rem;flex:1}
.post .more{margin-top:16px;font-family:var(--body);font-weight:600;color:var(--accent);font-size:.9rem}
@media(max-width:860px){.posts{grid-template-columns:1fr 1fr}}
@media(max-width:560px){.posts{grid-template-columns:1fr}}
/* FAQ */
.faq-list{max-width:780px;margin:0 auto}
.faq{border-bottom:1px solid var(--line)}
.faq summary{cursor:pointer;padding:24px 0;font-family:var(--display);font-size:1.2rem;font-weight:600;list-style:none;display:flex;justify-content:space-between;align-items:center}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:'+';color:var(--accent);font-size:1.6rem;font-weight:300}
.faq[open] summary::after{content:'\\2013'}
.faq p{padding:0 0 24px;color:var(--muted)}
/* CONTACT */
.contact{background:var(--soft)}
.contact .inner{display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center}
.contact .form{background:var(--card);border:1px solid var(--line);border-radius:var(--radius-lg);padding:36px}
.contact label{display:block;font-family:var(--body);font-size:.85rem;font-weight:600;margin:0 0 6px}
.contact input,.contact select,.contact textarea{width:100%;padding:13px 16px;border:1px solid var(--line);border-radius:var(--radius);margin-bottom:18px;font-family:var(--body);font-size:.95rem;background:var(--bg);color:var(--ink)}
.contact .info h3{font-size:2rem;margin-bottom:18px}
.contact .info .line{display:flex;gap:14px;align-items:center;margin-bottom:16px;font-family:var(--body)}
.contact .info .line b{font-size:1.1rem}
@media(max-width:820px){.contact .inner{grid-template-columns:1fr;gap:32px}}
/* FOOTER */
footer.ft{background:var(--ft-bg);color:var(--ft-ink);padding:64px 0 30px}
footer.ft .top{display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:40px;padding-bottom:40px;border-bottom:1px solid var(--ft-line)}
footer.ft .script{font-family:var(--script);font-size:2.4rem;color:var(--ft-accent)}
footer.ft p{color:var(--ft-muted);font-size:.95rem;margin-top:10px;max-width:320px}
footer.ft h4{font-family:var(--body);text-transform:uppercase;letter-spacing:.14em;font-size:.78rem;margin-bottom:16px;color:var(--ft-ink)}
footer.ft a{color:var(--ft-muted);display:block;margin-bottom:10px;font-family:var(--body);font-size:.93rem}
footer.ft a:hover{color:var(--ft-accent)}
.socials{display:flex;gap:14px;margin-top:6px}
.socials a{display:flex;align-items:center;justify-content:center;width:42px;height:42px;border:1px solid var(--ft-line);border-radius:50%;color:var(--ft-ink);margin:0}
.socials a:hover{background:var(--ft-accent);color:var(--on-accent);border-color:var(--ft-accent)}
.socials svg{width:18px;height:18px}
.copyright{padding-top:26px;color:var(--ft-muted);font-family:var(--body);font-size:.82rem;display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px}
.mockbar{background:var(--ink);color:#fff;text-align:center;font-family:var(--body);font-size:.8rem;padding:8px;letter-spacing:.04em}
.mockbar b{color:var(--gold)}
/* ARTICLE */
.article{max-width:760px;margin:0 auto;padding:60px 24px 0}
.article .cat{font-family:var(--body);text-transform:uppercase;letter-spacing:.16em;color:var(--accent);font-weight:700;font-size:.78rem}
.article h1{font-size:clamp(2rem,4.5vw,3.1rem);margin:14px 0 16px}
.article .meta{color:var(--muted);font-family:var(--body);font-size:.9rem;margin-bottom:30px}
.article .lead-img{border-radius:var(--radius-lg);overflow:hidden;margin-bottom:36px;box-shadow:0 24px 50px var(--shadow)}
.article p{font-size:1.12rem;color:var(--ink);margin-bottom:24px;line-height:1.75}
.article figure{margin:36px 0}
.article figure img{border-radius:var(--radius-lg);width:100%}
.article figcaption{text-align:center;color:var(--muted);font-family:var(--body);font-size:.85rem;margin-top:10px}
.article .cta-card{background:var(--soft);border:1px solid var(--line);border-radius:var(--radius-lg);padding:34px;text-align:center;margin:48px 0}
.article .cta-card h3{font-size:1.6rem;margin-bottom:12px}
.article .cta-card p{font-size:1rem;color:var(--muted);margin-bottom:20px}
/* ---- MOTION: scroll reveal, hero drift, accent underline, success check ---- */
.reveal{transition:opacity .9s cubic-bezier(.2,.7,.2,1),transform .9s cubic-bezier(.2,.7,.2,1)}
html.js .reveal{opacity:0;transform:translateY(30px)}
.reveal.in{opacity:1!important;transform:none!important}
.hero .bg img{animation:kenburns 28s ease-in-out infinite alternate;transform-origin:60% 50%}
@keyframes kenburns{0%{transform:scale(1.06)}100%{transform:scale(1.18) translate(-1.5%,-1.2%)}}
.sec-head h2{position:relative;display:inline-block}
.sec-head h2::after{content:"";position:absolute;left:50%;bottom:-14px;transform:translateX(-50%);width:0;height:2px;background:var(--accent);transition:width 1s .35s cubic-bezier(.2,.7,.2,1)}
.sec-head.in h2::after{width:56px}
.svc .ph img,.post .ph img{will-change:transform}
.quote-success{text-align:center;padding:38px 12px;animation:fadeUp .6s ease}
.quote-success h3{font-size:1.9rem;margin:16px 0 10px}
.quote-success p{color:var(--muted);max-width:340px;margin:0 auto}
.qcheck{width:76px;height:76px;margin:0 auto;border-radius:50%;background:var(--soft);display:flex;align-items:center;justify-content:center}
.qcheck svg{width:46px;height:46px}
.qcheck circle{stroke:var(--accent);stroke-width:2.5;fill:none;stroke-dasharray:151;stroke-dashoffset:151;animation:draw .6s .05s ease forwards}
.qcheck path{stroke:var(--accent);stroke-width:3.5;stroke-linecap:round;stroke-linejoin:round;fill:none;stroke-dasharray:42;stroke-dashoffset:42;animation:draw .45s .5s ease forwards}
@keyframes draw{to{stroke-dashoffset:0}}
@keyframes fadeUp{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}
.btn,.navcta{position:relative;overflow:hidden}
.btn::after{content:"";position:absolute;top:0;left:-120%;width:60%;height:100%;background:linear-gradient(120deg,transparent,rgba(255,255,255,.35),transparent);transform:skewX(-20deg);transition:left .7s ease}
.btn:hover::after{left:140%}
@media(prefers-reduced-motion:reduce){.reveal{opacity:1;transform:none;transition:none}.hero .bg img{animation:none}.track{animation:none!important}.sec-head.in h2::after{transition:none}}
"""

THEMES = {
 "editorial": dict(
   label="Editorial Boutique",
   fonts="Cormorant+Garamond:wght@500;600;700&family=Jost:wght@400;500;600&family=Pinyon+Script",
   vars="""
    --display:'Cormorant Garamond',serif; --body:'Jost',sans-serif; --script:'Pinyon Script',cursive; --dw:600;
    --bg:#fbf9f4; --ink:#2b2a26; --muted:#6f6c63; --accent:#7c8a6e; --on-accent:#fff; --gold:#c0a062;
    --soft:#f3efe6; --card:#ffffff; --line:#e7e1d4; --shadow:rgba(60,55,40,.12);
    --radius:8px; --radius-lg:16px;
    --nav-bg:rgba(251,249,244,.86);
    --hero-scrim:linear-gradient(90deg,rgba(20,20,16,.62),rgba(20,20,16,.15)); --hero-ink:#fdfcf8; --hero-accent:#dvar; --hero-accent:#e7d9b8;
    --ft-bg:#2b2a26; --ft-ink:#f3efe6; --ft-muted:#a8a294; --ft-accent:#c9b888; --ft-line:#43413a;
   """),
 "artisan": dict(
   label="Warm Artisan Market",
   fonts="Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Nunito+Sans:wght@400;600;700&family=Caveat:wght@600",
   vars="""
    --display:'Fraunces',serif; --body:'Nunito Sans',sans-serif; --script:'Caveat',cursive; --dw:600;
    --bg:#fdf8f0; --ink:#3a2b21; --muted:#7a6555; --accent:#c0612f; --on-accent:#fff; --gold:#d99a3a;
    --soft:#f5e9d8; --card:#fffdf9; --line:#ecdcc6; --shadow:rgba(120,70,30,.14);
    --radius:14px; --radius-lg:22px;
    --nav-bg:rgba(253,248,240,.9);
    --hero-scrim:linear-gradient(90deg,rgba(45,28,18,.66),rgba(45,28,18,.18)); --hero-ink:#fff7ec; --hero-accent:#f4c98a;
    --ft-bg:#3a2b21; --ft-ink:#f5e9d8; --ft-muted:#bda690; --ft-accent:#e09a4a; --ft-line:#54402f;
   """),
 "moody": dict(
   label="Moody Gourmet",
   fonts="Playfair+Display:wght@500;600;700&family=Inter:wght@400;500;600&family=Pinyon+Script",
   vars="""
    --display:'Playfair Display',serif; --body:'Inter',sans-serif; --script:'Pinyon Script',cursive; --dw:600;
    --bg:#15110f; --ink:#efe7dc; --muted:#a99e90; --accent:#c8a76a; --on-accent:#1a1512; --gold:#d9b878;
    --soft:#1f1916; --card:#211a16; --line:#352a23; --shadow:rgba(0,0,0,.5);
    --radius:8px; --radius-lg:14px;
    --nav-bg:rgba(21,17,15,.82);
    --hero-scrim:linear-gradient(90deg,rgba(10,8,6,.78),rgba(10,8,6,.35)); --hero-ink:#f6efe3; --hero-accent:#d9b878;
    --ft-bg:#0e0b09; --ft-ink:#efe7dc; --ft-muted:#8e8276; --ft-accent:#c8a76a; --ft-line:#2c241e;
   """),
}

IG = {
 "fb": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M22 12a10 10 0 10-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.2c-1.2 0-1.6.8-1.6 1.6V12h2.7l-.4 2.9h-2.3v7A10 10 0 0022 12z"/></svg>',
 "google": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 11v3.2h5.1c-.2 1.3-1.5 3.9-5.1 3.9-3.1 0-5.6-2.6-5.6-5.7S8.9 6.7 12 6.7c1.8 0 2.9.7 3.6 1.4l2.4-2.3C16.4 4.2 14.4 3.3 12 3.3 7 3.3 3 7.3 3 12.3s4 9 9 9c5.2 0 8.6-3.6 8.6-8.8 0-.6-.1-1-.2-1.5H12z"/></svg>',
 "yelp": '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12.5 2c-.9 0-3.7.9-4.4 1.6-.4.4-.5.9-.3 1.4l3 6.7c.5 1 2 .7 2-.4l.2-8.2c0-.7-.6-1.2-1.7-1.1zM7.3 13.2 3.6 12c-.5-.2-1 0-1.3.5-.5 1-.8 3.4-.5 4.5.1.5.5.9 1.1.9l4.1-.4c1-.1 1.2-1.6.2-2zm2 2.3c-.4-.3-1-.2-1.3.2L5.4 19c-.4.5-.3 1.1.2 1.5.9.6 3.1 1.3 4 1.2.5 0 .9-.4 1-.9l.3-4.1c0-.6-.4-.9-1.6-1.2zm5.9.3c-.4-.5-1-.5-1.4-.1l-.3.3c-.6.7-.3 1.7.1 2.3l2.4 3.3c.3.4.9.5 1.4.2 1-.6 2.6-2.4 3-3.4.2-.5 0-1-.5-1.2L15.1 15.8zm5.4-4.6-4 1.2c-1 .3-.9 1.8.2 2l4 .4c.6 0 1-.4 1.1-.9.3-1.1 0-3.5-.5-4.5-.3-.5-.8-.6-1.3-.4z"/></svg>',
}

def social_icons(prefix=""):
    return (f'<div class="socials">'
            f'<a href="{SOCIAL["facebook"]}" target="_blank" rel="noopener" aria-label="Facebook">{IG["fb"]}</a>'
            f'<a href="{SOCIAL["google"]}" target="_blank" rel="noopener" aria-label="Google reviews">{IG["google"]}</a>'
            f'<a href="{SOCIAL["yelp"]}" target="_blank" rel="noopener" aria-label="Yelp">{IG["yelp"]}</a>'
            f'</div>')

def head(theme, title, prefix=""):
    t = THEMES[theme]
    return f"""<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="A La Cart Charcuterie Co. Mobile charcuterie, grazing tables, boards, cups, and cart catering for weddings and events in Lawrence, KS and the Greater Topeka and Kansas City metros.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family={t['fonts']}&display=swap" rel="stylesheet">
<style>:root{{{t['vars']}}}{BASE_CSS}</style>
<script>document.documentElement.classList.add('js')</script></head><body>
<div class="mockbar">CONCEPT MOCKUP for A La Cart Charcuterie Co. &nbsp;&middot;&nbsp; Theme: <b>{t['label']}</b> &nbsp;&middot;&nbsp; built by Eagle Point Publishing</div>"""

def nav(prefix=""):
    links = ["Services","Gallery","Reviews","Journal","Areas","Contact"]
    nl = "".join(f'<a href="{prefix}index_THEME.html#{l.lower()}">{l}</a>' for l in links)
    return f"""<header class="nav"><div class="wrap">
<a class="brand" href="{prefix}index_THEME.html"><span class="script">A La Cart</span><span class="sub">Charcuterie Co.</span></a>
<nav>{nl}<a class="navcta" href="{prefix}index_THEME.html#contact">Book Now</a></nav>
</div></header>"""

def footer(prefix=""):
    svc = "".join(f'<a href="{prefix}index_THEME.html#services">{s["name"]}</a>' for s in SERVICES[:5])
    return f"""<footer class="ft"><div class="wrap">
<div class="top">
 <div><div class="script">A La Cart</div><p>{BIZ['tagline']} Hand built and styled on site by Rebecca, serving Lawrence and the Greater Topeka and Kansas City metros.</p>{social_icons(prefix)}</div>
 <div><h4>Services</h4>{svc}</div>
 <div><h4>Get in touch</h4>
   <a href="tel:{BIZ['phone_raw']}">{BIZ['phone_display']}</a>
   <a href="mailto:{BIZ['email']}">{BIZ['email']}</a>
   <a href="{SOCIAL['google']}" target="_blank" rel="noopener">Read our Google reviews</a>
   <a href="{SOCIAL['yelp']}" target="_blank" rel="noopener">Find us on Yelp</a>
   <a href="{SOCIAL['facebook']}" target="_blank" rel="noopener">Follow on Facebook</a>
 </div>
</div>
<div class="copyright"><span>&copy; 2026 A La Cart Charcuterie Co. &middot; Lawrence, KS</span><span>Concept design by Eagle Point Publishing</span></div>
</div></footer>
<script>
(function(){{
 var sel=['.sec-head','.intro .txt','.intro .pic','.svc','.post','.gal a','.areas .chips span','.faq','.contact .info','#quoteWrap','.article > p','.article figure','.lead-img','.cta-card'];
 var els=[];sel.forEach(function(s){{document.querySelectorAll(s).forEach(function(e){{e.classList.add('reveal');els.push(e);}});}});
 document.querySelectorAll('.svc-grid,.posts,.gal').forEach(function(g){{Array.prototype.forEach.call(g.children,function(c,i){{c.style.transitionDelay=(i*0.08)+'s';}});}});
 if('IntersectionObserver' in window){{
   var io=new IntersectionObserver(function(en){{en.forEach(function(x){{if(x.isIntersecting){{x.target.classList.add('in');io.unobserve(x.target);}}}});}},{{threshold:0.12,rootMargin:'0px 0px -7% 0px'}});
   els.forEach(function(e){{io.observe(e);}});
 }} else {{ els.forEach(function(e){{e.classList.add('in');}}); }}
 var hero=document.querySelectorAll('.hero .inner > *');
 hero.forEach(function(e,i){{e.style.opacity=0;e.style.transform='translateY(22px)';e.style.transition='opacity 1s '+(i*0.13+0.2)+'s ease,transform 1s '+(i*0.13+0.2)+'s cubic-bezier(.2,.7,.2,1)';}});
 requestAnimationFrame(function(){{requestAnimationFrame(function(){{hero.forEach(function(e){{e.style.opacity=1;e.style.transform='none';}});}});}});
 var f=document.getElementById('quoteForm');
 if(f){{f.addEventListener('submit',function(ev){{ev.preventDefault();
   var w=document.getElementById('quoteWrap');var nm=(f.querySelector('[name=name]')||{{}}).value||'';
   w.innerHTML='<div class=\\'quote-success\\'><div class=\\'qcheck\\'><svg viewBox=\\'0 0 52 52\\'><circle cx=\\'26\\' cy=\\'26\\' r=\\'23\\'/><path d=\\'M16 27l7 7 14-15\\'/></svg></div><h3>Thank you'+(nm?', '+nm.split(' ')[0]:'')+'!</h3><p>Your request is on its way. Rebecca will reply within one business day with availability and pricing.</p></div>';
   w.scrollIntoView({{behavior:'smooth',block:'center'}});
 }});}}
}})();
</script>
<script>setTimeout(function(){{var n=document.querySelectorAll('.reveal');for(var i=0;i<n.length;i++){{n[i].classList.add('in');}}var h=document.querySelectorAll('.hero .inner > *');for(var j=0;j<h.length;j++){{h[j].style.opacity=1;h[j].style.transform='none';}}}},3000);</script>
</body></html>"""

def reviews_carousel(speed="110s"):
    cards = []
    loop = REVIEWS + REVIEWS  # duplicate for seamless loop
    for r in loop:
        cards.append(f"""<a class="rev" href="{r['url']}" target="_blank" rel="noopener">
<div class="stars">{stars(r['stars'])}</div>
<div class="txt">"{html.escape(r['text'])}"</div>
<div class="ft"><span class="who">{html.escape(r['name'])}</span><span class="src">{r['src']} &#8599;</span></div></a>""")
    return f"""<section class="reviews" id="reviews"><div class="wrap">
<div class="sec-head"><div class="eyebrow">Loved by our guests</div><h2>Five stars, across every platform</h2>
<p>Real reviews from Google, Yelp, and Facebook. Tap any card to read it at the source.</p></div></div>
<div class="marquee"><div class="track" style="--marquee-speed:{speed}">{''.join(cards)}</div></div>
<div class="wrap" style="text-align:center;margin-top:40px"><a class="btn ghost" href="{SOCIAL['google']}" target="_blank" rel="noopener">See all reviews</a></div>
</section>"""

def services_section(prefix=""):
    cards = ""
    for s in SERVICES:
        cards += f"""<div class="svc"><div class="ph">{img_tag(s['img'],s['name'],prefix=prefix)}</div>
<div class="body"><h3>{s['name']}</h3><div class="price">{s['price']}</div><p>{s['blurb']}</p></div></div>"""
    return f"""<section id="services"><div class="wrap"><div class="sec-head">
<div class="eyebrow">What we create</div><h2>Charcuterie for every occasion</h2>
<p>From an individual cup to a full wedding grazing table, every order is built by hand and styled to your event.</p></div>
<div class="svc-grid">{cards}</div></div></section>"""

def hero(theme, prefix=""):
    return f"""<section class="hero">
<div class="bg">{img_tag('hero_cart','A La Cart branded charcuterie cart at an outdoor wedding',prefix=prefix)}</div>
<div class="scrim"></div>
<div class="wrap"><div class="inner">
<div class="eyebrow">Lawrence &middot; Topeka &middot; Kansas City</div>
<h1>Charcuterie that becomes the centerpiece</h1>
<p class="lede">Grazing tables, boards, cups, and our signature mobile cart. Beautifully built by hand, styled on site, and impossible to forget.</p>
<div class="cta-row"><a class="btn" href="#contact">Request a quote</a><a class="btn ghost" href="#services">View services</a></div>
</div></div>
<div class="wrap badge-row"><span><b>5.0{STAR}</b> on Google</span><span><b>#1</b> in the Lawrence map pack</span><span><b>Weddings</b> &amp; events welcome</span></div>
</section>"""

def intro(prefix=""):
    return f"""<section id="story"><div class="wrap"><div class="intro">
<div class="txt"><div class="eyebrow">Our story</div>
<h2>Hand built, styled on site, made to be remembered</h2>
<p>A La Cart Charcuterie Co. is a Lawrence, Kansas based maker of grazing tables, charcuterie boards, cups, and boxes for weddings, parties, and everything in between. Rebecca is the artist behind every spread.</p>
<p>The reviews say it best. Guests do not just eat what she builds, they photograph it, talk about it, and ask who made it. That attention to detail is the whole point.</p>
<a class="btn" href="#contact">Plan your event</a></div>
<div class="pic">{img_tag('cups_close','Branded A La Cart charcuterie cups',prefix=prefix)}<div class="tag">Crafted by Rebecca</div></div>
</div></div></section>"""

def gallery(prefix=""):
    items = ["board_round","cups_trio","trailer","box_big","boxes_clam","cup_wine","boxes_holiday","crackers"]
    cells = "".join(f'<a href="{SOCIAL["facebook"]}" target="_blank" rel="noopener">{img_tag(k,"A La Cart charcuterie",prefix=prefix)}</a>' for k in items)
    return f"""<section id="gallery"><div class="wrap"><div class="sec-head">
<div class="eyebrow">The spread</div><h2>A look at our work</h2>
<p>See more on our Facebook. Every board, box, and table is one of a kind.</p></div>
<div class="gal">{cells}</div></div></section>"""

def areas():
    chips = "".join(f"<span>{a}</span>" for a in BIZ["areas"])
    return f"""<section class="areas" id="areas"><div class="wrap"><div class="sec-head">
<div class="eyebrow" style="color:var(--on-accent);opacity:.85">Where we serve</div>
<h2>Lawrence and the Greater Topeka and Kansas City metros</h2>
<p style="color:var(--on-accent);opacity:.9">Based in Lawrence, KS and traveling throughout the region for weddings, parties, and corporate events.</p></div>
<div class="chips">{chips}</div></div></section>"""

def blog_teaser(prefix=""):
    cards = ""
    for b in BLOG[:3]:
        cards += f"""<a class="post" href="{prefix}blog/{b['slug']}.html">
<div class="ph">{img_tag(b['thumb'],b['title'],prefix=prefix)}</div>
<div class="body"><div class="cat">{b['cat']}</div><h3>{b['title']}</h3><p>{b['excerpt']}</p><span class="more">Read more &#8594;</span></div></a>"""
    return f"""<section id="journal"><div class="wrap"><div class="sec-head">
<div class="eyebrow">From the journal</div><h2>Tips, planning, and inspiration</h2>
<p>Ideas for weddings, parties, and gatherings across Lawrence and Kansas City.</p></div>
<div class="posts">{cards}</div>
<div style="text-align:center;margin-top:44px"><a class="btn ghost" href="{prefix}blog/index.html">Visit the journal</a></div></div></section>"""

def faq():
    items = "".join(f"<details class='faq'><summary>{q}</summary><p>{a}</p></details>" for q,a in FAQS)
    return f"""<section id="faq"><div class="wrap"><div class="sec-head">
<div class="eyebrow">Good to know</div><h2>Frequently asked</h2></div>
<div class="faq-list">{items}</div></div></section>"""

def contact():
    opts = "".join(f"<option>{s['name']}</option>" for s in SERVICES)
    events = ["Wedding","Graduation / Open house","Corporate / Office","Birthday / Private party","Baby or Bridal shower","Holiday gathering","Other"]
    eopts = "".join(f"<option>{e}</option>" for e in events)
    return f"""<section class="contact" id="contact"><div class="wrap"><div class="inner">
<div class="info"><div class="eyebrow">Let's plan something beautiful</div>
<h3>Request a quote</h3>
<p style="color:var(--muted);margin-bottom:24px">Tell us the date, the headcount, and the occasion. We will design a spread around it and send pricing. We ask for a few details so we can scope your event accurately and reply fast.</p>
<div class="line">&#9742; <b><a href="tel:{BIZ['phone_raw']}">{BIZ['phone_display']}</a></b></div>
<div class="line">&#9993; <a href="mailto:{BIZ['email']}">{BIZ['email']}</a></div>
<div class="line">&#9733; 5.0 on Google &middot; #1 in the Lawrence map pack</div>
{social_icons()}</div>
<div id="quoteWrap" class="form">
<form id="quoteForm">
<div style="display:grid;grid-template-columns:1fr 1fr;gap:0 16px">
 <div><label>Name</label><input name="name" required placeholder="Your name"></div>
 <div><label>Phone</label><input name="phone" placeholder="{BIZ['phone_display']}"></div>
</div>
<label>Email</label><input name="email" type="email" required placeholder="you@email.com">
<div style="display:grid;grid-template-columns:1fr 1fr;gap:0 16px">
 <div><label>Occasion</label><select name="occasion">{eopts}</select></div>
 <div><label>Service of interest</label><select name="service">{opts}</select></div>
</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:0 16px">
 <div><label>Event date</label><input name="date" type="text" placeholder="e.g. Aug 16, 2026"></div>
 <div><label>Guest count <span style="font-weight:400;color:var(--muted);font-size:.78rem">(to size your spread)</span></label><input name="guests" placeholder="e.g. 80"></div>
</div>
<label>Where is your event?</label><input name="location" placeholder="City or venue, e.g. Lawrence or Overland Park">
<label>Tell us about your event</label><textarea name="message" rows="4" placeholder="The vibe you want, colors, must haves, anything special..."></textarea>
<button type="submit" class="btn" style="width:100%">Send my quote request</button>
<p style="font-size:.78rem;color:var(--muted);text-align:center;margin-top:12px">We reply within one business day. No spam, ever.</p>
</form></div>
</div></div></section>"""

# ----------------------------------------------------------------------------- BUILD HOMEPAGES
def build_home(theme):
    body = (head(theme, f"A La Cart Charcuterie Co. | Grazing Tables, Boards & Cart Catering | Lawrence & Kansas City")
            + nav() + hero(theme) + intro() + services_section() + reviews_carousel(
                {"editorial":"120s","artisan":"100s","moody":"130s"}[theme])
            + gallery() + areas() + blog_teaser() + faq() + contact() + footer())
    body = body.replace("index_THEME.html", f"index_{theme}.html")
    with open(os.path.join(ROOT, f"index_{theme}.html"), "w") as f:
        f.write(body)

# ----------------------------------------------------------------------------- BUILD BLOG (in editorial theme)
def build_blog():
    os.makedirs(os.path.join(ROOT, "blog"), exist_ok=True)
    theme = "editorial"; pre = "../"
    # index
    cards = ""
    for b in BLOG:
        cards += f"""<a class="post" href="{b['slug']}.html"><div class="ph">{img_tag(b['thumb'],b['title'],prefix=pre)}</div>
<div class="body"><div class="cat">{b['cat']}</div><h3>{b['title']}</h3><p>{b['excerpt']}</p><span class="more">Read more &#8594;</span></div></a>"""
    idx = (head(theme,"The Journal | A La Cart Charcuterie Co.",pre) + nav(pre)
           + f"""<section style="padding-top:64px"><div class="wrap"><div class="sec-head">
<div class="eyebrow">The Journal</div><h2>Charcuterie tips, planning &amp; inspiration</h2>
<p>Ideas and guides for weddings, parties, and gatherings across Lawrence and the Greater Topeka and Kansas City metros.</p></div>
<div class="posts">{cards}</div></div></section>""" + footer(pre))
    idx = idx.replace("index_THEME.html", f"index_{theme}.html")
    open(os.path.join(ROOT,"blog","index.html"),"w").write(idx)
    # posts
    for i,b in enumerate(BLOG):
        paras = "".join(f"<p>{p}</p>" for p in b["body"][:1])
        # weave inline images between paragraphs
        figs = b["inline"]
        rest = b["body"][1:]
        mid = ""
        for j,p in enumerate(rest):
            mid += f"<p>{p}</p>"
            if j < len(figs):
                mid += f"<figure>{img_tag(figs[j],b['title'],prefix=pre)}<figcaption>A La Cart Charcuterie Co. &middot; {b['cat']}</figcaption></figure>"
        # any leftover figs
        for k in range(len(rest),len(figs)):
            mid += f"<figure>{img_tag(figs[k],b['title'],prefix=pre)}<figcaption>A La Cart Charcuterie Co.</figcaption></figure>"
        rel_prev = BLOG[(i-1)%len(BLOG)]; rel_next = BLOG[(i+1)%len(BLOG)]
        art = (head(theme, f"{b['title']} | A La Cart Charcuterie Co.", pre) + nav(pre)
          + f"""<article class="article"><div class="cat">{b['cat']}</div><h1>{b['title']}</h1>
<div class="meta">By Rebecca &middot; A La Cart Charcuterie Co. &middot; Lawrence, KS</div>
<div class="lead-img">{img_tag(b['thumb'],b['title'],prefix=pre)}</div>
{paras}{mid}
<div class="cta-card"><h3>Planning an event?</h3><p>Let us build something beautiful for your wedding, party, or gathering in Lawrence or Kansas City.</p>
<a class="btn" href="../index_{theme}.html#contact">Request a quote</a></div>
<p style="font-family:var(--body);font-size:.9rem;color:var(--muted)"><a href="../index_{theme}.html#journal" style="color:var(--accent);font-weight:600">&#8592; Back to the journal</a></p>
</article>
<section style="padding-top:40px"><div class="wrap"><div class="sec-head"><div class="eyebrow">Keep reading</div></div>
<div class="posts"><a class="post" href="{rel_prev['slug']}.html"><div class="ph">{img_tag(rel_prev['thumb'],rel_prev['title'],prefix=pre)}</div><div class="body"><div class="cat">{rel_prev['cat']}</div><h3>{rel_prev['title']}</h3></div></a>
<a class="post" href="{rel_next['slug']}.html"><div class="ph">{img_tag(rel_next['thumb'],rel_next['title'],prefix=pre)}</div><div class="body"><div class="cat">{rel_next['cat']}</div><h3>{rel_next['title']}</h3></div></a></div></div></section>"""
          + footer(pre))
        art = art.replace("index_THEME.html", f"index_{theme}.html")
        open(os.path.join(ROOT,"blog",f"{b['slug']}.html"),"w").write(art)

# ----------------------------------------------------------------------------- CHOOSER
def build_chooser():
    cards = ""
    blurbs = {"editorial":"Light, refined, magazine style. Cream and sage, elegant serif type, airy whitespace. An evolution of the current elegant brand.",
              "artisan":"Warm, handcrafted, local. Terracotta and oatmeal, friendly serif with a handwritten accent. The farmers market feel.",
              "moody":"Dramatic and luxe. Deep espresso with gold, food that pops against dark. Built for the wedding and high end event lane."}
    for tk,tv in THEMES.items():
        cards += f"""<a class="choice" href="index_{tk}.html">
<div class="cp">{img_tag('hero_cart' if tk=='editorial' else ('trailer' if tk=='artisan' else 'board_round'),tv['label'])}</div>
<div class="cb"><div class="num">Concept {'A' if tk=='editorial' else ('B' if tk=='artisan' else 'C')}</div><h3>{tv['label']}</h3><p>{blurbs[tk]}</p><span class="more">View this concept &#8594;</span></div></a>"""
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>A La Cart Charcuterie Co. | Website Concepts</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Jost:wght@400;500;600&family=Pinyon+Script&display=swap" rel="stylesheet">
<style>
*{{box-sizing:border-box;margin:0;padding:0}}body{{font-family:'Jost',sans-serif;background:#f3efe6;color:#2b2a26;line-height:1.6}}
.hd{{text-align:center;padding:80px 24px 40px}}.hd .script{{font-family:'Pinyon Script',cursive;font-size:3.4rem;color:#7c8a6e}}
.hd .sub{{letter-spacing:.2em;text-transform:uppercase;font-size:.78rem;color:#6f6c63;margin-top:6px}}
.hd h1{{font-family:'Cormorant Garamond',serif;font-size:2.6rem;margin:22px 0 10px}}.hd p{{color:#6f6c63;max-width:600px;margin:0 auto}}
.grid{{max-width:1180px;margin:30px auto 40px;padding:0 24px;display:grid;grid-template-columns:repeat(3,1fr);gap:28px}}
.choice{{background:#fff;border:1px solid #e7e1d4;border-radius:18px;overflow:hidden;text-decoration:none;color:inherit;transition:transform .25s,box-shadow .25s;display:flex;flex-direction:column}}
.choice:hover{{transform:translateY(-8px);box-shadow:0 30px 60px rgba(60,55,40,.16)}}
.cp{{aspect-ratio:4/3;overflow:hidden}}.cp img{{width:100%;height:100%;object-fit:cover}}
.cb{{padding:28px}}.num{{font-size:.72rem;letter-spacing:.16em;text-transform:uppercase;color:#7c8a6e;font-weight:700}}
.cb h3{{font-family:'Cormorant Garamond',serif;font-size:1.7rem;margin:8px 0 12px}}.cb p{{color:#6f6c63;font-size:.96rem}}
.more{{display:inline-block;margin-top:16px;color:#7c8a6e;font-weight:600}}
.ft{{text-align:center;padding:30px;color:#8a857a;font-size:.85rem}}
.bloglink{{text-align:center;padding-bottom:70px}}.bloglink a{{color:#7c8a6e;font-weight:600;text-decoration:none;border:1px solid #cfc8b8;padding:12px 26px;border-radius:8px}}
@media(max-width:860px){{.grid{{grid-template-columns:1fr}}}}
</style></head><body>
<div class="hd"><div class="script">A La Cart</div><div class="sub">Charcuterie Co.</div>
<h1>Three website concepts</h1><p>Prepared by Eagle Point Publishing for your review. Each concept is a full homepage using your real photos and reviews. Pick a direction and we build it out.</p></div>
<div class="grid">{cards}</div>
<div class="bloglink"><a href="blog/index.html">See the sample journal (12 articles) &#8594;</a></div>
<div class="ft">Concept mockups &middot; Eagle Point Publishing &middot; 2026</div>
</body></html>"""
    open(os.path.join(ROOT,"index.html"),"w").write(page)

for tk in THEMES: build_home(tk)
build_blog()
build_chooser()
print("BUILT:", sorted(os.listdir(ROOT)))
print("blog:", sorted(os.listdir(os.path.join(ROOT,"blog"))))
