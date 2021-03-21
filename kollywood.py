'''
Source:

Author: Raja CSP


'''
from flask import Flask,render_template
import random
import json

app = Flask(__name__)


FILEPATH = 'chemistry_meter.json'

def get_json_data():

    with open(FILEPATH) as json_file:
        data = json.load(json_file)
        
        print(data)

    return data

def store_json_data(data):

    with open(FILEPATH, 'w') as outfile:
        json.dump(data, outfile)

def get_chemistry_meter(actor_name, actress_name):

    c_key = actor_name + '_' + actress_name

    chemistry_dict = get_json_data()

    if(c_key in chemistry_dict):
        return chemistry_dict[c_key]

    ch_meter = random.randint(50, 100)

    chemistry_dict[c_key] = ch_meter

    # store into json
    store_json_data(chemistry_dict)

    # print(ch_meter)
    return ch_meter
    
@app.route("/", methods=["GET","POST"])
def startpy():

    # print('Vanakkam Chennai!')

    actor_name      = 'surya'
    actress_name    = 'jyohika'

    local_meter = get_chemistry_meter(actor_name, actress_name)

    print(f'{actor_name} - {actress_name} : {local_meter}')

    return render_template("index.html", actor=actor_name, actress=actress_name, score=local_meter)


if __name__ == "__main__":
    app.run( debug = True,host="0.0.0.0",port="3000")
    