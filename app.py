from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

# Replace 'your-openai-api-key' with your actual OpenAI API key
openai.api_key = 'your_api_key'

# index route
@app.route('/')
def index():
    return render_template('index.html')

# route to handle the chat messages
@app.route('/api', methods=['POST'])

def api():

    # a prompt or message fromt the user
    prompt = request.json['message']
    
    # getting response from the 
    message = generate_response(prompt)

    return jsonify({'message': message})

def generate_response(prompt):

    try:
        # openai API
        response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                max_tokens = 10   # can change to increase no of characters/words in response
        )
        if response.choices[0].message!=None:
            return response.choices[0].message.content

        else :
            return 'Failed to Generate response!'
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
