class llms:
    token_size = 100

    def __init__(self, query):
        self.query = query 

    def openai(self):
        print(f"I am openai, You asked {self.query}")

    def claude(self):
        print(f"I am claude, asked by you is {self.query}")

    def llama(self):
        print("I am llma")

obj_1 = llms("Akshay is a good boy")
obj_1.openai()