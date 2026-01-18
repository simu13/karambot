#!/usr/bin/env python3
"""
KaramBot Web Interface
Flask web app for browser-based interaction
"""

from flask import Flask, render_template, request, jsonify
from karambot_ollama import KaramBot
import os

app = Flask(__name__)
bot = None

def get_bot():
    """Get or create KaramBot instance"""
    global bot
    if bot is None:
        bot = KaramBot(model="llama-3.1-8b-instant")
    return bot

@app.route('/')
def index():
    """Serve the main chat page"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat messages"""
    # Check API key first
    if not os.environ.get('GROQ_API_KEY'):
        return jsonify({
            'error': 'Server configuration error: GROQ_API_KEY not set',
            'success': False
        }), 500

    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()

        if not user_message:
            return jsonify({'error': 'Empty message'}), 400

        # Get response from KaramBot
        bot_instance = get_bot()
        response = bot_instance.chat(user_message)

        return jsonify({
            'response': response,
            'success': True
        })

    except ValueError as e:
        return jsonify({
            'error': f'Configuration error: {str(e)}',
            'success': False
        }), 500
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500

@app.route('/save', methods=['POST'])
def save_conversation():
    """Save conversation history"""
    try:
        bot_instance = get_bot()
        bot_instance.save_conversation('web_conversation_log.json')
        return jsonify({
            'success': True,
            'message': 'Conversation saved successfully'
        })
    except Exception as e:
        return jsonify({
            'error': str(e),
            'success': False
        }), 500

@app.route('/health')
def health():
    """Health check endpoint"""
    api_key = os.environ.get('GROQ_API_KEY')
    if api_key:
        return jsonify({'status': 'ok', 'api': 'configured'})
    else:
        return jsonify({'status': 'error', 'api': 'missing GROQ_API_KEY'}), 503

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
