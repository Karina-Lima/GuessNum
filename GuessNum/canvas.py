import tkinter as tk
from PIL import Image, ImageDraw
import os
import subprocess

LARGURA, ALTURA = 196, 196
PATH_PROCESS = "process/process.png"


class Desenho:
    def __init__(self, root):
        self.root = root
        self.root.title("Advinha Número")

        self.canvas = tk.Canvas(self.root, bg="black", width=LARGURA, height=ALTURA)
        self.canvas.pack()

        self.imagem = Image.new("RGB", (LARGURA, ALTURA), "black")
        self.desenho = ImageDraw.Draw(self.imagem)
        self.ultimo_x, self.ultimo_y = None, None

        self.botao_submeter = tk.Button(
            self.root, text="Submeter", command=self.submeter
        )
        self.botao_submeter.pack()

        self.canvas.bind("<B1-Motion>", self.desenhar)
        self.canvas.bind("<ButtonRelease-1>", self.resetar)

    def desenhar(self, event):
        x, y = event.x, event.y
        if self.ultimo_x and self.ultimo_y:

            self.canvas.create_line(
                (self.ultimo_x, self.ultimo_y, x, y), fill="white", width=7
            )
            self.desenho.line(
                (self.ultimo_x, self.ultimo_y, x, y), fill="white", width=7
            )
        self.ultimo_x, self.ultimo_y = x, y

    def resetar(self, evento):
        self.ultimo_x, self.ultimo_y = None, None

    def submeter(self):
       
        self.imagem = self.imagem.resize((28, 28))
        self.imagem.save(PATH_PROCESS)

        print("Estamos analisando sua imagem ...")

        self.canvas.delete("all")
        self.imagem = Image.new("RGB", (LARGURA, ALTURA), "black")
        self.desenho = ImageDraw.Draw(self.imagem)

        subprocess.run(["python", "analise.py"])


root = tk.Tk()
app = Desenho(root)
root.mainloop()
