import datetime
import os

# Google Gemini API Library
import google.generativeai as genai

# 🔑 Your Gemini API Key is configured here!
GEMINI_API_KEY = "AQ.Ab8RN6I21-HSk9PMdDs5wLqFdzvlSQG42IXTS81dmCD_G9gR1Q"

# Configuring Gemini AI Model
try:
  genai.configure(api_key=GEMINI_API_KEY)
  # Using Gemini 1.5 Flash for ultra-fast and smart generation
  model = genai.GenerativeModel("gemini-1.5-flash")
  ai_enabled = True
except Exception as e:
  ai_enabled = False

print("=" * 65)
print(" 🚀 HDT DIGITAL - CIPHER GEMINI-POWERED EMPIRE v8.0")
print(" 👑 CEO & Founder: You | 🤖 AI Manager: Cipher (Powered by Gemini)")
print(" Brands: HDT Creations | Dark Logic Edits | HDT Visual")
print("=" * 65)


# Core Brain for Cipher using Gemini API
class CipherBrain:

  def generate_text(self, prompt):
    if ai_enabled:
      try:
        response = model.generate_content(prompt)
        return response.text.strip()
      except Exception as e:
        return f"API Error: {e}"
    else:
      return "[Fallback Mode] AI configuration failed."


# 1. YouTube Module (HDT Creations - Powered by Gemini)
class HDTCreationsYouTube:

  def __init__(self, brain):
    self.brain = brain

  def generate_hook(self, topic):
    prompt = (
        f"Write a viral, high-retention YouTube Shorts hook for a video about"
        f" '{topic}' on channel HDT Creations. Make it punchy, catchy, and under"
        " 15 words."
    )
    return self.brain.generate_text(prompt)

  def generate_caption(self, topic):
    prompt = (
        f"Write a short, engaging YouTube description caption and 5 trending"
        f" hashtags for HDT Creations about '{topic}'."
    )
    return self.brain.generate_text(prompt)


# 2. Instagram Automation Module (Dark Logic Edits - Powered by Gemini)
class DarkLogicEditsInstagram:

  def __init__(self, brain):
    self.brain = brain

  def handle_dm(self, sender, message):
    prompt = (
        f"Act as the professional AI manager for 'Dark Logic Edits'. A client"
        f" named @{sender} sent this message: '{message}'. Write a compelling"
        " auto-reply offering high-end cinematic edits and reels."
    )
    return self.brain.generate_text(prompt)


# 3. AI Video Prompt Generator (Powered by Gemini)
class AIVideoPromptGenerator:

  def __init__(self, brain):
    self.brain = brain

  def generate_prompt(self, video_concept):
    prompt = (
        f"Create a detailed AI video generation prompt (for tools like Runway or"
        f" Sora) featuring 4K cinematic lighting, high-contrast dark aesthetic,"
        f" and --ar 9:16 aspect ratio for the concept: '{video_concept}'"
    )
    return self.brain.generate_text(prompt)


# 4. Website & Lead Database Module (HDT Visual / HDT Digital)
class HDTVisualAgency:

  def __init__(self):
    self.lead_database = []

  def save_lead(self, name, service, contact):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    lead_data = {
        "time": timestamp,
        "name": name,
        "service": service,
        "contact": contact,
    }
    self.lead_database.append(lead_data)
    print(f"\n💾 [Database Updated] Lead saved successfully for {name}!")
    return lead_data

  def show_leads(self):
    print("\n📋 --- Current Stored Leads ---")
    for lead in self.lead_database:
      print(
          f"[{lead['time']}] {lead['name']} | Service: {lead['service']} |"
          f" Contact: {lead['contact']}"
      )


# 5. Client Outreach & Pitch Generator (Powered by Gemini)
class OutreachPitchGenerator:

  def __init__(self, brain):
    self.brain = brain

  def generate_pitch(self, creator_name, niche):
    prompt = (
        f"Write a short, persuasive cold outreach DM to a creator named"
        f" @{creator_name} who creates {niche} content. Pitch HDT Digital"
        " (hdtvisual.carrd.co) for video editing and offer a free sample"
        " edit."
    )
    return self.brain.generate_text(prompt)


# Main Execution Loop
def run_gemini_empire():
  brain = CipherBrain()
  yt = HDTCreationsYouTube(brain)
  ig = DarkLogicEditsInstagram(brain)
  ai_video = AIVideoPromptGenerator(brain)
  agency = HDTVisualAgency()
  outreach = OutreachPitchGenerator(brain)

  print("\n✨ [1] Gemini-Powered YouTube Hook (HDT Creations):")
  print(f"   > {yt.generate_hook('Cinematic Transitions')}")

  print("\n✨ [2] Gemini-Powered Dark Logic Edits IG Auto-Reply:")
  print(f"   > {ig.handle_dm('creator_alex', 'Need cinematic edits for my reels!')}")

  print("\n✨ [3] Gemini-Powered AI Video Prompt:")
  print(f"   -> {ai_video.generate_prompt('Cyberpunk Video Editing Montage')}")

  print("\n✨ [4] HDT Visual Website Lead Storage Test:")
  agency.save_lead("Aman Verma", "AI Automation", "aman@example.com")
  agency.show_leads()

  print("\n✨ [5] Gemini-Powered Cold Outreach Pitch:")
  print(f"   > {outreach.generate_pitch('rahul_vlogs', 'Gaming Shorts')}")

  print("\n" + "=" * 65)
  print(
      " ✅ Cipher Empire v8.0 (Powered by Google Gemini API) is Active, Boss! 🚀"
  )
  print("=" * 65)


if __name__ == "__main__":
  run_gemini_empire()
        

