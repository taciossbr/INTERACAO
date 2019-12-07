from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Fatequino",
                storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
                database_uri='mongodb://localhost:27017/chatterbot-db',
                logic_adapters=["chatterbot.logic.BestMatch"])


conversa = [
    "Oi",
    "Olá, eu sou o Fatequino!\nComo posso te ajudar?",
    "O professor Mario Marques está na faculdade?",
    "Sim!\nO professor Mario Marques está na sala 108.",
    "Obrigado.",
    "Qualquer dúvida é só me chamar!\nBoa aula!",
    "Eu vou passar?",
    "Com um BOT lindo como eu claro que sim ; )",
    "Eu vou passar em topicos?",
    "Se eu estou te respondendo creio que sim"
]

treino = ListTrainer(chatbot)
treino.train(conversa)



# resposta = chatbot.get_response("Oi")
# print(resposta)
