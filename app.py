import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))

from flask import Flask
from flask import render_template,jsonify,request
import requests
from rasa.core.agent import Agent
from models import *
# from knowledge import *
import random
from rasa_nlu.training_data import load_data
# from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter
import yaml
# from rasa_core.utils import EndpointConfig
# from rasa.utils.endpoints import EndpointConfig
import warnings
warnings.filterwarnings("ignore")


# training_data = load_data("./data/nlu.md")

# trainer to educate our pipeline
# trainer = Trainer(config.load("./config.yml"))

# train the model!
# interpreter = trainer.train(training_data)
# trainer = Trainer(config.load("./config.yml"))
# store it for future use
# model_directory = trainer.persist("./models/nlu", fixed_model_name="current")


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/current')
# action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)





def chatting(text_d):
    print("chatting function is loaded")
    responses = agent.handle_message(text_d)
    for response in responses:
#             # print(response["text"])
        return response["text"]





app = Flask(__name__)
app.secret_key = '12345'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat',methods=['POST'])
def chat():
    user_message = request.form["text"]
    print("User_message",user_message)
    result = chatting(user_message)
    print("Result",result)

    return jsonify({"status":"success","response":result})

app.config["DEBUG"] = True
if __name__ == "__main__":
    app.run(port=8080)
