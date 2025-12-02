import pandas as pd

# ==========================================
#  F1 RACE MASTER DATA
# ==========================================

# 1. VERY SAD (Tragedy, heavy moments)
very_sad_race = [
    "1994 San Marino GP – Senna’s fatal crash",
    "1994 San Marino GP – Ratzenberger’s fatal crash",
    "2014 Japanese GP – Jules Bianchi crash",
    "2015 Tribute to Bianchi – Drivers’ circle at Hungarian GP",
    "2019 Spa GP – Death of Anthoine Hubert",
    "2019 Spa – Tribute lap by Gasly & Leclerc",
    "2020 Bahrain GP – Grosjean’s fiery crash",
    "Murray Walker’s final message before passing (2021)",
    "2001 Monza – Drivers’ tribute after 9/11",
    "Ayrton Senna’s funeral procession clips",
    "Schumacher family interview about his health",
    "2012 Vettel radio after learning about a marshal incident",
    "2000 Monza GP – Track worker Paolo Gislimberti killed",
    "1977 South African GP – Tom Pryce fatal crash",
    "Tribute to Justin Wilson",
    "Jules Bianchi’s father interview",
    "1992 French GP – Erik Comas crash, Senna stops to help",
    "Pierre Gasly crying in the paddock after Hubert’s death",
    "Ayrton Senna qualifying lap discussion after his death",
    "2017 Monaco – Wehrlein flip crash"
]

# 2. SAD (Heartbreak, lost titles)
sad_race = [
    "2008 Brazil GP – Massa loses title by 1 point",
    "2021 Abu Dhabi GP – Hamilton loses title on final lap",
    "2016 Monaco GP – Ricciardo pit blunder",
    "2006 Japan GP – Schumacher’s engine failure",
    "Rosberg retirement announcement",
    "2018 Azerbaijan GP – Red Bull teammates crash",
    "2010 Turkish GP – Vettel & Webber collision",
    "2019 Brazil GP – Ferrari teammates crash",
    "2012 European GP – Hamilton vs Maldonado crash",
    "Kimi Räikkönen’s 'Leave me alone' radio",
    "2022 Abu Dhabi – Vettel retirement 'Danke Seb'",
    "2020 Sakhir GP – Russell’s heartbreak after Mercedes pit error",
    "2004 Monaco – Schumacher tunnel crash",
    "Jenson Button Honda years – repeated DNFs",
    "Gasly interview about struggles before Monza win",
    "Schumacher 1999 leg injury crash at Silverstone",
    "Alonso crying after losing 2012 title to Vettel",
    "2023 Qatar – Piastri nearly collapsing due to heat",
    "Kubica 2007 crash at Canada",
    "Williams struggles documentary clips"
]

# 3. NEUTRAL (Informational, Iconic, Tech)
neutral_race = [
    "Senna’s 1989 Monaco onboard qualifying lap",
    "Hamilton’s 2018 Singapore pole lap",
    "Verstappen first win – Spain 2016",
    "Hamilton Schumacher 2000 Spa overtake with Zonta",
    "Red Bull 1.82s pit stop record",
    "F1 aerodynamics explained – Tech Talk",
    "F1 Safety Car evolution documentary",
    "Halo introduction press conference (2018)",
    "1976 Japan GP – Lauda withdraws",
    "2020 Virtual GPs during COVID",
    "Brand comparison video: Ferrari vs McLaren history",
    "Team radio compilations",
    "F1 tire compounds explanation video",
    "Ferrari F2004 engine rev sound test",
    "Evolution of the F1 steering wheel video",
    "Comparison of fastest pit stops in F1 history",
    "McLaren 2012 pit stop disaster compilation",
    "Classic onboard: 2005 Suzuka – Alonso 130R pass",
    "Brundle explaining DRS technology",
    "Michael Schumacher’s interview on discipline & mindset",
    "The history of the Monaco tunnel onboard footage",
    "1988 McLaren dominance documentary",
    "Comparison: V6 Hybrid vs V10 vs V12 engine sounds",
    "Lap of the Gods: 2005 Japan Raikkonen onboard",
    "Inside Red Bull factory – engineering video",
    "Mercedes DAS system explanation (2020)",
    "2022 Bahrain testing – car porpoising footage",
    "Analysis of 2023 regulation changes",
    "FIA race director radio broadcasts",
    "Williams FW14B tech breakdown"
]

# 4. HAPPY (Feel-good, Funny, Wholesome)
happy_race = [
    "2012 Brazil – Vettel comeback drive for title",
    "Ricciardo’s 'shoey' montage",
    "CarLando (Norris + Sainz) funniest moments",
    "Kimi eats ice cream during red flag (Malaysia)",
    "Vettel singing on podium",
    "Alonso 'I am a lion' radio",
    "Mick Schumacher first points – Silverstone 2022",
    "Gasly Monza win",
    "Pérez comeback podium Turkey 2020",
    "Ricciardo impersonating Verstappen interview",
    "Behind the scenes: F1 paddock cats & animals",
    "George Russell 'I want to win' Mercedes signing",
    "2020 Sakhir GP – Pérez first career win",
    "F1 drivers attempting accents compilation",
    "Lando Norris Twitch streaming clips",
    "Vettel picking up trash & supporting green initiatives",
    "Lewis Hamilton's first win (Canada 2007)",
    "Button 2009 title celebration",
    "Kimi’s 'Bwoah' compilation",
    "F1 Guess the Car/Track challenges",
    "Albon & his mom wholesome interviews",
    "Hulkenberg 'Happy Birthday Daniel' serenade",
    "Daniil Kvyat baby announcement joke",
    "Zhou Guanyu first points – Canada 2022",
    "McLaren shadow esports team win celebrations",
    "Alpine team mates joking during press conferences",
    "Ferrari pit crew dancing video",
    "2013 Silverstone – Rosberg’s win + fans singing",
    "Bottas 'to whom it may concern' radio",
    "Ricciardo surprising McLaren factory workers"
]

# 5. VERY HAPPY (Triumphant, Legendary)
very_happy_race = [
    "Hamilton 7th title celebration (Turkey 2020)",
    "Jenson Button 2011 Canada chaotic win",
    "Rosberg & Hamilton reminiscing karting childhood",
    "Kimi’s 2018 US GP win",
    "McLaren 1–2 Monza 2021",
    "Alonso’s podium with Aston Martin (Bahrain 2023)",
    "Norris first F1 win (Miami 2024)",
    "Russell first F1 win (Brazil 2022)",
    "Fans singing Italian anthem at Monza after Ferrari win",
    "Max Verstappen first world championship celebration (2021)",
    "F1 drivers doing secret santa",
    "Daniel Ricciardo’s return to F1 (2023) announcement",
    "Vettel & Alonso post-race hugs",
    "Sebastian Vettel’s farewell donuts (Abu Dhabi 2022)",
    "Ferrari double podium celebrations",
    "2017 Azerbaijan chaos + surprise podium (Stroll P3)",
    "2020 Italian GP – Gasly podium celebration",
    "Ocon's first win (Hungary 2021)",
    "Norris & Hamilton hugging after Miami 2024 victory",
    "2022 Silverstone – insane multi-overtake battle"
]

# ==========================================
#  DATASET GENERATION LOGIC
# ==========================================

data = []

def add_race_entries(content_list, mood_label):
    for item in content_list:
        data.append({
            "Content": item,
            "Mood": mood_label,
            "Type": "F1 Moment"
        })

# Map lists to app moods
add_race_entries(very_sad_race, "Very sad")
add_race_entries(sad_race, "Sad")
add_race_entries(neutral_race, "Neutral")
add_race_entries(happy_race, "Happy")
add_race_entries(very_happy_race, "Very happy")

# Create DataFrame and Save
df = pd.DataFrame(data)
df.to_csv("race_data.csv", index=False)
print(f"Successfully created race_data.csv with {len(df)} F1 moments!")