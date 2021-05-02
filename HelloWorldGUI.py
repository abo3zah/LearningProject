from guizero import *

# confirmation message after closure
def do_this_on_close():
    if yesno("Close", "Do you want to quit?"):
        app.destroy()

# setting app the name
def say_my_name():
    if my_name.value=="":
        error("OH No", "Where is your name??")
    else:
        welcome_message.value = my_name.value

#initializing the app
app = App(title="Hello World", layout="grid")

#adding a text and setting the default value
welcome_message = Text(app, text="Welcome to my app", color="Red", grid=[0,0])

#adding a textbox with intial setting
my_name = TextBox(app, "Type your name", width=50, grid=[1,0])

#adding a pushbutton
update_text= PushButton(app, command=say_my_name, text="Dispaly your name", grid=[2,0])

# When user tries to close the app
app.when_closed =do_this_on_close

app.display()