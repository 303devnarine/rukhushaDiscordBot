import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
from time import sleep
import random
from inspirational_quotes import quote
from threading import Thread
from flask import Flask
from enum import Enum

load_dotenv()
token = os.getenv("DISCORD_TOKEN")

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()

intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="r.", owner_id=916816688186527844, intents=intents)

# Flask app for health checks
app = Flask(__name__)

@app.route('/')
def home():
   return "<h1> Discord bot is running! </h1>", 200

@app.route('/health')
def health():
   return "OK", 200

def run_flask():
   port = int(os.getenv("PORT", 15500))
   app.run(host='0.0.0.0', port=port)

@bot.event
async def on_ready():
   print(f"{bot.user} is online")
   await bot.tree.sync()
   await interaction.response.send_message("well well well. look who came.")

@bot.event
async def on_message(message):
   if message.author != bot.user:
      await interaction.response.send_message(":")
      return

   await bot.process_commands(message)

@bot.tree.command(name="coinflip", description="Flips a coin.")
async def coinflip(interaction: discord.Interaction):
   username = interaction.user.mention
   await interaction.response.send_message(f"{username}, the coin landed on {"Heads" if random.randint(0, 1) == 0 else "Tails"}.")

@bot.tree.command(name="inspirational_quote", description="Sends you an inspiration quote!")
async def inspirational_quote(interaction: discord.Interaction):
   q = quote()
   await interaction.response.send_message(f"*{q['quote']}*\n{q['author']}")

class Suit(Enum):
    MAJOR_ARCANA = "MAJOR ARCANA"
    WANDS = "WANDS"
    CUPS = "CUPS"
    SWORDS = "SWORDS"
    PENTACLES = "PENTACLES"

cards = [
	(0,  "The Fool",           Suit.MAJOR_ARCANA, "New beginnings, spontaneity, a free spirit",         "Recklessness, risk-taking, inconsideration"),
 	(1,  "The Magician",       Suit.MAJOR_ARCANA, "Willpower, resourcefulness, skill",                  "Manipulation, poor planning, untapped talents"),
	(2,  "The High Priestess", Suit.MAJOR_ARCANA, "Intuition, sacred knowledge, the subconscious",      "Secrets, disconnected intuition, withdrawal"),
	(3,  "The Empress",        Suit.MAJOR_ARCANA, "Femininity, beauty, nature, abundance",              "Creative block, dependence, smothering"),
	(4,  "The Emperor",        Suit.MAJOR_ARCANA, "Authority, structure, stability, fatherhood",        "Domination, rigidity, inflexibility"),
	(5,  "The Hierophant",     Suit.MAJOR_ARCANA, "Tradition, conformity, spiritual guidance",          "Rebellion, unconventionality, subversiveness"),
	(6,  "The Lovers",         Suit.MAJOR_ARCANA, "Love, harmony, alignment of values",                 "Disharmony, imbalance, misalignment of values"),
	(7,  "The Chariot",        Suit.MAJOR_ARCANA, "Control, willpower, victory, determination",         "Lack of control, aggression, no direction"),
	(8,  "Strength",           Suit.MAJOR_ARCANA, "Courage, patience, inner strength, compassion",      "Self-doubt, weakness, insecurity"),
	(9,  "The Hermit",         Suit.MAJOR_ARCANA, "Soul-searching, introspection, solitude",            "Isolation, loneliness, withdrawal"),
	(10, "Wheel of Fortune",   Suit.MAJOR_ARCANA, "Good luck, karma, life cycles, turning point",       "Bad luck, resistance to change, breaking cycles"),
	(11, "Justice",            Suit.MAJOR_ARCANA, "Fairness, truth, cause and effect, law",             "Unfairness, dishonesty, lack of accountability"),
	(12, "The Hanged Man",     Suit.MAJOR_ARCANA, "Surrender, new perspectives, pause",                 "Stalling, needless sacrifice, fear of change"),
	(13, "Death",              Suit.MAJOR_ARCANA, "Endings, change, transformation, transition",        "Resistance to change, stagnation, decay"),
	(14, "Temperance",         Suit.MAJOR_ARCANA, "Balance, moderation, patience, purpose",             "Imbalance, excess, lack of long-term vision"),
	(15, "The Devil",          Suit.MAJOR_ARCANA, "Materialism, bondage, addiction, shadow self",       "Releasing limiting beliefs, reclaiming power"),
	(16, "The Tower",          Suit.MAJOR_ARCANA, "Sudden upheaval, chaos, revelation",                 "Averting disaster, delaying the inevitable"),
	(17, "The Star",           Suit.MAJOR_ARCANA, "Hope, faith, renewal, serenity",                     "Despair, lack of faith, discouragement"),
	(18, "The Moon",           Suit.MAJOR_ARCANA, "Illusion, fear, the unconscious, confusion",         "Release of fear, unhealthy illusions dispersed"),
	(19, "The Sun",            Suit.MAJOR_ARCANA, "Joy, success, positivity, vitality",                 "Negativity, depression, sadness, blocked happiness"),
	(20, "Judgement",         Suit.MAJOR_ARCANA, "Reflection, reckoning, inner calling, absolution",   "Self-doubt, refusal of self-examination, indecision"),
	(21, "The World",          Suit.MAJOR_ARCANA, "Completion, integration, accomplishment, wholeness", "Incompletion, shortcuts, delayed success"),
	(22, "Ace of Wands",       Suit.WANDS, "Inspiration, new opportunities, growth, potential",  "Delays, lack of motivation, setbacks"),
	(23, "Two of Wands",       Suit.WANDS, "Future planning, progress, decisions",               "Fear of unknown, lack of planning, playing safe"),
	(24, "Three of Wands",     Suit.WANDS, "Expansion, foresight, overseas opportunities",       "Lack of foresight, obstacles, delays"),
	(25, "Four of Wands",      Suit.WANDS, "Celebration, harmony, marriage, community",          "Instability, lack of teamwork, conflict"),
	(26, "Five of Wands",      Suit.WANDS, "Conflict, competition, tension, diversity",          "Avoiding conflict, respecting differences"),
	(27, "Six of Wands",       Suit.WANDS, "Success, public reward, progress, pride",            "Egotism, disrepute, lack of recognition"),
	(28, "Seven of Wands",     Suit.WANDS, "Challenge, competition, perseverance, defense",      "Giving up, overwhelmed, yielding"),
	(29, "Eight of Wands",     Suit.WANDS, "Swiftness, action, air travel, movement",            "Delays, frustration, losing momentum"),
	(30, "Nine of Wands",      Suit.WANDS, "Resilience, persistence, last stand, test of faith", "Stubbornness, rigidity, on guard"),
	(31, "Ten of Wands",       Suit.WANDS, "Burden, responsibility, hard work, completion",      "Doing it all alone, carrying too much, collapse"),
	(32, "Page of Wands",      Suit.WANDS, "Exploration, excitement, freedom, adventure",        "Setbacks, lack of direction, hasty decisions"),
	(33, "Knight of Wands",    Suit.WANDS, "Energy, passion, adventure, impulsiveness",          "Haste, scattered energy, delays, frustration"),
	(34, "Queen of Wands",     Suit.WANDS, "Courage, confidence, independence, social butterfly","Selfishness, jealousy, insecurities"),
	(35, "King of Wands",      Suit.WANDS, "Natural-born leader, vision, entrepreneur, honor",   "Impulsiveness, haste, ruthlessness"),
	(36, "Ace of Cups",        Suit.CUPS, "New feelings, spirituality, intuition, love",        "Emotional loss, blocked creativity, emptiness"),
	(37, "Two of Cups",        Suit.CUPS, "Unified love, partnership, mutual attraction",       "Disharmony, distrust, imbalance in relationship"),
	(38, "Three of Cups",      Suit.CUPS, "Celebration, friendship, creativity, community",     "Overindulgence, gossip, isolation"),
	(39, "Four of Cups",       Suit.CUPS, "Meditation, contemplation, apathy, reevaluation",    "Retreat, withdrawal, missed opportunity"),
	(40, "Five of Cups",       Suit.CUPS, "Regret, failure, disappointment, pessimism",         "Acceptance, moving on, finding peace"),
	(41, "Six of Cups",        Suit.CUPS, "Revisiting the past, childhood memories, innocence", "Living in the past, naivety, unrealistic"),
	(42, "Seven of Cups",      Suit.CUPS, "Illusion, fantasy, wishful thinking, choices",       "Alignment, personal values, reality check"),
	(43, "Eight of Cups",      Suit.CUPS, "Walking away, disillusionment, abandonment",         "Fear of moving on, stagnation, avoidance"),
	(44, "Nine of Cups",       Suit.CUPS, "Contentment, satisfaction, gratitude, wish granted", "Inner happiness lacking, materialism, dissatisfaction"),
	(45, "Ten of Cups",        Suit.CUPS, "Divine love, blissful relationships, harmony, family","Broken home, shattered dreams, disconnection"),
	(46, "Page of Cups",       Suit.CUPS, "Creative opportunities, curiosity, possibility",     "Emotional immaturity, insecurity, disappointment"),
	(47, "Knight of Cups",     Suit.CUPS, "Creativity, romance, following the heart",           "Moodiness, disappointment, envy"),
	(48, "Queen of Cups",      Suit.CUPS, "Compassion, calm, comfort, emotional security",      "Martyrdom, insecurity, co-dependence"),
	(49, "King of Cups",       Suit.CUPS, "Emotional balance, compassion, diplomacy",           "Emotional manipulation, moodiness, volatility"),
	(50, "Ace of Swords",      Suit.SWORDS, "Breakthroughs, clarity, sharp mind, truth",          "Confusion, brutality, chaos"),
	(51, "Two of Swords",      Suit.SWORDS, "Indecision, choices, truce, stalemate",              "Indecision, confusion, information overload"),
	(52, "Three of Swords",    Suit.SWORDS, "Heartbreak, suffering, grief, sorrow",               "Recovery, forgiveness, moving on"),
	(53, "Four of Swords",     Suit.SWORDS, "Rest, recovery, contemplation, passive approach",    "Restlessness, burnout, stress"),
	(54, "Five of Swords",     Suit.SWORDS, "Conflict, defeat, win at all costs, betrayal",       "Reconciliation, making amends, past resentment"),
	(55, "Six of Swords",      Suit.SWORDS, "Transition, change, rite of passage, moving on",     "Resistance to change, unfinished business"),
	(56, "Seven of Swords",    Suit.SWORDS, "Betrayal, deception, getting away with something",   "Imposter syndrome, confession, coming clean"),
	(57, "Eight of Swords",    Suit.SWORDS, "Negative thoughts, self-imposed restriction, victim","Open to new perspectives, release, freedom"),
	(58, "Nine of Swords",     Suit.SWORDS, "Anxiety, worry, fear, depression, nightmares",       "Inner turmoil, releasing worry, despairing"),
	(59, "Ten of Swords",      Suit.SWORDS, "Painful endings, deep wounds, back-stabbing",        "Recovery, regeneration, resisting an end"),
	(60, "Page of Swords",     Suit.SWORDS, "New ideas, curiosity, vigilance, thirst for knowledge","All talk no action, deception, haste"),
	(61, "Knight of Swords",   Suit.SWORDS, "Ambitious, action-oriented, driven, fast-thinking",  "Restless, unfocused, impulsive, burn-out"),
	(62, "Queen of Swords",    Suit.SWORDS, "Independent, unbiased judgement, clear boundaries",  "Overly emotional, cold-heartedness, bitterness"),
	(63, "King of Swords",     Suit.SWORDS, "Mental clarity, intellectual power, authority, truth","Quiet power, inner truth, misuse of power"),
	(64, "Ace of Pentacles",   Suit.PENTACLES, "New financial opportunity, manifestation, abundance","Lost opportunity, lack of planning, scarcity"),
	(65, "Two of Pentacles",   Suit.PENTACLES, "Multiple priorities, time management, adaptability", "Overwhelmed, disorganized, juggling too much"),
	(66, "Three of Pentacles", Suit.PENTACLES, "Teamwork, collaboration, learning, implementation",  "Lack of teamwork, disorganized, misalignment"),
	(67, "Four of Pentacles",  Suit.PENTACLES, "Saving money, security, conservatism, scarcity",     "Greed, materialism, self-protection, insecurity"),
	(68, "Five of Pentacles",  Suit.PENTACLES, "Financial loss, poverty, lack mindset, isolation",   "Recovery from loss, spiritual poverty, forgiveness"),
	(69, "Six of Pentacles",   Suit.PENTACLES, "Giving, receiving, charity, generosity, sharing",    "Debt, self-care, strings attached, power dynamics"),
	(70, "Seven of Pentacles", Suit.PENTACLES, "Long-term vision, sustainable results, patience",    "Lack of long-term vision, no reward for work"),
	(71, "Eight of Pentacles", Suit.PENTACLES, "Apprenticeship, skill development, diligence",       "Self-development, perfectionism, misdirected energy"),
	(72, "Nine of Pentacles",  Suit.PENTACLES, "Abundance, luxury, self-sufficiency, refinement",    "Financial setbacks, over-investment, superficiality"),
	(73, "Ten of Pentacles",   Suit.PENTACLES, "Wealth, financial security, family, long-term success","Financial failure, loneliness, loss of stability"),
	(74, "Page of Pentacles",  Suit.PENTACLES, "Manifestation, financial opportunity, new beginnings","Lack of progress, procrastination, learn from failure"),
	(75, "Knight of Pentacles",Suit.PENTACLES, "Hard work, productivity, routine, conservatism",     "Laziness, boredom, feeling stuck"),
	(76, "Queen of Pentacles", Suit.PENTACLES, "Nurturing, practical, providing financially, warmth", "Financial independence, self-care, work-home conflict"),
	(77, "King of Pentacles",  Suit.PENTACLES, "Wealth, business, leadership, security, discipline",  "Financially inept, obsessed with wealth, stubborn"),
]

@bot.tree.command(name="tarot", description="Sends you a random tarot card, with its meaning.")
async def tarot(interaction: discord.Interaction):
   card = cards[random.randint(0,77)]
   await interaction.response.send_message(f"{card}")

if __name__ == "__main__":
   # Start Flask server in a separate thread
   flask_thread = Thread(target=run_flask)
   flask_thread.daemon = True
   flask_thread.start()

   # Start Discord bot
   bot.run(token, log_handler=handler, log_level=logging.DEBUG)
