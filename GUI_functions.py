import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

#############################
#     Initial Interface
#############################


def ini_GUI():
    initial_window = tk.Tk()
    initial_window.title("ID Logistics - Warehouse Simulation")

    data_intro_frame = tk.LabelFrame(
        initial_window, text="ID Logistics - Warehouse Simulation", padx=20, pady=20
    )
    data_intro_frame.grid(row=10, column=10, padx=10, pady=10, columnspan=3)

    def new_simulation():
        global selection
        selection = 1
        initial_window.destroy()

    # New Simulation Button
    new_sim_button = tk.Button(
        data_intro_frame, text="New Simulation", fg="blue", command=new_simulation
    )
    new_sim_button.grid(row=1, column=0, pady=10, columnspan=1)

    # FUNCIONAMIENTO CONTINUO DE LA INTERFAZ
    initial_window.mainloop()

    return selection


#############################
# Data introduction interface
#############################


def data_intro_GUI():
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
        global Num_Picks_min
        global Num_Picks_max
        global T_Wave
        global Num_Mission_min
        global Num_Mission_max
        global selection

        selection_map = click_map.get()
        Num_Robots = entry_num_robots.get()
        Num_Humans = entry_num_humans.get()
        High_Demand_Days = entry_High_Demand.get()
        Low_Demand_Days = entry_Low_Demand.get()
        Num_Picks_min = entry_Picks_min.get()
        Num_Picks_max = entry_Picks_max.get()
        T_Wave = entry_T_Waves.get()
        Num_Mission_min = entry_Mission_min.get()
        Num_Mission_max = entry_Mission_max.get()
        selection = 1

        data_introduction_window.destroy()

    def exit_simulation():
        global selection

        selection = 0

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

    Label_order_title = tk.Label(data_intro_frame, text="Picks")
    Label_order_title.grid(row=4, column=0, padx=10, pady=10)

    Label_Picks = tk.Label(data_intro_frame, text="Picks per Mission: ")
    Label_Picks.grid(row=5, column=0, pady=10)
    entry_Picks_min = tk.Entry(data_intro_frame, width=15)
    entry_Picks_min.grid(row=5, column=1)
    entry_Picks_max = tk.Entry(data_intro_frame, width=15)
    entry_Picks_max.grid(row=5, column=2)

    # Number of waves selection

    Label_waves_title = tk.Label(data_intro_frame, text="Waves")
    Label_waves_title.grid(row=4, column=3, padx=10, pady=10)

    Label_T_Waves = tk.Label(data_intro_frame, text="Time between waves (h): ")
    Label_T_Waves.grid(row=5, column=3, padx=20)
    entry_T_Waves = tk.Entry(data_intro_frame, width=15)
    entry_T_Waves.grid(row=5, column=4)

    Label_Mission = tk.Label(data_intro_frame, text="Missions per Wave: ")
    Label_Mission.grid(row=6, column=3)
    entry_Mission_min = tk.Entry(data_intro_frame, width=15)
    entry_Mission_min.grid(row=6, column=4, padx=0)
    entry_Mission_max = tk.Entry(data_intro_frame, width=15)
    entry_Mission_max.grid(row=6, column=5, padx=20)

    # Save Data
    save_map_button = tk.Button(
        data_intro_frame, text="Start Simulation", fg="blue", command=save_data
    )
    save_map_button.grid(row=8, column=0, pady=30, columnspan=4)

    # Exit
    exit_button = tk.Button(
        data_intro_frame, text="Exit Simulation", fg="red", command=exit_simulation
    )
    exit_button.grid(row=8, column=3, pady=30, columnspan=1)

    # FUNCIONAMIENTO CONTINUO DE LA INTERFAZ
    data_introduction_window.mainloop()

    if selection:
        initial_parameters = {
            "Selection_map": selection_map,
            "Num_Robots": Num_Robots,
            "Num_Humans": Num_Humans,
            "High_Demand_Days": High_Demand_Days,
            "Low_Demand_Days": Low_Demand_Days,
            "Num_Picks_min": Num_Picks_min,
            "Num_Picks_max": Num_Picks_max,
            "T_Wave": T_Wave,
            "Num_Mission_min": Num_Mission_min,
            "Num_Mission_max": Num_Mission_max,
            "Selection": selection,
        }
    else:
        initial_parameters = {"Selection": selection}

    return initial_parameters
