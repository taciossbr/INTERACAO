from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("Fatequino")

# conversa = [
#     "Oi",
#     "Olá, eu sou o Fatequino!\nComo posso te ajudar?",
#     "O professor Mario Marques está na faculdade?",
#     "Sim!\nO professor Mario Marques está na sala 108.",
#     "Obrigado.",
#     "Qualquer dúvida é só me chamar!\nBoa aula!",
# ]

# treino = ListTrainer(chatbot)
# treino.train(conversa)

while True:
    try:
        bot_input = chatbot.get_response(input())
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break

# resposta = chatbot.get_response("Oi")
# print(resposta)