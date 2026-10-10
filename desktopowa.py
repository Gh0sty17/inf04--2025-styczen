import tkinter as tk
from tkinter import filedialog, messagebox


def szyfruj(tekst_jawny: str, klucz: int) -> str:
    zaszyfrowane = []
    for znak in tekst_jawny:
        if znak == " " or znak == "\n":
            zaszyfrowane.append(znak)
        elif "a" <= znak <= "z":
            kod = (ord(znak) - ord("a") + klucz) % 26 + ord("a")
            zaszyfrowane.append(chr(kod))
        else:
            zaszyfrowane.append(znak)
    return "".join(zaszyfrowane)


class AplikacjaSzyfrujaca(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Szyfrowanie. Wykonane przez 00000000000")
        self.geometry("740x430")
        self.configure(bg="#5F9EA0")
        self.resizable(False, False)

        self.zaszyfrowany_tekst = ""

        self.utworz_widok()

    def rysuj_zaokraglony_prostokat(self, canvas, x1, y1, x2, y2, r=20, **kwargs):
        punkty = [
            x1 + r, y1,
            x1 + r, y1,
            x2 - r, y1,
            x2 - r, y1,
            x2, y1,
            x2, y1 + r,
            x2, y1 + r,
            x2, y2 - r,
            x2, y2 - r,
            x2, y2,
            x2 - r, y2,
            x2 - r, y2,
            x1 + r, y2,
            x1 + r, y2,
            x1, y2,
            x1, y2 - r,
            x1, y2 - r,
            x1, y1 + r,
            x1, y1 + r,
            x1, y1
        ]
        return canvas.create_polygon(punkty, **kwargs, smooth=True)

    def utworz_widok(self):
        lbl_klucz = tk.Label(
            self,
            text="Podaj wartość klucza",
            font=("Segoe UI", 15),
            bg="#5F9EA0",
            fg="#FAEBD7"
        )
        lbl_klucz.place(x=25, y=20)

        self.entry_klucz = tk.Entry(
            self,
            font=("Segoe UI", 11),
            width=8,
            justify="center",
            relief="flat"
        )
        self.entry_klucz.place(x=145, y=65, width=55, height=24)

        lbl_tekst = tk.Label(
            self,
            text="Podaj tekst",
            font=("Segoe UI", 15),
            bg="#5F9EA0",
            fg="#FAEBD7"
        )
        lbl_tekst.place(x=25, y=115)

        self.txt_tekst = tk.Text(
            self,
            font=("Segoe UI", 11),
            relief="flat",
            wrap="word"
        )
        self.txt_tekst.place(x=25, y=165, width=280, height=210)

        btn_szyfruj = tk.Button(
            self,
            text="Zaszyfruj",
            font=("Segoe UI", 10),
            bg="#ADD8E6",
            command=self.obsluga_szyfrowania,
            relief="groove",
            cursor="hand2"
        )
        btn_szyfruj.place(x=340, y=260, width=75, height=30)

        lbl_szyfr = tk.Label(
            self,
            text="Tekst zaszyfrowany",
            font=("Segoe UI", 15),
            bg="#5F9EA0",
            fg="#FAEBD7"
        )
        lbl_szyfr.place(x=435, y=20)

        self.canvas_wynik = tk.Canvas(
            self,
            width=280,
            height=265,
            bg="#5F9EA0",
            highlightthickness=0
        )
        self.canvas_wynik.place(x=435, y=65)

        self.rysuj_zaokraglony_prostokat(
            self.canvas_wynik,
            5, 5, 275, 260,
            r=25,
            outline="#FAEBD7",
            fill="#5F9EA0",
            width=2
        )

        self.tekst_wyniku_id = self.canvas_wynik.create_text(
            18, 18,
            anchor="nw",
            text="",
            fill="#F0F8FF",
            font=("Segoe UI", 11),
            width=245
        )

        btn_zapisz = tk.Button(
            self,
            text="Zapisz szyfr w pliku",
            font=("Segoe UI", 10),
            bg="#ADD8E6",
            command=self.obsluga_zapisu,
            relief="groove",
            cursor="hand2"
        )
        btn_zapisz.place(x=480, y=365, width=190, height=30)

    def obsluga_szyfrowania(self):
        tekst = self.txt_tekst.get("1.0", tk.END)
        if tekst.endswith("\n"):
            tekst = tekst[:-1]

        klucz_str = self.entry_klucz.get().strip()

        try:
            klucz = int(klucz_str)
        except ValueError:
            klucz = 0
            self.entry_klucz.delete(0, tk.END)
            self.entry_klucz.insert(0, "0")

        self.zaszyfrowany_tekst = szyfruj(tekst, klucz)
        self.canvas_wynik.itemconfig(self.tekst_wyniku_id, text=self.zaszyfrowany_tekst)

    def obsluga_zapisu(self):
        if not self.zaszyfrowany_tekst:
            messagebox.showwarning("Uwaga", "Brak tekstu do zapisania! Najpierw zaszyfruj tekst.")
            return

        sciezka_pliku = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Pliki tekstowe", "*.txt"), ("Wszystkie pliki", "*.*")],
            title="Zapisz zaszyfrowany tekst"
        )

        if sciezka_pliku:
            with open(sciezka_pliku, "w", encoding="utf-8") as plik:
                plik.write(self.zaszyfrowany_tekst)
            messagebox.showinfo("Sukces", "Zaszyfrowany tekst został zapisany pomyślnie.")


if __name__ == "__main__":
    app = AplikacjaSzyfrujaca()
    app.mainloop()