import json
import sys
import threading
import time

import panel as pn

from gym_jsbsim.plots import generate_figures

import argparse

parser = argparse.ArgumentParser(description='Start rendering server for log file in JSON format.')
parser.add_argument("--log_path", dest="log_path", type=str, default="/home/jsbsim/logs/log.json", help="the path to the log JSON file")
parser.add_argument("-p", "--port", dest="port", type=int, default=56000, help="the port for serving the rendered plots")

args = parser.parse_args()
FILE_PATH = args.log_path
PORT = args.port


def update_panel():
    old_log = None

    while True:
        try:
            with open(FILE_PATH, 'r') as file:
                log = json.load(file)
        except FileNotFoundError:
            import warnings
            warnings.warn(f"No JSON file at {FILE_PATH}.")
            continue
        except json.decoder.JSONDecodeError:
            continue

        if not old_log == log:
            while len(render_panel.objects) > 0:
                render_panel.objects.pop(0)
            figures = generate_figures(log)

            group_1 = pn.Row(figures['altitude'],
                             figures['attitude'],
                             figures['angular_vel'],
                             figures['deg_errors'],
                             )

            group_2 = pn.Row(figures['aileron'],
                             figures['elevator'],
                             )
            group_3 = pn.Column(group_2,
                                figures['rudder']
                                )

            group_4 = pn.Row(group_3,
                             figures['vel_grid']
                             )
            group_5 = pn.Column(group_1,
                                group_4
                                )

            render_panel.append(group_5)
            old_log = log

        time.sleep(1)


render_panel = pn.Column()

thread = threading.Thread(target=update_panel)
thread.daemon = True
thread.start()

render_panel.show(port=PORT)