import openai
from settings import OPENAI_SECRET_KEY

openai.api_key = OPENAI_SECRET_KEY

def main():

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
                lines.append(line)
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
            model="gpt-4",
            messages=messages,
            temperature=0,
            n=1,
        )
        
        content = response['choices'][0]['message']['content']  # type: ignore

        messages.append({'content': content, 'role': 'assistant'})
        print(content)

if __name__ == '__main__':
    main()
