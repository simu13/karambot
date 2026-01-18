# KaramBot 🙏
**AI-Powered Spiritual Chatbot for Student Stress Management**

---

## Project Overview

**Course:** OB&PPM (Organizational Behavior & People Process Management)
**Objective:** Demonstrate how AI-powered spiritual guidance can help university students manage stress, conflicts, and motivation challenges

KaramBot uses **Machine Learning (RAG architecture)** to provide compassionate guidance from sacred teachings:
- 🕉️ Bhagavad Gita (Hinduism)
- ☪️ Quran (Islam)
- ✝️ Bible (Christianity)
- ⚜️ Guru Granth Sahib (Sikhism)

---

## How It Works

### RAG Architecture (Retrieval-Augmented Generation)

```
User Message: "I'm stressed about my exams"
        ↓
1. Emotion Detection (keyword-based)
        ↓
2. Retrieve Relevant Teachings from spiritual_teachings.json
   (All 4 sacred texts for that emotion)
        ↓
3. Build Context-Rich Prompt
        ↓
4. Llama 3.1 8B Generates Natural Response
        ↓
5. Response includes: Empathy + Sacred Verse + Practical Advice
```

### Example Conversation

**You:** "I'm stressed about my exams. I keep worrying I'll fail."

**KaramBot:**
> I'm so sorry to hear you're feeling stressed about your exams 🙏. Remember, you're not alone in this. The Quran teaches:
>
> "إِنَّ مَعَ الْعُسْرِ يُسْرًا
> Indeed, with hardship comes ease." (94:6)
>
> This means that even in the midst of difficulty, there's always a way out. Today, try this: take 10 minutes to review your study plan and make small adjustments to break it down into manageable chunks. Focus on one subject at a time, and don't be afraid to ask for help when you need it. You got this! 💙

---

## Two Ways to Use KaramBot

### 🌐 Option 1: Web Interface (Recommended ⭐)
Beautiful browser-based chat interface - perfect for demos and user testing!

### 💻 Option 2: Terminal/Command Line
Simple text-based interface for quick testing.

---

## Quick Start (Web Interface) 🌐

### 1. Install Ollama

**Windows (Native):**
1. Download Ollama for Windows from https://ollama.com/download
2. Run the installer (`OllamaSetup.exe`)
3. Ollama will auto-start as a Windows service (runs in background)
4. Verify installation: Open Command Prompt and type `ollama --version`

**Windows (WSL2):**
```bash
# Open WSL2 terminal (Ubuntu)
curl -fsSL https://ollama.com/install.sh | sh
```

**Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**macOS:**
1. Download from https://ollama.com/download
2. Drag Ollama.app to Applications folder
3. Launch Ollama from Applications

### 2. Download Llama 3.1 Model

**Windows (Command Prompt or PowerShell):**
```cmd
ollama pull llama3.1:8b
REM Downloads ~4.7GB (takes 5-15 minutes)
```

**Linux/macOS/WSL:**
```bash
ollama pull llama3.1:8b
# Downloads ~4.7GB (takes 5-15 minutes)
```

### 3. Install Python Dependencies

**Windows (Command Prompt):**
```cmd
cd path\to\karambot
py -m pip install -r requirements.txt
```

**Linux/macOS/WSL:**
```bash
cd /path/to/karambot
pip3 install -r requirements.txt
```

### 4. Start the Web Server

**Windows (Native):**

Ollama is already running as a Windows service (no need for separate terminal).

Open Command Prompt:
```cmd
cd path\to\karambot
python app.py
```

**Windows (WSL2) / Linux / macOS:**

**Terminal 1 (keep running):**
```bash
ollama serve
```

**Terminal 2 (start web server):**
```bash
cd /path/to/karambot
python3 app.py
```

You should see:
```
🙏 KaramBot Web Interface Starting...
📱 Open your browser and go to: http://localhost:5000
```

### 5. Open in Browser

1. Open your browser (Chrome, Firefox, Edge, Safari)
2. Go to: **http://localhost:5000**
3. You should see the KaramBot web interface! 🎉

### 6. Start Chatting

Try these messages in the web chat:
- "I'm stressed about my exams"
- "I'm angry at my roommate"
- "I feel unmotivated to study"
- "I'm afraid of failing"

Click **"Save Chat"** button to save conversations to `web_conversation_log.json`.

---

## Alternative: Terminal/Command Line Interface 💻

If you prefer the simple terminal version:

**Run this instead of app.py:**

```bash
# Windows
python karambot_ollama.py

# Linux/macOS/WSL
python3 karambot_ollama.py
```

Type messages, press Enter. Type `quit` to exit. Conversations save to `conversation_log.json`.

---

## Technical Details

### Tech Stack
- **LLM:** Llama 3.1 8B (Meta, open-source)
- **Runtime:** Ollama (local inference, self-hosted)
- **Architecture:** RAG (Retrieval-Augmented Generation)
- **Knowledge Base:** 23 curated spiritual teachings (JSON)
- **Language:** Python 3.11+

### Why Self-Hosted?
- ✅ No external API calls (no OpenAI/Anthropic)
- ✅ Complete data privacy
- ✅ No per-call costs
- ✅ Learn production ML workflow

### Files Structure

```
karambot/
├── app.py                          # Web interface (Flask server)
├── karambot_ollama.py              # Core chatbot logic (RAG implementation)
├── templates/
│   └── index.html                  # Web chat UI
├── static/
│   └── style.css                   # Web interface styling
├── data/
│   └── spiritual_teachings.json    # Knowledge base (23 teachings)
├── requirements.txt                # Python dependencies (requests, flask)
├── student_feedback_form.md        # Survey template for testing
├── conversation_log.json           # Terminal chat logs
├── web_conversation_log.json       # Web chat logs
└── README.md                       # This file
```

---

## For Your Assignment

### Testing Protocol

1. **Recruit 5-10 students**
2. **Each student:**
   - Chats with KaramBot for 10 minutes
   - Describes a real stress/conflict situation
   - Rates the experience (1-5):
     - Helpfulness
     - Empathy
     - Relevance of advice
     - Would they use it again? (Yes/No)
3. **Collect data:**
   - Use `student_feedback_form.md` template
   - Save conversation logs (auto-saved)
   - Compare results

### Metrics to Report

| Metric | What to Measure |
|--------|----------------|
| **Response Time** | Average seconds per response |
| **Helpfulness** | Avg rating (1-5) |
| **Empathy** | Avg rating (1-5) |
| **Quote Accuracy** | % of responses with proper verse citations |
| **Practical Advice** | % of responses with actionable suggestions |
| **User Satisfaction** | % who would use it again |

### Report Structure

1. **Introduction**
   - Problem: Student stress levels in universities
   - Solution: AI-powered spiritual guidance
   - Technology: RAG with Llama 3.1

2. **Methodology**
   - How KaramBot works (RAG architecture)
   - Testing protocol (n=10 students)
   - Survey questions

3. **Results**
   - Satisfaction scores
   - Example conversations
   - Student feedback quotes

4. **Analysis**
   - What worked well
   - Limitations
   - Suggestions for improvement

5. **Conclusion**
   - Application to workplace wellbeing
   - Future potential (voice interface, mood tracking)

---

## Learning Outcomes

By building KaramBot, you learn:

✅ **Machine Learning:** Using real LLMs (Llama 3.1)
✅ **RAG Architecture:** Retrieval + Augmented Generation
✅ **Prompt Engineering:** Crafting effective system prompts
✅ **Emotion Detection:** Basic NLP (keyword-based)
✅ **Self-Hosted AI:** Running models locally (Ollama)
✅ **User Testing:** A/B testing, feedback collection
✅ **Evaluation:** Measuring model performance

**These are production ML skills!**

---

## Troubleshooting

### "Connection Error: Could not connect to Ollama"

**Windows (Native):**
1. Check if Ollama is running: Look for Ollama icon in system tray (bottom-right)
2. If not running, search "Ollama" in Start Menu and launch it
3. Or restart the service:
   - Open Services (Win + R, type `services.msc`)
   - Find "Ollama Service"
   - Right-click → Restart

**Linux/macOS/WSL:**
Make sure Ollama is running in another terminal:
```bash
ollama serve
```

### "Model not found"

**Windows:**
```cmd
ollama pull llama3.1:8b
```

**Linux/macOS/WSL:**
```bash
ollama pull llama3.1:8b
```

### First response is very slow (30-60 seconds)
**Fix:** This is **normal**! Model is loading into memory. Subsequent responses are faster (~3-5 seconds).

### Responses are too slow (>10 seconds)
**Fix:**
- Close other heavy applications (browsers, games, IDEs)
- Check RAM usage (Llama needs ~8GB free)
- **Windows:** Check Task Manager (Ctrl+Shift+Esc) → Performance → Memory
- **Linux/macOS:** Run `htop` or Activity Monitor
- Try smaller model: `ollama pull llama3.1:3b` (faster but less accurate)

### "python not found" or "pip not found" (Windows)
**Fix:**
1. Install Python 3.11+ from https://python.org/downloads
2. During installation, check ✅ "Add Python to PATH"
3. Restart Command Prompt
4. Verify: `python --version`

### Path issues on Windows
**Common mistakes:**
- ❌ `cd karambot` (missing drive/full path)
- ✅ `cd C:\Users\YourName\Downloads\karambot`

**Find your path:**
1. Open File Explorer, navigate to karambot folder
2. Click address bar, copy full path
3. Use in Command Prompt: `cd [paste path here]`

### "ModuleNotFoundError: No module named 'requests'"
**Fix:**
```cmd
pip install requests
```
Or if you have multiple Python versions:
```cmd
python -m pip install requests
```

---

## Connection to Real-World Applications

This architecture is similar to production AI systems:

| KaramBot (Learning) | Production AI |
|---------------------|---------------|
| Spiritual teachings | Medical protocols / Legal docs |
| Llama 3.1 8B (laptop) | Llama 3.1 70B (AWS GPUs) |
| Ollama (local) | vLLM (cloud) |
| 10 students testing | Thousands of users |
| Stress detection | Medical triage / Intent classification |

**Real applications:** Customer support bots, medical AI assistants, legal research tools, educational tutors.

---

## Credits

**Sacred Teachings Sources:**
- Bhagavad Gita (Bhaktivedanta Swami Prabhupada translation)
- Quran (Sahih International translation)
- Bible (New International Version)
- Guru Granth Sahib (Sant Singh Khalsa translation)

**Technology:**
- Llama 3.1 by Meta AI
- Ollama by Ollama team
- Python 3.11+

---

## License

This is an educational project for college coursework.
Sacred texts are used respectfully for spiritual guidance purposes.

---

**Built with:** Machine Learning, Compassion, and Respect for All Faiths 🙏✨
