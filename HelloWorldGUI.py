from guizero import App, Text
app = App(title="Hello World")
welcome_message = Text(app, text="Welcome to my app", size=40)
app.display()