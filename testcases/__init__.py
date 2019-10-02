import os, sys
sys.path.append(os.getcwd())

from base.clear_shot import clear_shot
from base.base_driver import env_config
env_config()
clear_shot()
