import os
import json
import tkinter as tk
from tkinter import ttk, messagebox
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


    def load_events(self):
        if os.path.exists(self.EVENTS_FILE):
            with open(self.EVENTS_FILE, 'r') as file:
                return json.load(file)
        return {}      


    def save_events(self):
        with open(self.EVENTS_FILE, 'w') as file:
            json.dump(self.events, file)


    def save_event(self, event, dialog):
        date = self.CALENDAR.get_date()

        if event:
            if date in self.events:
                self.events[date].append(event)
            else:
                self.events[date] = [event]
            self.save_events()
            messagebox.showinfo('Успех', 'Событие добавлено')
            dialog.destroy()
        else:
            messagebox.showwarning("Ошибка", "Событие не может быть пустым.")
        

    def add_event(self):
        dialog = tk.Toplevel(self.master)
        icon = Image.open('static/new-event-icon.png')
        photo = ImageTk.PhotoImage(icon)
        dialog.iconphoto(False, photo)
        dialog.title('Добавить событие')
        dialog.geometry('400x300')

        label = ttk.Label(dialog, text='Введите событие')
        label.pack(pady=10)

        event_text = tk.Text(dialog, height=10, width=30)
        event_text.pack(pady=10)

        add_event_button = ttk.Button(dialog, text='Добавить', command=lambda: self.save_event(event_text.get('1.0', tk.END).strip(), dialog))
        add_event_button.pack(pady=10)


    def view_events(self):
        date = self.CALENDAR.get_date()
        events_for_date = self.events.get(date, [])

        view_dialog = tk.Toplevel(self.master)
        view_dialog.title(f'События на {date}')
        view_dialog.geometry('400x300')

        label = ttk.Label(view_dialog, text=f'События на {date}:', font=('Helvetica', 14))
        label.pack(pady=10)

        if events_for_date:
            events_str = '\n'.join(events_for_date)
            events_label = ttk.Label(view_dialog, text=events_str)
            events_label.pack(pady=10)
        else:
            no_events_label = ttk.Label(view_dialog, text='Нет событий на этот день')
            no_events_label.pack(pady=10)


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Crypto Calendar')
    root.geometry('800x600')

    icon = Image.open('static/main-app-icon.png')
    photo = ImageTk.PhotoImage(icon)
    root.iconphoto(False, photo)

    app = EventApp(root)
    root.mainloop()