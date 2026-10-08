"""Generate animated SVG assets for the GitHub profile README."""
import math, random, os, sys

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
random.seed(7)

# ---------- shared palette ----------
BG0, BG1 = "#0B0D12", "#151B27"
LINE = "#2B3140"
TXT, MUTED = "#F3EFE7", "#9C978E"
GOLD = "#D4B27A"
CYAN, ORANGE, HOT, RED, GREEN = "#8EB8E0", "#E0925A", "#F1D3A0", "#C65A43", "#8CBFA0"
SANS = "Geist,'Helvetica Neue',Helvetica,Arial,sans-serif"
MONO = SANS
SERIF = "'Instrument Serif',Georgia,'Times New Roman',serif"

BASE_CSS = f"""
.sans{{font-family:{SANS}}} .mono{{font-family:{MONO};font-weight:500}} .serif{{font-family:{SERIF};font-weight:400}}
.spin{{transform-box:fill-box;transform-origin:center;animation:spin .22s linear infinite}}
@keyframes spin{{to{{transform:rotate(360deg)}}}}
.blink{{animation:blink 1.2s steps(2,start) infinite}}
@keyframes blink{{to{{visibility:hidden}}}}
.pulse{{animation:pulse 2.4s ease-in-out infinite}}
@keyframes pulse{{0%,100%{{opacity:.35}}50%{{opacity:1}}}}
.flow{{animation:flow 1s linear infinite}}
@keyframes flow{{to{{stroke-dashoffset:-32}}}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
"""


def frame(w, h, body, css="", label="", defs=""):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{label}">
<title>{label}</title>
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{BG0}"/><stop offset="1" stop-color="{BG1}"/></linearGradient>
<clipPath id="frame"><rect width="{w}" height="{h}" rx="16"/></clipPath>
<filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6"/></filter>
<filter id="soft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="2"/></filter>
<filter id="grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" stitchTiles="stitch"/><feColorMatrix values="0 0 0 0 1  0 0 0 0 .95  0 0 0 0 .88  0 0 0 .55 0"/></filter>
<filter id="mono" color-interpolation-filters="sRGB"><feColorMatrix values="0 0 0 0 .95  0 0 0 0 .93  0 0 0 0 .9  0 0 0 1 0"/></filter>
<radialGradient id="vignette" cx="30%" cy="0%" r="110%"><stop offset="0" stop-color="{GOLD}" stop-opacity=".07"/><stop offset=".6" stop-color="{GOLD}" stop-opacity="0"/></radialGradient>
{defs}
</defs>
<style>{BASE_CSS}{css}</style>
<g clip-path="url(#frame)">
<rect width="{w}" height="{h}" fill="url(#bg)"/>
<rect width="{w}" height="{h}" fill="url(#vignette)"/>
<rect width="{w}" height="{h}" filter="url(#grain)" opacity=".07"/>
{body}
</g>
<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="16" fill="none" stroke="{LINE}"/>
</svg>
"""


def stars(w, h, n, ymax=None, avoid=((0, 0, 620, 66),)):
    ymax = ymax or h
    out = []
    while len(out) < n:
        x, y = random.uniform(0, w), random.uniform(0, ymax)
        if any(a <= x <= c and b <= y <= d for a, b, c, d in avoid):
            continue
        r = random.choice([0.6, 0.8, 1, 1.2, 1.6])
        d = random.uniform(1.5, 4.5)
        dl = random.uniform(0, 4)
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="#fff" style="animation:twinkle {d:.2f}s ease-in-out {dl:.2f}s infinite"/>')
    return "\n".join(out)


def corner_brackets(w, h, m=14, s=16, c=CYAN):
    p = f"M{m},{m+s}V{m}H{m+s} M{w-m-s},{m}H{w-m}V{m+s} M{w-m},{h-m-s}V{h-m}H{w-m-s} M{m+s},{h-m}H{m}V{h-m-s}"
    return f'<path d="{p}" fill="none" stroke="{c}" stroke-opacity=".45" stroke-width="1.5"/>'


def header(label, title, x=24):
    return (f'<text x="{x}" y="32" class="sans" font-size="10.5" font-weight="500" letter-spacing="2.6" fill="{GOLD}">{label}</text>'
            f'<text x="{x}" y="60" class="serif" font-size="27" letter-spacing="-.3" fill="{TXT}">{title}</text>')


def write(name, svg):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(svg)


# =====================================================================
# HERO
# =====================================================================
def hero():
    W, H = 1200, 420
    streaks = []
    for i in range(16):
        x = random.uniform(0, W)
        L = random.uniform(10, 50)
        d = random.uniform(0.7, 1.8)
        dl = -random.uniform(0, 2)
        op = random.uniform(.06, .16)
        streaks.append(f'<line x1="{x:.0f}" y1="-60" x2="{x:.0f}" y2="{-60+L:.0f}" stroke="#9FC3FF" stroke-opacity="{op:.2f}" stroke-width="1" style="animation:fall {d:.2f}s linear {dl:.2f}s infinite"/>')
    smoke = []
    for i in range(9):
        d = 2.4
        dl = -i * d / 9
        dx = random.uniform(-22, 22)
        smoke.append(f'<circle cx="0" cy="0" r="9" fill="#C9D3E6" style="--dx:{dx:.0f}px;animation:smoke {d}s ease-out {dl:.2f}s infinite"/>')
    css = """
@keyframes twinkle{0%,100%{opacity:.25}50%{opacity:1}}
@keyframes fall{to{transform:translateY(540px)}}
.rocket{animation:shake .09s linear infinite alternate}
@keyframes shake{from{transform:translate(-.6px,0)}to{transform:translate(.6px,.8px)}}
.flame{transform-box:fill-box;transform-origin:50% 0;animation:flick .11s ease-in-out infinite alternate}
.flame2{transform-box:fill-box;transform-origin:50% 0;animation:flick .07s ease-in-out infinite alternate-reverse}
@keyframes flick{from{transform:scale(.9,.82)}to{transform:scale(1.06,1.12)}}
@keyframes smoke{0%{transform:translate(0,0) scale(.4);opacity:.55}100%{transform:translate(var(--dx),170px) scale(3.2);opacity:0}}
.drone{animation:bob 3.2s ease-in-out infinite}
@keyframes bob{0%,100%{transform:translate(0,0) rotate(-1.5deg)}50%{transform:translate(14px,-10px) rotate(1.5deg)}}
.prop{transform-box:fill-box;transform-origin:center;animation:blur .08s linear infinite alternate}
@keyframes blur{from{transform:scaleX(1)}to{transform:scaleX(.25)}}
.caret{animation:blink 1s steps(2,start) infinite}
.wp{animation:pulse 1.6s ease-in-out infinite}
.rise{opacity:0;animation:rise .9s cubic-bezier(.2,.7,.2,1) forwards}
@keyframes rise{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}
"""
    defs = f"""
<linearGradient id="flameG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".18" stop-color="{HOT}"/><stop offset=".55" stop-color="{ORANGE}"/><stop offset="1" stop-color="{RED}" stop-opacity="0"/></linearGradient>
<linearGradient id="nameG" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#F3DDB2"/><stop offset=".6" stop-color="{GOLD}"/><stop offset="1" stop-color="#B98A55"/></linearGradient>
<radialGradient id="earth" cx="50%" cy="0%" r="70%"><stop offset="0" stop-color="#24304A"/><stop offset="1" stop-color="#070C1A"/></radialGradient>
<linearGradient id="body" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#9AA6BC"/><stop offset=".45" stop-color="#F4F7FC"/><stop offset="1" stop-color="#8090AA"/></linearGradient>
<clipPath id="typeClip"><rect x="64" y="258" width="0" height="34"><animate attributeName="width" values="0;640;640;0" keyTimes="0;.32;.88;1" dur="9s" repeatCount="indefinite"/></rect></clipPath>
"""
    rocket = f"""
<g transform="translate(1010 92)">
  <g style="transform:translate(0,182px)">{''.join(smoke)}</g>
  <ellipse cx="0" cy="210" rx="34" ry="70" fill="{ORANGE}" opacity=".35" filter="url(#glow)"/>
  <path class="flame" d="M-15,176 C-17,214 -6,250 0,286 C6,250 17,214 15,176 Z" fill="url(#flameG)"/>
  <path class="flame2" d="M-8,176 C-9,198 -3,218 0,238 C3,218 9,198 8,176 Z" fill="#fff" opacity=".9"/>
  <g class="rocket">
    <path d="M-30,150 L-46,186 L-46,192 L-20,178 Z" fill="{RED}"/>
    <path d="M30,150 L46,186 L46,192 L20,178 Z" fill="#C2342A"/>
    <path d="M0,0 C18,22 24,52 24,80 L24,170 L-24,170 L-24,80 C-24,52 -18,22 0,0 Z" fill="url(#body)"/>
    <path d="M0,0 C9,11 15,24 19,38 L-19,38 C-15,24 -9,11 0,0 Z" fill="{RED}"/>
    <rect x="-24" y="118" width="48" height="8" fill="{BG1}" opacity=".8"/>
    <circle cx="0" cy="78" r="10" fill="{BG1}" stroke="#C8D2E4" stroke-width="3"/>
    <circle cx="-3" cy="75" r="3" fill="{CYAN}" opacity=".8"/>
    <path d="M-17,170 L-14,180 L14,180 L17,170 Z" fill="#4A5670"/>
    <path d="M-4,130 L-4,168 L4,168 L4,130 Z" fill="#B4BFD2" opacity=".6"/>
    
  </g>
</g>"""
    drone = f"""
<g transform="translate(800 92)"><g class="drone">
  <ellipse cx="0" cy="0" rx="74" ry="5" fill="#2A3A60"/>
  <rect x="-74" y="-2" width="148" height="4" rx="2" fill="#D5DDEB"/>
  <path d="M-34,-4 Q0,-16 34,-4 L30,6 Q0,12 -34,6 Z" fill="#E9EEF8"/>
  <rect x="-48" y="-12" width="3" height="10" fill="#8693AB"/><rect x="45" y="-12" width="3" height="10" fill="#8693AB"/>
  <rect x="-24" y="-12" width="3" height="10" fill="#8693AB"/><rect x="21" y="-12" width="3" height="10" fill="#8693AB"/>
  <ellipse class="prop" cx="-46.5" cy="-13" rx="17" ry="1.8" fill="{CYAN}" opacity=".85"/>
  <ellipse class="prop" cx="46.5" cy="-13" rx="17" ry="1.8" fill="{CYAN}" opacity=".85" style="animation-delay:-.03s"/>
  <ellipse class="prop" cx="-22.5" cy="-13" rx="13" ry="1.6" fill="{CYAN}" opacity=".6" style="animation-delay:-.05s"/>
  <ellipse class="prop" cx="22.5" cy="-13" rx="13" ry="1.6" fill="{CYAN}" opacity=".6" style="animation-delay:-.02s"/>
  <circle cx="-38" cy="0" r="2" fill="{RED}" class="blink"/><circle cx="38" cy="0" r="2" fill="{GREEN}" class="blink" style="animation-delay:-.6s"/>
  
</g></g>
"""
    text = f"""
<g class="rise" style="animation-delay:.1s"><text x="64" y="100" class="sans" font-size="11.5" font-weight="500" letter-spacing="3.2" fill="{GOLD}">AEROSPACE ENGINEER  ·  PROPULSION &amp; ENERGETICS</text></g>
<g class="rise" style="animation-delay:.3s"><text x="60" y="180" class="serif" font-size="88" letter-spacing="-1.5" fill="{TXT}">Manikandan</text></g>
<g class="rise" style="animation-delay:.5s"><text x="60" y="256" class="serif" font-size="88" font-style="italic" letter-spacing="-1.5" fill="url(#nameG)">Shanmugam</text></g>
<g class="rise" style="animation-delay:.8s"><text x="64" y="300" class="sans" font-size="16" fill="{TXT}" fill-opacity=".85">MSc Aeronautics &amp; Space, ISAE-ENSMA — propulsion, energetics &amp; autonomous flight</text></g>
<g class="rise" style="animation-delay:1s">
  <rect x="64" y="328" width="392" height="34" rx="17" fill="{GOLD}" fill-opacity=".06" stroke="{GOLD}" stroke-opacity=".55"/>
  <circle cx="84" cy="345" r="3.5" fill="{GOLD}" class="pulse"/>
  <text x="98" y="349.5" class="sans" font-size="13" fill="{TXT}">Available for a six-month internship from March 2027</text>
</g>"""
    hud = ""
    body = f"""
{stars(W, H, 55, avoid=((40, 70, 720, 385), (930, 20, 1190, 50), (960, 370, 1190, 410)))}
<g>{''.join(streaks)}</g>
<ellipse cx="560" cy="1180" rx="1100" ry="820" fill="url(#earth)"/>
<ellipse cx="560" cy="1180" rx="1100" ry="820" fill="none" stroke="{CYAN}" stroke-opacity=".35" stroke-width="1.5" filter="url(#soft)"/>
<ellipse cx="560" cy="1180" rx="1100" ry="820" fill="none" stroke="{CYAN}" stroke-opacity=".1" stroke-width="18" filter="url(#glow)"/>
{drone}
{rocket}
{text}
{hud}"""
    write("hero.svg", frame(W, H, body, css, "Manikandan Shanmugam — propulsion, energetics and autonomous flight", defs))


# =====================================================================
# ATREX ENGINE
# =====================================================================
def atrex():
    W, H = 1200, 450
    C = 240  # centerline
    mir = lambda y: 2 * C - y

    def casing_inner(x):
        if x <= 100: return 170
        if x <= 250: return 170 + (158 - 170) * (x - 100) / 150
        if x <= 700: return 158
        if x <= 880:
            t = (x - 700) / 180
            return 158 + (200 - 158) * (3 * t * t - 2 * t ** 3)
        return 200 + (148 - 200) * (x - 880) / 200

    def hub(x):
        if x < 40: return C
        if x <= 240: return C - 28 * (x - 40) / 200
        if x <= 620: return 212
        if x <= 720: return 212 + 28 * (x - 620) / 100
        return C

    def lane(f, upper=True, x0=40, x1=1200):
        pts = []
        for x in range(x0, x1 + 1, 10):
            ci = casing_inner(min(x, 1080))
            if x > 1080:  # free plume, slight expansion
                ci = 148 - (x - 1080) * 0.12
            hb = hub(x)
            if x < 100:  # upstream: free stream converging to intake
                ci = 170 - (100 - x) * .1
            y = ci + f * (hb - ci)
            pts.append((x, y if upper else mir(y)))
        return "M" + " L".join(f"{x},{y:.1f}" for x, y in pts)

    # color along the duct (fraction of path)
    def frac(x): return (x - 40) / 1160
    cols = f"#FFC58A;#FFC58A;{CYAN};{CYAN};#9AD8FF;{ORANGE};{HOT};#FFF0C8"
    kt = f"0;{frac(262):.3f};{frac(330):.3f};{frac(380):.3f};{frac(520):.3f};{frac(560):.3f};{frac(700):.3f};1"

    parts = []
    lanes = [(.22, True), (.55, True), (.85, True), (.22, False), (.55, False), (.85, False)]
    for li, (f, up) in enumerate(lanes):
        d = lane(f, up)
        n = 9
        for k in range(n):
            dur = 3.2
            begin = -(k * dur / n + li * .17)
            parts.append(
                f'<circle r="2.6" opacity=".95"><animateMotion dur="{dur}s" begin="{begin:.2f}s" repeatCount="indefinite" path="{d}"/>'
                f'<animate attributeName="fill" values="{cols}" keyTimes="{kt}" dur="{dur}s" begin="{begin:.2f}s" repeatCount="indefinite"/>'
                f'<animate attributeName="opacity" values="0;.95;.95;0" keyTimes="0;.04;.9;1" dur="{dur}s" begin="{begin:.2f}s" repeatCount="indefinite"/></circle>')

    gas = ("M100,170 L250,158 L700,158 C760,158 820,200 880,200 L1080,148 "
           "L1080,332 L880,280 C820,280 760,322 700,322 L250,322 L100,310 Z")
    shell = ("M100,170 L250,142 L700,142 C760,142 820,184 880,184 L1080,132 L1080,148 "
             "L880,200 C820,200 760,158 700,158 L250,158 Z")
    hubp = "M40,240 L240,212 L620,212 L720,240 L620,268 L240,268 Z"

    # precooler tube bank
    pre = []
    for x in (272, 286, 300, 314, 328):
        for y in range(164, 208, 9):
            pre.append(f'<circle cx="{x}" cy="{y}" r="2.6"/><circle cx="{x}" cy="{mir(y)}" r="2.6"/>')
    # HX tubes in combustor
    hx = []
    for x in (600, 614, 628, 642):
        for y in range(166, 208, 10):
            hx.append(f'<circle cx="{x}" cy="{y}" r="2.6"/><circle cx="{x}" cy="{mir(y)}" r="2.6"/>')
    # fan blades (scrolling)
    blades = "".join(f'<path d="M378,{y} l20,8 l0,4 l-20,-8 Z"/>' for y in range(120, 340, 11))
    tip = "".join(f'<path d="M424,{y} l14,5 l0,3 l-14,-5 Z"/>' for y in range(100, 380, 7))
    # combustor flames
    flames = []
    for i, (y, s) in enumerate([(176, 1), (196, .8), (mir(176), 1), (mir(196), .8)]):
        flames.append(f'<path class="cf" style="animation-delay:{-i*.05:.2f}s" d="M530,{y} q30,-7 70,0 q-40,7 -70,0 Z" transform="translate(0 0)" fill="url(#combG)"/>')
    diamonds = []
    for i, (x, w, h) in enumerate([(1112, 40, 120), (1162, 36, 96)]):
        diamonds.append(f'<path class="sd" style="animation-delay:{-i*.25}s" d="M{x-w/2},{C} L{x},{C-h/2} L{x+w/2},{C} L{x},{C+h/2} Z" fill="none" stroke="#FFF2D0" stroke-width="1.5"/>')

    css = """
.fan{animation:fan .12s linear infinite}
@keyframes fan{to{transform:translateY(11px)}}
.tip{animation:tip .12s linear infinite}
@keyframes tip{to{transform:translateY(7px)}}
.cf{transform-box:fill-box;transform-origin:0 50%;animation:cf .09s ease-in-out infinite alternate}
@keyframes cf{from{transform:scale(.85,.7)}to{transform:scale(1.1,1.25)}}
.sd{animation:sd .35s ease-in-out infinite alternate}
@keyframes sd{from{opacity:.25}to{opacity:.9}}
.frost{animation:pulse 1.8s ease-in-out infinite}
.lh2{stroke-dasharray:6 10;animation:flow .8s linear infinite}
"""
    defs = f"""
<radialGradient id="combG" cx="0" cy="50%" r="100%"><stop offset="0" stop-color="#fff"/><stop offset=".3" stop-color="{HOT}"/><stop offset="1" stop-color="{ORANGE}" stop-opacity="0"/></radialGradient>
<linearGradient id="plume" x1="0" x2="1"><stop offset="0" stop-color="{HOT}" stop-opacity=".55"/><stop offset="1" stop-color="{ORANGE}" stop-opacity="0"/></linearGradient>
<linearGradient id="h2warm" x1="0" x2="1"><stop offset="0" stop-color="{CYAN}"/><stop offset="1" stop-color="{ORANGE}"/></linearGradient>
<clipPath id="fanUp"><path d="M378,158 H400 V212 H378 Z M378,268 H400 V322 H378 Z"/></clipPath>
<clipPath id="tipC"><path d="M424,143 H440 V157 H424 Z M424,323 H440 V337 H424 Z"/></clipPath>
<clipPath id="gasC"><path d="{gas}"/></clipPath>
"""
    labels = [(150, 150, "①", "INTAKE", "ram air"), (300, 285, "②", "PRECOOLER", "LH₂ cools air"),
              (400, 440, "③", "FAN + TIP TURBINE", "driven by hot H₂"), (600, 640, "④", "COMBUSTOR + HX", "H₂ / air burn"),
              (900, 900, "⑤", "CD NOZZLE", "expansion")]
    lab = []
    for tx, x, n, t, s in labels:
        lab.append(f'<path d="M{tx},375 V382 H{x} V388" fill="none" stroke="{MUTED}" stroke-opacity=".6"/>'
                   f'<text x="{x}" y="404" text-anchor="middle" class="mono" font-size="11.5" letter-spacing="1.2" fill="{TXT}">{n} {t}</text>'
                   f'<text x="{x}" y="421" text-anchor="middle" class="sans" font-size="11.5" fill="{MUTED}">{s}</text>')

    body = f"""
{stars(W, H, 25)}
{header("PROPULSION", "ATREX precooled air-turbo ramjet", 32)}
<text x="{W-32}" y="36" class="serif" font-style="italic" font-size="19" text-anchor="end" fill="{TXT}">Four engines → <tspan fill="{GOLD}">30 km, Mach 5–6</tspan></text>
<!-- LH2 system -->
<rect x="246" y="70" width="108" height="30" rx="15" fill="{CYAN}" fill-opacity=".1" stroke="{CYAN}" stroke-opacity=".7"/>
<text x="300" y="89.5" text-anchor="middle" class="mono" font-size="11" fill="{CYAN}">LH₂ TANK</text>
<path class="lh2" d="M300,100 V142" stroke="{CYAN}" stroke-width="2.5" fill="none"/>
<path class="lh2" d="M322,142 V116 H600 V142" stroke="url(#h2warm)" stroke-width="2.5" fill="none"/>
<path class="lh2" d="M446,142 V128 H530 V142" stroke="{ORANGE}" stroke-width="2.5" fill="none"/>
<path class="lh2" d="M628,338 V364 H432 V338" stroke="{ORANGE}" stroke-width="2.5" fill="none"/>
<text x="470" y="110" class="mono" font-size="10" fill="{MUTED}">H₂ heated in HX →</text>
<text x="530" y="360" class="mono" font-size="10" fill="{MUTED}" text-anchor="middle">← drives tip turbine</text>
<!-- engine -->
<path d="{gas}" fill="#0A1226"/>
<g clip-path="url(#gasC)">
  <rect x="520" y="150" width="200" height="180" fill="{ORANGE}" opacity=".12" filter="url(#glow)"/>
  {''.join(flames)}
</g>
<path d="M1080,148 Q1140,150 1200,140 L1200,340 Q1140,330 1080,332 Z" fill="url(#plume)"/>
{''.join(diamonds)}
<g>{''.join(parts)}</g>
<path d="{shell}" fill="#1A2643" stroke="#3A4C74"/>
<path d="{shell}" fill="#1A2643" stroke="#3A4C74" transform="matrix(1 0 0 -1 0 {2*C})"/>
<path d="{hubp}" fill="#1E2B4D" stroke="#3A4C74"/>
<g fill="none" stroke="{CYAN}" stroke-width="1.4" class="frost">{''.join(pre)}</g>
<g fill="none" stroke="{ORANGE}" stroke-width="1.4">{''.join(hx)}</g>
<g clip-path="url(#fanUp)"><g class="fan" fill="#C8D2E4">{blades}</g></g>
<g clip-path="url(#tipC)"><g class="tip" fill="{ORANGE}">{tip}</g></g>
<g fill="{HOT}">{''.join(f'<circle cx="530" cy="{y}" r="2"/><circle cx="530" cy="{mir(y)}" r="2"/>' for y in (172, 186, 200))}</g>
<g>{''.join(lab)}</g>
<g class="mono" font-size="10" fill="{MUTED}">
  <circle cx="{W-300}" cy="56" r="4" fill="#E8C29A"/><text x="{W-290}" y="60">hot ram air</text>
  <circle cx="{W-200}" cy="56" r="4" fill="{CYAN}"/><text x="{W-190}" y="60">precooled</text>
  <circle cx="{W-108}" cy="56" r="4" fill="{ORANGE}"/><text x="{W-98}" y="60">burnt gas</text>
</g>"""
    write("atrex.svg", frame(W, H, body, css, "Animated ATREX precooled air-turbo ramjet cross-section", defs))


# =====================================================================
# H2/O2 THRUST CHAMBER
# =====================================================================
def thrust():
    W, H = 600, 380
    C = 215
    # chamber geometry (upper wall)
    wall = "M70,165 L230,165 C262,165 272,196 290,196 C330,196 400,170 470,148"
    wallL = "M70,265 L230,265 C262,265 272,234 290,234 C330,234 400,260 470,282"
    gas = wall + " L470,282 C400,260 330,234 290,234 C272,234 262,265 230,265 L70,265 Z"
    diamonds = "".join(
        f'<path class="sd" style="animation-delay:{-i*.12:.2f}s" d="M{x-w/2},{C} L{x},{C-h/2} L{x+w/2},{C} L{x},{C+h/2} Z" fill="#FFFFFF" fill-opacity=".14" stroke="#FFF2D0" stroke-width="1.2"/>'
        for i, (x, w, h) in enumerate([(498, 46, 104), (548, 40, 84), (592, 34, 66)]))
    spray = []
    for i in range(14):
        y = 175 + i * 6.5
        d = random.uniform(.5, .9)
        spray.append(f'<circle cx="74" cy="{y:.0f}" r="1.6" fill="{CYAN if i%2 else "#E6F4FF"}" style="animation:spray {d:.2f}s linear {-random.uniform(0,1):.2f}s infinite"/>')
    css = """
@keyframes twinkle{0%,100%{opacity:.25}50%{opacity:1}}
@keyframes spray{0%{transform:translateX(0);opacity:1}100%{transform:translateX(70px);opacity:0}}
.sd{animation:sd .3s ease-in-out infinite alternate}
@keyframes sd{from{opacity:.3}to{opacity:1}}
.core{animation:core .12s ease-in-out infinite alternate}
@keyframes core{from{opacity:.82}to{opacity:1}}
.lh2{stroke-dasharray:6 10;animation:flow .8s linear infinite}
.regen{stroke-dasharray:4 8;animation:flow 1.1s linear infinite reverse}
"""
    defs = f"""
<linearGradient id="chG" x1="0" x2="1"><stop offset="0" stop-color="{HOT}" stop-opacity=".7"/><stop offset=".25" stop-color="#FFFFFF"/><stop offset=".52" stop-color="{HOT}"/><stop offset=".75" stop-color="{ORANGE}" stop-opacity=".85"/><stop offset="1" stop-color="{RED}" stop-opacity=".6"/></linearGradient>
<linearGradient id="plumeT" x1="0" x2="1"><stop offset="0" stop-color="{HOT}" stop-opacity=".8"/><stop offset="1" stop-color="{ORANGE}" stop-opacity="0"/></linearGradient>
<clipPath id="gasT"><path d="{gas}"/></clipPath>
"""
    body = f"""
{stars(W, H, 25)}
{header("COMBUSTION", "Hydrogen–oxygen thrust chamber")}
<!-- feed lines -->
<path class="lh2" d="M40,90 H58 V180" stroke="{CYAN}" stroke-width="2.5" fill="none"/>
<path class="lh2" d="M40,340 H58 V250" stroke="#E6F4FF" stroke-width="2.5" fill="none"/>
<text x="24" y="84" class="mono" font-size="10" fill="{CYAN}">LH₂</text>
<text x="24" y="358" class="mono" font-size="10" fill="#E6F4FF">LOX</text>
<!-- chamber -->
<path d="{gas}" fill="#140A10"/>
<g clip-path="url(#gasT)">
  <path class="core" d="{gas}" fill="url(#chG)"/>
  {''.join(spray)}
</g>
<path d="M470,148 L600,118 L600,312 L470,282 Z" fill="url(#plumeT)"/>
{diamonds}
<path d="{wall}" fill="none" stroke="#C8D2E4" stroke-width="5" stroke-linecap="round"/>
<path d="{wallL}" fill="none" stroke="#C8D2E4" stroke-width="5" stroke-linecap="round"/>
<path class="regen" d="{wall}" fill="none" stroke="{CYAN}" stroke-width="1.5" transform="translate(0 -6)"/>
<path class="regen" d="{wallL}" fill="none" stroke="{CYAN}" stroke-width="1.5" transform="translate(0 6)"/>
<rect x="62" y="160" width="10" height="110" rx="2" fill="#6B7894"/>
<g class="mono" font-size="10" fill="{MUTED}">
  <text x="290" y="182" text-anchor="middle">throat</text>
  <text x="150" y="294" text-anchor="middle">chamber</text>
  <text x="400" y="292" text-anchor="middle">bell nozzle</text>
</g>
<g transform="translate(330 76)">
  <text class="sans" font-size="10" font-weight="500" fill="{MUTED}" letter-spacing="2">ADIABATIC FLAME TEMPERATURE</text>
  <text y="40" class="serif" font-size="44" fill="{HOT}">3,498 K</text>
</g>
<text x="300" y="352" text-anchor="middle" class="mono" font-size="10.5" fill="{MUTED}" letter-spacing="1.2">H₂O · OH · H · O · H₂ · O₂  — equilibrium species</text>
"""
    write("thrust-chamber.svg", frame(W, H, body, css, "Animated H2/O2 rocket thrust chamber with Mach diamonds", defs))


# =====================================================================
# MACH 4 DIAMOND AIRFOIL
# =====================================================================
def shocks():
    W, H = 600, 380
    C = 205
    LE, MID, TE, t = (150, C), (300, C - 22), (450, C), 22
    th = math.atan(t / 150)                     # half-angle
    beta = math.radians(23.5)                   # LE shock angle, M=4
    fan_angles = [math.radians(a) for a in (27, 21, 15, 9, 4)]
    te_ang = math.radians(12)

    def shock_y(x):  # upper LE shock line
        return C - math.tan(beta) * (x - LE[0])

    def fan_y(x, a):
        return MID[1] - math.tan(a) * (x - MID[0])

    def te_y(x):
        return C - math.tan(te_ang) * (x - TE[0])

    # state machine streamlines
    def streamline(y0):
        st, x, y, pts = 0, 0.0, y0, []
        mid_fan = math.radians(15)
        while x <= W + 10:
            if st == 0 and x >= LE[0] and y >= shock_y(x): st = 1
            if st == 1 and x >= MID[0] and y >= fan_y(x, mid_fan): st = 2
            if st == 2 and x >= TE[0] and y >= te_y(x): st = 3
            slope = {0: 0, 1: -math.tan(th), 2: math.tan(th), 3: 0}[st]
            pts.append((x, y))
            x += 3
            y += slope * 3
        return pts

    def path(pts, flip=False):
        return "M" + " L".join(f"{x:.1f},{(2*C-y if flip else y):.1f}" for x, y in pts)

    sl = []
    for i, gap in enumerate((8, 26, 52, 86, 124)):
        p = streamline(C - gap)
        dl = -i * .13
        for flip in (False, True):
            sl.append(f'<path d="{path(p, flip)}" class="sl" style="animation-delay:{dl:.2f}s" fill="none" stroke="#B8D6FF" stroke-opacity=".55" stroke-width="1.2"/>')

    def ray(p, a, L, flip=False):
        x2, y2 = p[0] + L * math.cos(a), p[1] - L * math.sin(a)
        if flip:
            return f"M{p[0]},{2*C-p[1]} L{x2:.1f},{2*C-y2:.1f}"
        return f"M{p[0]},{p[1]} L{x2:.1f},{y2:.1f}"

    shocks_ = []
    fans = []
    for flip in (False, True):
        shocks_.append(f'<path class="sh" d="{ray(LE, beta, 420, flip)}"/>')
        shocks_.append(f'<path class="sh" d="{ray(TE, te_ang, 260, flip)}" style="animation-delay:-.4s"/>')
        for k, a in enumerate(fan_angles):
            fans.append(f'<path d="{ray(MID, a, 340, flip)}" stroke-opacity="{.75 - k*.12:.2f}"/>')

    # tinted regions (upper) — compression between LE shock & first fan ray; expansion between last fan ray & TE shock
    def pt(p, a, L): return (p[0] + L * math.cos(a), p[1] - L * math.sin(a))
    s_end, f0_end = pt(LE, beta, 420), pt(MID, fan_angles[0], 340)
    f4_end, te_end = pt(MID, fan_angles[-1], 340), pt(TE, te_ang, 260)
    comp = [LE, MID, f0_end, s_end]
    expn = [MID, TE, te_end, f4_end]
    poly = lambda ps, flip=False: " ".join(f"{x:.1f},{(2*C-y if flip else y):.1f}" for x, y in ps)

    css = """
@keyframes twinkle{0%,100%{opacity:.25}50%{opacity:1}}
.sl{stroke-dasharray:10 14;animation:sl .6s linear infinite}
@keyframes sl{to{stroke-dashoffset:-24}}
.sh{fill:none;stroke:#FFFFFF;stroke-width:2.2;animation:sh 1.6s ease-in-out infinite}
@keyframes sh{0%,100%{stroke-opacity:.55}50%{stroke-opacity:1}}
"""
    defs = '<clipPath id="field"><rect x="0" y="70" width="600" height="270"/></clipPath>'
    body = f"""
{stars(W, H, 20)}
{header("SUPERSONIC CFD", "Diamond airfoil at Mach 4")}
<g clip-path="url(#field)">
  <polygon points="{poly(comp)}" fill="{ORANGE}" fill-opacity=".08"/>
  <polygon points="{poly(comp, True)}" fill="{ORANGE}" fill-opacity=".08"/>
  <polygon points="{poly(expn)}" fill="{CYAN}" fill-opacity=".14"/>
  <polygon points="{poly(expn, True)}" fill="{CYAN}" fill-opacity=".14"/>
  {''.join(sl)}
  <g fill="none" stroke="{CYAN}" stroke-width="1.2">{''.join(fans)}</g>
  {''.join(shocks_)}
</g>
<polygon points="{LE[0]},{C} {MID[0]},{C-t} {TE[0]},{C} {MID[0]},{C+t}" fill="#D5DDEB" stroke="#fff" stroke-width="1"/>
<g class="mono" font-size="10.5">
  <text x="26" y="{C-8}" fill="{TXT}" font-size="22" class="serif" font-style="italic">M∞ = 4</text>
  <path d="M28,{C+8} H110" stroke="{TXT}" stroke-width="1.5"/>
  <path d="M104,{C+4} L112,{C+8} L104,{C+12}" fill="none" stroke="{TXT}" stroke-width="1.5"/>
  <text x="330" y="88" fill="#fff">oblique shock</text>
  <text x="462" y="140" fill="{CYAN}">expansion fan</text>
  <text x="440" y="{2*C-118}" fill="#fff">TE shock</text>
</g>
<g class="mono" font-size="10" fill="{MUTED}" letter-spacing="1.2">
  <rect x="24" y="352" width="10" height="10" fill="{ORANGE}" fill-opacity=".5"/><text x="40" y="361">compression</text>
  <rect x="140" y="352" width="10" height="10" fill="{CYAN}" fill-opacity=".5"/><text x="156" y="361">expansion</text>
  <text x="576" y="361" text-anchor="end">+ Busemann biplane · nozzle flows NPR 8 / 12</text>
</g>
"""
    write("supersonic.svg", frame(W, H, body, css, "Animated Mach 4 diamond airfoil with oblique shocks and expansion fans", defs))


# =====================================================================
# TWO-PHASE LOOP THERMOSYPHON
# =====================================================================
def thermo():
    W, H = 600, 380
    riser = "M110,300 V110 H200"
    down = "M340,150 V320 H230"
    bubbles = []
    for i in range(16):
        d = random.uniform(2.2, 3.4)
        r = random.choice([2, 2.5, 3, 3.5, 4])
        bubbles.append(f'<circle r="{r}" fill="#EAF6FF" fill-opacity=".85"><animateMotion dur="{d:.2f}s" begin="{-random.uniform(0, d):.2f}s" repeatCount="indefinite" path="{riser}"/>'
                       f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;.1;.8;1" dur="{d:.2f}s" begin="{-random.uniform(0,d):.2f}s" repeatCount="indefinite"/></circle>')
    # slug (geyser) bubble — the instability
    bubbles.append(f'<rect x="-4" y="-14" width="8" height="28" rx="4" fill="#fff" fill-opacity=".9"><animateMotion dur="5s" repeatCount="indefinite" keyPoints="0;0;1;1" keyTimes="0;.55;.85;1" calcMode="linear" path="{riser}"/>'
                   f'<animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;.55;.58;.82;.85" dur="5s" repeatCount="indefinite"/></rect>')
    # T(t) trace: noisy oscillation with periodic spikes
    pts = []
    for i in range(0, 401, 4):
        y = 12 * math.sin(i / 400 * 4 * math.pi) + 4 * math.sin(i / 400 * 22 * math.pi)
        if i % 200 in range(120, 140):
            y -= 14 * math.sin((i % 200 - 120) / 20 * math.pi)
        pts.append(f"{i},{-y:.1f}")
    trace = "M" + " L".join(pts)
    heat = "".join(f'<path class="heat" style="animation-delay:{-k*.3:.1f}s" d="M{x},356 q-5,-8 0,-16 q5,-8 0,-16" fill="none" stroke="{ORANGE}" stroke-width="2"/>' for k, x in enumerate((92, 122, 152, 182, 212)))
    css = """
@keyframes twinkle{0%,100%{opacity:.25}50%{opacity:1}}
.heat{animation:heat 1.2s ease-in infinite}
@keyframes heat{0%{opacity:0;transform:translateY(6px)}40%{opacity:1}100%{opacity:0;transform:translateY(-10px)}}
.liq{stroke-dasharray:5 9;animation:flow 1.4s linear infinite}
.cool{stroke-dasharray:5 9;animation:flow .9s linear infinite}
.trace{animation:trace 4s linear infinite}
@keyframes trace{to{transform:translateX(-200px)}}
.evap{animation:evap 2s ease-in-out infinite}
@keyframes evap{0%,100%{fill-opacity:.25}50%{fill-opacity:.55}}
"""
    defs = '<clipPath id="scope"><rect x="384" y="250" width="192" height="80" rx="6"/></clipPath>'
    sensor = lambda x, y, t, d=0: (f'<circle cx="{x}" cy="{y}" r="9" fill="{BG0}" stroke="{GREEN}"/><text x="{x}" y="{y+3.5}" text-anchor="middle" class="mono" font-size="9.5" fill="{GREEN}">{t}</text>'
                                   f'<circle cx="{x+8}" cy="{y-8}" r="2.2" fill="{GREEN}" class="blink" style="animation-delay:{d}s"/>')
    body = f"""
{stars(W, H, 18)}
{header("RESEARCH · INSTITUT PPRIME", "Two-phase loop thermosyphon")}
<!-- condenser -->
<g>{''.join(f'<rect x="{x}" y="72" width="4" height="18" fill="#2E4B7A"/>' for x in range(208, 330, 10))}</g>
<rect x="200" y="90" width="140" height="48" rx="6" fill="{CYAN}" fill-opacity=".15" stroke="{CYAN}"/>
<text x="270" y="118" text-anchor="middle" class="mono" font-size="11" fill="{CYAN}">CONDENSER</text>
<path class="cool" d="M190,80 H350" stroke="{CYAN}" stroke-opacity=".6" stroke-width="1.5"/>
<!-- pipes -->
<path d="{riser}" fill="none" stroke="#2A3858" stroke-width="16" stroke-linejoin="round"/>
<path d="{riser}" fill="none" stroke="#123056" stroke-width="10" stroke-linejoin="round"/>
<path d="M340,138 V320 H230" fill="none" stroke="#2A3858" stroke-width="16" stroke-linejoin="round"/>
<path d="M340,138 V320 H230" fill="none" stroke="#1D5AA0" stroke-width="10" stroke-linejoin="round"/>
<path class="liq" d="M340,140 V320 H232" fill="none" stroke="#8CC8FF" stroke-width="2"/>
{''.join(bubbles)}
<!-- evaporator -->
<rect class="evap" x="80" y="296" width="150" height="40" rx="6" fill="{ORANGE}" stroke="{ORANGE}"/>
<text x="155" y="321" text-anchor="middle" class="mono" font-size="11" fill="{TXT}">EVAPORATOR</text>
{heat}
<text x="236" y="352" class="mono" font-size="10" fill="{ORANGE}">q″ in</text>
<text x="134" y="286" class="mono" font-size="10" fill="{MUTED}" transform="rotate(-90 134 286)">riser · vapour ↑</text>
<text x="364" y="300" class="mono" font-size="10" fill="{MUTED}" transform="rotate(-90 364 300)">downcomer · liquid ↓</text>
{sensor(136, 160, "P", -.3)}{sensor(318, 172, "ṁ", -.7)}{sensor(270, 290, "T", 0)}{sensor(170, 110, "T", -.5)}
<!-- camera -->
<g transform="translate(26 150)"><rect width="30" height="20" rx="3" fill="#2A3858" stroke="{MUTED}"/><path d="M30,6 L40,2 V18 L30,14 Z" fill="#2A3858" stroke="{MUTED}"/><circle cx="15" cy="10" r="5" fill="{BG0}" stroke="{CYAN}"/><circle cx="25" cy="4" r="1.6" fill="{RED}" class="blink"/></g>
<text x="26" y="186" class="mono" font-size="9" fill="{MUTED}">high-speed</text>
<!-- analysis panel -->
<text x="390" y="104" class="sans" font-size="10" font-weight="500" fill="{MUTED}" letter-spacing="2">MATLAB ANALYSIS</text>
<g class="serif" font-size="20" font-style="italic" fill="{TXT}">
  <text x="390" y="136">R<tspan font-size="13" dy="4">th</tspan><tspan dy="-4"> = ΔT / Q</tspan></text>
  <text x="390" y="166">h = q″ / ΔT</text>
  <text x="390" y="196">Nu = f (Re, Pr)</text>
</g>
<text x="390" y="234" class="sans" font-size="10" font-weight="500" fill="{MUTED}" letter-spacing="2">FLOW INSTABILITY</text>
<rect x="384" y="250" width="192" height="80" rx="6" fill="{BG0}" stroke="{LINE}"/>
<g clip-path="url(#scope)">
  <g stroke="{LINE}" stroke-width=".7">{''.join(f'<line x1="{x}" y1="250" x2="{x}" y2="330"/>' for x in range(400, 576, 24))}</g>
  <g transform="translate(384 290)"><path class="trace" d="{trace}" fill="none" stroke="{ORANGE}" stroke-width="1.8"/></g>
</g>
"""
    write("thermosyphon.svg", frame(W, H, body, css, "Animated two-phase loop thermosyphon experiment", defs))


# =====================================================================
# VTOL 4+1
# =====================================================================
def vtol():
    W, H = 1200, 440
    rot = []
    for i, (x, y) in enumerate([(230, 112), (450, 112), (230, 330), (450, 330)]):
        cw = "" if i in (0, 3) else "animation-direction:reverse;"
        rot.append(f"""
<g class="lift">
  <circle cx="{x}" cy="{y}" r="52" fill="{CYAN}" fill-opacity=".07" stroke="{CYAN}" stroke-opacity=".35" stroke-dasharray="3 5"/>
  <g class="spin" style="{cw}animation-duration:.18s"><path d="M{x-50},{y-3} Q{x},{y-7} {x+50},{y+3} Q{x},{y+7} {x-50},{y-3} Z" fill="#D9E3F2" fill-opacity=".55"/><circle cx="{x}" cy="{y}" r="52" fill="none"/></g>
</g>
<g class="still">
  <path d="M{x-50},{y-3} Q{x},{y-7} {x+50},{y+3} Q{x},{y+7} {x-50},{y-3} Z" fill="#D9E3F2" transform="rotate(35 {x} {y})"/>
</g>
<circle cx="{x}" cy="{y}" r="8" fill="#3B4A6B" stroke="#C8D2E4"/>""")
    wp = [(760, 330), (820, 130), (960, 100), (1100, 190), (1060, 330), (900, 360)]
    mission = "M" + " L".join(f"{x},{y}" for x, y in wp) + " Z"
    css = """
@keyframes twinkle{0%,100%{opacity:.25}50%{opacity:1}}
.lift{animation:hover 10s ease-in-out infinite}
.still{animation:cruise 10s ease-in-out infinite}
@keyframes hover{0%,45%{opacity:1}55%,92%{opacity:0}100%{opacity:1}}
@keyframes cruise{0%,45%{opacity:0}55%,92%{opacity:1}100%{opacity:0}}
.push{transform-box:fill-box;transform-origin:center;animation:pushp .06s linear infinite alternate}
@keyframes pushp{from{transform:scaleX(1)}to{transform:scaleX(.2)}}
.shadow{transform-box:fill-box;transform-origin:center;animation:sh 3s ease-in-out infinite}
@keyframes sh{0%,100%{transform:scale(1);opacity:.35}50%{transform:scale(.96);opacity:.25}}
.wpt{animation:pulse 1.8s ease-in-out infinite}
.route{stroke-dasharray:6 8;animation:flow 1.2s linear infinite}
"""
    grid = "".join(f'<line x1="{x}" y1="40" x2="{x}" y2="410" />' for x in range(720, 1170, 40)) + \
           "".join(f'<line x1="700" y1="{y}" x2="1170" y2="{y}" />' for y in range(60, 410, 40))
    body = f"""
{stars(W, H, 25)}
{header("JURY’S FAVOURITE · DASSAULT UAV CHALLENGE 2026", "ENSMAERO VTOL 4+1", 32)}
<!-- mode readout -->
<g class="mono" font-size="10.5" letter-spacing="1.2">
  <g class="lift"><circle cx="38" cy="372" r="3.5" fill="{CYAN}" class="pulse"/><text x="50" y="376" class="serif" font-style="italic" font-size="17" letter-spacing="0" fill="{CYAN}">Hover</text></g>
  <g class="still"><circle cx="38" cy="372" r="3.5" fill="{GOLD}" class="pulse"/><text x="50" y="376" class="serif" font-style="italic" font-size="17" letter-spacing="0" fill="{GOLD}">Cruise</text></g>
</g>
<!-- aircraft (top view) -->
<g transform="translate(0 4)">
<ellipse class="shadow" cx="355" cy="236" rx="270" ry="70" fill="#000" filter="url(#glow)"/>
<path d="M80,206 Q80,198 90,198 L310,194 L370,194 L590,198 Q600,198 600,206 L600,222 Q600,230 590,230 L370,240 L310,240 L90,230 Q80,230 80,222 Z" fill="#E4EAF4" stroke="#fff"/>
<path d="M90,226 L310,236 L370,236 L590,226" fill="none" stroke="#9AA8C2"/>
<rect x="226" y="112" width="8" height="250" rx="4" fill="#C3CEE0"/>
<rect x="446" y="112" width="8" height="250" rx="4" fill="#C3CEE0"/>
<path d="M216,356 H464 V370 H216 Z" fill="#D5DDEB" stroke="#fff"/>
<path d="M326,120 Q340,84 354,120 L358,340 Q340,352 322,340 Z" fill="#F4F7FC" stroke="#fff"/>
<path d="M332,128 Q340,108 348,128 L348,150 L332,150 Z" fill="{BG1}" opacity=".85"/>
<rect x="335" y="170" width="10" height="40" rx="2" fill="{CYAN}" fill-opacity=".35"/>
<g class="still"><rect class="push" x="318" y="348" width="44" height="4" rx="2" fill="{ORANGE}"/></g>
<circle cx="84" cy="214" r="3" fill="{RED}" class="blink"/><circle cx="596" cy="214" r="3" fill="{GREEN}" class="blink" style="animation-delay:-.6s"/>
{''.join(rot)}
</g>
<g class="mono" font-size="10.5" fill="{MUTED}">
  <path d="M84,414 V404 M84,409 H596 M596,404 V414" stroke="{MUTED}" fill="none" transform="translate(0 0)"/>
  <rect x="300" y="401" width="80" height="16" fill="{BG1}"/><text x="340" y="413" text-anchor="middle" fill="{TXT}">2.0 m span</text>
</g>
<g class="mono" font-size="10.5" fill="{MUTED}" letter-spacing="1.2">
  <text x="32" y="250" font-size="9" fill="{GOLD}" letter-spacing="2">FLIGHT CONTROLLER</text><text x="32" y="266" class="sans" font-size="12" letter-spacing="0" fill="{TXT}">SpeedyBee F405</text>
  <text x="32" y="290" font-size="9" fill="{GOLD}" letter-spacing="2">SOFTWARE</text><text x="32" y="306" class="sans" font-size="12" letter-spacing="0" fill="{TXT}">Python, C++</text>
  <text x="32" y="330" font-size="9" fill="{GOLD}" letter-spacing="2">MY ROLE</text><text x="32" y="346" class="sans" font-size="12" letter-spacing="0" fill="{TXT}">Propulsion &amp; CFD</text>
</g>
<!-- mission planner panel -->
<rect x="700" y="40" width="470" height="370" rx="12" fill="{BG0}" fill-opacity=".7" stroke="{LINE}"/>
<g stroke="{LINE}" stroke-width=".6" opacity=".7">{grid}</g>
<text x="718" y="68" class="serif" font-size="19" fill="{TXT}">Mission planning <tspan font-style="italic" fill="{MUTED}">— plain-language control over MAVLink</tspan></text>
<path class="route" d="{mission}" fill="none" stroke="{CYAN}" stroke-width="1.6"/>
{''.join(f'<g><circle class="wpt" style="animation-delay:{-i*.3:.1f}s" cx="{x}" cy="{y}" r="7" fill="none" stroke="{CYAN}"/><text x="{x+12}" y="{y-8}" class="mono" font-size="10" fill="{TXT}">{"H" if i==0 else "WP"+str(i)}</text></g>' for i, (x, y) in enumerate(wp))}
<path d="M-8,-6 L10,0 L-8,6 L-4,0 Z" fill="{ORANGE}"><animateMotion dur="12s" repeatCount="indefinite" rotate="auto" path="{mission}"/></path>
<g class="mono" font-size="10" fill="{MUTED}" letter-spacing="1.2">
  <text x="718" y="396">TAKE-OFF  ·  WAYPOINTS  ·  LANDING  ·  RETURN TO LAUNCH</text>
</g>
"""
    write("vtol.svg", frame(W, H, body, css, "Animated VTOL 4+1 UAV with mission planner", ""))


# =====================================================================
# STATS STRIP
# =====================================================================
def stats():
    W, H = 1200, 140
    cells = [("100+", "FLIGHT HOURS", "as drone pilot", GOLD),
             ("2026", "JURY’S FAVOURITE", "Dassault UAV · 28 teams", GOLD),
             ("20", "TEAM FOUNDED", "Team Phoenix · SAE", GOLD),
             ("3,498 K", "H₂/O₂ FLAME", "adiabatic, Cantera", GOLD),
             ("Mach 3", "ATREX CYCLE", "at 12 km altitude", GOLD),
             ("A1/A3", "EU DRONE PILOT", "DGAC certified", GOLD)]
    cw = W / len(cells)
    out = []
    for i, (n, a, b, c) in enumerate(cells):
        x = i * cw + 28
        out.append(f"""<g>
  <text x="{x}" y="60" class="serif" font-size="40" fill="{TXT}">{n}</text>
  <text x="{x}" y="84" class="sans" font-size="10" font-weight="500" letter-spacing="2" fill="{c}">{a}</text>
  <text x="{x}" y="102" class="sans" font-size="11.5" fill="{MUTED}">{b}</text>
  <rect x="{x}" y="116" width="{cw-56:.0f}" height="1.5" rx=".75" fill="{LINE}"/>
  <rect x="{x}" y="116" width="{cw-56:.0f}" height="1.5" rx=".75" fill="{c}" class="bar" style="animation-delay:{i*.25:.2f}s"/>
</g>""")
        if i:
            out.append(f'<line x1="{i*cw:.0f}" y1="26" x2="{i*cw:.0f}" y2="114" stroke="{LINE}"/>')
    css = """
.bar{transform-box:fill-box;transform-origin:0 50%;animation:bar 4s cubic-bezier(.3,.7,.2,1) infinite}
@keyframes bar{0%{transform:scaleX(0)}40%,85%{transform:scaleX(1);opacity:1}100%{transform:scaleX(1);opacity:0}}
"""
    write("stats.svg", frame(W, H, "".join(out), css, "Key numbers: 100+ flight hours, Jury's Favourite among 28 teams, 20-member team founded, 3498 K, Mach 3, EU drone pilot"))


# =====================================================================
# DIVIDER (contrail)
# =====================================================================
def divider():
    W, H = 1200, 36
    css = f"""
.trail{{transform-box:fill-box;transform-origin:0 50%;animation:trail 7s linear infinite}}
@keyframes trail{{0%{{transform:scaleX(0);opacity:1}}85%{{transform:scaleX(1);opacity:1}}100%{{transform:scaleX(1);opacity:0}}}}
.ship{{animation:ship 7s linear infinite}}
@keyframes ship{{0%{{transform:translateX(0)}}85%{{transform:translateX(1200px)}}100%{{transform:translateX(1200px)}}}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
"""
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="divider">
<defs><linearGradient id="t" x1="0" x2="1"><stop offset="0" stop-color="{CYAN}" stop-opacity="0"/><stop offset=".85" stop-color="{CYAN}" stop-opacity=".5"/><stop offset="1" stop-color="{ORANGE}"/></linearGradient></defs>
<style>{css}</style>
<line x1="0" y1="18" x2="{W}" y2="18" stroke="{LINE}" stroke-dasharray="2 6"/>
<rect class="trail" x="0" y="17" width="{W}" height="2" fill="url(#t)"/>
<g class="ship"><g transform="translate(0 18)">
  <circle r="7" fill="{ORANGE}" opacity=".35"/>
  <path d="M-10,-4 L6,-4 L12,0 L6,4 L-10,4 Z" fill="#E9EEF8"/><path d="M-10,-4 L-14,-8 L-14,8 L-10,4 Z" fill="{RED}"/>
</g></g>
</svg>
"""
    write("divider.svg", svg)


# =====================================================================
# AUTONOMOUS FLIGHT — typeset project cards with logos
# =====================================================================
CARDS = [
    ("card-dassault.svg", ["dassault-aviation.svg", "isae-ensma.png"],
     "ENSMAERO, ISAE-ENSMA · October 2025 – present",
     "Dassault UAV Challenge 2026", "Jury’s Favourite Award",
     "Our modular autonomous VTOL 4+1 with a 2 m wingspan won the Prix Coup de cœur du jury among 28 teams. "
     "I was responsible for propulsion design and CFD optimisation. I also integrated the sensors with a SpeedyBee F405 "
     "flight controller and wrote control algorithms in Python and C++, refined through ground and flight testing."),
    ("card-phoenix.svg", ["team-phoenix.jpg", "sae-international.svg"],
     "Loyola-ICAM, Chennai · 2022 – 2025",
     "Team Phoenix", "Founder & captain",
     "I built a 20-member UAV team from scratch, and it won an award at the SAE Autonomous Drone Development Challenge 2024 "
     "(payload category). We took each drone from SolidWorks design through FEA and 3D printing to flight test, with Gazebo "
     "simulation along the way. I logged more than 100 hours as the team’s pilot."),
    ("card-reconnaissance.svg", ["team-reconnaissance.jpg"],
     "Hindustan Technology Business Incubator · 2024 – 2025",
     "Team Reconnaissance", "VTOL design & development",
     "Autonomous VTOL aircraft built on a Holybro flight controller with an NVIDIA Jetson Nano companion computer. "
     "I ran the flight-test campaigns, wrote Python pipelines for flight data, and tuned mission planning for fixed-wing "
     "and multirotor platforms."),
    ("card-mcp.svg", ["ardupilot.png"],
     "Personal project · ongoing",
     "Natural-language drone control", "Pixhawk · ArduPilot · MAVLink",
     "A Python server that turns language-model tool calls into MAVLink commands for a Pixhawk running ArduPilot: "
     "telemetry, arming, take-off, waypoints, landing and return to launch. I test it in ArduPilot’s simulator."),
    ("card-fc.svg", ["emblem:pid"],
     "Personal project",
     "A flight controller of my own", "Automatic PID tuning",
     "A custom quadcopter controller that tunes its own PID control loops, so a new build is ready to fly as soon as it’s set up."),
]


def _measure():
    from fontTools.ttLib import TTFont
    import urllib.request
    cache = os.path.join(os.path.expanduser("~"), ".cache", "readme-fonts")
    os.makedirs(cache, exist_ok=True)
    url = FONTS[2][3]
    local = os.path.join(cache, url.rsplit("/", 1)[-1])
    if not os.path.exists(local):
        urllib.request.urlretrieve(url, local)
    f = TTFont(local)
    cmap, hmtx, upm = f.getBestCmap(), f["hmtx"], f["head"].unitsPerEm
    return lambda text, size: sum(hmtx[cmap.get(ord(ch), cmap[ord("n")])][0] for ch in text) * size / upm


def _wrap(text, width, size, measure):
    """Balanced wrap: same line count as a greedy wrap, but even line lengths (no orphans)."""
    best = _greedy(text, width, size, measure)
    lo = width * .5
    while width - lo > 2:
        mid = (lo + width) / 2
        if len(_greedy(text, mid, size, measure)) == len(best):
            width = mid
        else:
            lo = mid
    return _greedy(text, width, size, measure)


def _greedy(text, width, size, measure):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if measure(t, size) > width and cur:
            lines.append(cur); cur = w
        else:
            cur = t
    return lines + [cur]


def _emblem(kind, w, h):
    """Gold line-art emblems drawn in the page's own style (local coords, w x h tile)."""
    g = f'stroke="{GOLD}" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"'
    cx, cy = w / 2, h / 2
    if kind == "vtol":  # top view of the VTOL 4+1, lift rotors spinning
        rotors = "".join(
            f'<circle cx="{cx+dx}" cy="{cy+dy}" r="15" stroke-opacity=".3" stroke-dasharray="2 3"/>'
            f'<g class="spin" style="animation-duration:.3s{";animation-direction:reverse" if dx*dy > 0 else ""}"><line x1="{cx+dx-14}" y1="{cy+dy}" x2="{cx+dx+14}" y2="{cy+dy}" stroke-width="2"/></g>'
            for dx, dy in ((-26, -30), (26, -30), (-26, 30), (26, 30)))
        return (f'<g {g}>{rotors}'
                f'<rect x="{cx-70}" y="{cy-5}" width="140" height="10" rx="5" fill="{BG0}"/>'
                f'<line x1="{cx-26}" y1="{cy-30}" x2="{cx-26}" y2="{cy+40}"/><line x1="{cx+26}" y1="{cy-30}" x2="{cx+26}" y2="{cy+40}"/>'
                f'<line x1="{cx-30}" y1="{cy+42}" x2="{cx+30}" y2="{cy+42}" stroke-width="2.5"/>'
                f'<path d="M{cx},{cy-44} C{cx+6},{cy-38} {cx+6},{cy-20} {cx+5},{cy+34} L{cx-5},{cy+34} C{cx-6},{cy-20} {cx-6},{cy-38} {cx},{cy-44} Z" fill="{BG0}"/>'
                f'<line x1="{cx-7}" y1="{cy+37}" x2="{cx+7}" y2="{cy+37}" stroke="{ORANGE}" stroke-width="2" class="pulse"/></g>')
    if kind == "mcp":  # a sentence becomes a flight path
        path = f"M{cx-18},{cy-2} C{cx+8},{cy-2} {cx-4},{cy+34} {cx+26},{cy+30} S{cx+48},{cy-6} {cx+52},{cy-22}"
        return (f'<g {g}>'
                f'<path d="M{cx-66},{cy-34} h48 a8,8 0 0 1 8,8 v20 a8,8 0 0 1 -8,8 h-30 l-10,10 v-10 h-8 a8,8 0 0 1 -8,-8 v-20 a8,8 0 0 1 8,-8 Z"/>'
                + "".join(f'<circle cx="{cx-54+i*12}" cy="{cy-16}" r="2" fill="{GOLD}" stroke="none" class="pulse" style="animation-delay:{-i*.4:.1f}s"/>' for i in range(3))
                + f'<path d="{path}" stroke-dasharray="3 5" class="flow" stroke-opacity=".8"/>'
                f'<circle cx="{cx+26}" cy="{cy+30}" r="3" stroke-opacity=".7"/>'
                f'<g transform="translate({cx+52} {cy-30})"><line x1="-9" y1="-7" x2="9" y2="7"/><line x1="-9" y1="7" x2="9" y2="-7"/>'
                + "".join(f'<circle cx="{px}" cy="{py}" r="4.5"/>' for px, py in ((-11, -9), (11, -9), (-11, 9), (11, 9)))
                + f'<rect x="-3.5" y="-3.5" width="7" height="7" rx="1.5" fill="{BG0}"/></g>'
                f'<circle r="2.6" fill="{ORANGE}" stroke="none"><animateMotion dur="3s" repeatCount="indefinite" path="{path}"/></circle></g>')
    if kind == "pid":  # step response settling onto its setpoint
        x0, x1, ybase, yset = 22, w - 20, h - 26, 44
        pts = []
        for i in range(61):
            t = i / 60 * 6.5
            yv = 1 - math.exp(-0.55 * t) * (math.cos(2.2 * t) + 0.25 * math.sin(2.2 * t))
            pts.append(f"{x0 + (x1 - x0) * i / 60:.1f},{ybase - (ybase - yset) * yv:.1f}")
        curve = "M" + " L".join(pts)
        return (f'<g {g}>'
                f'<line x1="{x0}" y1="{ybase}" x2="{x1}" y2="{ybase}" stroke-opacity=".3"/>'
                f'<line x1="{x0}" y1="{yset}" x2="{x1}" y2="{yset}" stroke-opacity=".45" stroke-dasharray="3 4"/>'
                f'<path d="{curve}" stroke-width="2" pathLength="100" stroke-dasharray="100" class="draw"/></g>'
                f'<text x="{x0}" y="{h-10}" class="serif" font-style="italic" font-size="14" fill="{GOLD}" fill-opacity=".8">K<tspan font-size="9" dy="2">p</tspan><tspan dy="-2">  K</tspan><tspan font-size="9" dy="2">i</tspan><tspan dy="-2">  K</tspan><tspan font-size="9" dy="2">d</tspan></text>'
                f'<text x="{x1}" y="{yset-6}" text-anchor="end" class="sans" font-size="8.5" font-weight="500" letter-spacing="1.5" fill="{MUTED}">SETPOINT</text>')
    raise ValueError(kind)


def _logo_tile(x, y, w, h, fname):
    import base64
    if fname.startswith("emblem:"):
        return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{BG0}"/>'
                f'<g transform="translate({x} {y})">{_emblem(fname[7:], w, h)}</g>'
                f'<rect x="{x+.5}" y="{y+.5}" width="{w-1}" height="{h-1}" rx="14" fill="none" stroke="{GOLD}" stroke-opacity=".35"/>')
    path = os.path.join(OUT, "logos", fname)
    data = base64.b64encode(open(path, "rb").read()).decode()
    mime = {"svg": "image/svg+xml", "png": "image/png"}.get(fname.rsplit(".", 1)[-1], "image/jpeg")
    own = fname in ("team-phoenix.jpg", "team-reconnaissance.jpg")  # my teams' marks keep their colours
    pad = {"team-phoenix.jpg": 0, "team-reconnaissance.jpg": 8}.get(fname, 24)
    clip = f"clip{abs(hash((fname, x, y)))}"
    fit = "xMidYMid slice" if pad == 0 else "xMidYMid meet"
    tone = "" if own else ' filter="url(#mono)" opacity=".92"'
    return (f'<clipPath id="{clip}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14"/></clipPath>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{"#000" if own else BG0}"/>'
            f'<image clip-path="url(#{clip})" x="{x+pad}" y="{y+pad}" width="{w-2*pad}" height="{h-2*pad}" preserveAspectRatio="{fit}"{tone} href="data:{mime};base64,{data}"/>'
            f'<rect x="{x+.5}" y="{y+.5}" width="{w-1}" height="{h-1}" rx="14" fill="none" stroke="{GOLD}" stroke-opacity=".35"/>')


def cards():
    measure = _measure()
    W, PAD, TW, TH, GAP = 1200, 36, 176, 128, 12
    tx = PAD + TW + 40
    tw = 780  # ~95 characters: a comfortable measure, leaves air on the right
    css = """
.rise{opacity:0;animation:rise .9s cubic-bezier(.2,.7,.2,1) forwards}
@keyframes rise{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
.rule{transform-box:fill-box;transform-origin:0 50%;animation:rule 1.4s cubic-bezier(.3,.7,.2,1) .2s both}
@keyframes rule{from{transform:scaleX(0)}to{transform:scaleX(1)}}
.draw{animation:draw 4.5s cubic-bezier(.4,.1,.2,1) infinite}
@keyframes draw{0%{stroke-dashoffset:100}55%,85%{stroke-dashoffset:0;opacity:1}100%{stroke-dashoffset:0;opacity:0}}
"""
    from xml.sax.saxutils import escape as esc
    for name, logos, label, title, sub, body in CARDS:
        lines = [esc(l) for l in _wrap(body, tw, 15, measure)]
        label, title, sub = esc(label), esc(title), esc(sub)
        text_h = 96 + len(lines) * 24
        tiles_h = len(logos) * TH + (len(logos) - 1) * GAP
        H = max(text_h, tiles_h) + 2 * PAD - 8
        ty = (H - tiles_h) / 2
        tiles = "".join(_logo_tile(PAD, ty + i * (TH + GAP), TW, TH, f) for i, f in enumerate(logos))
        tspans = "".join(f'<tspan x="{tx}" dy="{0 if i == 0 else 24}">{l}</tspan>' for i, l in enumerate(lines))
        y0 = (H - text_h) / 2
        content = f"""
{tiles}
<g class="rise" style="animation-delay:.1s">
  <text x="{tx}" y="{y0+14}" class="sans" font-size="13" font-weight="500" fill="{GOLD}">{label}</text>
  <text x="{tx}" y="{y0+52}" class="serif" font-size="36" letter-spacing="-.4" fill="{TXT}">{title} <tspan font-style="italic" fill="{GOLD}">— {sub}</tspan></text>
</g>
<rect class="rule" x="{tx}" y="{y0+68}" width="64" height="1.5" fill="{GOLD}"/>
<g class="rise" style="animation-delay:.3s"><text x="{tx}" y="{y0+98}" class="sans" font-size="15" fill="{TXT}" fill-opacity=".86">{tspans}</text></g>
"""
        write(name, frame(W, int(H), content, css, f"{title} — {sub}"))


# =====================================================================
# Embed subsetted fonts (GitHub serves SVGs as images, so web fonts must be inline)
# =====================================================================
FONTS = [  # (family, style, weight, url)
    ("Instrument Serif", "normal", 400, "https://fonts.gstatic.com/s/instrumentserif/v5/jizBRFtNs2ka5fXjeivQ4LroWlx-2zI.ttf"),
    ("Instrument Serif", "italic", 400, "https://fonts.gstatic.com/s/instrumentserif/v5/jizHRFtNs2ka5fXjeivQ4LroWlx-6zATiw.ttf"),
    ("Geist", "normal", 400, "https://fonts.gstatic.com/s/geist/v5/gyBhhwUxId8gMGYQMKR3pzfaWI_RnOM4nQ.ttf"),
    ("Geist", "normal", 500, "https://fonts.gstatic.com/s/geist/v5/gyBhhwUxId8gMGYQMKR3pzfaWI_RruM4nQ.ttf"),
]


def embed_fonts():
    import base64, html, io, re, urllib.request
    from fontTools import subset
    from fontTools.ttLib import TTFont
    cache = os.path.join(os.path.expanduser("~"), ".cache", "readme-fonts")
    os.makedirs(cache, exist_ok=True)
    for name in os.listdir(OUT):
        if not name.endswith(".svg"):
            continue
        p = os.path.join(OUT, name)
        svg = open(p).read()
        chars = set(html.unescape("".join(re.findall(r">([^<>]+)<", svg.split("</style>", 1)[-1])))) | set("0123456789")
        faces = []
        for fam, style, weight, url in FONTS:
            local = os.path.join(cache, url.rsplit("/", 1)[-1])
            if not os.path.exists(local):
                urllib.request.urlretrieve(url, local)
            font = TTFont(local)
            opts = subset.Options(); opts.flavor = "woff2"; opts.layout_features = ["kern", "liga"]; opts.hinting = False
            sub = subset.Subsetter(opts); sub.populate(text="".join(chars)); sub.subset(font)
            buf = io.BytesIO(); font.flavor = "woff2"; font.save(buf)
            b64 = base64.b64encode(buf.getvalue()).decode()
            faces.append(f"@font-face{{font-family:'{fam}';font-style:{style};font-weight:{weight};src:url(data:font/woff2;base64,{b64}) format('woff2')}}")
        svg = svg.replace("<style>", "<style>" + "".join(faces), 1)
        open(p, "w").write(svg)


for fn in (hero, atrex, thrust, shocks, thermo, vtol, stats, divider, cards):
    fn()
embed_fonts()
print("ok")
