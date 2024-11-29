# make sure ngrok is downloaded on your system and have a strong internet connection
# open the command prompt on your system and type ngrok http 5000
#copy the  url starting with https to the whatsauto app


from flask import Flask, request
import json
import argparse
from transformers import AutoModelWithLMHead, AutoTokenizer
import torch


parser = argparse.ArgumentParser(
    description="Process chatbot variables. for help run python bot.py -h"
)
parser.add_argument(
    "-m", "--model", type=str, default="medium", help="Size of DialoGPT model"
)
parser.add_argument(
    "-s",
    "--steps",
    type=int,
    default=100,
    help="Number of steps to run the Dialogue System for",
)

args = parser.parse_args()
tokenizer = AutoTokenizer.from_pretrained(f"microsoft/DialoGPT-{args.model}")
model = AutoModelWithLMHead.from_pretrained(f"microsoft/DialoGPT-{args.model}")

app = Flask(__name__)

#accepts post requests from whatsauto
@app.route("/bot", methods=["POST"])
def bot():
    for step in range(args.steps):
        #Get the message body from whatsauto in small letters
        incoming_msg = request.values.get('message', '').lower()
        print('incomming message:', incoming_msg)
        #Encode the new user input,add the eos_token and return a tensor in pytorch
        new_user_input_ids = tokenizer.encode(
            incoming_msg + tokenizer.eos_token, return_tensors="pt"
        )

         #add the new user input tokens to the chat history
        bot_input_ids =(
            torch.cat([chat_history_ids , new_user_input_ids], dim=-1)
            if step > 0 else
            new_user_input_ids
        )
        #generate a response while limiting the total chat history to 1000 tokens
        chat_history_ids = model.generate(
            bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id
        )

       # Print the last output tokens from dialogpt
        A= tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        # Print the output and convert to string
        print({A})
        reply={'reply': A}
        print(reply)
        return (reply)






if __name__ == "__main__":
    app.run()


























