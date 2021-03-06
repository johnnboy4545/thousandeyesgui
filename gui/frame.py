import tkinter as tk
from tkinter import ttk
from logon.logon import logon
from tk_functions.date_methods import gui_date_class
from request.request import thousand_api
from tk_functions.boxing import updating_box

class MainApp(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.agentId_list = thousand_api().agentId
        self.testId_list = thousand_api().testId
        self.usernames = logon().credintail

        parent.title("Thousandeyes Interface")
        parent['background']='#E7E7E7'

        ttk.Label(parent, text="User").grid(row=0)
        ttk.Label(parent, text="Start Date").grid(row=1)
        ttk.Label(parent, text="End Date").grid(row=2)
        ttk.Label(parent, text="TestID").grid(row=3)
        ttk.Label(parent, text="AgentId").grid(row=4)

        self.user = tk.StringVar()
        self.testId = tk.StringVar()
        self.agentId = tk.StringVar()

        user_entry = ttk.Combobox(parent, width = 27, textvariable = self.user)
        testid_entry = ttk.Combobox(parent, width=27, textvariable = self.testId)

        user_entry['values'] = tuple(self.usernames.keys())
        testid_entry['values'] = tuple(key['type'] for key in self.testId_list)

        user_entry.grid(row=0, column=1)
        testid_entry.grid(row=3, column=1)
        updating_box(parent,self.agentId,tuple((key['agentName'] for key in self.agentId_list)),  4, 1)

        self.entry_start_date_month = tk.IntVar(value='')
        self.entry_start_date_day = tk.IntVar(value='')
        self.entry_start_date_year = tk.IntVar(value='')
        self.entry_start_date_hour = tk.IntVar(value='')
        self.entry_start_date_minutes = tk.IntVar(value='')
        self.entry_start_am_pm = tk.StringVar()

        date_frame_entry_start = ttk.Frame(parent)
        frame_entry_month_start = ttk.Entry(date_frame_entry_start,textvariable=self.entry_start_date_month, width=2)
        frame_label_slash_1_start = ttk.Label(date_frame_entry_start, text = '/')
        frame_entry_day_start = ttk.Entry(date_frame_entry_start, textvariable=self.entry_start_date_day, width=2)
        frame_label_slash_2_start = ttk.Label(date_frame_entry_start, text='/')
        frame_entry_year_start = ttk.Entry(date_frame_entry_start, textvariable=self.entry_start_date_year, width=2)
        frame_label_space_start = ttk.Label(date_frame_entry_start, text=' ')
        frame_entry_hour_start = ttk.Entry(date_frame_entry_start, textvariable=self.entry_start_date_hour, width=2)
        frame_label_colon_start = ttk.Label(date_frame_entry_start, text=':')
        frame_entry_minute_start = ttk.Entry(date_frame_entry_start, textvariable=self.entry_start_date_minutes, width=2)
        frame_entry_am_pm = ttk.Combobox(date_frame_entry_start, textvariable=self.entry_start_am_pm, width=3)

        frame_entry_am_pm['values'] = ('am','pm')

        date_frame_entry_start.grid(row = 1, column = 1)
        frame_entry_month_start.pack(side="left")
        frame_label_slash_1_start.pack(side='left')
        frame_entry_day_start.pack(side="left")
        frame_label_slash_2_start.pack(side='left')
        frame_entry_year_start.pack(side="left")
        frame_label_space_start.pack(side="left")
        frame_entry_hour_start.pack(side="left")
        frame_label_colon_start.pack(side="left")
        frame_entry_minute_start.pack(side="left")
        frame_entry_am_pm.pack(side = 'left')

        self.entries_start = gui_date_class([frame_entry_month_start, frame_entry_day_start, frame_entry_year_start, frame_entry_hour_start, frame_entry_minute_start])

        frame_entry_month_start.bind('<KeyRelease>', lambda e: self.entries_start._check(0, 2))
        frame_entry_day_start.bind('<KeyRelease>', lambda e: self.entries_start._check(1, 2))
        frame_entry_year_start.bind('<KeyRelease>', lambda e: self.entries_start._check(2, 2))
        frame_entry_hour_start.bind('<KeyRelease>', lambda e: self.entries_start._check(3, 2))
        frame_entry_minute_start.bind('<KeyRelease>', lambda e: self.entries_start._check(4, 2))

        self.entry_end_date_month = tk.IntVar(value='')
        self.entry_end_date_day = tk.IntVar(value='')
        self.entry_end_date_year = tk.IntVar(value='')
        self.entry_end_date_hour = tk.IntVar(value='')
        self.entry_end_date_minutes = tk.IntVar(value='')
        self.entry_end_am_pm = tk.StringVar()

        date_frame_entry_end = ttk.Frame(parent)
        frame_entry_month_end = ttk.Entry(date_frame_entry_end, textvariable=self.entry_end_date_month, width=2)
        frame_label_slash_1_end = ttk.Label(date_frame_entry_end, text = '/')
        frame_entry_day_end = ttk.Entry(date_frame_entry_end, textvariable=self.entry_end_date_day, width=2)
        frame_label_slash_2_end = ttk.Label(date_frame_entry_end, text='/')
        frame_entry_year_end = ttk.Entry(date_frame_entry_end, textvariable=self.entry_end_date_year, width=2)
        frame_label_space_end = ttk.Label(date_frame_entry_end, text=' ')
        frame_entry_hour_end = ttk.Entry(date_frame_entry_end, textvariable=self.entry_end_date_hour, width=2)
        frame_label_colon_end = ttk.Label(date_frame_entry_end, text=':')
        frame_entry_minute_end = ttk.Entry(date_frame_entry_end, textvariable=self.entry_end_date_minutes, width=2)
        frame_entry_am_pm_end = ttk.Combobox(date_frame_entry_end, textvariable = self.entry_end_am_pm, width = 3)

        date_frame_entry_end.grid(row = 2, column = 1)
        frame_entry_month_end.pack(side="left")
        frame_label_slash_1_end.pack(side='left')
        frame_entry_day_end.pack(side="left")
        frame_label_slash_2_end.pack(side='left')
        frame_entry_year_end.pack(side="left")
        frame_label_space_end.pack(side="left")
        frame_entry_hour_end.pack(side="left")
        frame_label_colon_end.pack(side="left")
        frame_entry_minute_end.pack(side="left")
        frame_entry_am_pm_end.pack(side = 'left')

        frame_entry_am_pm_end['values'] = ('am', 'pm')

        self.entries_end = gui_date_class([frame_entry_month_end, frame_entry_day_end, frame_entry_year_end, frame_entry_hour_end, frame_entry_minute_end])

        frame_entry_month_end.bind('<KeyRelease>', lambda e: self.entries_end._check(0, 2))
        frame_entry_day_end.bind('<KeyRelease>', lambda e: self.entries_end._check(1, 2))
        frame_entry_year_end.bind('<KeyRelease>', lambda e: self.entries_end._check(2, 2))
        frame_entry_hour_end.bind('<KeyRelease>', lambda e: self.entries_end._check(3, 2))
        frame_entry_minute_end.bind('<KeyRelease>', lambda e: self.entries_end._check(4, 2))

        submit_button = ttk.Button(parent, text='Submit', command=self.retreive_credintails)
        submit_button.grid(row=6, column=1)
