from tkinter import *

def formal():
    window.destroy()
    def btn_clicked():
        print("Button Clicked")


    window1 = Tk()

    window1.geometry("1280x720")
    window1.configure(bg = "#ffffff")
    canvas1 = Canvas(
        window1,
        bg = "#ffffff",
        height = 720,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas1.place(x = 0, y = 0)

    background1_img = PhotoImage(file = f"background1.png")
    background1 = canvas1.create_image(
        561.0, 391.0,
        image=background1_img)

    entry0_img = PhotoImage(file = f"img_textBox0.png")
    entry0_bg = canvas1.create_image(
        510.0, 136.5,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#c4c4c4",
        highlightthickness = 0)

    entry0.place(
        x = 281, y = 120,
        width = 458,
        height = 31)

    entry1_img = PhotoImage(file = f"img_textBox1.png")
    entry1_bg = canvas1.create_image(
        510.0, 78.0,
        image = entry1_img)

    entry1 = Entry(
        bd = 0,
        bg = "#c4c4c4",
        highlightthickness = 0)

    entry1.place(
        x = 281, y = 62,
        width = 458,
        height = 30)

    entry2_img = PhotoImage(file = f"img_textBox2.png")
    entry2_bg = canvas1.create_image(
        569.0, 252.5,
        image = entry2_img)

    entry2 = Entry(
        bd = 0,
        bg = "#c4c4c4",
        highlightthickness = 0)

    entry2.place(
        x = 399, y = 236,
        width = 340,
        height = 31)

    entry3_img = PhotoImage(file = f"img_textBox3.png")
    entry3_bg = canvas1.create_image(
        607.0, 194.5,
        image = entry3_img)

    entry3 = Entry(
        bd = 0,
        bg = "#c4c4c4",
        highlightthickness = 0)

    entry3.place(
        x = 475, y = 178,
        width = 264,
        height = 31)

    entry4_img = PhotoImage(file = f"img_textBox4.png")
    entry4_bg = canvas1.create_image(
        446.0, 369.5,
        image = entry4_img)

    entry4 = Entry(
        bd = 0,
        bg = "#c4c4c4",
        highlightthickness = 0)

    entry4.place(
        x = 153, y = 353,
        width = 586,
        height = 31)

    entry5_img = PhotoImage(file = f"img_textBox5.png")
    entry5_bg = canvas1.create_image(
        569.0, 311.0,
        image = entry5_img)

    entry5 = Entry(
        bd = 0,
        bg = "#c4c4c4",
        highlightthickness = 0)

    entry5.place(
        x = 399, y = 295,
        width = 340,
        height = 30)

    entry6_img = PhotoImage(file = f"img_textBox6.png")
    entry6_bg = canvas1.create_image(
        549.0, 485.5,
        image = entry6_img)

    entry6 = Entry(
        bd = 0,
        bg = "#c4c4c4",
        highlightthickness = 0)

    entry6.place(
        x = 359, y = 469,
        width = 380,
        height = 31)

    entry7_img = PhotoImage(file = f"img_textBox7.png")
    entry7_bg = canvas1.create_image(
        522.0, 427.5,
        image = entry7_img)

    entry7 = Entry(
        bd = 0,
        bg = "#c4c4c4",
        highlightthickness = 0)

    entry7.place(
        x = 305, y = 411,
        width = 434,
        height = 31)

    entry8_img = PhotoImage(file = f"img_textBox8.png")
    entry8_bg = canvas1.create_image(
        593.0, 602.0,
        image = entry8_img)

    entry8 = Entry(
        bd = 0,
        bg = "#c4c4c4",
        highlightthickness = 0)

    entry8.place(
        x = 447, y = 586,
        width = 292,
        height = 30)

    entry9_img = PhotoImage(file = f"img_textBox9.png")
    entry9_bg = canvas1.create_image(
        592.5, 655.5,
        image = entry9_img)

    entry9 = Entry(
        bd = 0,
        bg = "#c4c4c4",
        highlightthickness = 0)

    entry9.place(
        x = 446, y = 639,
        width = 293,
        height = 31)

    entry10_img = PhotoImage(file = f"img_textBox10.png")
    entry10_bg = canvas1.create_image(
        510.0, 543.5,
        image = entry10_img)

    entry10 = Entry(
        bd = 0,
        bg = "#c4c4c4",
        highlightthickness = 0)

    entry10.place(
        x = 281, y = 527,
        width = 458,
        height = 31)

    entry11_img = PhotoImage(file = f"img_textBox11.png")
    entry11_bg = canvas1.create_image(
        1010.0, 339.0,
        image = entry11_img)

    entry11 = Text(
        bd = 0,
        bg = "#c4c4c4",
        highlightthickness = 0)

    entry11.place(
        x = 768, y = 92,
        width = 484,
        height = 492)

    img0 = PhotoImage(file = f"imgz.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = formal,
        relief = "flat")

    b0.place(
        x = 939, y = 613,
        width = 217,
        height = 71)

    window1.resizable(False, False)
    window1.mainloop()



def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1280x720")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    640.0, 413.0,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = formal,
    relief = "flat")

b0.place(
    x = 58, y = 286,
    width = 322,
    height = 61)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 479, y = 286,
    width = 322,
    height = 61)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 58, y = 422,
    width = 322,
    height = 61)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = 479, y = 422,
    width = 322,
    height = 61)

img4 = PhotoImage(file = f"img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b4.place(
    x = 900, y = 422,
    width = 322,
    height = 61)

img5 = PhotoImage(file = f"img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b5.place(
    x = 900, y = 286,
    width = 322,
    height = 61)

window.resizable(False, False)
window.mainloop()


