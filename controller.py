from flask import Flask, jsonify, request, Response
import subprocess
#import asyncio

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'pong'})

@app.route('/example', methods=['GET'])
def examble():
    example_script = 'example.py'
    answer = subprocess.run(['python', example_script], capture_output=True)
    return answer.stdout, 200

# @app.route('/question/<prompt>', methods=['GET'])
# def question(prompt):
#     gpt_script = 'privateGPT-Answer.py ' + str(prompt)
#     answer = subprocess.run(['python', gpt_script], capture_output=True)
#     return answer.stdout, 200

@app.route('/question/<prompt>', methods=['GET'])
def question(prompt):
    gpt_script = 'privateGPT-Answer.py ' + str(prompt)
    result = subprocess.check_output(['python', gpt_script]).decode('utf-8').strip()
    return Response(result, status=200, mimetype='text/plain')

# @app.route('/question/<prompt>', methods=['GET'])
# def question(prompt):
#     gpt_script = 'privateGPT-Answer.py ' + str(prompt)
#     process = subprocess.Popen(['python', gpt_script], stdout=subprocess.PIPE)
#     process.wait()
#     output, _ = process.communicate()
#     return Response(output, status=200, mimetype='text/plain')

if __name__ == '__main__':
    #asyncio.run(app.run(host='localhost', port=8081))
    app.run(host='localhost', port=8081)
