import openai
from settings import OPENAI_SECRET_KEY
import argparse

openai.api_key = OPENAI_SECRET_KEY

def main(model, temperature):

    messages = []
    while True:
        try:
            first_line = True
            lines = []
            while True:
                if first_line:
                    line = input("\n>> ")
                else:
                    line = input("")
                first_line = False
                line and lines.append(line)
                message = "\n".join(lines)
                if not line and message.strip():
                    break

            message = "\n".join(lines)
            
            if message == "quit" or message == "q":
                break
            messages.append({'role': 'user', 'content': message})

            print('\n\nChatGPT is thinking...\n\n')
        except KeyboardInterrupt:
            continue


        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature,
            n=1,
        )
        
        content = response['choices'][0]['message']['content']  # type: ignore

        messages.append({'content': content, 'role': 'assistant'})
        print(content)

if __name__ == '__main__':
    try:
        from settings import MODEL
    except:
        MODEL = 'gpt-4'
    try:
        from settings import TEMPERATURE
    except:
        TEMPERATURE = 0
    parser = argparse.ArgumentParser(description='Chat with GPT')
    parser.add_argument('--model', type=str, default=MODEL, help='GPT model to use')
    parser.add_argument('--temperature', type=float, default=TEMPERATURE, help='GPT temperature')
    model = parser.parse_args().model
    temperature = parser.parse_args().temperature
    print(f'Using model {model} with temperature {temperature}')
    main(model=model, temperature=temperature)
