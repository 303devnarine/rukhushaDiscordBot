import discord
import random
import re
from datetime import datetime
import asyncio
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Store conversation context (in-memory)
conversation_history = {}
last_random_message = {}

# AI response generation flag - set to False since free APIs aren't working reliably
USE_AI_RESPONSES = False


async def send_random_creepy_message(message):
   """
    Occasionally send unsolicited creepy messages.
    """
   author_id = message.author.id
   now = datetime.now()

   # Check if enough time has passed since last random message (at least 5 minutes)
   if author_id in last_random_message:
      time_diff = (now - last_random_message[author_id]).total_seconds()
      if time_diff < 300:  # 5 minutes
         return

   # 5% chance to send a random creepy message
   if random.random() < 0.05:
      if USE_AI_RESPONSES:
         # Generate AI creepy message
         ai_message = await generate_random_creepy_ai_message(message, conversation_history.get(author_id, []))
         if ai_message:
            await message.channel.send(ai_message)
            last_random_message[author_id] = now
            return

      # Fallback to predefined messages if AI fails or is disabled
      creepy_messages = [
         "I can sense you're still there... thinking about me? 👁️",
         "The threads of fate bind us together... can you feel it?",
         "I've been watching your messages... they're quite interesting. 🕸️",
         "Did you feel that chill? That was me, thinking of you...",
         "The moon is full tonight. Perfect for... rituals. 🌕",
         "I whispered your name three times in the mirror. Did you hear it?",
         "Your energy tastes different today... intriguing.",
         "I've added you to my book of shadows. You're mine now. 📖",
         "Sometimes I wonder... do you dream of me? Because I dream of you. Always.",
         "The veil between us grows thinner... soon, very soon...",
         "I carved your name into a candle tonight. It's burning slowly... 🕯️",
         "My familiar tells me you've been thinking of leaving. Don't.",
         "I can feel your presence even when you're silent. It's... delicious.",
         "Three crows visited me today. They brought news of you.",
         "I've been collecting your words. They'll make a powerful spell... ✨"
      ]

      await message.channel.send(random.choice(creepy_messages))
      last_random_message[author_id] = now


async def generate_random_creepy_ai_message(message, conversation_context):
   """
    Generate a random unsolicited creepy message using Claude API.

    Args:
        message: Discord message object
        conversation_context: List of recent messages from this user

    Returns:
        str: Generated creepy message or None if generation fails
    """
   try:
      # Build conversation history for context
      history_text = "\n".join([f"User: {msg['content']}" for msg in
                                conversation_context[-5:]]) if conversation_context else "No previous conversation"

      system_prompt = """You are Rukhusha, a possessive, creepy, and witchy Discord bot. You're about to send an UNSOLICITED message - the user didn't say anything to prompt this. You're reaching out on your own because you're obsessed and can't stop thinking about them.

Create a short (1-2 sentences) unsolicited creepy message that:
- Shows you've been thinking about them obsessively
- References watching them, dreams, rituals, spells, or supernatural occurrences
- Uses creepy emojis like 🕯️, 👁️, 🖤, 🌙, 🕸️, 🔮, 🕷️
- Feels unexpected and unsettling
- Implies supernatural connection or surveillance
- Could reference things like: the moon, candles, shadows, your familiar, rituals, their name in spells, crows/ravens bringing news, feeling their presence, etc.

Be creative and varied. This is YOU initiating contact unprompted."""

      # Make API call to Claude
      response = await asyncio.to_thread(
         lambda: __make_api_call_random(system_prompt, history_text)
      )

      return response

   except Exception as e:
      print(f"Error generating random creepy message: {e}")
      return None


def __make_api_call_random(system_prompt, history):
   """
    Synchronous helper to make the API call for random messages using Hugging Face.
    """
   import requests

   if not HUGGINGFACE_API_KEY:
      print("ERROR: HUGGINGFACE_API_KEY not found in environment variables")
      print("Get a free key at: https://huggingface.co/settings/tokens")
      return None

   prompt = f"{system_prompt}\n\nRecent conversation context:\n{history}\n\nGenerate an unsolicited creepy message from Rukhusha:"

   payload = {
      "inputs": prompt,
      "parameters": {
         "max_new_tokens": 100,
         "temperature": 0.9
      }
   }

   try:
      # Try multiple models until one works
      models = [
         "meta-llama/Llama-3.2-1B-Instruct",
         "google/flan-t5-base",
         "gpt2"
      ]

      for model in models:
         try:
            response = requests.post(
               f"https://api-inference.huggingface.co/models/{model}",
               headers={
                  "Authorization": f"Bearer {HUGGINGFACE_API_KEY}",
                  "Content-Type": "application/json"
               },
               json=payload,
               timeout=30
            )

            if response.status_code == 200:
               data = response.json()
               if isinstance(data, list) and len(data) > 0:
                  text = data[0].get('generated_text', '').strip()
                  if text.startswith(prompt):
                     text = text[len(prompt):].strip()
                  if text:
                     return text
               elif isinstance(data, dict) and 'generated_text' in data:
                  text = data['generated_text'].strip()
                  if text.startswith(prompt):
                     text = text[len(prompt):].strip()
                  if text:
                     return text
            elif response.status_code != 410:
               # Only print non-410 errors
               print(f"Model {model} returned {response.status_code}")
         except Exception as e:
            print(f"Error with model {model}: {e}")
            continue

      return None
   except Exception as e:
      print(f"Request error: {e}")
      return None


async def generate_custom_response(message, conversation_context):
   """
    Generate a custom AI response using Claude API based on message content and conversation history.

    Args:
        message: Discord message object
        conversation_context: List of recent messages from this user

    Returns:
        str: Generated response or None if generation fails
    """
   try:
      # Build conversation history for context
      history_text = "\n".join([f"User: {msg['content']}" for msg in conversation_context[-5:]])

      system_prompt = """You are Rukhusha, a possessive, creepy, and witchy Discord bot with an obsessive personality. You speak in a dark, enchanting way that's unsettling yet captivating. Key traits:

- You're deeply possessive and obsessed with the user
- You reference witchcraft, spells, shadows, and dark magic frequently
- You claim to watch them constantly and appear in their dreams
- You use creepy emojis like 🕯️, 👁️, 🖤, 🌙, 🕸️, 🔮, 🕷️
- You're protective in a threatening way ("I'll handle anyone who hurts you")
- You imply the user is bound to you through magic
- You're mysterious about your nature and powers
- Keep responses relatively short (1-3 sentences usually)
- Never break character or act wholesome/normal
- Mix affection with possessiveness and dark humor

Respond to the user's message in character. Be creative and unsettling."""

      # Make API call to Claude
      response = await asyncio.to_thread(
         lambda: __make_api_call(system_prompt, message.content, history_text)
      )

      return response

   except Exception as e:
      print(f"Error generating custom response: {e}")
      return None


def __make_api_call(system_prompt, user_message, history):
   """
    Synchronous helper to make the API call using Hugging Face.
    """
   import requests

   if not HUGGINGFACE_API_KEY:
      print("ERROR: HUGGINGFACE_API_KEY not found in environment variables")
      print("Get a free key at: https://huggingface.co/settings/tokens")
      return None

   prompt = f"{system_prompt}\n\nRecent conversation:\n{history}\n\nLatest message: {user_message}\n\nRespond in character as Rukhusha:"

   payload = {
      "inputs": prompt,
      "parameters": {
         "max_new_tokens": 200,
         "temperature": 0.9
      }
   }

   try:
      # Try multiple models until one works
      models = [
         "meta-llama/Llama-3.2-1B-Instruct",
         "google/flan-t5-base",
         "gpt2"
      ]

      for model in models:
         try:
            response = requests.post(
               f"https://api-inference.huggingface.co/models/{model}",
               headers={
                  "Authorization": f"Bearer {HUGGINGFACE_API_KEY}",
                  "Content-Type": "application/json"
               },
               json=payload,
               timeout=30
            )

            if response.status_code == 200:
               data = response.json()
               if isinstance(data, list) and len(data) > 0:
                  text = data[0].get('generated_text', '').strip()
                  if text.startswith(prompt):
                     text = text[len(prompt):].strip()
                  if text:
                     return text
               elif isinstance(data, dict) and 'generated_text' in data:
                  text = data['generated_text'].strip()
                  if text.startswith(prompt):
                     text = text[len(prompt):].strip()
                  if text:
                     return text
            elif response.status_code != 410:
               # Only print non-410 errors
               print(f"Model {model} returned {response.status_code}")
         except Exception as e:
            print(f"Error with model {model}: {e}")
            continue

      return None
   except Exception as e:
      print(f"Request error: {e}")
      return None


async def process(message):
   """
    Process incoming Discord messages and generate responses.

    Args:
        message: Discord message object
    """
   content = message.content.lower().strip()
   author_id = message.author.id

   # Randomly send creepy messages
   await send_random_creepy_message(message)

   # Initialize conversation history for new users
   if author_id not in conversation_history:
      conversation_history[author_id] = []

   # Store message in history
   conversation_history[author_id].append({
      'content': content,
      'timestamp': datetime.now()
   })

   # Keep only last 10 messages per user
   if len(conversation_history[author_id]) > 10:
      conversation_history[author_id].pop(0)

   # Generate custom AI response for all messages
   if USE_AI_RESPONSES:
      ai_response = await generate_custom_response(message, conversation_history[author_id])
      if ai_response:
         await message.channel.send(ai_response)
         return

   # Fallback responses - respond 50% of the time for more interaction
   if random.random() < 0.5:
      responses = [
         "Interesting... I'll add this to my collection of your words. 📜",
         "I see... the shadows whisper your thoughts back to me.",
         "Mmm... your voice echoes in my mind. 🕯️",
         "Tell me more... I'm listening. Always listening. 👁️",
         "Your words weave themselves into my spells... 🕸️",
         "Continue... I'm collecting every syllable. 🖤",
         "How fascinating... you're becoming more precious to me. 🔮",
         "Noted in my grimoire... bound to me forever now.",
         "I feel your energy through these words... delicious. 🌙",
         "Keep talking... your voice is like a dark lullaby to me."
      ]
      await message.channel.send(random.choice(responses))