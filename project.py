# now you fucked up
from tkinter import *
import os


def aadhar_form_clicked():
    print("Aadhar Form Button Clicked")
    aadhar = page2()
    aadhar.aadhar_form()


def btn_clicked():
    print("any other button is clicked")


class page2():  # This code is for aadhar page
    def __init__(self, parent, controllor):
        tk.Frame.__init__(self, parent)
        window = Tk()

        window.geometry("1280x720")
        window.configure(bg="#ffffff")
        canvas = Canvas(
            window,
            bg="#ffffff",
            height=720,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        canvas.place(x=0, y=0)

        entry0_img = PhotoImage(
            file="D:\page2\Proxlight_Designer_Export\img_textBox0.png")
        entry0_bg = canvas.create_image(
            978.0, 54.5,
            image=entry0_img)

        entry0 = Entry(
            bd=0,
            bg="#c4c4c4",
            highlightthickness=0)

        entry0.place(
            x=699, y=32,
            width=558,
            height=43)

        entry1_img = PhotoImage(
            file="D:\page2\Proxlight_Designer_Export\img_textBox1.png")
        entry1_bg = canvas.create_image(
            1020.5, 127.5,
            image=entry1_img)

        entry1 = Entry(
            bd=0,
            bg="#c4c4c4",
            highlightthickness=0)

        entry1.place(
            x=784, y=105,
            width=473,
            height=43)

        entry2_img = PhotoImage(
            file="D:\page2\Proxlight_Designer_Export\img_textBox2.png")
        entry2_bg = canvas.create_image(
            1020.5, 205.5,
            image=entry2_img)

        entry2 = Entry(
            bd=0,
            bg="#c4c4c4",
            highlightthickness=0)

        entry2.place(
            x=784, y=183,
            width=473,
            height=43)

        entry3_img = PhotoImage(
            file="D:\page2\Proxlight_Designer_Export\img_textBox3.png")
        entry3_bg = canvas.create_image(
            978.0, 278.5,
            image=entry3_img)

        entry3 = Entry(
            bd=0,
            bg="#c4c4c4",
            highlightthickness=0)

        entry3.place(
            x=699, y=256,
            width=558,
            height=43)

        entry4_img = PhotoImage(
            file="D:\page2\Proxlight_Designer_Export\img_textBox4.png")
        entry4_bg = canvas.create_image(
            978.0, 54.5,
            image=entry4_img)

        entry4 = Entry(
            bd=0,
            bg="#c4c4c4",
            highlightthickness=0)

        entry4.place(
            x=699, y=32,
            width=558,
            height=43)

        entry5_img = PhotoImage(
            file="D:\page2\Proxlight_Designer_Export\img_textBox5.png")
        entry5_bg = canvas.create_image(
            966.0, 278.5,
            image=entry5_img)

        entry5 = Entry(
            bd=0,
            bg="#c4c4c4",
            highlightthickness=0)

        entry5.place(
            x=675, y=256,
            width=582,
            height=43)

        entry6_img = PhotoImage(
            file="D:\page2\Proxlight_Designer_Export\img_textBox6.png")
        entry6_bg = canvas.create_image(
            997.5, 356.5,
            image=entry6_img)

        entry6 = Entry(
            bd=0,
            bg="#c4c4c4",
            highlightthickness=0)

        entry6.place(
            x=738, y=334,
            width=519,
            height=43)

        entry7_img = PhotoImage(
            file="D:\page2\Proxlight_Designer_Export\img_textBox7.png")
        entry7_bg = canvas.create_image(
            997.5, 429.5,
            image=entry7_img)

        entry7 = Entry(
            bd=0,
            bg="#c4c4c4",
            highlightthickness=0)

        entry7.place(
            x=738, y=407,
            width=519,
            height=43)

        entry8_img = PhotoImage(
            file="D:\page2\Proxlight_Designer_Export\img_textBox8.png")
        entry8_bg = canvas.create_image(
            997.5, 507.5,
            image=entry8_img)

        entry8 = Entry(
            bd=0,
            bg="#c4c4c4",
            highlightthickness=0)

        entry8.place(
            x=738, y=485,
            width=519,
            height=43)

        entry9_img = PhotoImage(
            file="D:\page2\Proxlight_Designer_Export\img_textBox9.png")
        entry9_bg = canvas.create_image(
            1051.0, 580.5,
            image=entry9_img)

        entry9 = Entry(
            bd=0,
            bg="#c4c4c4",
            highlightthickness=0)

        entry9.place(
            x=845, y=558,
            width=412,
            height=43)

        entry10_img = PhotoImage(
            file="D:\page2\Proxlight_Designer_Export\img_textBox10.png")
        entry10_bg = canvas.create_image(
            1051.0, 656.5,
            image=entry10_img)

        entry10 = Entry(
            bd=0,
            bg="#c4c4c4",
            highlightthickness=0)

        entry10.place(
            x=845, y=634,
            width=412,
            height=43)

        background_img = PhotoImage(
            file="D:\page2\Proxlight_Designer_Export\\background.png")
        background = canvas.create_image(
            422.5, 360.0,
            image=background_img)

        window.resizable(False, False)
        window.mainloop()


class page1():
    pg1 = Tk()
    pg1.title('docSmith')
    pg1.geometry("1280x720")
    pg1.configure(bg="#f89a00")
    canvas = Canvas(
        pg1,
        bg="#f89a00",
        height=720,
        width=1280,
        bd=0,
        highlightthickness=0,
        relief="ridge")
    canvas.place(x=0, y=0)

    background_img = PhotoImage(file=r"D:\Export\\background.png")
    background = canvas.create_image(
        697.0, 125.0,
        image=background_img)

    img0 = PhotoImage(file=r"D:\Export\img0.png")
    b0 = Button(
        image=img0,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    b0.place(
        x=146, y=259,
        width=240,
        height=76)

    img1 = PhotoImage(file=r"D:\Export\img1.png")
    b1 = Button(
        image=img1,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    b1.place(
        x=895, y=259,
        width=240,
        height=76)

    img2 = PhotoImage(file=r"D:\Export\img2.png")
    b2 = Button(
        image=img2,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")
    b2.place(
        x=525, y=259,
        width=240,
        height=76)

    img3 = PhotoImage(file=r"D:\Export\img3.png")
    b3 = Button(
        image=img3,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    b3.place(
        x=143, y=544,
        width=240,
        height=76)

    img4 = PhotoImage(file=r"D:\Export\img4.png")
    b4 = Button(
        image=img4,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    b4.place(
        x=522, y=544,
        width=240,
        height=76)

    img5 = PhotoImage(file=r"D:\Export\ADAHAR -1.png")
    b5 = Button(
        image=img5,
        borderwidth=0,
        highlightthickness=0,
        command=aadhar_form_clicked,
        relief="flat")

    b5.place(
        x=891, y=544,
        width=244,
        height=82)

    img6 = PhotoImage(file=r"D:\Export\img6.png")
    b6 = Button(
        image=img6,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    b6.place(
        x=698, y=408,
        width=240,
        height=76)

    img7 = PhotoImage(file=r"D:\Export\img7.png")
    b7 = Button(
        image=img7,
        borderwidth=0,
        highlightthickness=0,
        command=btn_clicked,
        relief="flat")

    b7.place(
        x=328, y=410,
        width=240,
        height=76)

    pg1.resizable(False, False)
    pg1.mainloop()


'''import fpdf

data=[1,2,3,4,5,6]

pdf = fpdf.FPDF(format='letter')
pdf.add_page()
pdf.set_font("Arial", size=12)

for i in str(data):
	pdf.write(5,i)
pdf.output("testings.pdf")'''
