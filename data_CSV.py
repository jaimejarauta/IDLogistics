from pathlib import Path
import pandas as pd


def data_CSV(mission):
    # This function creates a new CSV or updates an existing one with the given data.
    for i in range(0, len(mission.get_picksdone()) - 1):
        dataArray = [
            mission.get_picksdone()[i].get_missionID(),
            mission.get_picksdone()[i].get_pickID(),
            mission.get_picksdone()[i].get_pos(),
            mission.get_robotassigned(),
            mission.get_picksdone()[i].get_human_assigned(),
            mission.get_numpicks(),
            round(mission.get_tstart(), 1),
            round(mission.get_picksdone()[i].get_waittime(), 1),
            round(mission.get_picksdone()[i].get_actualwaittime(), 1),
            round(mission.get_picksdone()[i].get_picktime(), 1),
            round(mission.get_picksdone()[i].get_humantime(), 1),
            mission.get_intersec(),
            mission.get_false(),
        ]

        column_names = [  # Name of columns to be declared in csv
            "ID Mision",
            "ID Pick",
            "Posición",
            "Robot Asignado",
            "Humano Asignado",
            "Número de Picks",
            "Tiempo de Inicio",
            "Tiempo de espera a que llegue el humano",
            "Tiempo espera a asignación humano",
            "Tiempo de pick total",
            "Tiempo pick humano cte",
            "Intersecciones",
            "Error False",
        ]

        file_path = Path("data.csv")  # The directory should be set for each computer
        if file_path.exists():  # If the file exists, it is updated.
            data = pd.DataFrame([dataArray])
            data.to_csv(
                file_path, mode="a", index=False, na_rep="Unknown", header=False
            )
        else:
            # If not, it creates
            data = pd.DataFrame([dataArray], columns=column_names)
            data.to_csv(
                file_path, mode="a", index=False, na_rep="Unknown", header=column_names
            )
