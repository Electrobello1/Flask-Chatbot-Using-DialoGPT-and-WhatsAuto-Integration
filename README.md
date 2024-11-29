# Flask Chatbot Using DialoGPT and WhatsAuto Integration

This project implements a chatbot powered by Microsoft's DialoGPT and integrates it with WhatsAuto for automated responses.

## Features
- Processes messages using Microsoft's DialoGPT pre-trained models.
- Accepts HTTP POST requests for message interaction.
- Includes setup instructions for deploying the chatbot locally with Flask and exposing it online via **ngrok**.

## Prerequisites
Before running the chatbot, ensure the following are installed on your system:
1. Python 3.7 or higher.
2. Flask and required Python libraries (`transformers`, `torch`, etc.).
3. **ngrok** for exposing the local Flask server to the internet.
4. A strong internet connection.

## Setup Instructions

### 1. Install Dependencies
Use pip to install the required dependencies:
```bash
pip install requirements.txt
```
### 2. Download ngrok
If you don’t have ngrok, download and install it from ngrok's official website.

### 3.  Run the Flask App
Start the chatbot server locally by running the following command:
```bash
python bot.py --model medium --steps 100
```

- model: The size of the DialoGPT model (small, medium, or large). Defaults to medium.
- steps: The number of dialogue steps. Defaults to 100.

### 4. Expose the Server via ngrok
- Open a separate terminal window.
-Run ngrok to expose the Flask server on port 5000

```bash
ngrok http 5000
```
### 4. Integrate with WhatsAuto
Open the WhatsAuto app on your device.
Set the webhook URL to the one copied from ngrok (e.g., https://abc123.ngrok.io/bot).
Ensure WhatsAuto is configured to send POST requests with a message field containing the text.
### How It Works
WhatsAuto sends incoming messages to the chatbot server via the /bot endpoint.
The chatbot processes the message using DialoGPT and responds with an appropriate reply.
WhatsAuto receives the reply and sends it back to the user.
### Example Request and Response
Incoming Request
```json
{
  "message": "hello chatbot"
}
```
### Server Response
```json
{
  "reply": "Hello! How can I assist you today?"
}
```