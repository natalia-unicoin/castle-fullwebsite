import re

with open('/Users/Nati/.gemini/antigravity/scratch/Castle_Website_Final/index_v2.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_earn_section = """
    <!-- V2 Block (Replaces How it works -> EARN TOKENS) -->
    <section class="earn-tokens-section" style="background-color: #0A0F1C; background-image: radial-gradient(circle at top right, rgba(160,63,163,0.15) 0%, transparent 40%); color: #FFFFFF; padding: 120px 0;">
        <div class="container" style="max-width: 1000px; margin: 0 auto;">
            
            <div style="text-align: left; margin-bottom: 60px;">
                <h2 style="font-size: clamp(40px, 5vw, 56px); font-weight: 700; color: #D4AF37; line-height: 1.1; margin-bottom: 24px; font-family: 'Inter', sans-serif; text-transform: uppercase; letter-spacing: -1px;">
                    Earn Tokens.<br>Transform your wealth.
                </h2>
                <p style="font-size: clamp(18px, 2.5vw, 22px); color: rgba(255,255,255,0.9); line-height: 1.6; max-width: 900px; font-weight: 400; font-family: 'Inter', sans-serif;">
                    At <strong>Castle</strong>, you don't just manage your money—you build <strong>equity</strong> in a financial network designed for the bold. Here, your intellect, influence, and initiative aren't just valued—they're rewarded.
                </p>
            </div>

            <div style="text-align: left; margin-bottom: 50px;">
                <h3 style="font-size: clamp(20px, 3vw, 24px); font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 16px; font-family: 'Inter', sans-serif;">
                    Tokenize your financial empowerment
                </h3>
                <p style="font-size: 18px; color: rgba(255,255,255,0.7); max-width: 800px; font-family: 'Inter', sans-serif;">
                    Own your journey—earn tokens as a founding partner in an economy that rewards your influence, your work, and your vision.
                </p>
            </div>

            <!-- 4 Circles Grid -->
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 40px; margin-bottom: 80px; text-align: center;">
                <div style="display: flex; flex-direction: column; align-items: center;">
                    <div style="width: 120px; height: 120px; border-radius: 50%; background: linear-gradient(135deg, #1E3A2F, #2A5A4A); margin-bottom: 20px; display: flex; align-items: center; justify-content: center; box-shadow: inset 0 0 20px rgba(0,0,0,0.5), 0 10px 20px rgba(0,0,0,0.3); border: 2px solid rgba(255,255,255,0.1);">
                        <span style="font-size: 40px;">💼</span>
                    </div>
                    <h4 style="font-size: 16px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: #FFFFFF; margin-bottom: 12px;">Earn UNI</h4>
                    <p style="font-size: 14px; color: rgba(255,255,255,0.7); line-height: 1.5;">Earn Unicoins by taking control of your money.</p>
                </div>
                
                <div style="display: flex; flex-direction: column; align-items: center;">
                    <div style="width: 120px; height: 120px; border-radius: 50%; background: linear-gradient(135deg, #1A365D, #2B6CB0); margin-bottom: 20px; display: flex; align-items: center; justify-content: center; box-shadow: inset 0 0 20px rgba(0,0,0,0.5), 0 10px 20px rgba(0,0,0,0.3); border: 2px solid rgba(255,255,255,0.1);">
                        <span style="font-size: 40px;">🤝</span>
                    </div>
                    <h4 style="font-size: 16px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: #FFFFFF; margin-bottom: 12px;">Invite Friends</h4>
                    <p style="font-size: 14px; color: rgba(255,255,255,0.7); line-height: 1.5;">Earn when you expand your network.</p>
                </div>

                <div style="display: flex; flex-direction: column; align-items: center;">
                    <div style="width: 120px; height: 120px; border-radius: 50%; background: linear-gradient(135deg, #4A148C, #7B1FA2); margin-bottom: 20px; display: flex; align-items: center; justify-content: center; box-shadow: inset 0 0 20px rgba(0,0,0,0.5), 0 10px 20px rgba(0,0,0,0.3); border: 2px solid rgba(255,255,255,0.1);">
                        <span style="font-size: 40px;">💡</span>
                    </div>
                    <h4 style="font-size: 16px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: #FFFFFF; margin-bottom: 12px;">Contribute Intellect</h4>
                    <p style="font-size: 14px; color: rgba(255,255,255,0.7); line-height: 1.5;">Share insights and predictions that shape the community.</p>
                </div>

                <div style="display: flex; flex-direction: column; align-items: center;">
                    <div style="width: 120px; height: 120px; border-radius: 50%; background: linear-gradient(135deg, #B7791F, #ECC94B); margin-bottom: 20px; display: flex; align-items: center; justify-content: center; box-shadow: inset 0 0 20px rgba(0,0,0,0.5), 0 10px 20px rgba(0,0,0,0.3); border: 2px solid rgba(255,255,255,0.1);">
                        <span style="font-size: 40px;">🏆</span>
                    </div>
                    <h4 style="font-size: 16px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: #FFFFFF; margin-bottom: 12px;">Climb the Leaderboard</h4>
                    <p style="font-size: 14px; color: rgba(255,255,255,0.7); line-height: 1.5;">Get rewarded for your expertise and influence.</p>
                </div>
            </div>

            <!-- Bottom Section -->
            <div style="text-align: left; position: relative;">
                <h3 style="font-size: clamp(24px, 3.5vw, 30px); font-weight: 700; color: #D4AF37; margin-bottom: 20px; text-transform: uppercase; font-family: 'Inter', sans-serif;">
                    Build Wealth Together
                </h3>
                <p style="font-size: 18px; color: rgba(255,255,255,0.9); line-height: 1.6; font-family: 'Inter', sans-serif; margin-bottom: 30px; max-width: 850px;">
                    This is more than a platform; it's a <strong>collective ascent</strong>. As you build, you don't just earn. You <strong>invest</strong>. Your network becomes an <strong>equity stake</strong>. Your intellect creates ownership. Your influence drives opportunity.
                </p>
                
                <p style="font-size: 18px; font-weight: 700; color: #FFFFFF; margin-bottom: 16px;">Your rewards are your path:</p>
                
                <ul style="list-style: none; padding: 0; margin-bottom: 50px; font-size: 16px; color: rgba(255,255,255,0.8); line-height: 1.8;">
                    <li style="position: relative; padding-left: 20px; margin-bottom: 10px;"><span style="position: absolute; left: 0; color: #D4AF37;">•</span> Stake tokens in a financial economy that values your contribution.</li>
                    <li style="position: relative; padding-left: 20px; margin-bottom: 10px;"><span style="position: absolute; left: 0; color: #D4AF37;">•</span> Unlock <strong style="color: white;">special investment opportunities</strong> as your reputation grows.</li>
                    <li style="position: relative; padding-left: 20px; margin-bottom: 10px;"><span style="position: absolute; left: 0; color: #D4AF37;">•</span> Earn <strong style="color: white;">Unicoin</strong> rewards that expand as the Castle network grows.</li>
                    <li style="position: relative; padding-left: 20px; margin-bottom: 10px;"><span style="position: absolute; left: 0; color: #D4AF37;">•</span> Become a <strong style="color: white;">founding partner</strong> by investing with your work and access, not just your capital.</li>
                </ul>

                <div style="text-align: center;">
                    <a href="https://docs.google.com/forms/d/e/1FAIpQLSfUnfm9YraHz4X4FBUcvN_vpguLsqBqj_Bkx6rl9P36k7Cigw/viewform" target="_blank" style="display: inline-block; background: linear-gradient(180deg, #FAD961 0%, #D4AF37 100%); color: #111111; font-weight: 700; font-size: 16px; text-transform: uppercase; letter-spacing: 2px; padding: 16px 40px; border-radius: 50px; text-decoration: none; box-shadow: 0 10px 20px rgba(0,0,0,0.3); border: 1px solid #FFE77A; transition: transform 0.2s;">
                        Start Building
                    </a>
                </div>
            </div>

        </div>
    </section>
"""

# Find the V2 placeholder block and replace it
placeholder_start = "<!-- V2 Block (Replaces How it works) -->"
old_block_end = "</section>" # we need to cleverly replace the section.
import re
# Use regex to find the entire v2-block section
html = re.sub(r'<!-- V2 Block \(Replaces How it works\) -->\s*<section class="v2-block".*?</section>', new_earn_section, html, flags=re.DOTALL)

with open('/Users/Nati/.gemini/antigravity/scratch/Castle_Website_Final/index_v2.html', 'w', encoding='utf-8') as f:
    f.write(html)
