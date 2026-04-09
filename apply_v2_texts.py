import re

with open('/Users/Nati/.gemini/antigravity/scratch/Castle_Website_Final/index_v2.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Insert Statement Section after Hero
statement_code = """
    <!-- Statement -->
    <section class="statement-section" style="background-color: #FFFFFF; padding: 120px 0; text-align: center;">
        <div class="container" style="max-width: 1000px; margin: 0 auto;">
            <h2 style="font-size: clamp(48px, 6vw, 72px); font-weight: 700; line-height: 1.1; color: #111111; margin: 0; letter-spacing: -2px;">
                Women were Taught to Save,<br>not to <span style="color: #A03FA3;">Build Wealth.</span>
            </h2>
            <p style="font-size: clamp(32px, 4vw, 48px); font-weight: 600; color: #111111; margin-top: 20px; font-family: 'Caveat', cursive; line-height: 1; margin-bottom: 40px;">
                Castle changes that.
            </p>
            <p style="font-size: clamp(20px, 2.5vw, 26px); color: #1A1A1A; line-height: 1.5; font-weight: 500; font-family: 'Inter', sans-serif; margin-bottom: 40px;">
                Castle is a new financial ecosystem where intelligence meets community—empowering women to build real wealth, achieve independence, and create lasting legacy.
            </p>
            <p style="font-size: clamp(18px, 2vw, 20px); font-weight: 600; color: #4B5563; text-transform: uppercase; letter-spacing: 2px;">
                This is not about Managing Money.<br><span style="color: #111111; font-weight: 800;">This is about Owning your Future.</span>
            </p>
        </div>
    </section>
"""
if "<!-- V2 Block" in html and "<!-- Statement -->" not in html:
    html = html.replace('<!-- V2 Block (Replaces How it works) -->', statement_code + '\n    <!-- V2 Block (Replaces How it works) -->')


# 2. What makes us Different?
old_different = """    <!-- What Makes Us Different -->
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
    </section>"""

new_different = """    <!-- What Makes Us Different -->
    <section class="different-section" style="background-color: #111111; color: #FFFFFF; padding: 100px 0;">
        <div class="container" style="max-width: 1000px; text-align: center;">
            <h2 class="section-title" style="color: #FFFFFF; margin-bottom: 30px;">What makes us Different?</h2>
            <p style="font-size: clamp(24px, 3.5vw, 36px); font-weight: 500; color: #FFFFFF; line-height: 1.3; margin-bottom: 60px;">
                Most programs teach what to do with money.<br>
                <span style="color: #A03FA3; font-weight: 700;">We transform how women think about money.</span>
            </p>
            
            <p style="font-size: 18px; color: rgba(255,255,255,0.7); text-transform: uppercase; letter-spacing: 2px; font-weight: 700; margin-bottom: 30px;">Castle combines:</p>
            <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 16px; margin-bottom: 60px; font-size: clamp(18px, 2.5vw, 24px); font-weight: 700; font-family: 'Inter', sans-serif;">
                <span>Psychology</span> <span style="color: #A03FA3;">+</span>
                <span>Finance</span> <span style="color: #A03FA3;">+</span>
                <span>Technology</span> <span style="color: #A03FA3;">+</span>
                <span>Community</span>
            </div>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px;">
                <div style="border: 1px solid rgba(255,255,255,0.2); border-radius: 8px; padding: 40px;">
                    <h3 style="font-size: 24px; font-weight: 700; margin-bottom: 10px; color: #FFFFFF;">A system designed specifically for women</h3>
                </div>
                <div style="border: 1px solid rgba(255,255,255,0.2); border-radius: 8px; padding: 40px;">
                    <h3 style="font-size: 24px; font-weight: 700; margin-bottom: 10px; color: #FFFFFF;">A scalable, measurable transformation model</h3>
                </div>
            </div>
        </div>
    </section>"""
html = html.replace(old_different, new_different)


# 3. Platform Pillars (using Manifesto 5 items)
# Wait, "y ahi va lo de Cohort y lo demas" implies the original 5 items.
old_platform = """    <!-- Platform Pillars -->
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
    </section>"""

new_platform = """    <!-- Platform Pillars -->
    <section id="program" class="platform-pillars" style="padding: 100px 0; background: #FFFFFF;">
        <div class="container">
            <h2 class="section-title">Core Platform Pillars</h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px; margin-top: 60px;">
                <div style="border: 1px solid #111111; border-radius: 8px; padding: 30px; background: #FFFFFF;">
                    <h3 style="font-size: 24px; font-weight: 700; margin-bottom: 16px; color: #111111;">01. Cohort Learning</h3>
                </div>
                <div style="border: 1px solid #111111; border-radius: 8px; padding: 30px; background: #FFFFFF;">
                    <h3 style="font-size: 24px; font-weight: 700; margin-bottom: 16px; color: #111111;">02. Account Aggregation</h3>
                </div>
                <div style="border: 1px solid #111111; border-radius: 8px; padding: 30px; background: #FFFFFF;">
                    <h3 style="font-size: 24px; font-weight: 700; margin-bottom: 16px; color: #111111;">03. AI Money & Wealth Coach</h3>
                </div>
                <div style="border: 1px solid #111111; border-radius: 8px; padding: 30px; background: #FFFFFF;">
                    <h3 style="font-size: 24px; font-weight: 700; margin-bottom: 16px; color: #111111;">04. Investment Marketplace</h3>
                </div>
                <div style="border: 1px solid #111111; border-radius: 8px; padding: 30px; background: #FFFFFF;">
                    <h3 style="font-size: 24px; font-weight: 700; margin-bottom: 16px; color: #111111;">05. Social Wealth Building</h3>
                </div>
            </div>
        </div>
    </section>"""
html = html.replace(old_platform, new_platform)


# 4. Community Section
old_community = """    <!-- Community -->
    <section id="influence" class="community-section" style="padding: 100px 0; background: #FFFFFF; border-top: 1px solid #111111;">
        <div class="container" style="text-align: left;">
            <h2 class="section-title" style="text-align: left; font-size: clamp(60px, 8vw, 100px); letter-spacing: -3px;">The Network</h2>
            <div style="display: flex; flex-direction: column; gap: 30px; margin-top: 60px; max-width: 800px;">
                <p style="font-size: clamp(24px, 3.5vw, 36px); font-weight: 600; color: #111111; line-height: 1.2;">1. Wealth is built in proximity to excellence.</p>
                <p style="font-size: clamp(24px, 3.5vw, 36px); font-weight: 600; color: #111111; line-height: 1.2;">2. Leverage collective intelligence.</p>
                <p style="font-size: clamp(24px, 3.5vw, 36px); font-weight: 600; color: #111111; line-height: 1.2;">3. Win together.</p>
            </div>
        </div>
    </section>"""

new_community = """    <!-- Community -->
    <section id="influence" class="community-section" style="padding: 120px 0; background: #F8F8FA; border-top: 1px solid #111111;">
        <div class="container" style="text-align: center; max-width: 1000px;">
            <h2 class="section-title" style="font-size: clamp(52px, 7vw, 90px); letter-spacing: -3px; margin-bottom: 40px; color: #111111;">Women Don't Build Wealth Alone.</h2>
            
            <div style="display: flex; align-items: center; justify-content: center; gap: clamp(16px, 4vw, 40px); margin-bottom: 60px; font-weight: 700; font-size: clamp(18px, 2.5vw, 24px); letter-spacing: 2px; color: #A03FA3;">
                <span>CIRCLES</span>
                <span>COHORTS</span>
                <span>NETWORKS</span>
            </div>

            <div style="display: flex; flex-direction: column; gap: 20px; font-weight: 700; font-size: clamp(28px, 4vw, 44px); color: #111111; line-height: 1.2; margin-bottom: 60px;">
                <p>Connection becomes capital.</p>
                <p>Community becomes power.</p>
                <p>Wealth becomes inevitable.</p>
            </div>
            
            <a href="https://docs.google.com/forms/d/e/1FAIpQLSfUnfm9YraHz4X4FBUcvN_vpguLsqBqj_Bkx6rl9P36k7Cigw/viewform" target="_blank" class="btn btn-large" style="background-color: #111111; color: white;">Build Your Castle</a>
        </div>
    </section>"""
html = html.replace(old_community, new_community)

with open('/Users/Nati/.gemini/antigravity/scratch/Castle_Website_Final/index_v2.html', 'w', encoding='utf-8') as f:
    f.write(html)
