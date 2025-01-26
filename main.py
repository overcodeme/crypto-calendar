import os
import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, simpledialog
from tkcalendar import Calendar
from PIL import Image, ImageTk



class EventApp:
    def __init__(self, master):
        self.master = master

        self.DATA_FOLDER = 'data'
        self.EVENTS_FILE = os.path.join(self.DATA_FOLDER, 'events.json')
        self.events = self.load_events()

        self.CALENDAR = Calendar(master, selectmode='day', year=2025, month=1, day=1)
        self.CALENDAR.pack(pady=20)

        self.ADD_BUTTON = ttk.Button(master, text='Добавить', command=self.add_event)
        self.ADD_BUTTON.pack(pady=10)

        self.VIEW_BUTTON = ttk.Button(master, text='Просмотреть', command=self.view_events)
        self.VIEW_BUTTON.pack(pady=10)

        # Текстовый виджет для ввода текущего события
        self.event_text = tk.Text(master, height=10, width=50)
        self.event_text.pack(pady=20)


    def load_events(self):
        if os.path.exists(self.EVENTS_FILE):
            with open(self.EVENTS_FILE, 'r') as file:
                return json.load(file)
        return {}        


    def save_events(self):
        with open(self.EVENTS_FILE, 'w') as file:
            json.dump(self.events, file)


    def add_event_dialog(self):
        dialog = tk.Toplevel(self.master)
        dialog.title('Добавить событие')
        dialog.geometry('400x300')

        label = tk.Label(dialog, text='Введите событие')
        label.pack(pady=10)

        self.event_text = tk.Text(dialog, height=10)
        self.event_text.pack(pady=10)

        add_event_button = tk.Text(dialog, height=10)
        add_event_button.pack(pady=20)

    
    def add_event(self):
        date = self.CALENDAR.get_date()
        event = self.event_text.get('1.0', tk.END).strip()

        if event:
            if date in self.events:
                self.events[date].append(event)
            else:
                self.events[date] = [event]
            self.save_events()
            self.event_text.insert(tk.END, 'Событие добавлено!\n')


    def view_events(self):
        date = self.CALENDAR.get_date()
        events_for_date = self.events.get(date, [])

        self.event_text.delete(1.0, tk.END)

        if events_for_date:
            events_str = '\n'.join(events_for_date) 
            self.event_text.insert(tk.END, f"События на {date}:\n{events_str}\n")
        else:
            self.event_text.insert(tk.END, f"Нет событий на {date}.\n")
        
        print(self.events) 


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Crypto Calendar')
    root.geometry('800x600')

    icon = Image.open('static/app-icon.jpg')
    photo = ImageTk.PhotoImage(icon)
    root.iconphoto(False, photo)

    app = EventApp(root)
    root.mainloop()