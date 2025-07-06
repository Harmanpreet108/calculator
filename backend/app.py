from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)  # Allow frontend to talk to backend

# Main AI calculator function
def ai_calculator(message):
    message = message.lower()

    if "add" in message or "plus" in message:
        nums = [int(x) for x in re.findall(r'\d+', message)]
        return sum(nums)

    elif "subtract" in message or "minus" in message:
        nums = [int(x) for x in re.findall(r'\d+', message)]
        return nums[0] - nums[1]

    elif "multiply" in message or "times" in message:
        nums = [int(x) for x in re.findall(r'\d+', message)]
        result = 1
        for n in nums:
            result *= n
        return result

    elif "divide" in message or "by" in message:
        nums = [int(x) for x in re.findall(r'\d+', message)]
        return nums[0] / nums[1]

    elif "square root" in message:
        num = int(re.search(r'\d+', message).group())
        return num ** 0.5

    else:
        try:
            # For math expressions like "2 + 3 * 4"
            return eval(message)
        except:
            return "Sorry, I couldn’t understand."

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    message = data.get('expression', '')
    result = ai_calculator(message)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
