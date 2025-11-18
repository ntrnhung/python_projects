from tkinter import *
import requests

def get_quote():
    response = requests.get("https://taylorswiftapi.onrender.com/get")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text = quote)


window = Tk()
window.title("Taylor Sings...")
window.config(padx=30, pady=50, bg="white")

canvas = Canvas(width=400, height=350, highlightthickness=0, bg="white")
background_img = PhotoImage(file="background.png")
canvas.create_image(200, 175, image=background_img)
quote_text = canvas.create_text(200, 160, text="Taylor Quote Goes HERE", width=300, font=("Arial", 18, "bold"), fill="black")
canvas.grid(row=0, column=0)

taylor_img = PhotoImage(file="taylor.png")
taylor_button = Button(image=taylor_img, highlightthickness=0, borderwidth=0, command=get_quote)
taylor_button.grid(row=1, column=0)



window.mainloop()