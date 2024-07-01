import streamlit as st
import streamlit_antd_components as sac

from project.TxtGenerator import txt_generator
from project.PromptManager import prompt_manager
from project.OutputManager import output_manager
from project.ApiManeger import api_maneger

st.set_page_config(
    page_title="文案生成器",
    layout="wide",
    initial_sidebar_state="expanded"
)

with st.sidebar.container():
    menu = sac.menu(
        items=[
            sac.MenuItem('API_KEY管理', icon='bi bi-key'),
            sac.MenuItem('营销文案生成器', icon='book'),
            sac.MenuItem('生鲜文案生成器', icon='file'),
            sac.MenuItem('菜品推荐', icon='bi bi-book'),
            sac.MenuItem('提示词管理', icon='file-earmark-break'),
            sac.MenuItem('输出管理', icon='file'),
        ],
        key='menu',
        open_index=[1]
    )

with st.container():
    if menu == 'API_KEY管理':
        api_maneger()
    elif menu == '营销文案生成器':
        txt_generator()
    elif menu == '生鲜文案生成器':
        txt_generator()
    elif menu == '菜品推荐':
        txt_generator()
    elif menu == '提示词管理':
        prompt_manager()
    elif menu == '输出管理':
        output_manager()
