import re

with open('/Users/Nati/.gemini/antigravity/scratch/Castle_Website_Final/index_v2.html', 'r', encoding='utf-8') as f:
    html = f.read()

# CSS Modifications
html = re.sub(r'border-radius:\s*\d+px;', 'border-radius: 8px;', html)
html = html.replace('padding: 100px 0;', 'padding: 60px 0;')
html = html.replace('padding: 120px 0;', 'padding: 60px 0;')
html = html.replace('padding: 140px 0;', 'padding: 80px 0;')
html = html.replace('padding: 140px 0 80px 0;', 'padding: 80px 0 60px 0;')
html = html.replace('padding: 80px 0;', 'padding: 60px 0;')

html = html.replace('background-color: #F8F8FA;', 'background-color: #FFFFFF;')
html = html.replace('background-color: #F9FAFB;', 'background-color: #FFFFFF;')
html = html.replace('background-color: #F9EFE5;', 'background-color: #FFFFFF;')
html = html.replace('background-color: #F3F4F6;', 'background-color: #FFFFFF;')
# Keep #F9FAFB for blog cards or just #FFFFFF? Let's use #FFFFFF with a solid border.
html = html.replace('background: #F9FAFB;', 'background: #FFFFFF;')
html = html.replace('border: 1px solid #E5E7EB;', 'border: 1px solid #111111;')

# Replace "Join the Waitlist" button in Hero to "Get early access"
html = html.replace('>Join the Waitlist</a>', '>Get early access</a>')

# Replace Hero Headline
hero_old = """<h1 class="hero-title">Build Your<br><span class="highlight">Castle</span></h1>"""
hero_new = """<h1 class="hero-title" style="font-size: clamp(48px, 6vw, 84px); letter-spacing: -2px;">Castle is the <span class="highlight">OS (Operating System)</span><br>of Women's Wealth.</h1>"""
html = html.replace(hero_old, hero_new)

# Generate Body parts
# We will construct the new sections and replace the old body contents between <!-- Statement --> and <!-- 11. Blog & Subscribe -->.

new_sections = """
    <!-- V2 Block (Replaces How it works) -->
    <section class="v2-block" style="background-color: #111111; color: #FFFFFF; padding: 80px 0;">
        <div class="container">
            <h2 class="section-title" style="color: #FFFFFF;">The Foundation</h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 24px; margin-top: 40px;">
                <div style="border: 1px solid rgba(255,255,255,0.2); border-radius: 8px; padding: 40px;">
                    <h3 style="font-size: 20px; font-weight: 700; margin-bottom: 15px;">Block 1</h3>
                    <p style="color: rgba(255,255,255,0.7); font-size: 15px;">Content placeholder for block 1. Will be updated tomorrow.</p>
                </div>
                <div style="border: 1px solid rgba(255,255,255,0.2); border-radius: 8px; padding: 40px;">
                    <h3 style="font-size: 20px; font-weight: 700; margin-bottom: 15px;">Block 2</h3>
                    <p style="color: rgba(255,255,255,0.7); font-size: 15px;">Content placeholder for block 2. Will be updated tomorrow.</p>
                </div>
                <div style="border: 1px solid rgba(255,255,255,0.2); border-radius: 8px; padding: 40px;">
                    <h3 style="font-size: 20px; font-weight: 700; margin-bottom: 15px;">Block 3</h3>
                    <p style="color: rgba(255,255,255,0.7); font-size: 15px;">Content placeholder for block 3. Will be updated tomorrow.</p>
                </div>
                <div style="border: 1px solid rgba(255,255,255,0.2); border-radius: 8px; padding: 40px;">
                    <h3 style="font-size: 20px; font-weight: 700; margin-bottom: 15px;">Block 4</h3>
                    <p style="color: rgba(255,255,255,0.7); font-size: 15px;">Content placeholder for block 4. Will be updated tomorrow.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Manifesto Minimalist -->
    <section id="reality" class="reality-section" style="padding: 100px 0; background-color: #FFFFFF;">
        <div class="container" style="max-width: 800px; text-align: center;">
            <p class="section-eyebrow">OUR VISION</p>
            <h2 class="section-title">The Manifesto</h2>
            <p style="font-size: clamp(20px, 3vw, 24px); color: #111111; font-weight: 500; font-family: 'Inter', sans-serif; line-height: 1.5; margin-top: 24px;">
                We are building the definitive framework for absolute financial independence. No compromises.
            </p>
        </div>
    </section>

    <!-- What Makes Us Different -->
    <section class="different-section" style="background-color: #1A1A1A; color: #FFFFFF; padding: 80px 0;">
        <div class="container">
            <h2 class="section-title" style="color: #FFFFFF;">What Makes Us Different</h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 24px; margin-top: 60px;">
                <div style="border-top: 2px solid #A03FA3; padding-top: 24px;">
                    <h4 style="font-size: 18px; font-weight: 700; margin-bottom: 10px;">Built for Scale</h4>
                    <p style="font-size: 14px; color: rgba(255,255,255,0.7);">We don't do basic financial literacy. We build institutional-grade frameworks.</p>
                </div>
                <div style="border-top: 2px solid #A03FA3; padding-top: 24px;">
                    <h4 style="font-size: 18px; font-weight: 700; margin-bottom: 10px;">Ownership Economy</h4>
                    <p style="font-size: 14px; color: rgba(255,255,255,0.7);">Our users own the network. Web3 integration means true alignment of incentives.</p>
                </div>
                <div style="border-top: 2px solid #A03FA3; padding-top: 24px;">
                    <h4 style="font-size: 18px; font-weight: 700; margin-bottom: 10px;">AI-Driven Precision</h4>
                    <p style="font-size: 14px; color: rgba(255,255,255,0.7);">Algorithms that continuously optimize your wealth-building path with zero friction.</p>
                </div>
                <div style="border-top: 2px solid #A03FA3; padding-top: 24px;">
                    <h4 style="font-size: 18px; font-weight: 700; margin-bottom: 10px;">Curated Network</h4>
                    <p style="font-size: 14px; color: rgba(255,255,255,0.7);">Surround yourself exclusively with driven, high-agency women builders.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Platform Pillars -->
    <section id="program" class="platform-pillars" style="padding: 100px 0; background: #FFFFFF;">
        <div class="container">
            <h2 class="section-title">Platform Pillars</h2>
            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-top: 60px;">
                <div style="border: 1px solid #111111; border-radius: 8px; padding: 40px; background: #FFFFFF;">
                    <img src="./public/images/common/manifesto-acct.jpg" style="width: 100%; height: 200px; object-fit: cover; border-radius: 8px; margin-bottom: 24px;">
                    <h3 style="font-size: 24px; font-weight: 700; margin-bottom: 16px; color: #111111;">Intelligence</h3>
                    <p style="font-size: 16px; color: #4B5563;">Aggregated insights and continuous monitoring of your total wealth footprint.</p>
                </div>
                <div style="border: 1px solid #111111; border-radius: 8px; padding: 40px; background: #FFFFFF;">
                    <img src="./public/images/common/manifesto-invest.jpg" style="width: 100%; height: 200px; object-fit: cover; border-radius: 8px; margin-bottom: 24px;">
                    <h3 style="font-size: 24px; font-weight: 700; margin-bottom: 16px; color: #111111;">Marketplace</h3>
                    <p style="font-size: 16px; color: #4B5563;">Direct access to vetted investment opportunities and premium asset classes.</p>
                </div>
                <div style="border: 1px solid #111111; border-radius: 8px; padding: 40px; background: #FFFFFF;">
                    <img src="./public/images/common/manifesto-social.jpg" style="width: 100%; height: 200px; object-fit: cover; border-radius: 8px; margin-bottom: 24px;">
                    <h3 style="font-size: 24px; font-weight: 700; margin-bottom: 16px; color: #111111;">Social Graph</h3>
                    <p style="font-size: 16px; color: #4B5563;">Connect and co-invest with trusted circles inside the Castle network.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Community -->
    <section id="influence" class="community-section" style="padding: 100px 0; background: #FFFFFF; border-top: 1px solid #111111;">
        <div class="container" style="text-align: left;">
            <h2 class="section-title" style="text-align: left; font-size: clamp(60px, 8vw, 100px); letter-spacing: -3px;">The Network</h2>
            <div style="display: flex; flex-direction: column; gap: 30px; margin-top: 60px; max-width: 800px;">
                <p style="font-size: clamp(24px, 3.5vw, 36px); font-weight: 600; color: #111111; line-height: 1.2;">1. Wealth is built in proximity to excellence.</p>
                <p style="font-size: clamp(24px, 3.5vw, 36px); font-weight: 600; color: #111111; line-height: 1.2;">2. Leverage collective intelligence.</p>
                <p style="font-size: clamp(24px, 3.5vw, 36px); font-weight: 600; color: #111111; line-height: 1.2;">3. Win together.</p>
            </div>
        </div>
    </section>

    <!-- Challenge Teaser -->
    <section class="challenge-teaser" style="padding: 60px 0; background: #A03FA3; color: white; text-align: center;">
        <div class="container">
            <h2 style="font-size: 40px; font-weight: 700; margin-bottom: 12px; letter-spacing: -1px;">The 21-Day Genesis Challenge</h2>
            <p style="font-size: 18px; margin-bottom: 24px; font-weight: 500;">Rewire your financial DNA in three weeks.</p>
            <a href="#" class="btn" style="background: white; color: #A03FA3;">Accept Challenge</a>
        </div>
    </section>

    <!-- Final Form CTA -->
    <section class="final-cta-section" style="background-color: #FFFFFF; padding: 100px 0; text-align: center; border-top: 1px solid #111111;">
        <div class="container final-cta-container">
            <h2 class="final-title" style="color: #111111;">Join The Inner Circle.</h2>
            <p style="font-size: 18px; color: #4B5563; margin-bottom: 40px; max-width: 600px;">Shape the future of the definitive wealth operating system.</p>
            <a href="https://docs.google.com/forms/d/e/1FAIpQLSfUnfm9YraHz4X4FBUcvN_vpguLsqBqj_Bkx6rl9P36k7Cigw/viewform" target="_blank" class="final-btn" style="background-color: #111111; color: #FFFFFF; border-radius: 8px;">Get early access</a>
        </div>
    </section>
"""

# Now we need to slice the HTML
start_marker = "<!-- Statement -->"
end_marker = "<!-- 11. Blog & Subscribe -->"

if start_marker in html and end_marker in html:
    part1 = html.split(start_marker)[0]
    part3 = html.split(end_marker)[1]
    
    html = part1 + new_sections + "\n    " + end_marker + part3
else:
    print("WARNING: Markers not found!")

# Also simplify header links
html = html.replace('<a href="#reality">Mission</a>', '<a href="#reality">Manifesto</a>')
html = html.replace('<a href="#program">Platform</a>', '<a href="#program">Pillars</a>')
html = html.replace('<a href="#influence">Community</a>', '<a href="#influence">Network</a>')
html = re.sub(r'<a href="#partnerships">Partners</a>\s*', '', html)

with open('/Users/Nati/.gemini/antigravity/scratch/Castle_Website_Final/index_v2.html', 'w', encoding='utf-8') as f:
    f.write(html)
