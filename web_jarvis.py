from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime
import os
from main import Jarvis

app = Flask(__name__)
jarvis = Jarvis()

# Store responses for the web
responses = []

@app.route('/')
def home():
    """Main dashboard"""
    return render_template('index.html')

@app.route('/api/command', methods=['POST'])
def execute_command():
    """Command execute करो"""
    data = request.json
    command = data.get('command', '').strip()
    
    if not command:
        return jsonify({'error': 'Empty command'}), 400
    
    # Execute command
    result = jarvis.process_command(command)
    
    # Get the response (read last line from log)
    try:
        with open('jarvis_log.txt', 'r') as f:
            lines = f.readlines()
            response = lines[-1].strip() if lines else "No response"
    except:
        response = "Error executing command"
    
    return jsonify({
        'command': command,
        'response': response,
        'timestamp': datetime.now().strftime("%H:%M:%S")
    })

@app.route('/api/history')
def get_history():
    """History return करो"""
    try:
        with open('jarvis_log.txt', 'r') as f:
            history = f.read()
        return jsonify({'history': history})
    except:
        return jsonify({'history': 'No history'})

@app.route('/api/config')
def get_config():
    """Config return करो"""
    return jsonify(jarvis.config)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
