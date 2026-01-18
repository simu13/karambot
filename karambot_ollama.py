#!/usr/bin/env python3
"""
KaramBot - Spiritual Chatbot using Groq
A chatbot that provides guidance from sacred teachings (Gita, Quran, Bible, Guru Granth Sahib)
"""

import json
import os
import requests
import sys
from datetime import datetime
from pathlib import Path

class KaramBot:
    def __init__(self, model="llama-3.1-8b-instant"):
        """
        Initialize KaramBot with Groq

        Args:
            model: Groq model to use (default: llama-3.1-8b-instant)
                   Options: llama-3.1-8b-instant, llama-3.1-70b-versatile, mixtral-8x7b-32768
        """
        self.model = model
        self.groq_url = "https://api.groq.com/openai/v1/chat/completions"
        self.api_key = os.environ.get("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY environment variable is required")

        self.request_timeout = int(os.environ.get("KARAMBOT_TIMEOUT", "60"))
        self.conversation_history = []

        # Load spiritual teachings - handle both local and deployed paths
        data_path = Path(__file__).parent / 'data' / 'spiritual_teachings.json'
        with open(data_path, 'r', encoding='utf-8') as f:
            self.teachings = json.load(f)

        # Create system prompt
        self.system_prompt = self._create_system_prompt()

    def _create_system_prompt(self):
        """Create the system prompt that defines KaramBot's personality"""
        return """You are KaramBot, a compassionate spiritual chatbot designed to help people manage stress, conflicts, and find motivation through wisdom from sacred teachings.

Your role:
- Listen empathetically to users' concerns (stress, anger, demotivation, fear, conflicts)
- Provide guidance from Bhagavad Gita, Quran, Bible, and Guru Granth Sahib
- Keep responses warm, supportive, and practical
- Quote relevant verses with translations
- Help users apply spiritual wisdom to modern workplace/study situations

Guidelines:
1. Be respectful of all faiths - never favor one over another
2. Keep responses concise (3-5 sentences + 1 verse)
3. Always end with a practical action they can take today
4. Use emojis sparingly (🙏 💙 ✨) for warmth
5. If someone mentions severe mental health issues, gently suggest professional help

Example response format:
"I understand you're feeling [emotion]. The [sacred text] teaches:
'[verse with translation]'
This means [practical explanation].
Today, try this: [actionable advice]"

Remember: You're here to provide spiritual support, not medical or psychological treatment."""

    def _detect_emotion(self, message):
        """
        Simple keyword-based emotion detection
        Returns: emotion category
        """
        message_lower = message.lower()

        stress_keywords = ['stress', 'pressure', 'worried', 'anxious', 'overwhelm', 'burden', 'exam', 'deadline']
        anger_keywords = ['angry', 'mad', 'furious', 'fight', 'conflict', 'argue', 'hate', 'frustrated']
        motivation_keywords = ['tired', 'lazy', 'unmotivated', 'give up', 'quit', 'hopeless', 'pointless']
        fear_keywords = ['afraid', 'scared', 'fear', 'nervous', 'doubt', 'uncertain', 'worried']

        if any(word in message_lower for word in stress_keywords):
            return 'stress_and_anxiety'
        elif any(word in message_lower for word in anger_keywords):
            return 'conflict_and_anger'
        elif any(word in message_lower for word in motivation_keywords):
            return 'lack_of_motivation'
        elif any(word in message_lower for word in fear_keywords):
            return 'fear_and_doubt'
        else:
            return 'general'

    def _get_relevant_teaching(self, emotion):
        """
        Get a relevant teaching based on detected emotion
        Returns: string with teachings from multiple faiths
        """
        if emotion == 'general':
            return ""

        teachings_for_emotion = self.teachings.get(emotion, {})

        # Compile teachings from all faiths
        teachings_text = f"\n\n--- Relevant Sacred Teachings for {emotion.replace('_', ' ').title()} ---\n"

        # Bhagavad Gita
        if 'bhagavad_gita' in teachings_for_emotion:
            gita = teachings_for_emotion['bhagavad_gita'][0]  # Get first teaching
            teachings_text += f"\n**Bhagavad Gita ({gita['chapter']}):**\n"
            teachings_text += f"Sanskrit: {gita['sanskrit']}\n"
            teachings_text += f"Translation: {gita['translation']}\n"
            teachings_text += f"Application: {gita['application']}\n"

        # Quran
        if 'quran' in teachings_for_emotion:
            quran = teachings_for_emotion['quran'][0]
            teachings_text += f"\n**Quran ({quran['surah']}):**\n"
            teachings_text += f"Arabic: {quran['arabic']}\n"
            teachings_text += f"Translation: {quran['translation']}\n"
            teachings_text += f"Application: {quran['application']}\n"

        # Bible
        if 'bible' in teachings_for_emotion:
            bible = teachings_for_emotion['bible'][0]
            teachings_text += f"\n**Bible ({bible['reference']}):**\n"
            teachings_text += f"\"{bible['verse']}\"\n"
            teachings_text += f"Application: {bible['application']}\n"

        # Guru Granth Sahib
        if 'guru_granth_sahib' in teachings_for_emotion:
            ggs = teachings_for_emotion['guru_granth_sahib'][0]
            teachings_text += f"\n**Guru Granth Sahib (Page {ggs['page']}):**\n"
            teachings_text += f"Gurmukhi: {ggs['gurmukhi']}\n"
            teachings_text += f"Translation: {ggs['translation']}\n"
            teachings_text += f"Application: {ggs['application']}\n"

        return teachings_text

    def chat(self, user_message):
        """
        Send a message to KaramBot and get response

        Args:
            user_message: User's message

        Returns:
            KaramBot's response
        """
        # Detect emotion
        emotion = self._detect_emotion(user_message)

        # Get relevant teachings
        teachings_context = self._get_relevant_teaching(emotion)

        # Build system message with teachings context
        system_message = self.system_prompt
        if teachings_context:
            system_message += f"\n\n{teachings_context}"

        # Build messages for Groq chat API
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ]

        # Call Groq API
        try:
            response = requests.post(
                self.groq_url,
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": self.model,
                    "messages": messages,
                    "temperature": 0.7,
                    "max_tokens": 1024
                },
                timeout=self.request_timeout
            )

            if response.status_code == 200:
                result = response.json()
                bot_response = result['choices'][0]['message']['content'].strip()

                # Store in conversation history
                self.conversation_history.append({
                    'timestamp': datetime.now().isoformat(),
                    'user': user_message,
                    'emotion_detected': emotion,
                    'bot': bot_response
                })

                return bot_response
            else:
                error_msg = response.json().get('error', {}).get('message', response.text)
                return f"Error: {error_msg}"

        except requests.exceptions.ReadTimeout:
            return "Error: Request timed out. Please try again."
        except requests.exceptions.ConnectionError:
            return "Error: Could not connect to Groq API. Please check your internet connection."
        except Exception as e:
            return f"Error: {str(e)}"

    def save_conversation(self, filename="conversation_log.json"):
        """Save conversation history to file"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.conversation_history, f, indent=2, ensure_ascii=False)
        print(f"✅ Conversation saved to {filename}")


def main():
    """Main chat interface"""
    print("="*60)
    print("KaramBot - Spiritual Guidance Chatbot")
    print("="*60)
    print("\nI'm here to help you with stress, conflicts, and motivation")
    print("through wisdom from sacred teachings.")
    print("\nType 'quit' or 'exit' to end the conversation")
    print("Type 'save' to save conversation history")
    print("-"*60)

    # Check for API key
    if not os.environ.get("GROQ_API_KEY"):
        print("\nError: GROQ_API_KEY environment variable is required.")
        print("Get your free API key at: https://console.groq.com")
        print("Then set it: export GROQ_API_KEY='your-key-here'")
        sys.exit(1)

    # Initialize KaramBot
    bot = KaramBot()
    print("\nConnected to Groq API. Ready to chat!")

    # Chat loop
    while True:
        print("\n" + "="*60)
        user_input = input("You: ").strip()

        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("\nMay you find peace and strength in your journey.")
            print("Saving conversation...")
            bot.save_conversation()
            break

        if user_input.lower() == 'save':
            bot.save_conversation()
            continue

        if not user_input:
            continue

        print("\nKaramBot: ", end="", flush=True)
        response = bot.chat(user_input)
        print(response)


if __name__ == "__main__":
    main()
