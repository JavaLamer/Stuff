from flask import Flask
from flask import request,render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def main_page():
    return "hello world"

# Изначально у нас пустой список сообщений
# Все сообщения будет добавлять и читать из этого списка
all_messages = []

# .append() добавляет новый элемент в список all_messages.append(новый элемент)
# Аргументы - то что надо знать функции чтобы выполнить свою работу

# Функция добавления нового сообщения
def add_message(sender, text):
    # Создать новое сообщение (словарь) и добавить его в список
    new_message = {
        "name": sender,
        "text": text,
        "time": datetime.now().strftime("%H:%M:%S") # ДЗ: подставить текущее время Часы:Минуты
    }
    all_messages.append(new_message)

def errors(error):

    if error == 1:
        errors = "Sorry, 404 error, but who are you ?"
    if error == 2:
        errors = "Sorry, 405 error, you forget write message"
    if error == 3:
        errors = "Sorry, 406 error, remember your name"

    name = "Undefind"
    error_message = {
        "name": name,
        "text": errors,
        "time": datetime.now().strftime("%H:%M:%S")
    }
    all_messages.append(error_message)





add_message("Майк", "Всем приветы в этом чате")
add_message("Чапа", "Что такое Путхон?")
add_message("Васисуалий", "Пайтон это очень круто, гыгыгы")
add_message("Васисуалий12", "Пайтон это очень круто, гыгыгы")
add_message("Васисуалий23", "Пайтон это очень круто, гыгыгы")
add_message("Васисуалий44", "Пайтон это очень круто, гыгыгы")


@app.route("/get_messages")
def getMessages():
    return {"messages": all_messages}

@app.route("/send_message")
def send_message():
    name = request.args.get("name")
    text = request.args.get("text")
    if name == "" or text == "":
        if text == "" and name == "":
            return errors(1)
        if text == "":
            return errors(2)
        if name == "":
            return errors(3)
    else:
         return add_message(name,text)


@app.route("/chat")
def chat_def():
    return render_template("html_file.html")


app.run(debug=True)