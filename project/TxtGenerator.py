import os
import toml
import time
import datetime

import streamlit as st
import streamlit_antd_components as sac

def TxtG():
    project_dir = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
    config_dir = project_dir + "/config/"  # 配置文件

    print(project_dir)
    print(config_dir)
