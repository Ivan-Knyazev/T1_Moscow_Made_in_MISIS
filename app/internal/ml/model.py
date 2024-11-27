from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelForCausalLM
from mistralai import Mistral


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
