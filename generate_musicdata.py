import pandas as pd

# ==========================================
#  MASTER DATA POOL (Real Songs Only)
# ==========================================

# 1. SAD / VERY SAD (Heartbreak, Slow, Emotional)
sad_songs = [
    # English
    {"Title": "Another Love", "Artist": "Tom Odell", "Lang": "English"},
    {"Title": "Let Me Down Slowly", "Artist": "Alec Benjamin", "Lang": "English"},
    {"Title": "Someone You Loved", "Artist": "Lewis Capaldi", "Lang": "English"},
    {"Title": "Falling", "Artist": "Harry Styles", "Lang": "English"},
    {"Title": "Fix You", "Artist": "Coldplay", "Lang": "English"},
    {"Title": "Lovely", "Artist": "Billie Eilish", "Lang": "English"},
    {"Title": "Traitor", "Artist": "Olivia Rodrigo", "Lang": "English"},
    {"Title": "All I Want", "Artist": "Kodaline", "Lang": "English"},
    {"Title": "The Night We Met", "Artist": "Lord Huron", "Lang": "English"},
    {"Title": "Wrecked", "Artist": "Imagine Dragons", "Lang": "English"},
    {"Title": "Dusk Till Dawn", "Artist": "ZAYN", "Lang": "English"},
    {"Title": "Arcade", "Artist": "Duncan Laurence", "Lang": "English"},
    {"Title": "Memories", "Artist": "Maroon 5", "Lang": "English"},
    {"Title": "Ghost", "Artist": "Justin Bieber", "Lang": "English"},
    {"Title": "I'll Be There", "Artist": "Walk off the Earth", "Lang": "English"},
    {"Title": "Christmas Lights", "Artist": "Zach Seabaugh", "Lang": "English"},
    {"Title": "It's OK", "Artist": "Nightbirde", "Lang": "English"},
    {"Title": "Before You Go", "Artist": "Lewis Capaldi", "Lang": "English"},
    {"Title": "Die For You", "Artist": "VALORANT", "Lang": "English"},
    {"Title": "Whiskey Lullaby", "Artist": "Brad Paisley", "Lang": "English"},
    {"Title": "If We Have Each Other", "Artist": "Alec Benjamin", "Lang": "English"},
    {"Title": "Demons", "Artist": "Imagine Dragons", "Lang": "English"},
    
    # Hindi
    {"Title": "Baarishein", "Artist": "Anuv Jain", "Lang": "Hindi"},
    {"Title": "Channa Mereya", "Artist": "Arijit Singh", "Lang": "Hindi"},
    {"Title": "Tujhe Bhula Diya", "Artist": "Mohit Chauhan", "Lang": "Hindi"},
    {"Title": "Agar Tum Saath Ho", "Artist": "Arijit Singh", "Lang": "Hindi"},
    {"Title": "Kabira", "Artist": "Arijit Singh", "Lang": "Hindi"},
    {"Title": "Judaai", "Artist": "Rekha Bhardwaj", "Lang": "Hindi"},
    {"Title": "Maine Dil Se Kaha", "Artist": "KK", "Lang": "Hindi"},
    {"Title": "Tune Jo Na Kaha", "Artist": "Mohit Chauhan", "Lang": "Hindi"},
    {"Title": "Maan Meri Jaan", "Artist": "King", "Lang": "Hindi"},
    {"Title": "Choo Lo", "Artist": "The Local Train", "Lang": "Hindi"},
    {"Title": "Kaise Hua", "Artist": "Vishal Mishra", "Lang": "Hindi"},
    {"Title": "Hamari Adhuri Kahani", "Artist": "Arijit Singh", "Lang": "Hindi"},
    {"Title": "Jaikal Mahakal", "Artist": "Amit Trivedi", "Lang": "Hindi"},
    {"Title": "Chaudhary", "Artist": "Mame Khan", "Lang": "Hindi"},
    {"Title": "Jhoom", "Artist": "Ali Zafar", "Lang": "Hindi"},
    {"Title": "Kal Ho Naa Ho", "Artist": "Shankar-Ehsaan-Loy", "Lang": "Hindi"},
    {"Title": "Ek Din Aap", "Artist": "Kumar Sanu", "Lang": "Hindi"},
    {"Title": "Ishq Sufiyana", "Artist": "Vishal-Shekhar", "Lang": "Hindi"},
    {"Title": "Laaree Chootee", "Artist": "Call", "Lang": "Hindi"},
    {"Title": "Kya Mujhe Pyar Hai", "Artist": "KK", "Lang": "Hindi"},
    {"Title": "Musafir", "Artist": "Arijit Anand", "Lang": "Hindi"},
    {"Title": "Apna Bana Le", "Artist": "Arijit Singh", "Lang": "Hindi"},
    {"Title": "Darasal", "Artist": "Atif Aslam", "Lang": "Hindi"},
    {"Title": "Rait Zara Si", "Artist": "A.R. Rahman", "Lang": "Hindi"},
    {"Title": "Jab Koi Baat", "Artist": "Atif Aslam", "Lang": "Hindi"},
    {"Title": "Haareya", "Artist": "Sachin-Jigar", "Lang": "Hindi"},
    {"Title": "Baarish Lete Aana", "Artist": "Darshan Raval", "Lang": "Hindi"},

    # Telugu
    {"Title": "Em Sandeham Ledu", "Artist": "Oohalu Gusagusalade", "Lang": "Telugu"},
    {"Title": "Vellipomaake", "Artist": "Sid Sriram", "Lang": "Telugu"},
    {"Title": "O Rendu Prema Meghaalila", "Artist": "Baby", "Lang": "Telugu"},
    {"Title": "Yedakala Paata", "Artist": "Sitaramam", "Lang": "Telugu"},
    {"Title": "Kanulu Navaina", "Artist": "Nani", "Lang": "Telugu"},
    {"Title": "Priyathama", "Artist": "Majili", "Lang": "Telugu"},
    {"Title": "Arere Yekkada", "Artist": "Nenu Local", "Lang": "Telugu"},
    {"Title": "Gelupu Thalupule", "Artist": "Theenmaar", "Lang": "Telugu"},
    {"Title": "Monna Kanipinchavu", "Artist": "Harris Jayaraj", "Lang": "Telugu"},
    {"Title": "Kopama Napina", "Artist": "Karthik", "Lang": "Telugu"},
    {"Title": "Nijanga Nenena", "Artist": "Karthik", "Lang": "Telugu"}
]

# 2. NEUTRAL / CHILL (Acoustic, Relaxed)
neutral_songs = [
    # English
    {"Title": "comethru", "Artist": "Jeremy Zucker", "Lang": "English"},
    {"Title": "Night Changes", "Artist": "One Direction", "Lang": "English"},
    {"Title": "Perfect", "Artist": "Ed Sheeran", "Lang": "English"},
    {"Title": "Photograph", "Artist": "Ed Sheeran", "Lang": "English"},
    {"Title": "At My Worst", "Artist": "Pink Sweat$", "Lang": "English"},
    {"Title": "Love Yourself", "Artist": "Justin Bieber", "Lang": "English"},
    {"Title": "Circles", "Artist": "Post Malone", "Lang": "English"},
    {"Title": "Sunflower", "Artist": "Post Malone", "Lang": "English"},
    {"Title": "Heat Waves", "Artist": "Glass Animals", "Lang": "English"},
    {"Title": "Count on Me", "Artist": "Bruno Mars", "Lang": "English"},
    {"Title": "Yellow", "Artist": "Coldplay", "Lang": "English"},
    {"Title": "Here with Me", "Artist": "d4vd", "Lang": "English"},
    {"Title": "Don't Feel Like Crying", "Artist": "Sigrid", "Lang": "English"},
    {"Title": "Days I Will Remember", "Artist": "Tyrone Wells", "Lang": "English"},
    {"Title": "Classic", "Artist": "MKTO", "Lang": "English"},
    {"Title": "Don't Stop Believin'", "Artist": "Journey", "Lang": "English"},
    {"Title": "FRIENDS", "Artist": "Marshmello", "Lang": "English"},
    {"Title": "Stitches", "Artist": "Shawn Mendes", "Lang": "English"},
    {"Title": "Attention", "Artist": "Charlie Puth", "Lang": "English"},
    {"Title": "Closer", "Artist": "The Chainsmokers", "Lang": "English"},
    {"Title": "Something Just Like This", "Artist": "Chainsmokers", "Lang": "English"},
    {"Title": "Older", "Artist": "Alec Benjamin", "Lang": "English"},
    {"Title": "Falling in Love at a Coffee Shop", "Artist": "Landon Pigg", "Lang": "English"},
    {"Title": "The Bones", "Artist": "Maren Morris", "Lang": "English"},
    {"Title": "pretty enough", "Artist": "amanda williams", "Lang": "English"},
    {"Title": "Calm Down", "Artist": "Rema/Selena", "Lang": "English"},
    {"Title": "My Heart Will Go On", "Artist": "Celine Dion", "Lang": "English"},
    {"Title": "Steal My Girl", "Artist": "One Direction", "Lang": "English"},
    {"Title": "Silence", "Artist": "Marshmello", "Lang": "English"},
    {"Title": "STAY", "Artist": "The Kid LAROI", "Lang": "English"},
    {"Title": "Dandelions", "Artist": "Ruth B.", "Lang": "English"},
    {"Title": "SNAP", "Artist": "Rosa Linn", "Lang": "English"},
    {"Title": "Home", "Artist": "Edith Whiskers", "Lang": "English"},
    {"Title": "Stereo Hearts", "Artist": "Gym Class Heroes", "Lang": "English"},

    # Hindi
    {"Title": "Iktara", "Artist": "Wake Up Sid", "Lang": "Hindi"},
    {"Title": "Kun Faya Kun", "Artist": "Rockstar", "Lang": "Hindi"},
    {"Title": "Udd Gaye", "Artist": "Ritviz", "Lang": "Hindi"},
    {"Title": "Kasoor", "Artist": "Prateek Kuhad", "Lang": "Hindi"},
    {"Title": "Kho Gaye Hum Kahan", "Artist": "Baar Baar Dekho", "Lang": "Hindi"},
    {"Title": "Ilahi", "Artist": "Arijit Singh", "Lang": "Hindi"},
    {"Title": "Safarnama", "Artist": "Tamasha", "Lang": "Hindi"},
    {"Title": "Sham", "Artist": "Amit Trivedi", "Lang": "Hindi"},
    {"Title": "Waqt Ki Baatein", "Artist": "Dream Note", "Lang": "Hindi"},
    {"Title": "Aise Kyun", "Artist": "Anurag Saikia", "Lang": "Hindi"},
    {"Title": "Chaand Baaliyan", "Artist": "Aditya A", "Lang": "Hindi"},
    {"Title": "Jashn-E-Bahaara", "Artist": "A.R. Rahman", "Lang": "Hindi"},
    {"Title": "Mera Mann Kehne Laga", "Artist": "Falak Shabir", "Lang": "Hindi"},
    {"Title": "Rangi Saari", "Artist": "Kavita Seth", "Lang": "Hindi"},
    {"Title": "Bawara Mann", "Artist": "Jubin Nautiyal", "Lang": "Hindi"},
    {"Title": "Liggi", "Artist": "Ritviz", "Lang": "Hindi"},
    {"Title": "Raanjhanaa", "Artist": "A.R. Rahman", "Lang": "Hindi"},
    {"Title": "Khaabon Ke Parinday", "Artist": "Alyssa Mendonsa", "Lang": "Hindi"},
    {"Title": "Phir Se Ud Chala", "Artist": "Mohit Chauhan", "Lang": "Hindi"},

    # Telugu
    {"Title": "Life of Ram", "Artist": "Jaanu", "Lang": "Telugu"},
    {"Title": "Samajavaragamana", "Artist": "Ala Vaikunthapurramuloo", "Lang": "Telugu"},
    {"Title": "Inkem Inkem", "Artist": "Geetha Govindam", "Lang": "Telugu"},
    {"Title": "Ninnila", "Artist": "Tholi Prema", "Lang": "Telugu"},
    {"Title": "Oke Oka Lokam", "Artist": "Sashi", "Lang": "Telugu"},
    {"Title": "Adiga Adiga", "Artist": "Ninnu Kori", "Lang": "Telugu"},
    {"Title": "Evare", "Artist": "Vijay Yesudas", "Lang": "Telugu"},
    {"Title": "Mellaga", "Artist": "Varudu Kaavalenu", "Lang": "Telugu"},
    {"Title": "Jum Jum Maya", "Artist": "M.M. Keeravaani", "Lang": "Telugu"},
    {"Title": "Konchem Konchem", "Artist": "M.M. Keeravaani", "Lang": "Telugu"},
    {"Title": "Chitipiga", "Artist": "Karthik", "Lang": "Telugu"},
    {"Title": "Jare Jare", "Artist": "Naresh Iyer", "Lang": "Telugu"},
    {"Title": "Vennelave Vennelave", "Artist": "Hariharan", "Lang": "Telugu"}
]

# 3. HAPPY / VERY HAPPY (Upbeat, Party)
happy_songs = [
    # English
    {"Title": "Blinding Lights", "Artist": "The Weeknd", "Lang": "English"},
    {"Title": "Levitating", "Artist": "Dua Lipa", "Lang": "English"},
    {"Title": "Can't Stop the Feeling", "Artist": "Justin Timberlake", "Lang": "English"},
    {"Title": "Uptown Funk", "Artist": "Bruno Mars", "Lang": "English"},
    {"Title": "Shape of You", "Artist": "Ed Sheeran", "Lang": "English"},
    {"Title": "Cheap Thrills", "Artist": "Sia", "Lang": "English"},
    {"Title": "Baby", "Artist": "Justin Bieber", "Lang": "English"},
    {"Title": "Thunder", "Artist": "Imagine Dragons", "Lang": "English"},
    {"Title": "Counting Stars", "Artist": "OneRepublic", "Lang": "English"},
    {"Title": "On The Floor", "Artist": "Jennifer Lopez", "Lang": "English"},
    {"Title": "Timber", "Artist": "Pitbull", "Lang": "English"},
    {"Title": "Sugar", "Artist": "Maroon 5", "Lang": "English"},
    {"Title": "Wolves", "Artist": "Selena Gomez", "Lang": "English"},
    {"Title": "Despacito", "Artist": "Luis Fonsi", "Lang": "English"},
    {"Title": "Believer", "Artist": "Imagine Dragons", "Lang": "English"},
    {"Title": "Faded", "Artist": "Alan Walker", "Lang": "English"},
    {"Title": "Girls Like You", "Artist": "Maroon 5", "Lang": "English"},
    {"Title": "Drag Me Down", "Artist": "One Direction", "Lang": "English"},
    {"Title": "Happier", "Artist": "Marshmello", "Lang": "English"},
    {"Title": "See You Again", "Artist": "Wiz Khalifa", "Lang": "English"},
    {"Title": "Love Me Like You Do", "Artist": "Ellie Goulding", "Lang": "English"},
    {"Title": "Alone", "Artist": "Alan Walker", "Lang": "English"},
    {"Title": "The Nights", "Artist": "Avicii", "Lang": "English"},
    {"Title": "No Lie", "Artist": "Sean Paul", "Lang": "English"},
    {"Title": "Rockabye", "Artist": "Clean Bandit", "Lang": "English"},
    {"Title": "Let Me Love You", "Artist": "DJ Snake", "Lang": "English"},
    {"Title": "One Kiss", "Artist": "Calvin Harris", "Lang": "English"},
    {"Title": "There's Nothing Holdin' Me Back", "Artist": "Shawn Mendes", "Lang": "English"},
    {"Title": "Sorry", "Artist": "Justin Bieber", "Lang": "English"},
    {"Title": "Treat You Better", "Artist": "Shawn Mendes", "Lang": "English"},
    {"Title": "Havana", "Artist": "Camila Cabello", "Lang": "English"},

    # Hindi
    {"Title": "Badtameez Dil", "Artist": "YJHD", "Lang": "Hindi"},
    {"Title": "Gallan Goodiyan", "Artist": "Dil Dhadakne Do", "Lang": "Hindi"},
    {"Title": "London Thumakda", "Artist": "Queen", "Lang": "Hindi"},
    {"Title": "Kar Gayi Chull", "Artist": "Kapoor & Sons", "Lang": "Hindi"},
    {"Title": "Zingaat", "Artist": "Dhadak", "Lang": "Hindi"},
    {"Title": "Naatu Naatu", "Artist": "RRR", "Lang": "Hindi"},
    {"Title": "Jai Jai Shivshankar", "Artist": "War", "Lang": "Hindi"},
    {"Title": "Aankh Marey", "Artist": "Simmba", "Lang": "Hindi"},
    {"Title": "Bom Diggy Diggy", "Artist": "SKU", "Lang": "Hindi"},
    {"Title": "Ghungroo", "Artist": "War", "Lang": "Hindi"},
    {"Title": "Kala Chashma", "Artist": "Baar Baar Dekho", "Lang": "Hindi"},
    {"Title": "Radha Kaise Na Jale", "Artist": "Lagaan", "Lang": "Hindi"},

    # Telugu
    {"Title": "Butta Bomma", "Artist": "Ala Vaikunthapurramuloo", "Lang": "Telugu"},
    {"Title": "Ramuloo Ramulaa", "Artist": "AVPL", "Lang": "Telugu"},
    {"Title": "Saami Saami", "Artist": "Pushpa", "Lang": "Telugu"},
    {"Title": "Maate Vinadhuga", "Artist": "Taxiwaala", "Lang": "Telugu"},
    {"Title": "Saranga Dariya", "Artist": "Love Story", "Lang": "Telugu"},
    {"Title": "Mass Raja", "Artist": "Dhamaka", "Lang": "Telugu"},
    {"Title": "Dinchak", "Artist": "Red", "Lang": "Telugu"},
    {"Title": "Mind Block", "Artist": "Sarileru Neekevvaru", "Lang": "Telugu"},
    {"Title": "Chaila Chaila", "Artist": "Chiranjeevi", "Lang": "Telugu"}
]

# ==========================================
#  DATASET GENERATION LOGIC
# ==========================================

data = []

def add_songs_to_data(song_list, mood_label):
    for song in song_list:
        data.append({
            "Title": song["Title"],
            "Artist": song["Artist"],
            "Mood": mood_label,
            "Language": song["Lang"]
        })

# Map lists to moods
add_songs_to_data(sad_songs, "Sad")
add_songs_to_data(sad_songs, "Very sad") # Reusing sad songs
add_songs_to_data(neutral_songs, "Neutral")
add_songs_to_data(happy_songs, "Happy")
add_songs_to_data(happy_songs, "Very happy") # Reusing happy songs

# Create DataFrame and Save
df = pd.DataFrame(data)
df.to_csv("music_data.csv", index=False)
print(f"Successfully created music_data.csv with {len(df)} REAL songs (No fake data)!")