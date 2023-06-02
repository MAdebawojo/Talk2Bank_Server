import openai
from FAQ import faq
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# open api key- put your own api key
# always remember to remove your ai key before you push the code
openai.api_key = ''

faq_string = ""
for i, (question, answer) in enumerate(faq.items()):
    faq_string += f"{i+1}. FAQ: {question}\nResponse: {answer}\n\n"


@app.route('/chat', methods=['POST'])
def chat():
    language = 'English'
    request_data = request.get_json()
    message = request_data['message']

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[
                                                {"role": "system", "content": f"Your name is Talk2bank." +
                                                 "You are a helpful assistant that communicates with a user in" +
                                                 "any specified african language. In addition to your main role, " +
                                                 "you are to answer any FAQ questions in the specified language " + "with the appropriate answer from {faq_string}"},
                                                {"role": "user",
                                                    "content": f"Communicate with me in {language}"},
                                                {"role": "user", "content": message},
                                            ])
    responseJSON = {
        "message": response['choices'][0]['message']['content'],
        "sent": False,
    }
    return jsonify(responseJSON)


if __name__ == '__main__':
    print('Server is listening...')
    app.run(debug=True, port=5000)
