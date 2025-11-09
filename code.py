import tkinter as tk
from tkinter import ttk
import time
import pickle
import heapq
from tkinter import colorchooser
from tkinter import simpledialog
from tkinter import messagebox







# Wörterbuch für Buchstabenübersetzungen in der ersten Sprache
buchstaben_uebersetzungen_ardenvell = {
    "a": "l",
    "b": "i",
    "c": "s",
    "d": "r",
    "e": "k",
    "f": "d",
    "g": "v",
    "h": "w",
    "i": "g",
    "j": "n",
    "k": "z",
    "l": "n",
    "m": "n",
    "n": "x",
    "o": "y",
    "p": "p",
    "q": "",
    "r": "q",
    "s": "b",
    "t": "d",
    "u": "e",
    "v": "t",
    "w": "a",
    "x": "c",
    "y": "c",
    "z": "u",
    "A": "L",
    "B": "I",
    "C": "S",
    "D": "R",
    "E": "K",
    "F": "D",
    "G": "V",
    "H": "W",
    "I": "G",
    "J": "N",
    "K": "Z",
    "L": "N",
    "M": "N",
    "N": "X",
    "O": "Y",
    "P": "P",
    "Q": "",
    "R": "Q",
    "S": "B",
    "T": "D",
    "U": "E",
    "V": "T",
    "W": "A",
    "X": "C",
    "Y": "C",
    "Z": "U",
    # ... (Ihre Übersetzungen für die Ardenvellische Sprache hier)
}

buchstaben_uebersetzungen_ardenvell_to_german = {
    "l": "a",
    "i": "b",
    "s": "c",
    "r": "d",
    "k": "e",
    "d": "f",
    "v": "g",
    "w": "h",
    "g": "i",
    "n": "j",
    "z": "k",
    "x": "n",
    "y": "o",
    "p": "p",
    "": "q",
    "q": "r",
    "b": "s",
    "d": "t",
    "e": "u",
    "t": "v",
    "a": "w",
    "c": "x",
    "c": "y",
    "u": "z",
    "L": "A",
    "I": "B",
    "S": "C",
    "R": "D",
    "K": "E",
    "D": "F",
    "V": "G",
    "W": "H",
    "G": "I",
    "N": "J",
    "Z": "K",
    "X": "N",
    "Y": "O",
    "P": "P",
    "": "Q",
    "Q": "R",
    "B": "S",
    "D": "T",
    "E": "U",
    "T": "V",
    "A": "W",
    "C": "X",
    "C": "Y",
    "U": "Z"
    # ... (Ihre Übersetzungen für die Ardenvellische Sprache hier)
}




buchstaben_uebersetzungen_sued = {
    'a': 'u',
    'b': 'g',
    'c': 'z',
    'd': 'p',
    'e': 'o',
    'f': 'm',
    'g': 'b',
    'h': 'h',
    'i': 'i',
    'j': 's',
    'k': 'x',
    'l': 'n',
    'm': 'c',
    'n': 'r',
    'o': 'e',
    'p': 'd',
    'q': 'q',
    'r': 'f',
    's': 'm',
    't': 'd',
    'u': 'a',
    'v': 'v',
    'w': 'v',
    'x': 'p',
    'y': 'i',
    'z': 'c',
    'ä': 'ue',
    'ö': 'oe',
    'ü': 'ae',
    'ß': 'ss',
    'A': 'U',
    'B': 'G',
    'C': 'Z',
    'D': 'P',
    'E': 'O',
    'F': 'M',
    'G': 'B',
    'H': 'H',
    'I': 'I',
    'J': 'S',
    'K': 'X',
    'L': 'N',
    'M': 'C',
    'N': 'R',
    'O': 'E',
    'P': 'D',
    'Q': 'Q',
    'R': 'F',
    'S': 'M',
    'T': 'D',
    'U': 'A',
    'V': 'V',
    'W': 'V',
    'X': 'P',
    'Y': 'I',
    'Z': 'C',
    'Ä': 'UE',
    'Ö': 'OE',
    'Ü': 'AE',
    'ß': 'SS',  
   
    # ... (Ihre Übersetzungen für die erste Sprache hier)
}

buchstaben_uebersetzungen_sued_to_german = {
    'u': 'a',
    'g': 'b',
    'z': 'c',
    'p': 'd',
    'o': 'e',
    'm': 'f',
    'b': 'g',
    'h': 'h',
    'i': 'i',
    's': 'j',
    'x': 'k',
    'n': 'l',
    'c': 'm',
    'r': 'n',
    'e': 'o',
    'd': 'p',
    'q': 'q',
    'f': 'r',
    'm': 's',
    'd': 't',
    'a': 'u',
    'v': 'v',
    'v': 'w',
    'p': 'x',
    'i': 'y',
    'c': 'z',
    'ue': 'ä',
    'oe': 'ö',
    'ae': 'ü',
    'ss': 'ß',
    'U': 'A',
    'G': 'B',
    'Z': 'C',
    'P': 'D',
    'O': 'E',
    'M': 'F',
    'B': 'G',
    'H': 'H',
    'I': 'I',
    'S': 'J',
    'X': 'K',
    'N': 'L',
    'C': 'M',
    'R': 'N',
    'E': 'O',
    'D': 'P',
    'Q': 'Q',
    'F': 'R',
    'M': 'S',
    'D': 'T',
    'A': 'U',
    'V': 'V',
    'V': 'W',
    'P': 'X',
    'I': 'Y',
    'C': 'Z',
    'UE': 'Ä',
    'OE': 'Ö',
    'AE': 'Ü',
    'SS': 'ß',
    # ... (Ihre Übersetzungen für die erste Sprache hier)
}


# Wörterbuch für Buchstabenübersetzungen in der zweiten Sprache
buchstaben_uebersetzungen_ost = {
    "a": "i",
    "b": "p",
    "c": "k",
    "d": "t",
    "e": "ä",
    "f": "v",
    "g": "q",
    "h": "h",
    "i": "y",
    "j": "i",
    "k": "c",
    "l": "w",
    "m": "n",
    "n": "m",
    "o": "u",
    "p": "b",
    "q": "g",
    "r": "x",
    "s": "ß",
    "t": "d",
    "u": "o",
    "v": "f",
    "w": "v",
    "x": "ks",
    "y": "ü",
    "z": "ts",
    "ä": "e",
    "ö": "ü",
    "ü": "ö",
    "ß": "skh",
    "A": "I",
    "B": "P",
    "C": "K",
    "D": "T",
    "E": "Ä",
    "F": "V",
    "G": "Q",
    "H": "H",
    "I": "Y",
    "J": "I",
    "K": "C",
    "L": "W",
    "M": "N",
    "N": "M",
    "O": "U",
    "P": "B",
    "Q": "G",
    "R": "X",
    "S": "ß",
    "T": "D",
    "U": "O",
    "V": "F",
    "W": "V",
    "X": "KS",
    "Y": "Ü",
    "Z": "TS",
    "Ä": "E",
    "Ö": "Ü",
    "Ü": "Ö",
    "ß": "SKH",
    # ... (Ihre Übersetzungen für die zweite Sprache hier)
}
balken = 0
buchstaben_uebersetzungen_ost_to_german = {
    "i": "a",
    "p": "b",
    "k": "c",
    "t": "d",
    "ä": "e",
    "v": "f",
    "q": "g",
    "h": "h",
    "y": "i",
    "i": "j",
    "c": "k",
    "w": "l",
    "n": "m",
    "m": "n",
    "u": "o",
    "b": "p",
    "g": "q",
    "x": "r",
    "ß": "s",
    "d": "t",
    "o": "u",
    "f": "v",
    "v": "w",
    "ks": "x",
    "ü": "y",
    "ts": "z",
    "e": "ä",
    "ü": "ö",
    "ö": "ü",
    "skh": "ß",
    "I": "A",
    "P": "B",
    "K": "C",
    "T": "D",
    "Ä": "E",
    "V": "F",
    "Q": "G",
    "H": "H",
    "Y": "J",
    "I": "J",
    "C": "K",
    "W": "L",
    "N": "M",
    "M": "N",
    "U": "O",
    "B": "P",
    "G": "Q",
    "X": "R",
    "ß": "S",
    "D": "T",
    "O": "U",
    "F": "V",
    "V": "W",
    "KS": "X",
    "Ü": "Y",
    "TS": "Z",
    "E": "Ä",
    "Ü": "Ö",
    "Ö": "Ü",
    "SKH": "ß"
    # ... (Ihre Übersetzungen für die zweite Sprache hier)
}
global a, b, c, e, f, g, h, i, j, k, l, m, n, oo, p, q, r, s, t, u, v, w, x, y, z

a = ""

b = ""
c = ""
d = ""
e = ""
f = ""
g = ""
h = ""
i = ""
j = ""
k = ""
l = ""
m = ""
n = ""
oo = ""
p =  ""
q = ""
r = ""
s = ""
t = ""
u = ""
v = ""
w = ""
x = ""
y = ""
z = ""

class Netzplaner:
    def __init__(self, master):
        self.master = master
        self.master.title("Slimeplaner")
        
        self.canvas = tk.Canvas(self.master, bg="white", width=600, height=400)
        self.canvas.pack(expand=True, fill=tk.BOTH)
        self.add_intermediate_stop_button = tk.Button(self.master, text="Umsteigemöglichkeit hinzufügen", command=self.add_intermediate_stop_prompt)
        self.add_intermediate_stop_button.pack()
        self.stations = {}  # Dictionary zur Verfolgung von Stationen und ihren Koordinaten
        self.lines = []
        self.current_line = []
        self.build_mode = True  # Bau-Modus aktiviert

        self.entry = tk.Entry(self.master)
        self.entry.pack(side=tk.TOP, fill=tk.X)  # Entry-Feld oben am Fenster hinzufügen

        self.canvas.bind("<Button-1>", self.add_station)

        # Button zum Erstellen einer Linie hinzufügen
        self.create_line_button = tk.Button(self.master, text="Linie erstellen", command=self.create_line)
        self.create_line_button.pack()

        # Button zum Ändern der Linienfarbe hinzufügen
        self.choose_color_button = tk.Button(self.master, text="Linienfarbe wählen", command=self.choose_color)
        self.choose_color_button.pack()

        # Button zum Speichern und Laden hinzufügen
        self.save_load_button = tk.Button(self.master, text="Speichern/Laden", command=self.save_load)
        self.save_load_button.pack()

        # Schalter für den Bau-Modus
        self.build_mode_button = tk.Button(self.master, text="Bau-Modus deaktivieren", command=self.toggle_build_mode)
        self.build_mode_button.pack()

        self.line_color = "red"  # Standardfarbe
        
        # Buttons für die Bewegung des Canvas
        self.up_button = tk.Button(self.master, text="↑", command=lambda: self.move_canvas(0, -10))
        self.up_button.pack(side=tk.RIGHT)
        self.down_button = tk.Button(self.master, text="↓", command=lambda: self.move_canvas(0, 10))
        self.down_button.pack(side=tk.RIGHT)
        self.left_button = tk.Button(self.master, text="←", command=lambda: self.move_canvas(-10, 0))
        self.left_button.pack(side=tk.RIGHT)
        self.right_button = tk.Button(self.master, text="→", command=lambda: self.move_canvas(10, 0))
        self.right_button.pack(side=tk.RIGHT)
        self.routebutton = ttk.Button(self.master, text="Routenplaner öffnen", command=self.open_route_planner_window)
        self.routebutton.pack(side=tk.LEFT)

        # Tastatur-Navigation aktivieren
        self.master.bind("<Up>", lambda event: self.move_canvas(0, -10))
        self.master.bind("<Down>", lambda event: self.move_canvas(0, 10))
        self.master.bind("<Left>", lambda event: self.move_canvas(-10, 0))
        self.master.bind("<Right>", lambda event: self.move_canvas(10, 0))
        
    def open_route_planner_window(self):
        global window
        window = tk.Toplevel(self.master)
        window.title("Routenplaner")

        # Eingabefelder für Start- und Zielstationen
        start_label = tk.Label(window, text="Startstation:")
        start_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
        self.start_entry = tk.Entry(window)
        self.start_entry.grid(row=0, column=1, padx=10, pady=5)

        end_label = tk.Label(window, text="Zielstation:")
        end_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
        self.end_entry = tk.Entry(window)
        self.end_entry.grid(row=1, column=1, padx=10, pady=5)

        # Button zum Starten der Routenplanung
        calculate_button = tk.Button(window, text="Route berechnen", command=self.calculate_route)
        calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def dijkstra(self, start):
        distances = {station: float('inf') for station in self.stations}
        distances[start] = 0
        queue = [(0, start)]

        while queue:
            current_distance, current_station = heapq.heappop(queue)

            if current_distance > distances[current_station]:
                continue

            for neighbor, _ in self.get_neighbors(current_station):
                distance = current_distance + 1  # Hier könnte Ihre tatsächliche Distanz-Berechnung stehen

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))

        return distances
    def open_line_name_prompt(self):
        if not self.current_line:
            messagebox.showerror("Fehler", "Es wurde noch keine Linie erstellt.")
            return
    
        line_name = simpledialog.askstring("Linienname eingeben", "Bitte geben Sie einen Namen für die Linie ein:")
        if line_name:
            self.assign_line_name(line_name)

    def assign_line_name(self, line_name):
        if self.current_line:
            line = self.canvas.create_line([self.stations[point[2]][:2] for point in self.current_line], fill=self.line_color)
            self.lines.append((line, self.current_line, self.line_color, line_name))  # Linienname hinzufügen
            self.current_line = []

            # Linienname anzeigen
            for _, points, color, name in self.lines:
                if name == line_name:
                    for x, y, _ in points:
                        self.canvas.create_text(x, y - 10, text=line_name, anchor=tk.W, fill=color)

    def get_neighbors(self, station):
        neighbors = []
        for _, points, _ in self.lines:
            for i in range(len(points) - 1):
                if points[i][2] == station:
                    neighbors.append(points[i + 1][2])
                elif points[i + 1][2] == station:
                    neighbors.append(points[i][2])
        return [(neighbor, 1) for neighbor in neighbors]
    def calculate_route(self):
        start_station = self.start_entry.get()
        end_station = self.end_entry.get()
        window.destroy()

        if start_station not in self.stations:
            messagebox.showerror("Fehler", f"Die Startstation '{start_station}' existiert nicht.")
            return
        if end_station not in self.stations:
            messagebox.showerror("Fehler", f"Die Zielstation '{end_station}' existiert nicht.")

        distances = self.dijkstra(start_station)
        if distances[end_station] == float('inf'):
            messagebox.showinfo("Information", "Es gibt keine Verbindung zwischen den Stationen.")
        else:
            # Liste der durchlaufenden Stationen erstellen
            current_station = end_station
            route = [current_station]
            while current_station != start_station:
                for _, points, _ in self.lines:
                    for i in range(len(points) - 1):
                        if points[i + 1][2] == current_station:
                            route.append(points[i][2])
                            current_station = points[i][2]
                            break

            # Die Liste der durchlaufenden Stationen anzeigen
            messagebox.showinfo("Information", f"Die Route von {start_station} nach {end_station} führt über folgende Stationen:\n{', '.join(reversed(route))}")

    def remove_unused_points(self):
        used_points = set()
        for _, points, _ in self.lines:
            for _, _, name in points:
                used_points.add(name)

        for name in list(self.stations.keys()):
            if name not in used_points:
                del self.stations[name]
                self.canvas.delete(name)  # Den Punkt aus dem Canvas löschen

        # Punkte in der aktuellen Linie entfernen, falls sie nicht verwendet werden
        for x, y, name in self.current_line:
            if name not in used_points:
                self.current_line.remove((x, y, name))

    
    def add_station(self, event):
        if self.build_mode:  # Nur Punkt hinzufügen, wenn im Bau-Modus
            x, y = self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
            name = self.entry.get()  # Den Namen aus dem Entry-Feld abrufen
            self.entry.delete(0, "end")
            if name not in self.stations:  # Überprüfen, ob der Name bereits vorhanden ist
                self.stations[name] = (x, y)  # Station zum Dictionary hinzufügen
                self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="black")
                self.canvas.create_text(x-15, y, text=name, anchor=tk.E, tags=name)  # Namen links von den Punkten platzieren
            self.current_line.append((x, y, name))  # Namen zum Punkt hinzufügen
    def add_intermediate_stop(self, station):
        if self.build_mode:
            if station in self.stations:  # Überprüfen, ob die Station im Dictionary vorhanden ist
                x, y = self.stations[station]
                self.current_line.append((x, y, station))
            else:
                messagebox.showerror("Fehler", f"Die Station '{station}' existiert nicht.")

    def add_intermediate_stop_prompt(self):
        if self.build_mode:
            station = simpledialog.askstring("Umsteigemöglichkeit hinzufügen", "Bitte geben Sie den Namen der Station ein:")
            if station:
                self.add_intermediate_stop(station)  # Aufruf von add_intermediate_stop mit dem Namen der Station

    def get_stations_served_by_multiple_lines(self):
        stations_served_by_multiple_lines = {}
        for line, points, _ in self.lines:
            for _, _, name in points:
                if name in stations_served_by_multiple_lines:
                    stations_served_by_multiple_lines[name].append(line)
                else:
                    stations_served_by_multiple_lines[name] = [line]
        return {station: lines for station, lines in stations_served_by_multiple_lines.items() if len(lines) > 1}



    def create_line(self):
        if len(self.current_line) > 1:
            line = self.canvas.create_line([self.stations[point[2]][:2] for point in self.current_line], fill=self.line_color, width=3)
            self.lines.append((line, self.current_line, self.line_color))  # Farbe zur Linie hinzufügen
            self.current_line = []

    def choose_color(self):
        color = colorchooser.askcolor(title="Linienfarbe wählen")
        if color[1]:
            self.line_color = color[1]

    def save_load(self):
        self.remove_unused_points()  # Unbenutzte Punkte entfernen
        filename = "netzplan.pkl"
        if self.lines:  # Speichern
            with open(filename, "wb") as f:
                pickle.dump((self.lines, self.stations), f)
            print("Netzplan wurde gespeichert.")
        else:  # Laden
            try:
                with open(filename, "rb") as f:
                    self.lines, self.stations = pickle.load(f)
                print("Netzplan wurde geladen.")
                self.draw_lines()
            except FileNotFoundError:
                print("Es gibt keinen gespeicherten Netzplan.")

    def draw_lines(self):
        self.canvas.delete("all")  # Vor dem Zeichnen alle Elemente löschen
        for line, points, color in self.lines:
            self.canvas.create_line([self.stations[point[2]][:2] for point in points], fill=color)
            for x, y, name in points:
                self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="black")  # Punkte wieder zeichnen
                self.canvas.create_text(x-15, y, text=name, anchor=tk.E, tags=name)  # Namen links von den Punkten platzieren
                self.canvas.tag_bind(name, "<Button-1>", lambda event, name=name: self.open_line_creation_window(name))

    def open_line_creation_window(self, name):
        if self.build_mode == False:
            window = tk.Toplevel(self.master)
            window.title("Linie erstellen")
            button = tk.Button(window, text=f"Linie von {name} erstellen", command=lambda: self.start_line_creation(name))
            button.pack()

    def start_line_creation(self, name):
        self.current_line = [(x, y, n) for x, y, n in self.current_line if n == name]

    def toggle_build_mode(self):
        if self.build_mode:
            self.build_mode = False
            self.build_mode_button.config(text="Bau-Modus aktivieren")
        else:
            self.build_mode = True
            self.build_mode_button.config(text="Bau-Modus deaktivieren")

    def move_canvas(self, dx, dy):
        self.canvas.xview_scroll(dx, "units")
        self.canvas.yview_scroll(dy, "units")

    def run(self):
        self.draw_lines()
        self.master.mainloop()
try:
    with open('custom.pickle', 'rb') as filea:
        
        a = pickle.load(filea)
    with open('custom.pickle', 'rb') as fileb:
       
        b = pickle.load(fileb)
    with open('custom.pickle', 'rb') as filec:
       
        c = pickle.load(filec)
    with open('custom.pickle', 'rb') as filed:
        
        d = pickle.load(filed)
    with open('custom.pickle', 'rb') as filee:
       
        e = pickle.load(filee)
    with open('custom.pickle', 'rb') as filef:
        
        f = pickle.load(filef)
    with open('custom.pickle', 'rb') as fileg:
        
        g = pickle.load(fileg)
    with open('custom.pickle', 'rb') as fileh:
        
        h = pickle.load(fileh)
    with open('custom.pickle', 'rb') as filei:
        
        i = pickle.load(filei)
    with open('custom.pickle', 'rb') as filej:
        
        j = pickle.load(filej)
    with open('custom.pickle', 'rb') as filek:
        
        k = pickle.load(filek)
    with open('custom.pickle', 'rb') as filel:
        
        l = pickle.load(filel)
    with open('custom.pickle', 'rb') as filem:
        
        m = pickle.load(filem)
    with open('custom.pickle', 'rb') as filen:
      
        n = pickle.load(filen)
    with open('custom.pickle', 'rb') as fileo:
        
        oo = pickle.load(fileo)
    with open('custom.pickle', 'rb') as filep:
        
        p = pickle.load(filep)
    with open('custom.pickle', 'rb') as fileq:
        
        q = pickle.load(fileq)
    with open('custom.pickle', 'rb') as filer:
        
        r = pickle.load(filer)
    with open('custom.pickle', 'rb') as files:
        
        s = pickle.load(files)
    with open('custom.pickle', 'rb') as filet:
      
        t = pickle.load(filet)
    with open('custom.pickle', 'rb') as fileu:
        
        u = pickle.load(fileu)
    with open('custom.pickle-', 'rb') as filev:
       
        v = pickle.load(filev)
    with open('custom.pickle', 'rb') as filew:
       
        w = pickle.load(filew)
    with open('custom.pickle', 'rb') as filex:
       
        x = pickle.load(filex)
    with open('custom.pickle', 'rb') as filey:
        
        y = pickle.load(filey)
    with open('custom.pickle', 'rb') as filez:
                
        z = pickle.load(filez)

except FileNotFoundError:
    text = None

buchstaben_uebersetzungen_custom = {
    "a": a,
    "b": b,
    "c": c,
    "d": d,
    "e": e,
    "f": f,
    "g": g,
    "h": h,
    "i": i,
    "j": j,
    "k": k,
    "l": l,
    "m": m,
    "n": n,
    "o": oo,
    "p": p,
    "q": q,
    "r": r,
    "s": s,
    "t": t,
    "u": u,
    "v": v,
    "w": w,
    "x": x,
    "y": y,
    "z": z,
} 

ard_title = "Gainaxische Kodierung"

balken = 0  # Initialisieren der balken-Variablen
bolken = "True"  # Initialisieren der bolken-Variablen
passfertig = False
ladenfertig = False
def fertigstellen():
    global ladenfertig
    global balken, bolken
    bolken = "True"
    if ladenfertig == False:
        while bolken == "True":
            if balken == 100 or balken > 100:
                bolken = "False"
                print("lädt 100%")
                time.sleep(2)
                print("Laden erfolgreich")
            else:
                print("lädt " + str(balken) + "%")  # Ändern Sie den Ausdruck in str(balken)
                balken += 1
                time.sleep(0.05)
    else:
        print("Laden erfolgreich")
            
    ladenfertig = True
    if passfertig == True and ladenfertig == True:
        passwordwindow.destroy()
def nö():
    auswahl.title("Wähle zuerst eine Sprache")
    time.sleep(3)
    auswahl.title("Sprache wählen")
def articlesearchgenerell():
    global auswahl
    auswahl = tk.Tk()
    auswahl.title("Sprache wählen")
    auswahl.protocol("WM_DELETE_WINDOW", nö)
    auswahl.geometry("500x500")
    suedsleimisch = ttk.Button(auswahl, text="Südsleimisch", command=sarticlesearch)
    suedsleimisch.pack()
    ostsleimisch = ttk.Button(auswahl, text="Ostsleimisch", command=oarticlesearch)
    ostsleimisch.pack()
    abbrechen = ttk.Button(auswahl, text="Abbrechen", command=auswahl.destroy)
    abbrechen.pack()
    auswahl.mainloop()
def helpdestroy():
	helpwindow.title("Drücke den schließen Button")
	time.sleep(3)
	helpwindow.title("Hilfe(für die ausgewählte Sprache)")
def logtranslate():
    global a, b, c, d, e, f, g, h, i, j, k, l, m, n, oo, p, q, r, s, t, u, v, w, x, y, z
    a = aentry.get()
    b = bentry.get()
    c = centry.get()
    d = dentry.get()
    e = eentry.get()
    f = fentry.get()
    g = gentry.get()
    h = hentry.get()
    i = ientry.get()
    j = jentry.get()
    k = kentry.get()
    l = lentry.get()
    m = mentry.get()
    n = nentry.get()
    oo = oentry.get()
    p = pentry.get()
    q = qentry.get()
    r = rentry.get()
    s = sentry.get()
    t = tentry.get()
    u = uentry.get()
    v = ventry.get()
    w = wentry.get()
    x = xentry.get()
    y = yentry.get()
    z = zentry.get()
    file = open('custom.pickle', 'wb') 
    pickle.dump(a, filea)
    file = open('custom.pickle', 'wb')
    pickle.dump(b, fileb)
    file = open('custom.pickle', 'wb')
    pickle.dump(c, filec)
    file = open('custom.pickle', 'wb')
    pickle.dump(d, filed)
    file = open('custom.pickle', 'wb')
    pickle.dump(e, filee)
    file = open('custom.pickle', 'wb')
    pickle.dump(f, filef)
    file = open('custom.pickle', 'wb')
    pickle.dump(g, fileg)
    file = open('custom.pickle', 'wb')
    pickle.dump(h, fileh)
    file = open('custom.pickle', 'wb')
    pickle.dump(i, filei)
    file = open('custom.pickle', 'wb')
    pickle.dump(j, filej)
    file = open('custom.pickle', 'wb')
    pickle.dump(k, filek)
    file = open('custom.pickle', 'wb')
    pickle.dump(l, filel)
    file = open('custom.pickle', 'wb')
    pickle.dump(m, filem)
    file = open('custom.pickle', 'wb')
    pickle.dump(n, filen)
    file = open('custom.pickle', 'wb')
    pickle.dump(oo, fileo)
    file = open('custom.pickle', 'wb')
    pickle.dump(p, filep)
    file = open('custom.pickle', 'wb')
    pickle.dump(q, fileq)
    file = open('custom.pickle', 'wb')
    pickle.dump(r, filer)
    file = open('custom.pickle', 'wb')
    pickle.dump(s, files)
    file = open('custom.pickle', 'wb')
    pickle.dump(t, filet)
    file = open('custom.pickle', 'wb')
    pickle.dump(u, fileu)
    file = open('custom.pickle', 'wb')
    pickle.dump(v, filev)
    file = open('custom.pickle', 'wb')
    pickle.dump(w, filew)
    file = open('custom.pickle', 'wb')
    pickle.dump(x, filex)
    file = open('custom.pickle', 'wb')
    pickle.dump(y, filey)
    file = open('custom.pickle', 'wb')
    pickle.dump(z, filez)
    
                                                          
    
def custom():
    customwindow = tk.Tk()
    customwindow.title("ERSTELLE DEINE EIGENE SCHRIFT")
    global aentry, bentry, centry, dentry, eentry, fentry, gentry, hentry, ientry, jentry, kentry, lentry, mentry, nentry, oentry, pentry, qentry, rentry, sentry, tentry, uentry, ventry, wentry, xentry, yentry, zentry
    aentry = tk.Entry(customwindow, width=50)
    aentry.pack()
    bentry = tk.Entry(customwindow, width=50)
    bentry.pack()
    centry = tk.Entry(customwindow, width=50)
    centry.pack()
    dentry = tk.Entry(customwindow, width=50)
    dentry.pack()
    eentry = tk.Entry(customwindow, width=50)
    eentry.pack()
    fentry = tk.Entry(customwindow, width=50)
    fentry.pack()
    gentry = tk.Entry(customwindow, width=50)
    gentry.pack()
    hentry = tk.Entry(customwindow, width=50)
    hentry.pack()
    ientry = tk.Entry(customwindow, width=50)
    ientry.pack()
    jentry = tk.Entry(customwindow, width=50)
    jentry.pack()
    kentry = tk.Entry(customwindow, width=50)
    kentry.pack()
    lentry = tk.Entry(customwindow, width=50)
    lentry.pack()
    mentry = tk.Entry(customwindow, width=50)
    mentry.pack()
    nentry = tk.Entry(customwindow, width=50)
    nentry.pack()
    oentry = tk.Entry(customwindow, width=50)
    oentry.pack()
    pentry = tk.Entry(customwindow, width=50)
    pentry.pack()
    qentry = tk.Entry(customwindow, width=50)
    qentry.pack()
    rentry = tk.Entry(customwindow, width=50)
    rentry.pack()
    sentry = tk.Entry(customwindow, width=50)
    sentry.pack()
    tentry = tk.Entry(customwindow, width=50)
    tentry.pack()
    uentry = tk.Entry(customwindow, width=50)
    uentry.pack()
    ventry = tk.Entry(customwindow, width=50)
    ventry.pack()
    wentry = tk.Entry(customwindow, width=50)
    wentry.pack()
    xentry = tk.Entry(customwindow, width=50)
    xentry.pack()
    yentry = tk.Entry(customwindow, width=50)
    yentry.pack()
    zentry = tk.Entry(customwindow, width=50)
    zentry.pack()
    fertig = ttk.Button(customwindow, text="Fertig", command=logtranslate)
    fertig.pack()
    customwindow.mainloop()
def hilfe():
    global helpwindow
    helpwindow = tk.Tk() 
    helpwindow.title("Hilfe(für die ausgewählte Sprache)")
    helpwindow.geometry("1000x1200")
    helpwindow.configure(bg="white")
    helpwindow.protocol("WM_DELETE_WINDOW",  helpdestroy)
    global helpinput
    helpinput = tk.Entry(helpwindow, width=50)
    helpinput.pack()
    global articlelog
    articlelog = ttk.Button(helpwindow, text="OK", command=articlesearchgenerell)
    articlelog.pack()
    global helpoutput
    helpoutput = tk.Entry(helpwindow, width=50)
    helpoutput.pack()
    helpclosebutton = ttk.Button(helpwindow, text="Schließen", command=helpwindow.destroy)
    helpclosebutton.pack()
    verbius = tk.Label(helpwindow, text="Verben", bg="red")
    verbius.pack()
    praesens = tk.Label(helpwindow, text="Präsens schreibt man  mit Pronomen", bg="white")
    praesens.pack()
    praeteritum = tk.Label(helpwindow, text="Präteritum schreibt man mit PronomenB", bg="white")
    praeteritum.pack()
    perfekt = tk.Label(helpwindow, text="Perfekt schreibt man mit PronomenC", bg="white")
    perfekt.pack()
    plusquamperfekt = tk.Label(helpwindow, text="Plusquamperfekt schreibt man mit PronomenD", bg="white")
    plusquamperfekt.pack()
    futur1 = tk.Label(helpwindow, text="Futur 1 schreibt man mit Pronomen1", bg="white")
    futur1.pack()
    futur2 = tk.Label(helpwindow, text="Futur 2 schreibt man mit Pronomen2", bg="white")
    futur2.pack()
    substantivius = tk.Label(helpwindow, text="Substantive", bg="blue")
    substantivius.pack()
    tab = tk.Label(helpwindow, text="Fall          Singular         Plural", bg="white")
    tab.pack()
    nom = tk.Label(helpwindow, text="Nominativ     der/die/das      Die", bg="white")
    nom.pack()
    acc = tk.Label(helpwindow, text="Akkusativ     den              den2", bg="white")
    acc.pack()
    gen = tk.Label(helpwindow, text="Genitiv       des              Der", bg="white")
    gen.pack()
    dat = tk.Label(helpwindow, text="Dativ         dem              Den", bg="white")
    dat.pack()
    überschrift = tk.Label(helpwindow, text="Possesivpronomen:", bg="green")
    überschrift.pack()
    possesivius = tk.Label(helpwindow, text="Person   Singular     Plural", bg="white")
    possesivius.pack()
    ersteperson = tk.Label(helpwindow, text="1. ich   mein        meine", bg="white")
    ersteperson.pack()
    zweiteperson = tk.Label(helpwindow, text="2. du   dein        deine", bg="white")
    zweiteperson.pack()
    dritteperson = tk.Label(helpwindow, text="3. er/sie/es   ihr/sein    ihre/seine", bg="white")
    dritteperson.pack()

    helpwindow.mainloop()
    if s == True:
        articlelog.config(command=sarticlesearch)
    elif ostsl == True:
        articlelog.config(command=oarticlesearch)

global start

global bg_for_Label
bg_for_Label = "white"
def oarticlesearch():
    auswahl.destroy()
    details = {
        'der': {'t': '(os)', 'c': 'n', 'n': 's', 'g': 'm'},#Substantive
        'die': {'t': '(os)', 'c': 'n', 'n': 's', 'g': 'f'},
        'das': {'t': '(os)', 'c': 'n', 'n': 's', 'g': 'n'},
        'Die': {'t': '(os)', 'c': 'n', 'n': 'p', 'g': 'n'},
        'des': {'t': '(os)', 'c': 'g', 'n': 's', 'g': 'm'},
        'Der': {'t': '(os)', 'c': 'g', 'n': 'p', 'g': 'm'},
        'dem': {'t': '(os)', 'c': 'd', 'n': 's', 'g': 'n'},
        'Den': {'t': '(os)', 'c': 'd', 'n': 'p', 'g': 'n'},
        'den': {'t': '(os)', 'c': 'a', 'n': 's', 'g': 'n'},
        'den2': {'t': '(os)', 'c': 'a', 'n': 'p', 'g': 'n'},
        'mein': {'t': '(ou)', 'c': 'q', 'n': 's', 'g': 'p'},
        'meine': {'t': '(i)', 'c': 'q', 'n': 'p', 'g': 'p'},
        'ich': {'t': '(as)', 'c': '1', 'n': 'A', 'g': 'A'},#Verben
        'du': {'t': '(as)', 'c': '2', 'n': 'A', 'g': 'A'},
        'er': {'t': '(as)', 'c': '3', 'n': 'A', 'g': 'A'},
        'sie': {'t': '(as)', 'c': '3', 'n': 'A', 'g': 'A'},
        'es': {'t': '(as)', 'c': '3', 'n': 'A', 'g': 'A'},
        'wir': {'t': '(as)', 'c': '4', 'n': 'A', 'g': 'A'},
        'ihr': {'t': '(as)', 'c': '5', 'n': 'A', 'g': 'A'},
        'Sie': {'t': '(as)', 'c': '6', 'n': 'A', 'g': 'A'},
        'ichB': {'t': '(as)', 'c': '1', 'n': 'B', 'g': 'A'},#Präteritum
        'duB': {'t': '(as)', 'c': '2', 'n': 'B', 'g': 'A'},
        'erB': {'t': '(as)', 'c': '3', 'n': 'B', 'g': 'A'},
        'sieB': {'t': '(as)', 'c': '3', 'n': 'B', 'g': 'A'},
        'esB': {'t': '(as)', 'c': '3', 'n': 'B', 'g': 'A'},
        'wirB': {'t': '(as)', 'c': '4', 'n': 'B', 'g': 'A'},
        'ihrB': {'t': '(as)', 'c': '5', 'n': 'B', 'g': 'A'},
        'SieB': {'t': '(as)', 'c': '6', 'n': 'B', 'g': 'A'},
        'ichC': {'t': '(as)', 'c': '1', 'n': 'B', 'g': 'A'},#Perfekt (fast das gleiche wie Präteritum)
        'duC': {'t': '(as)', 'c': '2', 'n': 'B', 'g': 'A'},
        'erC': {'t': '(as)', 'c': '3', 'n': 'B', 'g': 'A'},
        'sieC': {'t': '(as)', 'c': '3', 'n': 'B', 'g': 'A'},
        'esC': {'t': '(as)', 'c': '3', 'n': 'B', 'g': 'A'},
        'wirC': {'t': '(as)', 'c': '4', 'n': 'B', 'g': 'A'},
        'ihrC': {'t': '(as)', 'c': '5', 'n': 'B', 'g': 'A'},
        'SieC': {'t': '(as)', 'c': '6', 'n': 'B', 'g': 'A'},
        'ichD': {'t': '(as)', 'c': '1', 'n': 'B', 'g': 'A'},#Plusquamperfekt (Das gleiche wie Präteritum)
        'duD': {'t': '(as)', 'c': '2', 'n': 'B', 'g': 'A'},
        'erD': {'t': '(as)', 'c': '3', 'n': 'B', 'g': 'A'},
        'sieD': {'t': '(as)', 'c': '3', 'n': 'B', 'g': 'A'},
        'esD': {'t': '(as)', 'c': '3', 'n': 'B', 'g': 'A'},
        'wirD': {'t': '(as)', 'c': '4', 'n': 'B', 'g': 'A'},
        'ihrD': {'t': '(as)', 'c': '5', 'n': 'B', 'g': 'A'},
        'SieD': {'t': '(as)', 'c': '6', 'n': 'B', 'g': 'A'},
        'ich1': {'t': '(as)', 'c': '1', 'n': '1', 'g': 'A'},#Futur 1
        'du1': {'t': '(as)', 'c': '2', 'n': '1', 'g': 'A'},
        'er1': {'t': '(as)', 'c': '3', 'n': '1', 'g': 'A'},
        'sie1': {'t': '(as)', 'c': '3', 'n': '1', 'g': 'A'},
        'es1': {'t': '(as)', 'c': '3', 'n': '1', 'g': 'A'},
        'wir1': {'t': '(as)', 'c': '4', 'n': '1', 'g': 'A'},
        'ihr1': {'t': '(as)', 'c': '5', 'n': '1', 'g': 'A'},
        'Sie1': {'t': '(as)', 'c': '6', 'n': '1', 'g': 'A'},
        'ich2': {'t': '(as)', 'c': '1', 'n': '1', 'g': 'A'},#Futur 2
        'du2': {'t': '(as)', 'c': '2', 'n': '1', 'g': 'A'},
        'er2': {'t': '(as)', 'c': '3', 'n': '1', 'g': 'A'},
        'sie2': {'t': '(as)', 'c': '3', 'n': '1', 'g': 'A'},
        'es2': {'t': '(as)', 'c': '3', 'n': '1', 'g': 'A'},
        'wir2': {'t': '(as)', 'c': '4', 'n': '1', 'g': 'A'},
        'ihr2': {'t': '(as)', 'c': '5', 'n': '1', 'g': 'A'},
        'Sie2': {'t': '(as)', 'c': '6', 'n': '1', 'g': 'A'},
        '1': {'t': 'Bezugswort', 'c': 'Q', 'n': '1', 'g': 'S'},
        '2': {'t': 'Bezugswort', 'c': 'Q', 'n': '2', 'g': 'S'},
        '3': {'t': 'Bezugswort', 'c': 'Q', 'n': '3', 'g': 'S'},
        'dein': {'t': '(au)', 'c': 't', 'n': 's', 'g': 'p'},
        'deine': {'t': '(ohu)', 'c': 't', 'n': 'p', 'g': 'p'},
        'sein': {'t': '(eu)', 'c': 'y', 'n': 's', 'g': 'p'},
        'ihr': {'t': '(eu)', 'c': 'y', 'n': 's', 'g': 'p'},
        'sein': {'t': '(uu)', 'c': 'y', 'n': 'p', 'g': 'p'},
        'ihr': {'t': '(uu)', 'c': 'y', 'n': 'p', 'g': 'p'},
        
    }

    endings = {
        'as': '(es)',
        'ns': '(il)',
        'np': '(es)',
        'gsm': '( di il)',
        'gpm': '(di es)',
        'ds': "(d'il)",
        'dp': '(da es)',
        'as': '(il)',
        '1A': '(ou)',
        '2A': '(a)',
        '3A': '(e)',
        '4A': '(i)',
        '5A': '(o)',
        '6A': '(u)',
        '1B': '(ouda)',
        '2B': '(ada)',
        '3B': '(eda)',          
        '4B': '(ida)',
        '5B': '(oda)',
        '6B': '(uda)',
        '11': '(oucci)',
        '21': '(acci)',
        '31': '(ecci)',
        '41': '(icci)',
        '51': '(occi)',
        '61': '(ucci)',
        'Q1': 'Endung des Bezugwortes (el)',
        'Q2': 'Endung des Bezugwortes (iacu)',
        'Q3': 'Endung des Bezugwortes (taree)',
        'qs': '(ou)',
        'qp': '(i)',
        'ts': '(au)',
        'tp': '(ohu)',
        'ys': '(eu)',
        'yp': '(uu)',
 

    }

    examples = helpinput.get().split(",")
    translated = []
    for example in examples:
        parts = example.split('-')
        if len(parts) == 1:
            translated.append(example)
            
        
        main = parts[1]
        word_grammar = details[parts[0]]
        casus_numerus = word_grammar['c'] + word_grammar['n']
        translated.append(f"{word_grammar['t']} {main}{endings[casus_numerus]}")
        translatet = " ".join(translated)
        translatet.replace("{", "")
        translatet.replace("}", "")
    helpoutput.delete(0, "end")
    helpoutput.insert(0, translatet)
    print(examples)
    print("----------------------------------------------------------------------------------------------------")
    print(translatet )
def sarticlesearch():
    auswahl.destroy()
    details = {
        'der': {'t': '(i)', 'c': 'n', 'n': 's', 'g': 'm'},#Substantive
        'die': {'t': '(i)', 'c': 'n', 'n': 's', 'g': 'f'},
        'das': {'t': '(i)', 'c': 'n', 'n': 's', 'g': 'n'},
        'Die': {'t': '(oi)', 'c': 'n', 'n': 'p', 'g': 'n'},
        'des': {'t': '(ioi)', 'c': 'g', 'n': 's', 'g': 'm'},
        'mein': {'t': '(ohoi)', 'c': 'q', 'n': 's', 'g': 'p'},
        'dein': {'t': '(soi)', 'c': 't', 'n': 's', 'g': 'p'},
        'Der': {'t': '(ioi)', 'c': 'g', 'n': 'p', 'g': 'm'},
        'meine': {'t': '(soi)', 'c': 'q', 'n': 'p', 'g': 'p'},
        'deine': {'t': '(tisoi)', 'c': 't', 'n': 'p', 'g': 'p'},
        'dem': {'t': '(oi)', 'c': 'd', 'n': 's', 'g': 'n'},
        'Den': {'t': '(isi)', 'c': 'd', 'n': 'p', 'g': 'n'},
        'den': {'t': '(umi)', 'c': 'a', 'n': 's', 'g': 'n'},
        'den2': {'t': '(osi)', 'c': 'a', 'n': 'p', 'g': 'n'},
        'ich': {'t': '(ohi)', 'c': '1', 'n': 'A', 'g': 'A'},#Verben
        'du': {'t': '(si)', 'c': '2', 'n': 'A', 'g': 'A'},
        'er': {'t': '(ti)', 'c': '3', 'n': 'A', 'g': 'A'},
        'sie': {'t': '(ti)', 'c': '3', 'n': 'A', 'g': 'A'},
        'es': {'t': '(ti)', 'c': '3', 'n': 'A', 'g': 'A'},
        'wir': {'t': '(umi)', 'c': '4', 'n': 'A', 'g': 'A'},
        'ihr': {'t': '(tisi)', 'c': '5', 'n': 'A', 'g': 'A'},
        'Sie': {'t': '(unti)', 'c': '6', 'n': 'A', 'g': 'A'},
        'ichB': {'t': '(bami)', 'c': '1', 'n': 'B', 'g': 'A'},#Präteritum
        'duB': {'t': '(basi)', 'c': '2', 'n': 'B', 'g': 'A'},
        'erB': {'t': '(bati)', 'c': '3', 'n': 'B', 'g': 'A'},
        'sieB': {'t': '(bati)', 'c': '3', 'n': 'B', 'g': 'A'},
        'esB': {'t': '(bati)', 'c': '3', 'n': 'B', 'g': 'A'},
        'wirB': {'t': '(bamumi)', 'c': '4', 'n': 'B', 'g': 'A'},
        'ihrB': {'t': '(batisi)', 'c': '5', 'n': 'B', 'g': 'A'},
        'SieB': {'t': '(bunti)', 'c': '6', 'n': 'B', 'g': 'A'},
        'ichC': {'t': '(cada bami)', 'c': '1', 'n': 'B', 'g': 'A'},#Perfekt (fast das gleiche wie Präteritum)
        'duC': {'t': '(cada basi)', 'c': '2', 'n': 'B', 'g': 'A'},
        'erC': {'t': '(cada bati)', 'c': '3', 'n': 'B', 'g': 'A'},
        'sieC': {'t': '(cada bati)', 'c': '3', 'n': 'B', 'g': 'A'},
        'esC': {'t': '(cada bati)', 'c': '3', 'n': 'B', 'g': 'A'},
        'wirC': {'t': '(cada bamumi)', 'c': '4', 'n': 'B', 'g': 'A'},
        'ihrC': {'t': '(cada batisi)', 'c': '5', 'n': 'B', 'g': 'A'},
        'SieC': {'t': '(cada bunti)', 'c': '6', 'n': 'B', 'g': 'A'},
        'ichD': {'t': '(bami)', 'c': '1', 'n': 'B', 'g': 'A'},
        '1': {'t': 'Bezugswort', 'c': 'Q', 'n': '1', 'g': 'S'},
        '2': {'t': 'Bezugswort', 'c': 'Q', 'n': '2', 'g': 'S'},
        '3': {'t': 'Bezugswort', 'c': 'Q', 'n': '3', 'g': 'S'},
     #Plusquamperfekt (Das gleiche wie Präteritum)
        'duD': {'t': '(basi)', 'c': '2', 'n': 'B', 'g': 'A'},
        'erD': {'t': '(bati)', 'c': '3', 'n': 'B', 'g': 'A'},
        'sieD': {'t': '(bati)', 'c': '3', 'n': 'B', 'g': 'A'},
        'esD': {'t': '(bati)', 'c': '3', 'n': 'B', 'g': 'A'},
        'wirD': {'t': '(bamumi)', 'c': '4', 'n': 'B', 'g': 'A'},
        'ihrD': {'t': '(batisi)', 'c': '5', 'n': 'B', 'g': 'A'},
        'SieD': {'t': '(bunti)', 'c': '6', 'n': 'B', 'g': 'A'},
        'ich1': {'t': '(euhi)', 'c': '1', 'n': '1', 'g': 'A'},#Futur 1
        'du1': {'t': '(eusi)', 'c': '2', 'n': '1', 'g': 'A'},
        'er1': {'t': '(euti)', 'c': '3', 'n': '1', 'g': 'A'},
        'sie1': {'t': '(euti)', 'c': '3', 'n': '1', 'g': 'A'},
        'es1': {'t': '(euti)', 'c': '3', 'n': '1', 'g': 'A'},
        'wir1': {'t': '(eumusi)', 'c': '4', 'n': '1', 'g': 'A'},
        'ihr1': {'t': '(eutisi)', 'c': '5', 'n': '1', 'g': 'A'},
        'Sie1': {'t': '(eunti)', 'c': '6', 'n': '1', 'g': 'A'},
        'ich2': {'t': '(cada euhi)', 'c': '1', 'n': '1', 'g': 'A'},#Futur 2
        'du2': {'t': '(cada eusi)', 'c': '2', 'n': '1', 'g': 'A'},
        'er2': {'t': '(cada euti)', 'c': '3', 'n': '1', 'g': 'A'},
        'sie2': {'t': '(cada euti)', 'c': '3', 'n': '1', 'g': 'A'},
        'es2': {'t': '(cada euti)', 'c': '3', 'n': '1', 'g': 'A'},
        'wir2': {'t': '(cada eumusi)', 'c': '4', 'n': '1', 'g': 'A'},
        'ihr2': {'t': '(cada eutisi)', 'c': '5', 'n': '1', 'g': 'A'},
        'Sie2': {'t': '(cada eunti)', 'c': '6', 'n': '1', 'g': 'A'},
        'sein': {'t': '(toi)', 'c': 'y', 'n': 's', 'g': 'p'},
        'ihr': {'t': '(toi)', 'c': 'y', 'n': 's', 'g': 'p'},
        'seine': {'t': '(untoi)', 'c': 'y', 'n': 'p', 'g': 'p'},
        'ihre': {'t': '(untoi)', 'c': 'y', 'n': 'p', 'g': 'p'},
        


    }

    endings = {
        'as': '(oso)',
        'ns': '(o)',
        'np': '(io)',
        'gsm': '(io)',
        'gpm': '(ioro)',
        'ds': '(o)',
        'dp': '(iso)',
        'as': '(umo)',
        '1A': '(oha)',
        '2A': '(sa)',
        '3A': '(ta)',
        '4A': '(uma)',
        '5A': '(tisa)',
        '6A': '(unta)',
        '1B': '(bama)',
        '2B': '(basa)',
        '3B': '(bata)',
        '4B': '(bamuma)',
        '5B': '(batisa)',
        '6B': '(bunta)',
        '11': '(euha)',
        '21': '(eusa)',
        '31': '(euta)',
        '41': '(eumusa)',
        '51': '(eutisa)',
        '61': '(eunta)',
        'Q1': 'Endung des Bezugwortes (el)',
        'Q2': 'Endung des Bezugwortes (iacu)',
        'Q3': 'Endung des Bezugwortes (taree)',
        'qs': '(oho)', 
        'ts': '(o)',
        'tp': '(io)',
        'ys': '(o)',
        'yp': '(io)',

    }
    ending = ""
    examples = helpinput.get().split(" ")
    translated = [] 
    for example in examples:
        parts = example.split('-')
        if len(parts) == 1:
            translated.append(example)
            
        
        main = parts[1]
        word_grammar = details[parts[0]]
        casus_numerus = word_grammar['c'] + word_grammar['n']
        ending = endings[casus_numerus]
       
        translated.append(f"{word_grammar['t']} {main}{ending}")
        translatet = " ".join(translated)
        translatet.replace("{", "")
        translatet.replace("}", "")
    helpoutput.delete(0, "end")
    helpoutput.insert(0, translatet)
    print(examples)
    print("----------------------------------------------------------------------------------------------------")
    print(translatet)
def controlofpassword():
    global controlofpassword
    global start
    global cont
    cont = password.get()
    if cont == "Sleim11":
        password.delete(0, "end")
        global passfertig
        passfertig = True
        print("Passwort richtig!")
        if passfertig == True and ladenfertig == True:
            
            passwordwindow.destroy()
def unsichtbarmachen():
    password.config(show="*")
    passotherlook.config(text="sichtbar machen", command=sichtbarmachen)
def sichtbarmachen():
    password.insert(0, "Sleim11")
    passotherlook.config(text="unsichtbar machen", command=unsichtbarmachen)
def beforeend():
    passwordwindow.destroy()
    quit() 
passwordwindow = tk.Tk()
passwordwindow.title("Sleim 15 Passwort")
passwordwindow.geometry("300x300")
passwordwindow.protocol("WM_DELETE_WINDOW", lambda: None)
fertig = ttk.Button(passwordwindow, text="Starten des Ladevorgangs", command=fertigstellen)
fertig.pack()
fortschrittsbalken = tk.Entry(passwordwindow, width=balken)
fortschrittsbalken.place(x=0,y=50)

passlabel = tk.Label(passwordwindow, text="Passwort:", bg="white")
password = tk.Entry(passwordwindow, width=50, show="*")
passlabel.pack()
password.pack()
passotherlook = ttk.Button(passwordwindow, text="Sichtbar", command=sichtbarmachen)

passcontrol = ttk.Button(passwordwindow, text="OK", command=controlofpassword)
passcontrol.pack()
beforeendbutton = ttk.Button(passwordwindow, text="Schließen", command=beforeend)
beforeendbutton.pack()
passwordwindow.mainloop()



def enter(event=None):
    global articlevariabl
    articlevariabl = False 
    befehl = command.get()
    global ard_title 
    global bg_for_Label
    global bg_for_Label
    bg_for_Label = "white"
    ard_title = "Gainaxische Kodierung"
    if befehl == "bg=black":
        start.configure(bg="black")
        bg_for_Label = "white"
    elif befehl == "bg=white":
        start.configure(bg="white")
        bg_for_Label = "white"
    elif befehl == "bg=grey":
        start.configure(bg="grey")
        bg_for_Label = "grey"
    elif befehl == "bg=blue":
        start.configure(bg="blue")
        bg_for_Label = "blue"
    elif befehl == "bg=green":
        start.configure(bg="green")
        bg_for_Label = "green"
    elif befehl == "bg=yellow":
        start.configure(bg="yellow")
        bg_for_Label = "yellow"
    elif befehl == "bg=orange":
        start.configure(bg="orange")
        bg_for_Label = "orange"
    elif befehl == "bg=red":
        start.configure(bg="red")
        bg_for_Label = "red"
    elif befehl == "bg=rose":
        start.configure(bg="pink")
        bg_for_Label = "pink"
    elif befehl == "bg=purple":
        start.configure(bg="purple")
        bg_for_Label = "purple"
    elif befehl == "bg=brown":
        start.configure(bg="brown")
        bg_for_Label = "brown"
    elif befehl == "bg=cyan":
        start.configure(bg="cyan")
        bg_for_Label = "cyan"
    elif befehl == "bg=lightblue":
        start.configure(bg="lightblue")
        bg_for_Label = "lightblue"
    elif befehl == "bg=lightgreen":
        start.configure(bg="lightgreen")
        bg_for_Label = "lightgreen"
    elif befehl == "Ardenvellisch":
        ard_title = "Ardenvellisch"
    elif befehl == "Gainaxische Kodierung":
        ard_title = "Gainaxische Kodierung"
    elif befehl == "close":
        print("Programm wird beendet.")
        start.destroy()
    elif befehl == "article":
        hilfe()
        
    elif befehl == "bg=dark_orange":
        start.configure(bg="#d9381e")
        bg_for_Label = "#d9381e"
    elif befehl == "bg=dark_blue":
        start.configure(bg="#000080")
        bg_for_Label = "#00008b"
    elif befehl == "bg=dark_green":
        start.configure(bg="#006400")
        bg_for_Label = "#006400"
    elif befehl == "bg=dark_red":
        start.configure(bg="#CD0000")
        bg_for_Label = "#8b0000"
    elif befehl == "bg=dark_purple":
        start.configure(bg="#800080")
        bg_for_Label = "#800080"
    elif befehl == "bg=dark_brown":
        start.configure(bg="#8b0000")
        bg_for_Label = "#a9a9a9"
    elif befehl == "bg=dark_cyan":
        start.configure(bg="dark_cyan")
        bg_for_Label = "dark_cyan"
    elif befehl == "bg=magenta":
        start.configure(bg="magenta")
        bg_for_Label = "magenta"
    elif befehl == "Article True":
        articlevariabl = True
    elif befehl == "Article False":
        articlevariabl = False
    elif befehl == "Hilfe":
        hilfe()
    elif befehl == "Südsleimisch":
        uebersetzungen = buchstaben_uebersetzungen_sued
    elif befehl == "Gainaxische Kodierung" or befehl == "Ardenvellisch":
        uebersetzungen = buchstaben_uebersetzungen_ardenvell
    elif befehl == "Ostsleimisch" or befehl == "O":
        uebersetzungen = buchstaben_uebersetzungen_ost
    elif befehl == "übersetzen" or befehl == "translate":
        uebersetzen()
    elif befehl.startswith("print-"):
        # Ausgabe des Teils des Texts nach "print-"
        output_text = befehl[len("print-"):]
        print(output_text)
    elif befehl == "custom":
        custom()
    elif befehl == "custom True":
        customlanguage()
    elif befehl == "Netzplaner":
        




        # pylint:disable= 'inconsistent use of tabs and spaces in indentation (<unknown>, line 84)'
        import tkinter as tk
        from tkinter import colorchooser, simpledialog, messagebox,ttk
        import pickle
        import heapq


        class Netzplaner:
            def __init__(self, master):
                self.master = master
                self.master.title("Slimeplaner")
                
                self.canvas = tk.Canvas(self.master, bg="white", width=600, height=400)
                self.canvas.pack(expand=True, fill=tk.BOTH)
                self.add_intermediate_stop_button = tk.Button(self.master, text="Umsteigemöglichkeit hinzufügen", command=self.add_intermediate_stop_prompt)
                self.add_intermediate_stop_button.pack()
                self.stations = {}  # Dictionary zur Verfolgung von Stationen und ihren Koordinaten
                self.lines = []
                self.current_line = []
                self.build_mode = True  # Bau-Modus aktiviert

                self.entry = tk.Entry(self.master)
                self.entry.pack(side=tk.TOP, fill=tk.X)  # Entry-Feld oben am Fenster hinzufügen

                self.canvas.bind("<Button-1>", self.add_station)

                # Button zum Erstellen einer Linie hinzufügen
                self.create_line_button = tk.Button(self.master, text="Linie erstellen", command=self.create_line)
                self.create_line_button.pack()

                # Button zum Ändern der Linienfarbe hinzufügen
                self.choose_color_button = tk.Button(self.master, text="Linienfarbe wählen", command=self.choose_color)
                self.choose_color_button.pack()

                # Button zum Speichern und Laden hinzufügen
                self.save_load_button = tk.Button(self.master, text="Speichern/Laden", command=self.save_load)
                self.save_load_button.pack()

                # Schalter für den Bau-Modus
                self.build_mode_button = tk.Button(self.master, text="Bau-Modus deaktivieren", command=self.toggle_build_mode)
                self.build_mode_button.pack()

                self.line_color = "red"  # Standardfarbe
                
                # Buttons für die Bewegung des Canvas
                self.up_button = tk.Button(self.master, text="↑", command=lambda: self.move_canvas(0, -10))
                self.up_button.pack(side=tk.RIGHT)
                self.down_button = tk.Button(self.master, text="↓", command=lambda: self.move_canvas(0, 10))
                self.down_button.pack(side=tk.RIGHT)
                self.left_button = tk.Button(self.master, text="←", command=lambda: self.move_canvas(-10, 0))
                self.left_button.pack(side=tk.RIGHT)
                self.right_button = tk.Button(self.master, text="→", command=lambda: self.move_canvas(10, 0))
                self.right_button.pack(side=tk.RIGHT)
                self.routebutton = ttk.Button(self.master, text="Routenplaner öffnen", command=self.open_route_planner_window)
                self.routebutton.pack(side=tk.LEFT)

                # Tastatur-Navigation aktivieren
                self.master.bind("<Up>", lambda event: self.move_canvas(0, -10))
                self.master.bind("<Down>", lambda event: self.move_canvas(0, 10))
                self.master.bind("<Left>", lambda event: self.move_canvas(-10, 0))
                self.master.bind("<Right>", lambda event: self.move_canvas(10, 0))
                
            def open_route_planner_window(self):
                global window
                window = tk.Toplevel(self.master)
                window.title("Routenplaner")

                # Eingabefelder für Start- und Zielstationen
                start_label = tk.Label(window, text="Startstation:")
                start_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
                self.start_entry = tk.Entry(window)
                self.start_entry.grid(row=0, column=1, padx=10, pady=5)

                end_label = tk.Label(window, text="Zielstation:")
                end_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
                self.end_entry = tk.Entry(window)
                self.end_entry.grid(row=1, column=1, padx=10, pady=5)

                # Button zum Starten der Routenplanung
                calculate_button = tk.Button(window, text="Route berechnen", command=self.calculate_route)
                calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

            def dijkstra(self, start):
                distances = {station: float('inf') for station in self.stations}
                distances[start] = 0
                queue = [(0, start)]

                while queue:
                    current_distance, current_station = heapq.heappop(queue)

                    if current_distance > distances[current_station]:
                        continue

                    for neighbor, _ in self.get_neighbors(current_station):
                        distance = current_distance + 1  # Hier könnte Ihre tatsächliche Distanz-Berechnung stehen

                        if distance < distances[neighbor]:
                            distances[neighbor] = distance
                            heapq.heappush(queue, (distance, neighbor))

                return distances
            def open_line_name_prompt(self):
                if not self.current_line:
                    messagebox.showerror("Fehler", "Es wurde noch keine Linie erstellt.")
                    return
            
                line_name = simpledialog.askstring("Linienname eingeben", "Bitte geben Sie einen Namen für die Linie ein:")
                if line_name:
                    self.assign_line_name(line_name)

            def assign_line_name(self, line_name):
                if self.current_line:
                    line = self.canvas.create_line([self.stations[point[2]][:2] for point in self.current_line], fill=self.line_color)
                    self.lines.append((line, self.current_line, self.line_color, line_name))  # Linienname hinzufügen
                    self.current_line = []

                    # Linienname anzeigen
                    for _, points, color, name in self.lines:
                        if name == line_name:
                            for x, y, _ in points:
                                self.canvas.create_text(x, y - 10, text=line_name, anchor=tk.W, fill=color)

            def get_neighbors(self, station):
                neighbors = []
                for _, points, _ in self.lines:
                    for i in range(len(points) - 1):
                        if points[i][2] == station:
                            neighbors.append(points[i + 1][2])
                        elif points[i + 1][2] == station:
                            neighbors.append(points[i][2])
                return [(neighbor, 1) for neighbor in neighbors]
            def calculate_route(self):
                start_station = self.start_entry.get()
                end_station = self.end_entry.get()
                window.destroy()

                if start_station not in self.stations:
                    messagebox.showerror("Fehler", f"Die Startstation '{start_station}' existiert nicht.")
                    return
                if end_station not in self.stations:
                    messagebox.showerror("Fehler", f"Die Zielstation '{end_station}' existiert nicht.")

                distances = self.dijkstra(start_station)
                if distances[end_station] == float('inf'):
                    messagebox.showinfo("Information", "Es gibt keine Verbindung zwischen den Stationen.")
                else:
                    # Liste der durchlaufenden Stationen erstellen
                    current_station = end_station
                    route = [current_station]
                    while current_station != start_station:
                        for _, points, _ in self.lines:
                            for i in range(len(points) - 1):
                                if points[i + 1][2] == current_station:
                                    route.append(points[i][2])
                                    current_station = points[i][2]
                                    break

                    # Die Liste der durchlaufenden Stationen anzeigen
                    messagebox.showinfo("Information", f"Die Route von {start_station} nach {end_station} führt über folgende Stationen:\n{', '.join(reversed(route))}")

            def remove_unused_points(self):
                used_points = set()
                for _, points, _ in self.lines:
                    for _, _, name in points:
                        used_points.add(name)

                for name in list(self.stations.keys()):
                    if name not in used_points:
                        del self.stations[name]
                        self.canvas.delete(name)  # Den Punkt aus dem Canvas löschen

                # Punkte in der aktuellen Linie entfernen, falls sie nicht verwendet werden
                for x, y, name in self.current_line:
                    if name not in used_points:
                        self.current_line.remove((x, y, name))

            
            def add_station(self, event):
                if self.build_mode:  # Nur Punkt hinzufügen, wenn im Bau-Modus
                    x, y = self.canvas.canvasx(event.x), self.canvas.canvasy(event.y)
                    name = self.entry.get()  # Den Namen aus dem Entry-Feld abrufen
                    self.entry.delete(0, "end")
                    if name not in self.stations:  # Überprüfen, ob der Name bereits vorhanden ist
                        self.stations[name] = (x, y)  # Station zum Dictionary hinzufügen
                        self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="black")
                        self.canvas.create_text(x-15, y, text=name, anchor=tk.E, tags=name)  # Namen links von den Punkten platzieren
                    self.current_line.append((x, y, name))  # Namen zum Punkt hinzufügen
            def add_intermediate_stop(self, station):
                if self.build_mode:
                    if station in self.stations:  # Überprüfen, ob die Station im Dictionary vorhanden ist
                        x, y = self.stations[station]
                        self.current_line.append((x, y, station))
                    else:
                        messagebox.showerror("Fehler", f"Die Station '{station}' existiert nicht.")

            def add_intermediate_stop_prompt(self):
                if self.build_mode:
                    station = simpledialog.askstring("Umsteigemöglichkeit hinzufügen", "Bitte geben Sie den Namen der Station ein:")
                    if station:
                        self.add_intermediate_stop(station)  # Aufruf von add_intermediate_stop mit dem Namen der Station

            def get_stations_served_by_multiple_lines(self):
                stations_served_by_multiple_lines = {}
                for line, points, _ in self.lines:
                    for _, _, name in points:
                        if name in stations_served_by_multiple_lines:
                            stations_served_by_multiple_lines[name].append(line)
                        else:
                            stations_served_by_multiple_lines[name] = [line]
                return {station: lines for station, lines in stations_served_by_multiple_lines.items() if len(lines) > 1}



            def create_line(self):
                if len(self.current_line) > 1:
                    line = self.canvas.create_line([self.stations[point[2]][:2] for point in self.current_line], fill=self.line_color)
                    self.lines.append((line, self.current_line, self.line_color))  # Farbe zur Linie hinzufügen
                    self.current_line = []

            def choose_color(self):
                color = colorchooser.askcolor(title="Linienfarbe wählen")
                if color[1]:
                    self.line_color = color[1]

            def save_load(self):
                self.remove_unused_points()  # Unbenutzte Punkte entfernen
                filename = "netzplan.pkl"
                if self.lines:  # Speichern
                    with open(filename, "wb") as f:
                        pickle.dump((self.lines, self.stations), f)
                    print("Netzplan wurde gespeichert.")
                else:  # Laden
                    try:
                        with open(filename, "rb") as f:
                            self.lines, self.stations = pickle.load(f)
                        print("Netzplan wurde geladen.")
                        self.draw_lines()
                    except FileNotFoundError:
                        print("Es gibt keinen gespeicherten Netzplan.")

            def draw_lines(self):
                self.canvas.delete("all")  # Vor dem Zeichnen alle Elemente löschen
                for line, points, color in self.lines:
                    self.canvas.create_line([self.stations[point[2]][:2] for point in points], fill=color)
                    for x, y, name in points:
                        self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="black")  # Punkte wieder zeichnen
                        self.canvas.create_text(x-15, y, text=name, anchor=tk.E, tags=name)  # Namen links von den Punkten platzieren
                        self.canvas.tag_bind(name, "<Button-1>", lambda event, name=name: self.open_line_creation_window(name))

            def open_line_creation_window(self, name):
                if self.build_mode == False:
                    window = tk.Toplevel(self.master)
                    window.title("Linie erstellen")
                    button = tk.Button(window, text=f"Linie von {name} erstellen", command=lambda: self.start_line_creation(name))
                    button.pack()

            def start_line_creation(self, name):
                self.current_line = [(x, y, n) for x, y, n in self.current_line if n == name]

            def toggle_build_mode(self):
                if self.build_mode:
                    self.build_mode = False
                    self.build_mode_button.config(text="Bau-Modus aktivieren")
                else:
                    self.build_mode = True
                    self.build_mode_button.config(text="Bau-Modus deaktivieren")

            def move_canvas(self, dx, dy):
                self.canvas.xview_scroll(dx, "units")
                self.canvas.yview_scroll(dy, "units")

            def run(self):
                self.draw_lines()
                self.master.mainloop()

        if __name__ == "__main__":
            root = tk.Tk()

            netzplaner = Netzplaner(root)
            netzplaner.run()


    else:
        print('"' + befehl + '" ist kein Befehl, bitte überprüfen Sie Ihre Eingabe!')
        
       

def uebersetze_buchstabe(buchstabe, sprache):
    if sprache == "Südsleimisch" or sprache == "S":
        uebersetzungen = buchstaben_uebersetzungen_sued
    elif sprache == "Ostsleimisch" or sprache == "O":
        uebersetzungen = buchstaben_uebersetzungen_ost
    elif sprache == "Ardenvellisch" or sprache == "A":
        uebersetzungen = buchstaben_uebersetzungen_ardenvell
    elif sprache == "Ardenvellisch zu deutsch" or sprache == "AZD":
        uebersetzungen = buchstaben_uebersetzungen_ardenvell_to_german
        sprache = "Ardenvellisch zu deutsch"
    elif sprache == "Ostsleimisch zu deutsch" or sprache == "OZD":
        uebersetzungen = buchstaben_uebersetzungen_ost_to_german
        sprache = "Ostsleimisch zu deutsch"
    elif sprache == "Südsleimisch zu deutsch" or sprache == "SZD":
        uebersetzungen = buchstaben_uebersetzungen_sued_to_german
        sprache = "Südsleimisch zu deutsch"
    elif sprache == "Custom":
        uebersetzungen = buchstaben_uebersetzungen_custom
    else:
        # Wenn die ausgewählte Sprache nicht erkannt wird, verwende die erste Sprache als Standard
        ausgabe_entry.insert(0, "Die Sprache wurde nicht erkannt. Nun ist Südsleimisch die Sprache.")
        uebersetzungen = buchstaben_uebersetzungen_sued                                                                                     
    
    return uebersetzungen.get(buchstabe, buchstabe)


def uebersetze_wort(wort, sprache):
      # Konvertiere das Wort nicht in Kleinbuchstaben, um Groß- und Kleinschreibung zu behandeln
    modifizierte_buchstaben = []
    
    in_klammern = False  # Eine Variable, um zu verfolgen, ob wir uns innerhalb von Klammern befinden
    inhalt_klammern = []  # Eine Liste, um den Inhalt der Klammern zu speichern
    
    for buchstabe in wort:
        if buchstabe == '(':
            in_klammern = True
        elif buchstabe == ')':
            in_klammern = False
            # Füge den Inhalt der Klammern zur Ausgabe hinzu
            modifizierte_buchstaben.extend(inhalt_klammern)
            # Lösche den Inhalt der Klammern
            inhalt_klammern = []
        elif in_klammern:
            inhalt_klammern.append(buchstabe)  # Füge den Buchstaben zum Inhalt der Klammern hinzu
        else:
            modifizierte_buchstaben.append(uebersetze_buchstabe(buchstabe, sprache))
    in_anf = False
    inhalt_anf = []
    for buchstabe in wort:
        if buchstabe == '[':
            in_anf = True
        elif buchstabe == ']':
            in_anf = False
            inhalt_anf = []
            modifizierte_buchstaben.extend(inhalt_klammern)
    return ''.join(modifizierte_buchstaben)

  
def customlanguage():
    global sprache
    sprache = "Custom"
    label.config(text="DEINE SPRACHE IST AUSGEWÄHLT :-)") 
    eingabe_entry.delete(0, "end")
    ausgabe_entry.delete(0, "end")
      

def ardenvell():
    global sprache
    sprache = "Ardenvellisch"
    label.config(text="Ardenvellisch ist ausgewählt.")
    add.config(text="Aboniert alle MrLuron auf YouTube!!! / liyxgkqd lnnk mrluron led cyedeik")
    eingabe_entry.delete(0, "end")
    ausgabe_entry.delete(0, "end")
    ard.config(text="wlnny aknd")
    sued.config(text="Südsleimisch")
    ost.config(text="Ostsleimisch")
    
    

   
def ardenvell_deutsch():
    global sprache
    sprache = "AZD"
    add.config(text="liyxgkqd lnnk mrluron led cyedeik / Aboniert alle MrLuron auf YouTube!!!")
    eingabe_entry.delete(0, "end")
    label.config(text="Gainaxische Kodierung zu deutsch ist ausgewählt.")
    ausgabe_entry.delete(0, "end")
    
def syso():
    global sprache
    sprache = "Südsleimisch"
    label.config(text="Südsleimisch ist ausgewählt.")
    add.config(text="Like an Sonstantins Scratchprojekte / bogorteha sonstantinio mfzfudzhdfesozxdooso")
    eingabe_entry.delete(0, "end")
    ausgabe_entry.delete(0, "end")
    sued.config(text="hunnei vondo")
    ard.config(text="Gainaxische Kodierung")
    ost.config(text="Ostsleimisch")
    
   

def syso_to_deutsch():
    global sprache
    sprache = "SZD"
    add.config(text="bogorteha sonstantinio mfzfudzhdfesozxdooso / Like an Sonstantins Scratchprojekte")
    eingabe_entry.delete(0, "end")
    label.config(text="Südsleimisch zu deutsch ist ausgewählt.")
    
   

ostsl = False
s = False
if s == True:
    ostsl = False
elif ostsl == True:
    s = False
def o():
    global sprache
    sprache = "Ostsleimisch"
    label.config(text="Ostsleimisch ist ausgewählt.")
    add.config(text="Zieht nach Irititidas / tsyähd mikh irititidas") 
    eingabe_entry.delete(0, "end")
    ausgabe_entry.delete(0, "end")
    ost.config(text="hiwwu väwd")
    ard.config(text="Gainaxische Kodierung")
    sued.config(text="Südsleimisch")
    global o
    o = True
    


def otg():
    global sprache
    sprache = "OZD"
    add.config(text="tsyähd mikh irititidas / Zieht nach Irititidas")
    eingabe_entry.delete(0, "end")
    label.config(text="Ostsleimisch zu deutsch ist ausgewählt.")
    ausgabe_entry.delete(0, "end")
    
    o = True



def uebersetzen():

    print(sprache + ":")
    
    eingabe = eingabe_entry.get()

    # Translation based on selected language
    uebersetzte_text = uebersetze_wort(eingabe, sprache)

    
    ausgabe_entry.delete(0, "end")  # Löschen Sie den aktuellen Text im Entry
    ausgabe_entry.insert(0, uebersetzte_text)  # Fügen Sie den übersetzten Text ein
    print(eingabe)
    print("-----------------------------------------------------------------------------")
    print(uebersetzte_text)





    


def beenden():
    start.destroy()
    print("Programm ordnungsgemäß geschlossen.")
    quit()




def to_german_def():
    sued.config(text="Südsleimisch zu Deutsch", command=syso_to_deutsch)
    label.config(text="Übersetzungen eventuel nich zu 100% korrekt!!!")
    ost.config(text="Aus dem Ostsleimischen in das deutsche übersetzen", command=otg)
    ard.config(text="Aus der Gainaxischen Kodierung in das deutsche übersetzen", command=ardenvell_deutsch)
    to_german.config(text="Aus dem Deutschen in eine beliebige Sprache übersetzen", command=to_slime_def)
    ausgabe_entry.delete(0, "end")
    eingabe_entry.delete(0, "end")
    

def to_slime_def():
    sued.config(text="Südsleimisch", command=syso)
    label.config(text="Dies ist ein Übersetzungsprogramm. Klammern in Ihrer Eingabe bleiben unverändert, und der Inhalt von Klammern wird nicht übersetzt.")
    ost.config(text="Ostsleimisch", command=o)
    ard.config(text="Gainaxische Kodierung", command=ardenvell)
    to_german.config(text="Von einer beliebigen Sprache in das deutsche übersetzen", command=to_german_def)
    ausgabe_entry.delete(0, "end")
    eingabe_entry.delete(0, "end")
def input(key):
    if key == "h":
        hilfe()
            
start = tk.Tk()
start.title("Sleim 15")
start.geometry("1300x800")
start.configure(bg="white")
bg_for_Label = "white"




global label
label = tk.Label(start, text="Dies ist ein Übersetzungsprogramm. Klammern in Ihrer Eingabe bleiben unverändert, und der Inhalt von Klammern wird nicht übersetzt.", bg="green")
label.pack()
helpbutton = ttk.Button(start, text="Hilfe", command=hilfe)
helpbutton.place(x=1300, y=0)
global sued
sued = ttk.Button(start, text="Südsleimisch", padding="20", command=syso)
sued.pack(fill="x")

global ost
ost = ttk.Button(start, text="Ostsleimisch", padding="20", command=o)
ost.pack(fill="x")

global ard
ard = ttk.Button(start, text=ard_title, padding="20", command=ardenvell)
ard.pack(fill="x")



global to_german
to_german = ttk.Button(start, text="Von einer beliebigen Sprache in das deutsche übersetzen", command=to_german_def)
to_german.pack()

global eingabe_entry
eingabe_entry = tk.Entry(start, width=50, text="Übersetzung")
eingabe_entry.pack()
eingabe_entry.insert(0, "Gib hier das zu übersetzende ein:")

uebersetzen_button = ttk.Button(start, text="Übersetzen", command=uebersetzen)
uebersetzen_button.pack()

global ausgabe_entry
ausgabe_entry = tk.Entry(start, width=50)
ausgabe_entry.pack()

beenden_button = ttk.Button(start, text="Beenden", padding="10", command=beenden)#2000 Zeilen (Stand Sleim 15 4.4.2024) Heute habe ich den Netzplaner intigriert
beenden_button.pack()


global command
command = tk.Entry(start, width=25)
command.place(x="00", y="00")
commant_log = ttk.Button(start, text="Enter", command=enter)
commant_log.place(x="165", y="0")

start.bind("<Return>", enter)
tippsuedueberschrift = tk.Label(start, text="Dies gilt für das Südsleimische:", bg=bg_for_Label)
tippsuedueberschrift.pack()
tippsuedverb = tk.Label(start, text="Verben:", bg="red")
tippsuedverb.pack()
tippsuedpraesens = tk.Label(start, text="Endungen des Präsens: 1.Sg: uha  2.Sg: usa  3.Sg: uta   1.Pl: umusa  2.Pl: utis  3.Pl: unta", bg=bg_for_Label)
tippsuedpraesens.pack()
tippsuedpraeteritum = tk.Label(start, text="Endungen des Präteritums: 1.Sg: iuha  2.Sg: iusa  3.Sg: iuta   1.Pl: iumusa  2.Pl: iutisa  3.Pl: iunta", bg=bg_for_Label)
tippsuedpraeteritum.pack()
tippsuedperfekt = tk.Label(start, text="Endungen des Perfekts: 1.Sg: auha  2.Sg: ausa  3.Sg: auta   1.Pl: aumusa  2.Pl: autisa  3.Pl: aunta", bg=bg_for_Label)
tippsuedperfekt.pack()
tippsuedfutur1 = tk.Label(start, text="Endungen vom ersten Futur: 1.Sg: euha  2.Sg: eusa  3.Sg: euta   1.Pl: eumusa  2.Pl: eutis  3.Pl: eunta", bg=bg_for_Label)
tippsuedfutur1.pack()
tippsuedfutur2 = tk.Label(start, text="Futur zwei: Hier musst du an das Verb im Futur 1 nur das Wort cada ranhängen", bg=bg_for_Label)
tippsuedfutur2.pack()
tippsuedplusquamperfekt = tk.Label(start, text="Endungen für das Plusquamperfekt: 1.Sg: ohuha  2.Sg: ohusa  3.Sg: ohuta   1.Pl: ohumusa  2.Pl: ohutis  3.Pl: ohunta", bg=bg_for_Label)
tippsuedplusquamperfekt.pack()
tippsuedimp = tk.Label(start, text="Endungen für den Imperativ: Sg: a Pl: teha", bg=bg_for_Label)
tippsuedimp.pack()
tippsuedsubstantiv = tk.Label(start, text="Substantive:", bg="blue")
tippsuedsubstantiv.pack()
tippsuedsubstantivsingular = tk.Label(start, text="Sg: Nom: o Gen: io Dat: o Akk: umo Abl: o Vok: eo", bg=bg_for_Label)
tippsuedsubstantivsingular.pack()
tippsuedsubstantivplural = tk.Label(start, text="Pl: Nom: io Gen: orumo Dat: iso Akk: oso Abl: iso Vok: io", bg=bg_for_Label)
tippsuedsubstantivplural.pack()
tippsuedadjektivueberschrift = tk.Label(start, text="Adjektive, Personalpronomen, Adverben, Konjunktionen und Possesivpronomen:", bg="green")
tippsuedadjektivueberschrift.pack()
adjektiv = tk.Label(start, text="Adjektiv: Hänge hierzu die Endung des beschriebenem Substantives an das Adjektiv und hänge daran ein i", bg=bg_for_Label)
adjektiv.pack()
adjst = tk.Label(start, text="Normal: i, Vergleich: ui, Am Meisten: ahui", bg=bg_for_Label)
adjst.pack()
possesiv = tk.Label(start, text="Adverben, Konjunktionen und Possesivpronomen: Hänge hier ein i dran", bg=bg_for_Label)
possesiv.pack()
personal = tk.Label(start, text="Personalpronomen haben die Endung des Wortes auf das sie siech beziehen, Genau wie Artikel.", bg=bg_for_Label)
personal.pack()





tippleere = tk.Label(start, text=" ", bg=bg_for_Label)
tippleere.pack()

tippoueberschrift = tk.Label(start, text="Dies gilt nur für das Ostsleimische:", bg=bg_for_Label)
tippoueberschrift.pack()

tippo = tk.Label(start, text="Hier musst du nichts machen!", bg=bg_for_Label)
tippo.pack()


tippkl = tk.Label(start, text="!!!Alle Endungen und Namen müssen in Klammern geschrieben werden!!!",bg="red")
tippkl.pack()

addueberschrift = tk.Label(start, text="Anzeige:", bg=bg_for_Label)
addueberschrift.pack()

global add
add =tk.Label(start, text="SPIELEN SIE THEO TOWN JETZT KOSTENLOS AUF DEM HANDY", bg="red")
add.pack()



sprache = "Südsleimisch"  # Starten Sie mit Südsleimisch als Standard




start.mainloop()
            
   
    



    







#To-Do-Liste:
#Übersetzung Markierbar machen für Copy-Paste Funktion +
#Paralele Website laufen lassen??? - 
#Schrift
#Ardenvellisch +
#Pogramm schöner machen -

#Diese liste muss abgearbeitet werden!!!!!!!!!!!!!!!!!!!!!!

























#500 Zeilen eigentlich 1000(stand Sleim 14)
