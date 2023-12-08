# main.py
import config

def enable_debug():
    config.settings["debug_mode"] = True

def perform_operation():
    if config.settings["debug_mode"]:
        print("Debug mode is enabled. Performing operation in debug mode.")
    else:
        print("Performing operation in standard mode.")

print("Initial debug mode:", config.settings["debug_mode"])
enable_debug()
perform_operation()
print("Final debug mode:", config.settings["debug_mode"])
