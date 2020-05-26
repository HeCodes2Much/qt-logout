# =====================================================
#                  Author TheCynicalTeam
# =====================================================

import subprocess
import os
import shutil
from pathlib import Path
import configparser

home = os.path.expanduser("~")
base_dir = os.path.dirname(os.path.realpath(__file__))
# here = Path(__file__).resolve()
working_dir = ''.join([str(Path(__file__).parents[2]), "/share/cynicalteam-logout/"])
# config = "etc/setting.conf"
if os.path.isfile(home + "/.config/cynicalteam-logout/settings.conf"):
    config = home + "/.config/cynicalteam-logout/settings.conf"
else:
    config = ''.join([str(Path(__file__).parents[3]), "/etc/cynicalteam-logout.conf"])
root_config = ''.join([str(Path(__file__).parents[3]), "/etc/cynicalteam-logout.conf"])

def _get_position(lists, value):
    data = [string for string in lists if value in string]
    position = lists.index(data[0])
    return position

def get_config(self, config):
    try:
        self.parser = configparser.RawConfigParser()
        self.parser.read(config)

        # Set some safe defaults
        self.opacity = 60

        # Check if we're using HAL, and init it as required.
        if self.parser.has_section("settings"):
            if self.parser.has_option("settings", "opacity"):
                self.opacity = int(self.parser.get("settings", "opacity"))/100
            if self.parser.has_option("settings", "buttons"):
                self.buttons = self.parser.get("settings", "buttons").split(",")
            if self.parser.has_option("settings", "icon_size"):
                self.icon_size = int(self.parser.get("settings", "icon_size"))
            if self.parser.has_option("settings", "icon_font_size"):
                self.icon_font_size = int(self.parser.get("settings", "icon_font_size"))
            if self.parser.has_option("settings", "title_font_size"):
                self.title_font_size = int(self.parser.get("settings", "title_font_size"))
            if self.parser.has_option("settings", "icon_font_weight"):
                self.icon_font_weight = self.parser.get("settings", "icon_font_weight")
            if self.parser.has_option("settings", "title_font_weight"):
                self.title_font_weight = self.parser.get("settings", "title_font_weight")

        if self.parser.has_section("commands"):
            if self.parser.has_option("commands", "lock"):
                self.cmd_lock = str(self.parser.get("commands", "lock"))

    except Exception as e:
        print(e)
        os.unlink(home + "/.config/cynicalteam-logout/settings.conf")
        if not os.path.isfile(home + "/.config/cynicalteam-logout/settings.conf"):
            shutil.copy(root_config, home + "/.config/cynicalteam-logout/settings.conf")
