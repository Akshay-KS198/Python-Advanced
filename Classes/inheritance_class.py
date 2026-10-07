from first_class import llms

class chatbot(llms):

    def __init__(self, model, query):
        self.model = model
        llms.__init__(self,query)

    def showme(self):
        print(f"I am calling {self.model}")
        llms.claude()

obj_inherit = chatbot("claude", "I want to access Akshay")
print(obj_inherit.claude())
