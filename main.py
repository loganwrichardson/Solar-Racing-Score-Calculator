import tkinter as tk

def calculate_score():
    try:
        ROSE_laps = float(ROSE_laps_entry.get())
        competitor_laps = float(competitor_laps_entry.get())

        ROSE_seats = float(ROSE_seats_entry.get())
        competitor_seats = float(competitor_seats_entry.get())

        ROSE_euc = float(ROSE_euc_entry.get())
        competitor_euc = float(competitor_euc_entry.get())

        ROSE_cars_cap = float(ROSE_cars_cap_entry.get())
        competitor_cars_cap = float(competitor_cars_cap_entry.get())

        ROSE_emc = float(ROSE_emc_entry.get())
        competitor_emc = float(competitor_emc_entry.get())

        ROSE_penalties = float(ROSE_penalties_entry.get())
        competitor_penalties = float(competitor_penalties_entry.get())

        ROSE_top_mov_dist = float(ROSE_top_mov_dist_entry.get())
        competitor_top_mov_dist = float(competitor_top_mov_dist_entry.get())

        ROSE_target_avg_spd = float(ROSE_targ_avg_spd_entry.get())
        competitor_target_avg_spd = float(competitor_targ_avg_spd_entry.get())

        ROSE_team_avg_spd = float(ROSE_team_avg_spd_entry.get())
        competitor_team_avg_spd = float(competitor_team_avg_spd_entry.get())

        ROSE_person_mile_distance = ROSE_laps * ROSE_seats
        ROSE_external_energy_usage = (ROSE_euc + 1) * ROSE_cars_cap + ROSE_emc
        ROSE_completion_factor = (ROSE_person_mile_distance - ROSE_penalties) / ROSE_top_mov_dist

        competitor_person_mile_distance = competitor_laps * competitor_seats
        competitor_external_energy_usage = (competitor_euc + 1) * competitor_cars_cap + competitor_emc
        competitor_completion_factor = (competitor_person_mile_distance - competitor_penalties) / competitor_top_mov_dist

        if ROSE_team_avg_spd >= ROSE_target_avg_spd:
            ROSE_Target_speed_derate = 1
        else:
            ROSE_Target_speed_derate = 0.6 ** ((ROSE_target_avg_spd - ROSE_team_avg_spd) ** 0.4)

        if competitor_team_avg_spd >= competitor_target_avg_spd:
            competitor_Target_speed_derate = 1
        else:
            competitor_Target_speed_derate = 0.6 ** ((competitor_target_avg_spd - competitor_team_avg_spd) ** 0.4)

        ROSE_Score = (ROSE_person_mile_distance / ROSE_external_energy_usage) * ROSE_completion_factor * ROSE_Target_speed_derate
        ROSE_score_label.config(text="ROSE Score: " + str(ROSE_Score))

        competitor_Score = (competitor_person_mile_distance / competitor_external_energy_usage) * competitor_completion_factor * competitor_Target_speed_derate
        competitor_score_label.config(text="competitor Score: " + str(competitor_Score))
    except:
        ROSE_score_label.config(text="ERROR \n Something is NULL")
        competitor_score_label.config(text="ERROR \n Something is NULL")

window = tk.Tk()
window.title("Score Calculator")

# Create input labels and entry field
tk.Label(window, text="ROSE").grid(row=0, column=1, padx=5, pady=5)
tk.Label(window, text="Competitor").grid(row=0, column=2, padx=5, pady=5)

tk.Label(window, text="Laps:").grid(row=1, column=0, padx=5, pady=5)
ROSE_laps_entry=tk.Entry(window)
ROSE_laps_entry.grid(row=1, column=1, padx=5, pady=5)
competitor_laps_entry=tk.Entry(window)
competitor_laps_entry.grid(row=1, column=2, padx=5, pady=5)

tk.Label(window, text="Seats:").grid(row=2, column=0, padx=5, pady=5)
ROSE_seats_entry = tk.Entry(window)
ROSE_seats_entry.grid(row=2, column=1, padx=5, pady=5)
competitor_seats_entry = tk.Entry(window)
competitor_seats_entry.grid(row=2, column=2, padx=5, pady=5)

tk.Label(window, text="Unmetered external energy in kWh:").grid(row=3, column=0, padx=5, pady=5)
ROSE_euc_entry = tk.Entry(window)
ROSE_euc_entry.grid(row=3, column=1, padx=5, pady=5)
competitor_euc_entry = tk.Entry(window)
competitor_euc_entry.grid(row=3, column=2, padx=5, pady=5)

tk.Label(window, text="Energy capacity of battery:").grid(row=4, column=0, padx=5, pady=5)
ROSE_cars_cap_entry = tk.Entry(window)
ROSE_cars_cap_entry.grid(row=4, column=1, padx=5, pady=5)
competitor_cars_cap_entry = tk.Entry(window)
competitor_cars_cap_entry.grid(row=4, column=2, padx=5, pady=5)

tk.Label(window, text="Metered external energy in kWh:").grid(row=5, column=0, padx=5, pady=5)
ROSE_emc_entry = tk.Entry(window)
ROSE_emc_entry.grid(row=5, column=1, padx=5, pady=5)
competitor_emc_entry = tk.Entry(window)
competitor_emc_entry.grid(row=5, column=2, padx=5, pady=5)

tk.Label(window, text="Penalties:").grid(row=6, column=0, padx=5, pady=5)
ROSE_penalties_entry = tk.Entry(window)
ROSE_penalties_entry.grid(row=6, column=1, padx=5, pady=5)
competitor_penalties_entry = tk.Entry(window)
competitor_penalties_entry.grid(row=6, column=2, padx=5, pady=5)

tk.Label(window, text="Highest Driving Distance of Any MOV:").grid(row=7, column=0, padx=5, pady=5)
ROSE_top_mov_dist_entry = tk.Entry(window)
ROSE_top_mov_dist_entry.grid(row=7, column=1, padx=5, pady=5)
competitor_top_mov_dist_entry = tk.Entry(window)
competitor_top_mov_dist_entry.grid(row=7, column=2, padx=5, pady=5)

tk.Label(window, text="Target Average Speed (30 for FSGP):").grid(row=8, column=0, padx=5, pady=5)
ROSE_targ_avg_spd_entry = tk.Entry(window)
ROSE_targ_avg_spd_entry.grid(row=8, column=1, padx=5, pady=5)
competitor_targ_avg_spd_entry = tk.Entry(window)
competitor_targ_avg_spd_entry.grid(row=8, column=2, padx=5, pady=5)

tk.Label(window, text="Overall Average Speed of the Team:").grid(row=9, column=0, padx=5, pady=5)
ROSE_team_avg_spd_entry = tk.Entry(window)
ROSE_team_avg_spd_entry.grid(row=9, column=1, padx=5, pady=5)
competitor_team_avg_spd_entry = tk.Entry(window)
competitor_team_avg_spd_entry.grid(row=9, column=2, padx=5, pady=5)

# Create the Calculate Score button
ROSE_calculate_button = tk.Button(window, text="Calculate Score", command=calculate_score)
ROSE_calculate_button.grid(row=20, column=1, columnspan=3,padx=5, pady=10)
# competitor_calculate_button = tk.Button(window, text="Calculate Score", command=calculate_score)
# competitor_calculate_button.grid(row=20, column=2, padx=5, pady=10)

# Create the score label
ROSE_score_label = tk.Label(window, text="Score: ")
ROSE_score_label.grid(row=21, column=1, padx=5, pady=10)
competitor_score_label = tk.Label(window, text="Score: ")
competitor_score_label.grid(row=21, column=2,  padx=5, pady=10)

window.mainloop()