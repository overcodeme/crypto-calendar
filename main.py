import tkinter as tk
from tkinter import messagebox, simpledialog
from tkcalendar import Calendar
import os
import json


class EventApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Crypto Calendar')
        self.master.geometry('800x600')

        self.data_folder = 'data'
        self.events_file = os.path.join(self.data_folder, 'events.json')
        self.events = self.load_events()

        self.calendar = Calendar(master, selectmode='day', year=2025, month=1, day=1)
        self.calendar.pack(pady=20)

        self.add_event_button = tk.Button(master, text='Добавить событие', command=self.add_event)
        self.add_event_button.pack(pady=10)

        self.view_events_button = tk.Button(master, text='Просмотреть событие', command=self.view_events)
        self.view_events_button.pack(pady=10)


    def load_events(self):
        if os.path.exists(self.events_file):
            with open(self.events_file, 'r') as file:
                return json.load(file)
        return {}        


    def save_events(self):
        with open(self.events_file, 'w') as file:
            json.dump(self.events, file)

    
    def add_event(self):
        date = self.calendar.get_date()
        event = simpledialog.askstring('Добавить событие', 'Введите событие:')

        if event:
            if date in self.events:
                self.events[date].append(event)
            else:
                self.events[date] = [event]
            messagebox.showinfo('Добавлено', 'Событие добавлено!')
            self.save_events()


    def view_events(self):
        date = self.calendar.get_date()
        events_for_date = self.events.get(date, [])

        if events_for_date:
            events_str = '\n'.join(events_for_date) 
        else:
            events_str = 'Нет событий'
        
        messagebox.showinfo("События", events_str)
        print(self.events) 



if __name__ == '__main__':
    root = tk.Tk()
    app = EventApp(root)
    root.mainloop()