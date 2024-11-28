from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelForCausalLM
from mistralai import Mistral
from ollama import chat
from ollama import ChatResponse
from openai import OpenAI




class Model:
    def __init__(self, model="", tokenizer=""):
        self.model = model
        self.tokenizer = tokenizer

        if model and tokenizer:
            self.init_model()

    def init_model(self):
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.tokenizer)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model)
        except:
            try:
                self.tokenizer = AutoTokenizer.from_pretrained(self.tokenizer)
                self.model = AutoModelForCausalLM.from_pretrained(self.model)
            except:
                raise ValueError("unable to load model")

    def generate(self, text):
        input_ids = self.tokenizer(text, return_tensors="pt").input_ids.cuda()

        outputs = self.model.generate(input_ids)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)


class Model_API(Model):
    def __init__(self, api_key, **kwargs):
        super().__init__(**kwargs)
        self.api_key = api_key

    def generate(self, text):
        model = "mistral-large-latest"

        client = Mistral(api_key=self.api_key)

        response = client.chat.complete(
            model=model,
            messages=[
                {"role": "user", "content": text}
            ]
        )

        return response.choices[0].message.content


def ollama(text):
    response: ChatResponse = chat(model='llama3', messages=[
        {
            'role': 'user',
            'content': text,
        },
    ])

    return response.message.content

class Model_llama_70B:
    def __init__(self, api_key):
        self.api_key = api_key

    def generate(self, text, api_key):
        openai = OpenAI(
            api_key=api_key,
            base_url="https://api.deepinfra.com/v1/openai",
        )

        stream = False  # or False

        chat_completion = openai.chat.completions.create(
            model="meta-llama/Meta-Llama-3-70B-Instruct",
            messages=[
                {"role": "user", "content": text},
            ],
            stream=stream,
        )

        s = ""
        if stream:
            for event in chat_completion:
                if event.choices[0].finish_reason:
                    print(event.choices[0].finish_reason)
                else:
                    s += str(event.choices[0].delta.content)
        else:
            return chat_completion.choices[0].message.content
        # print()
        # print(chat_completion.usage.prompt_tokens, chat_completion.usage.completion_tokens)