from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelForCausalLM
from mistralai import Mistral
from ollama import chat
from ollama import ChatResponse
from openai import OpenAI
import io




class Model:
    def __init__(self, model="", tokenizer=""):
        self.model = model
        self.tokenizer = tokenizer

        if model and tokenizer:
            self.init_model()

    async def init_model(self):
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(self.tokenizer)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(self.model)
        except:
            try:
                self.tokenizer = AutoTokenizer.from_pretrained(self.tokenizer)
                self.model = AutoModelForCausalLM.from_pretrained(self.model)
            except:
                raise ValueError("unable to load model")

    async def generate(self, text):
        input_ids = self.tokenizer(text, return_tensors="pt").input_ids.cuda()

        outputs = self.model.generate(input_ids)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)


class Model_API(Model):
    def __init__(self, api_key, **kwargs):
        super().__init__(**kwargs)
        self.api_key = api_key

    async def generate(self, text):
        model = "mistral-large-latest"

        client = Mistral(api_key=self.api_key)

        response = client.chat.complete(
            model=model,
            messages=[
                {"role": "user", "content": text}
            ]
        )

        return response.choices[0].message.content


async def ollama(text):
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

    def generate(self, text):
        openai = OpenAI(
            api_key=self.api_key,
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

class Model_llama_70B2:
    def __init__(self, api_key):
        self.api_key = api_key

    def generate(self, text):
        openai = OpenAI(
            api_key=self.api_key,
            base_url="https://api.deepinfra.com/v1/openai",
        )

        stream = False  # or False

        chat_completion = openai.chat.completions.create(
            model="meta-llama/Meta-Llama-3-70B-Instruct",
            messages=[
                {"role": "user", "content": f"""Есть данные из базы знаний: ## 7.4. Проблемы с ушами

### Инфекции ушей
Собаки с длинными или висячими ушами, такие как кокер-спаниели или бассет-хаунды, часто подвержены ушным инфекциям. Для профилактики:
- **Регулярная чистка.** Используйте специальные средства и ватные диски, избегайте глубокой чистки.
- **Проверка.** Осматривайте уши на наличие запаха, покраснения или выделений.
- **Сухость.** После купания тщательно сушите уши, чтобы предотвратить излишнюю влажность.

### Аллергические реакции
Если собака часто чешет уши, это может быть признаком аллергии. В таких случаях стоит проконсультироваться с ветеринаром для корректировки рациона или назначения лекарств.

---

## 8. Особенности ухода за щенками

### 8.1. Питание
- **Кормление.** Щенков кормят чаще, чем взрослых собак, обычно 3-4 раза в день. Используйте специализированные корма для щенков, богатые белком и кальцием.
- **Переходный период.** При смене корма вводите новый рацион постепенно в течение недели.

### 8.2. Прививки
- **График вакцинации.** Щенков вакцинируют с 6-8 недель и далее по графику ветеринара.
- **Антипаразитарная обработка.** Проводите профилактику глистов и обработку от блох согласно рекомендациям.

### 8.3. Социализация
- **Привычка к шуму.** Щенков важно приучать к городскому шуму, людям и другим животным.
- **Игры.** Используйте мягкие игрушки и избегайте чрезмерной физической нагрузки.

Ответь дай с дополнения с базы знаний на запрос: {text}"""},
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



if __name__ == '__main__':
    print(Model_llama_70B2("18kBsYH2IFrKDsA6sAgNRO4TotwkDa4j").generate("Питание"))