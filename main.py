import random

print("="*60)
print(" 🚀 HDT DIGITAL - MULTI-BRAND AI EMPIRE v5.0")
print(" 👑 CEO & Founder: You")
print(" 📺 YouTube Brand: HDT Creations")
print(" 🖤 IG Brand: Dark Logic Edits")
print(" 🌐 Agency Hub: HDT Visual (hdtvisual.carrd.co)")
print("="*60)

# 1. YouTube Growth Module (HDT Creations)
class HDTCreationsYouTube:
    def __init__(self):
        self.hooks = [
            "Stop scrolling if your views on HDT Creations are stuck at zero! 🛑🔥",
            "This one editing trick fixed my dead channel instantly... 🤫",
            "Why 99% of creators fail in the first 2 seconds (And how to fix it) ⚡",
            "Ye setting on karlo, shorts par views ki baarish ho jayegi! 📈"
        ]
    
    def generate_hook(self):
        return random.choice(self.hooks)
    
    def generate_caption(self, topic):
        caption = f"Level up your content game with HDT Creations! Today's focus: {topic}. 🎬✨"
        hashtags = "#HDTCreations #HDTDigital #YouTubeShorts #EditingTips #ViralReels"
        return caption, hashtags

# 2. Instagram Automation Module (Dark Logic Edits)
class DarkLogicEditsInstagram:
    def handle_dm(self, sender, message):
        print(f"\n📩 [Dark Logic Edits - IG DM] From @{sender}: '{message}'")
        msg = message.lower()
        
        if any(w in msg for w in ["edit", "video", "reels", "montage", "cinematic"]):
            return "Auto-Reply (Dark Logic Edits): Hey! Thanks for reaching out to Dark Logic Edits. We specialize in high-end cinematic edits and killer reels. Let's make your project look insane! 🖤🎬"
        elif any(w in msg for w in ["price", "cost", "rates"]):
            return "Auto-Reply (Dark Logic Edits): Thanks for your interest! Drop your project details and reference link, and we'll send you a custom quote. ⚡"
        else:
            return "Auto-Reply (Dark Logic Edits): Welcome to Dark Logic Edits! How can we elevate your visual style today? 🔥"

# 3. Website & General Inquiry Manager (HDT Visual / HDT Digital)
class HDTVisualManager:
    def handle_website_lead(self, name, service, email):
        print(f"\n🌐 [HDT Visual Website Lead] From: {name} ({email})")
        print(f"   -> Service Requested: {service}")
        return f"Auto-Response Sent to {email}: Thanks for visiting hdtvisual.carrd.co! Your request for '{service}' has been logged at HDT Digital. We'll connect soon. 🚀"

# Main Execution Loop (The Ultimate Dashboard)
def run_empire_system():
    yt_brand = HDTCreationsYouTube()
    ig_brand = DarkLogicEditsInstagram()
    web_brand = HDTVisualManager()
    
    print("\n✨ [HDT Creations - YouTube] Generating Next Short Hook:")
    print(f"   > {yt_brand.generate_hook()}")
    cap, tags = yt_brand.generate_caption("Cinematic Transitions")
    print(f"   -> Caption: {cap}")
    print(f"   -> Tags: {tags}")
    
    print("\n--- Testing Brand Interactions ---")
    # Testing Dark Logic Edits Instagram DM
    print(ig_brand.handle_dm("creative_soul", "Need cinematic edits for my new montage reels!"))
    
    # Testing HDT Visual Website Lead
    print(web_brand.handle_website_lead("Aman Verma", "AI Automation & Web Design", "aman@example.com"))
    
    print("\n" + "="*60)
    print(" ✅ All Brands (HDT Creations, Dark Logic Edits, HDT Visual) are live!")
    print("="*60)

if __name__ == "__main__":
    run_empire_system()
    

