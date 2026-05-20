from dataclasses import dataclass
from enum import Enum
import random

class Suit(Enum):
    MAJOR_ARCANA = "MAJOR ARCANA"
    WANDS = "WANDS"
    CUPS = "CUPS"
    SWORDS = "SWORDS"
    PENTACLES = "PENTACLES"

@dataclass(frozen=True)
class Card:
    id: int
    name: str
    suit: Suit
    upright: str
    reversed: str

class TarotDeck:
    cards = [
        Card(0,  "The Fool",           Suit.MAJOR_ARCANA, "New beginnings, spontaneity, a free spirit",         "Recklessness, risk-taking, inconsideration"),
        Card(1,  "The Magician",       Suit.MAJOR_ARCANA, "Willpower, resourcefulness, skill",                  "Manipulation, poor planning, untapped talents"),
        Card(2,  "The High Priestess", Suit.MAJOR_ARCANA, "Intuition, sacred knowledge, the subconscious",      "Secrets, disconnected intuition, withdrawal"),
        Card(3,  "The Empress",        Suit.MAJOR_ARCANA, "Femininity, beauty, nature, abundance",              "Creative block, dependence, smothering"),
        Card(4,  "The Emperor",        Suit.MAJOR_ARCANA, "Authority, structure, stability, fatherhood",        "Domination, rigidity, inflexibility"),
        Card(5,  "The Hierophant",     Suit.MAJOR_ARCANA, "Tradition, conformity, spiritual guidance",          "Rebellion, unconventionality, subversiveness"),
        Card(6,  "The Lovers",         Suit.MAJOR_ARCANA, "Love, harmony, alignment of values",                 "Disharmony, imbalance, misalignment of values"),
        Card(7,  "The Chariot",        Suit.MAJOR_ARCANA, "Control, willpower, victory, determination",         "Lack of control, aggression, no direction"),
        Card(8,  "Strength",           Suit.MAJOR_ARCANA, "Courage, patience, inner strength, compassion",      "Self-doubt, weakness, insecurity"),
        Card(9,  "The Hermit",         Suit.MAJOR_ARCANA, "Soul-searching, introspection, solitude",            "Isolation, loneliness, withdrawal"),
        Card(10, "Wheel of Fortune",    Suit.MAJOR_ARCANA, "Good luck, karma, life cycles, turning point",       "Bad luck, resistance to change, breaking cycles"),
        Card(11, "Justice",            Suit.MAJOR_ARCANA, "Fairness, truth, cause and effect, law",             "Unfairness, dishonesty, lack of accountability"),
        Card(12, "The Hanged Man",     Suit.MAJOR_ARCANA, "Surrender, new perspectives, pause",                 "Stalling, needless sacrifice, fear of change"),
        Card(13, "Death",              Suit.MAJOR_ARCANA, "Endings, change, transformation, transition",        "Resistance to change, stagnation, decay"),
        Card(14, "Temperance",         Suit.MAJOR_ARCANA, "Balance, moderation, patience, purpose",             "Imbalance, excess, lack of long-term vision"),
        Card(15, "The Devil",          Suit.MAJOR_ARCANA, "Materialism, bondage, addiction, shadow self",       "Releasing limiting beliefs, reclaiming power"),
        Card(16, "The Tower",          Suit.MAJOR_ARCANA, "Sudden upheaval, chaos, revelation",                 "Averting disaster, delaying the inevitable"),
        Card(17, "The Star",           Suit.MAJOR_ARCANA, "Hope, faith, renewal, serenity",                     "Despair, lack of faith, discouragement"),
        Card(18, "The Moon",           Suit.MAJOR_ARCANA, "Illusion, fear, the unconscious, confusion",         "Release of fear, unhealthy illusions dispersed"),
        Card(19, "The Sun",            Suit.MAJOR_ARCANA, "Joy, success, positivity, vitality",                 "Negativity, depression, sadness, blocked happiness"),
        Card(20, "Judgement",          Suit.MAJOR_ARCANA, "Reflection, reckoning, inner calling, absolution",   "Self-doubt, refusal of self-examination, indecision"),
        Card(21, "The World",          Suit.MAJOR_ARCANA, "Completion, integration, accomplishment, wholeness", "Incompletion, shortcuts, delayed success"),
        Card(22, "Ace of Wands",       Suit.WANDS, "Inspiration, new opportunities, growth, potential",  "Delays, lack of motivation, setbacks"),
        Card(23, "Two of Wands",       Suit.WANDS, "Future planning, progress, decisions",               "Fear of unknown, lack of planning, playing safe"),
        Card(24, "Three of Wands",     Suit.WANDS, "Expansion, foresight, overseas opportunities",       "Lack of foresight, obstacles, delays"),
        Card(25, "Four of Wands",      Suit.WANDS, "Celebration, harmony, marriage, community",          "Instability, lack of teamwork, conflict"),
        Card(26, "Five of Wands",      Suit.WANDS, "Conflict, competition, tension, diversity",          "Avoiding conflict, respecting differences"),
        Card(27, "Six of Wands",       Suit.WANDS, "Success, public reward, progress, pride",            "Egotism, disrepute, lack of recognition"),
        Card(28, "Seven of Wands",     Suit.WANDS, "Challenge, competition, perseverance, defense",      "Giving up, overwhelmed, yielding"),
        Card(29, "Eight of Wands",     Suit.WANDS, "Swiftness, action, air travel, movement",            "Delays, frustration, losing momentum"),
        Card(30, "Nine of Wands",      Suit.WANDS, "Resilience, persistence, last stand, test of faith", "Stubbornness, rigidity, on guard"),
        Card(31, "Ten of Wands",       Suit.WANDS, "Burden, responsibility, hard work, completion",      "Doing it all alone, carrying too much, collapse"),
        Card(32, "Page of Wands",      Suit.WANDS, "Exploration, excitement, freedom, adventure",        "Setbacks, lack of direction, hasty decisions"),
        Card(33, "Knight of Wands",    Suit.WANDS, "Energy, passion, adventure, impulsiveness",          "Haste, scattered energy, delays, frustration"),
        Card(34, "Queen of Wands",     Suit.WANDS, "Courage, confidence, independence, social butterfly","Selfishness, jealousy, insecurities"),
        Card(35, "King of Wands",      Suit.WANDS, "Natural-born leader, vision, entrepreneur, honor",   "Impulsiveness, haste, ruthlessness"),
        Card(36, "Ace of Cups",        Suit.CUPS, "New feelings, spirituality, intuition, love",        "Emotional loss, blocked creativity, emptiness"),
        Card(37, "Two of Cups",        Suit.CUPS, "Unified love, partnership, mutual attraction",       "Disharmony, distrust, imbalance in relationship"),
        Card(38, "Three of Cups",      Suit.CUPS, "Celebration, friendship, creativity, community",     "Overindulgence, gossip, isolation"),
        Card(39, "Four of Cups",       Suit.CUPS, "Meditation, contemplation, apathy, reevaluation",    "Retreat, withdrawal, missed opportunity"),
        Card(40, "Five of Cups",       Suit.CUPS, "Regret, failure, disappointment, pessimism",         "Acceptance, moving on, finding peace"),
        Card(41, "Six of Cups",        Suit.CUPS, "Revisiting the past, childhood memories, innocence", "Living in the past, naivety, unrealistic"),
        Card(42, "Seven of Cups",      Suit.CUPS, "Illusion, fantasy, wishful thinking, choices",       "Alignment, personal values, reality check"),
        Card(43, "Eight of Cups",      Suit.CUPS, "Walking away, disillusionment, abandonment",         "Fear of moving on, stagnation, avoidance"),
        Card(44, "Nine of Cups",       Suit.CUPS, "Contentment, satisfaction, gratitude, wish granted", "Inner happiness lacking, materialism, dissatisfaction"),
        Card(45, "Ten of Cups",        Suit.CUPS, "Divine love, blissful relationships, harmony, family","Broken home, shattered dreams, disconnection"),
        Card(46, "Page of Cups",       Suit.CUPS, "Creative opportunities, curiosity, possibility",     "Emotional immaturity, insecurity, disappointment"),
        Card(47, "Knight of Cups",     Suit.CUPS, "Creativity, romance, following the heart",           "Moodiness, disappointment, envy"),
        Card(48, "Queen of Cups",      Suit.CUPS, "Compassion, calm, comfort, emotional security",      "Martyrdom, insecurity, co-dependence"),
        Card(49, "King of Cups",       Suit.CUPS, "Emotional balance, compassion, diplomacy",           "Emotional manipulation, moodiness, volatility"),
        Card(50, "Ace of Swords",      Suit.SWORDS, "Breakthroughs, clarity, sharp mind, truth",          "Confusion, brutality, chaos"),
        Card(51, "Two of Swords",      Suit.SWORDS, "Indecision, choices, truce, stalemate",              "Indecision, confusion, information overload"),
        Card(52, "Three of Swords",    Suit.SWORDS, "Heartbreak, suffering, grief, sorrow",               "Recovery, forgiveness, moving on"),
        Card(53, "Four of Swords",     Suit.SWORDS, "Rest, recovery, contemplation, passive approach",    "Restlessness, burnout, stress"),
        Card(54, "Five of Swords",     Suit.SWORDS, "Conflict, defeat, win at all costs, betrayal",       "Reconciliation, making amends, past resentment"),
        Card(55, "Six of Swords",      Suit.SWORDS, "Transition, change, rite of passage, moving on",     "Resistance to change, unfinished business"),
        Card(56, "Seven of Swords",    Suit.SWORDS, "Betrayal, deception, getting away with something",   "Imposter syndrome, confession, coming clean"),
        Card(57, "Eight of Swords",    Suit.SWORDS, "Negative thoughts, self-imposed restriction, victim","Open to new perspectives, release, freedom"),
        Card(58, "Nine of Swords",     Suit.SWORDS, "Anxiety, worry, fear, depression, nightmares",       "Inner turmoil, releasing worry, despairing"),
        Card(59, "Ten of Swords",      Suit.SWORDS, "Painful endings, deep wounds, back-stabbing",        "Recovery, regeneration, resisting an end"),
        Card(60, "Page of Swords",     Suit.SWORDS, "New ideas, curiosity, vigilance, thirst for knowledge","All talk no action, deception, haste"),
        Card(61, "Knight of Swords",   Suit.SWORDS, "Ambitious, action-oriented, driven, fast-thinking",  "Restless, unfocused, impulsive, burn-out"),
        Card(62, "Queen of Swords",    Suit.SWORDS, "Independent, unbiased judgement, clear boundaries",  "Overly emotional, cold-heartedness, bitterness"),
        Card(63, "King of Swords",     Suit.SWORDS, "Mental clarity, intellectual power, authority, truth","Quiet power, inner truth, misuse of power"),
        Card(64, "Ace of Pentacles",   Suit.PENTACLES, "New financial opportunity, manifestation, abundance","Lost opportunity, lack of planning, scarcity"),
        Card(65, "Two of Pentacles",   Suit.PENTACLES, "Multiple priorities, time management, adaptability", "Overwhelmed, disorganized, juggling too much"),
        Card(66, "Three of Pentacles", Suit.PENTACLES, "Teamwork, collaboration, learning, implementation",  "Lack of teamwork, disorganized, misalignment"),
        Card(67, "Four of Pentacles",  Suit.PENTACLES, "Saving money, security, conservatism, scarcity",     "Greed, materialism, self-protection, insecurity"),
        Card(68, "Five of Pentacles",  Suit.PENTACLES, "Financial loss, poverty, lack mindset, isolation",   "Recovery from loss, spiritual poverty, forgiveness"),
        Card(69, "Six of Pentacles",   Suit.PENTACLES, "Giving, receiving, charity, generosity, sharing",    "Debt, self-care, strings attached, power dynamics"),
        Card(70, "Seven of Pentacles", Suit.PENTACLES, "Long-term vision, sustainable results, patience",    "Lack of long-term vision, no reward for work"),
        Card(71, "Eight of Pentacles", Suit.PENTACLES, "Apprenticeship, skill development, diligence",       "Self-development, perfectionism, misdirected energy"),
        Card(72, "Nine of Pentacles",  Suit.PENTACLES, "Abundance, luxury, self-sufficiency, refinement",    "Financial setbacks, over-investment, superficiality"),
        Card(73, "Ten of Pentacles",   Suit.PENTACLES, "Wealth, financial security, family, long-term success","Financial failure, loneliness, loss of stability"),
        Card(74, "Page of Pentacles",  Suit.PENTACLES, "Manifestation, financial opportunity, new beginnings","Lack of progress, procrastination, learn from failure"),
        Card(75, "Knight of Pentacles", Suit.PENTACLES, "Hard work, productivity, routine, conservatism",     "Laziness, boredom, feeling stuck"),
        Card(76, "Queen of Pentacles", Suit.PENTACLES, "Nurturing, practical, providing financially, warmth", "Financial independence, self-care, work-home conflict"),
        Card(77, "King of Pentacles",  Suit.PENTACLES, "Wealth, business, leadership, security, discipline",  "Financially inept, obsessed with wealth, stubborn"),
    ]

def drawCard():
    card = random.choice(TarotDeck.cards)
    is_reversed = random.randint(0, 1) == 1
    meaning = card.reversed if is_reversed else card.upright
    return {"id": card.id, "name": f"{card.name} {"Reversed" if is_reversed else "Upright"}", "suit": card.suit, "meaning": meaning}
