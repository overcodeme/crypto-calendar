import tkinter as tk
from tkinter import messagebox, simpledialog
from tkcalendar import Calendar


class EventApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Crypto Calendar')

        self.calendar = Calendar(master, selectmode='day', year=2025, month=1, day=1)
        self.calendar.pack(pady=20)

        self.add_event_button = tk.Button(master, text='Добавить событие', command=self.add_event)
        self.add_event_button.pack(pady=10)

        self.view_events_button = tk.Button(master, text='Просмотреть событие', command=self.view_events)
        self.view_events_button.pack(pady=10)

        self.event = {}

    
    def add_event(self):
        date = self.calendar.get_date()
        event = simpledialog.askstring('Добавить событие', 'Введите событие:')

        if event:
            if date in self.events:
                self.events[date].append(event)
            else:
                self.events[date] = event
            messagebox.showinfo('Добавлено', 'Событие добавлено!')


    def view_events(self):
        date = self.calendar.get_date()
        events_for_date = self.events.get(date, [])

        if events_for_date:
            events_text = '\n'.join(events_for_date)
            messagebox.showinfo(f'События на {date}', events_text)
        else:
            messagebox.showinfo(f'События на {date}', 'Нет событий на этот день')


if __name__ == '__main__':
    root = tk.Tk()
    app = EventApp(root)
    root.mainloop()