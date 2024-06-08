from data_logger import DataLogger
import matplotlib.pyplot as plt
import random, time

#masurements
# Input voltage 
# Opto-feedback voltage -> Vout
# Duty (sampled and mean is taken
# external current

#----> Output power

#==================== INITIALIZATION ============================
PARAM_NUMBER_OF_LOGS = 10
external_current_references = [None, "input_current", "output_current"] #static dict
EXTERNAL_CURRENT_REFERENCE = external_current_references[1]

input_voltage_logger = DataLogger(title = "Input Voltage",number_of_logs=PARAM_NUMBER_OF_LOGS, inclusive_data_bounds=[float("-inf"), float("inf")]) 
opto_feedback_logger = DataLogger(title = "Output Voltage", number_of_logs=PARAM_NUMBER_OF_LOGS, inclusive_data_bounds=[float("-inf"), float("inf")])
external_current_logger = DataLogger(title = "External Current", number_of_logs=PARAM_NUMBER_OF_LOGS, inclusive_data_bounds=[float("-inf"), float("inf")])
duty_logger = DataLogger(title = "Duty cycle",number_of_logs=PARAM_NUMBER_OF_LOGS, inclusive_data_bounds=[float("-inf"), float("inf")])
duty_more_logs_logger = DataLogger(title = "Duty cycle",number_of_logs=(10*PARAM_NUMBER_OF_LOGS), inclusive_data_bounds=[float("-inf"), float("inf")])

power_logger_calculated = DataLogger(title = "Calculated Power", number_of_logs= PARAM_NUMBER_OF_LOGS, inclusive_data_bounds=[float("-inf"), float("inf")])

loggers_to_consider = [input_voltage_logger, opto_feedback_logger, external_current_logger, duty_logger, power_logger_calculated, duty_more_logs_logger]
fig, axs = plt.subplots(3, 2, figsize=(12, 10))
axs = axs.flatten()  # Flatten the 2D array of axes

while True:
    # TODO: ==================== LOG DATA ============================
    # TODO: should communicate with arduino and get the recent data

    random_data = random.uniform(0, 1)
    input_voltage_logger.append_data(new_data=random_data, should_check_bound=True, raise_if_not_in_bound=True)
    opto_feedback_logger.append_data(new_data=random_data, should_check_bound=True, raise_if_not_in_bound=True)
    external_current_logger.append_data(new_data=random_data, should_check_bound=True, raise_if_not_in_bound=True)
    duty_logger.append_data(new_data=random_data, should_check_bound=True, raise_if_not_in_bound=True)
    duty_more_logs_logger.append_data(new_data=random_data, should_check_bound=True, raise_if_not_in_bound=True)

    # ==================== DISPLAY ============================
    power_logs = [0] * PARAM_NUMBER_OF_LOGS
    for log_index, current_log in enumerate(external_current_logger.get_logs()):
        if EXTERNAL_CURRENT_REFERENCE is None:
            break
        elif EXTERNAL_CURRENT_REFERENCE == "input_current":
            power_logs[log_index] = current_log * input_voltage_logger.get_logs()[log_index]
        elif EXTERNAL_CURRENT_REFERENCE == "output_current":
            power_logs[log_index] = current_log * opto_feedback_logger.get_logs()[log_index]
    power_logger_calculated.set_logs(data_logs=power_logs)

    # Prepare data for plotting
    titles = []
    lists_of_values = []
    for logger in loggers_to_consider:
        titles.append(logger.get_title())
        lists_of_values.append(logger.get_logs())

    # Clear previous plots
    for ax in axs:
        ax.clear()

    # Create subplots
    for i in range(len(loggers_to_consider)):
        axs[i].plot(lists_of_values[i], label=titles[i])
        axs[i].set_ylabel("Value")
        axs[i].set_title(titles[i])
        axs[i].legend()
        axs[i].grid(True)  # Add grid to each plot

    plt.tight_layout()
    plt.draw()
    plt.pause(0.2)