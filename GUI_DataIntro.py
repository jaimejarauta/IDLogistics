from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo

#############################
# Data introduction interface
#############################

data_introduction_window = tk.Tk()
data_introduction_window.title(
    "ID Logistics - Warehouse Simulation - Data Introduction"
)

data_intro_frame = tk.LabelFrame(
    data_introduction_window, text="Data Introduction", padx=20, pady=20
)
data_intro_frame.grid(row=10, column=10, padx=10, pady=10, columnspan=3)


def save_data():
    global selection_map
    global Num_Robots
    global Num_Humans
    global High_Demand_Days
    global Low_Demand_Days
    global Num_order_mission_min
    global Num_order_mission_max
    global Num_article_order_min
    global Num_article_order_max
    global T_Wave
    global Num_Mission_Wave_min
    global Num_Mission_Wave_max

    selection_map = click_map.get()
    Num_Robots = entry_num_robots.get()
    Num_Humans = entry_num_humans.get()
    High_Demand_Days = entry_High_Demand.get()
    Low_Demand_Days = entry_Low_Demand.get()
    Num_order_mission_min = entry_Order_Mission_min.get()
    Num_order_mission_max = entry_Order_Mission_max.get()
    Num_article_order_min = entry_Articles_Orders_min.get()
    Num_article_order_max = entry_Articles_Orders_max.get()
    T_Wave = entry_T_Waves.get()
    Num_Mission_Wave_min = entry_Mission_Wave_min.get()
    Num_Mission_Wave_max = entry_Mission_Wave_max.get()

    data_introduction_window.destroy()


# Title

Label_map_title = tk.Label(data_intro_frame, text="DATA INTRODUCTION")
Label_map_title.grid(row=0, column=0, padx=10, pady=10, columnspan=6)

# Map Selection

menu_options_map = [
    "Seseña",
    "Tarancón SPF",
    "Tarancón CTF",
]

Label_map_title = tk.Label(data_intro_frame, text="Map Selection")
Label_map_title.grid(row=1, column=0, padx=10, pady=10)

click_map = tk.StringVar()
click_map.set(menu_options_map[0])
menu_map = tk.OptionMenu(data_intro_frame, click_map, *menu_options_map)
menu_map.grid(row=2, column=0)

# Number of robots selection

Label_agent_title = tk.Label(data_intro_frame, text="Agents")
Label_agent_title.grid(row=1, column=1, padx=10, pady=10)

Label_Robot = tk.Label(data_intro_frame, text="Number of robots")
Label_Robot.grid(row=2, column=1, padx=10)
entry_num_robots = tk.Entry(data_intro_frame, width=15)
entry_num_robots.grid(row=2, column=2)

# Number of humans selection

Label_Humans = tk.Label(data_intro_frame, text="Number of humans")
Label_Humans.grid(row=3, column=1, padx=10)
entry_num_humans = tk.Entry(data_intro_frame, width=15)
entry_num_humans.grid(row=3, column=2)

# Demand Selection

Label_demand_title = tk.Label(data_intro_frame, text="Demand")
Label_demand_title.grid(row=1, column=3, padx=10, pady=10)

Label_High_Demand = tk.Label(data_intro_frame, text="High demand days: ")
Label_High_Demand.grid(row=2, column=3, padx=10, pady=10)
entry_High_Demand = tk.Entry(data_intro_frame, width=15)
entry_High_Demand.grid(row=2, column=4)


Label_Low_Demand = tk.Label(data_intro_frame, text="Low demand days: ")
Label_Low_Demand.grid(row=3, column=3, padx=10)
entry_Low_Demand = tk.Entry(data_intro_frame, width=15)
entry_Low_Demand.grid(row=3, column=4)

# Order Selection

Label_order_title = tk.Label(data_intro_frame, text="Orders")
Label_order_title.grid(row=4, column=0, padx=10, pady=10)

Label_Order_Mission = tk.Label(data_intro_frame, text="Orders per mission: ")
Label_Order_Mission.grid(row=5, column=0, pady=10)
entry_Order_Mission_min = tk.Entry(data_intro_frame, width=15)
entry_Order_Mission_min.grid(row=5, column=1)
entry_Order_Mission_max = tk.Entry(data_intro_frame, width=15)
entry_Order_Mission_max.grid(row=5, column=2)

Label_Articles_Orders = tk.Label(data_intro_frame, text="Articles per order: ")
Label_Articles_Orders.grid(row=6, column=0)
entry_Articles_Orders_min = tk.Entry(data_intro_frame, width=15)
entry_Articles_Orders_min.grid(row=6, column=1)
entry_Articles_Orders_max = tk.Entry(data_intro_frame, width=15)
entry_Articles_Orders_max.grid(row=6, column=2)

# Number of waves selection

Label_waves_title = tk.Label(data_intro_frame, text="Waves")
Label_waves_title.grid(row=4, column=3, padx=10, pady=10)

Label_T_Waves = tk.Label(data_intro_frame, text="Time between waves (h): ")
Label_T_Waves.grid(row=5, column=3, padx=20)
entry_T_Waves = tk.Entry(data_intro_frame, width=15)
entry_T_Waves.grid(row=5, column=4)

Label_Mission_Wave = tk.Label(data_intro_frame, text="Mission per wave: ")
Label_Mission_Wave.grid(row=6, column=3)
entry_Mission_Wave_min = tk.Entry(data_intro_frame, width=15)
entry_Mission_Wave_min.grid(row=6, column=4, padx=0)
entry_Mission_Wave_max = tk.Entry(data_intro_frame, width=15)
entry_Mission_Wave_max.grid(row=6, column=5, padx=20)

# Save Data
save_map_button = tk.Button(
    data_intro_frame, text="Start Simulation", fg="blue", command=save_data
)
save_map_button.grid(row=8, column=0, pady=30, columnspan=6)

# FUNCIONAMIENTO CONTINUO DE LA INTERFAZ
data_introduction_window.mainloop()


######################
# Simulating Interface
######################

'''
# msg_box_frm_sub_content = tk.Frame(self.msg_box_frm_content, bg='yellow', bd=2, width=1000)

simulating_window = tk.Tk()
simulating_window.title("ID Logistics - Warehouse Simulation - Simulating")

simulating_frame = tk.LabelFrame(simulating_window, text="Simulating", padx=20, pady=20)
simulating_frame.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

# Title

Simulating_title = tk.Label(simulating_frame, text="Simulating")
Simulating_title.grid(row=0, column=0, padx=10, pady=10, columnspan=4)

# Running Time

Label_day_title = tk.Label(simulating_frame, text="Day")
Label_day_title.grid(row=1, column=1, padx=10, pady=10)
Label_hour_title = tk.Label(simulating_frame, text="Hour")
Label_hour_title.grid(row=1, column=2, padx=10, pady=10)
Label_minute_title = tk.Label(simulating_frame, text="Minute")
Label_minute_title.grid(row=1, column=3, padx=10, pady=10)
Label_time_title = tk.Label(simulating_frame, text="Running Time: ")
Label_time_title.grid(row=2, column=0, padx=10, pady=10)

day_sub_frm = tk.Frame(simulating_frame, width=15, relief=tk.GROOVE)
day_sub_frm.grid(row=2, column=1, padx=10, pady=10)
Label_day_value = tk.Label(day_sub_frm, text="00", bg="grey")
Label_day_value.grid(row=0, column=0, padx=10, pady=10)

"""
Label_T_Waves = tk.Label(data_intro_frame, text="Time between waves (h): ")
Label_T_Waves.grid(row=5, column=3)
entry_T_Waves = tk.Entry(data_intro_frame, width=15)
entry_T_Waves.grid(row=5, column=4)

Label_Mission_Wave = tk.Label(data_intro_frame, text="Mission per wave: ")
Label_Mission_Wave.grid(row=6, column=3)
entry_Mission_Wave_min = tk.Entry(data_intro_frame, width=15)
entry_Mission_Wave_min.grid(row=6, column=4, padx=30)
entry_Mission_Wave_max = tk.Entry(data_intro_frame, width=15)
entry_Mission_Wave_max.grid(row=6, column=5)
"""

simulating_window.mainloop()

'''
