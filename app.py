import random
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

from dados import monster


co0 = "#444466"
co1 = "#feffff"
co2 = "#6f9fbd"
co3 = "#38576b"
co4 = "#403d3d"
co5 = "#ef5350"

menu = Tk()

menu.title('MONSTER-DEX-PYTHON')

menu.geometry('550x500')

menu.configure(bg=co0)


ttk.Separator(menu, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(menu)
style.theme_use("clam")

frame_poke = Frame(menu, width=550, height=290, relief="flat")

frame_poke.grid(row=1, column=0)


def trocar_monster(i):
    global image_pok, pok_image

    frame_poke["bg"] = "#444466"

    pok_nome["text"] = i
    pok_nome["bg"] = monster[i]["tipo"][2]
    pok_tipo["text"] = monster[i]["habilidades"][0]
    pok_tipo["bg"] = monster[i]["tipo"][2]
    pok_id["text"] = monster[i]["tipo"][0]
    pok_id["bg"] = monster[i]["tipo"][2]

    image_pok = monster[i]["tipo"][1]

    image_pok = Image.open(image_pok)

    image_pok = image_pok.resize((238, 238))

    image_pok = ImageTk.PhotoImage(image_pok)

    pok_image = Label(frame_poke, image=image_pok, relief="flat",
                      anchor=CENTER, font=("fixedsys 20"), bg=monster[i]["tipo"][2], fg=co1)
    pok_image.place(x=60, y=50)

    pok_tipo.lift()
    pok_id.lift()

    pok_hp["text"] = monster[i]["status"][0]
    pok_especie["text"] = monster[i]["tipo"][0]
    pok_atack["text"] = monster[i]["status"][1]
    pok_fraquesa["text"] = monster[i]["status"][2]


pok_nome = Label(frame_poke, text="", relief="flat",
                 anchor=CENTER, font=("fixedsys 20"), bg=co1, fg=co1)
pok_nome.place(x=12, y=15)

pok_tipo = Label(frame_poke, text="", relief="flat",
                 anchor=CENTER, font=("Ivy 10 bold"), bg=co1, fg=co1)
pok_tipo.place(x=12, y=55)

pok_id = Label(frame_poke, text="", relief="flat",
               anchor=CENTER, font=("fixedsys 20"), bg=co1, fg=co1)
pok_id.place(x=12, y=80)

pok_status = Label(menu, text="Status", relief="flat",
                   anchor=CENTER, font=("Verdana 20"), bg=co1, fg=co0)
pok_status.place(x=10, y=310)

pok_especie = Label(menu, text="", relief="flat",
                    anchor=CENTER, font=("Verdana 10"), bg=co1, fg=co4)
pok_especie.place(x=10, y=360)

pok_hp = Label(menu, text="", relief="flat",
               anchor=CENTER, font=("Verdana 10"), bg=co1, fg=co4)
pok_hp.place(x=10, y=390)

pok_atack = Label(menu, text="", relief="flat",
                  anchor=CENTER, font=("Verdana 10"), bg=co1, fg=co4)
pok_atack.place(x=10, y=420)

pok_fraquesa = Label(menu, text="", relief="flat",
                     anchor=CENTER, font=("Verdana 10"), bg=co1, fg=co4)
pok_fraquesa.place(x=10, y=450)

# MONSTER1 FUNDO
image_pok_1 = Image.open('images/NergiC.png')

image_pok_1 = image_pok_1.resize((40, 40))

image_pok_1 = ImageTk.PhotoImage(image_pok_1)

# MONSTER1

a_pok_1 = Button(menu, command=lambda: trocar_monster("Nergigante"), image=image_pok_1, text="Nergigante", width=150, relief="flat",
                 overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Verdana 12"), bg=co1, fg=co0)
a_pok_1.place(x=375, y=10)

image_pok_2 = Image.open('images/bazelC.png')

image_pok_2 = image_pok_2.resize((40, 40))

image_pok_2 = ImageTk.PhotoImage(image_pok_2)


a_pok_2 = Button(menu, command=lambda: trocar_monster("Bazel"), image=image_pok_2, text="Bazel", width=150, relief="flat",
                 overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Verdana 12"), bg=co1, fg=co0)
a_pok_2.place(x=375, y=65)

# MONSTER2

image_pok_3 = Image.open('images/ValC.png')

image_pok_3 = image_pok_3.resize((40, 40))

image_pok_3 = ImageTk.PhotoImage(image_pok_3)

a_pok_3 = Button(menu, command=lambda: trocar_monster("Vaal Hazak"), image=image_pok_3, text="Vaal Hazak", width=150, relief="flat",
                 overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=("Verdana 12"), bg=co1, fg=co0)
a_pok_3.place(x=375, y=120)

Lista_monsters = ["Nergigante", "Bazel", "Vaal Hazak"]

monster_escolhido = random.sample(Lista_monsters, 1)

trocar_monster(monster_escolhido[0])

menu.mainloop()
