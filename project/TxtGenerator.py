import os
import toml

import streamlit as st
import streamlit_antd_components as sac
from . import utils
def txt_generator():
    project_dir = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
    config_dir = project_dir + "/config/"  # 配置文件

    api_config = toml.load(config_dir + "api.toml")  # 加载API配置
    openai_key = api_config["GPT"]["openai_key"]
    openai_base = api_config["GPT"]["openai_base"]
    kimi_key = api_config["KIMI"]["kimi_key"]
    kimi_base = api_config["KIMI"]["kimi_base"]
    deepseek_key = api_config["DEEPSEEK"]["deepseek_key"]
    deepseek_base = api_config["DEEPSEEK"]["deepseek_base"]
    chatglm_key = api_config["CHATGLM"]["chatglm_key"]
    chatglm_base = api_config["CHATGLM"]["chatglm_base"]

    generator_config = toml.load(config_dir + "generator.toml")

    col1, col2 = st.columns([0.4, 0.6], gap="medium")
    with col1:

        with st.expander("**选择模型**", expanded=True):
            generator_model = sac.chip(
                items=[
                    sac.ChipItem(label='moonshot-v1-8k'),
                    sac.ChipItem(label='glm-4-flash'),
                    sac.ChipItem(label='deepseek-chat'),
                ], format_func='title', direction='vertical', radius='sm',
                multiple=True, return_index=False
            )
            if generator_model:
                generator_config["GENERATOR"]["generator_model"] = generator_model
            else: sac.alert(
                label='**请选择模型**',
                description='**选择模型不能为空**',
                size='lg', radius=20, icon=True, closable=True, color='error')

        with st.expander("**主要领域**", expanded=True):
            main_areas = sac.cascader(items=[
                sac.CasItem('无'),
                sac.CasItem('电脑', icon='node-plus-fill', children=[
                    sac.CasItem('整机'),
                    sac.CasItem('CPU'),
                    sac.CasItem('主板'),
                    sac.CasItem('散热'),
                    sac.CasItem('内存'),
                    sac.CasItem('显卡'),
                    sac.CasItem('硬盘'),
                    sac.CasItem('电源'),
                    sac.CasItem('机箱'),
                ]),
                sac.CasItem('生活', icon='node-plus-fill', children=[
                    sac.CasItem('日常用品'),
                    sac.CasItem('卫生'),
                    sac.CasItem('厨房'),
                ]),
                sac.CasItem('女士', icon='node-plus-fill', children=[
                    sac.CasItem('护肤'),
                    sac.CasItem('化妆品'),
                    sac.CasItem('美容'),
                    sac.CasItem('美发'),
                    sac.CasItem('美甲'),
                    sac.CasItem('服装'),
                    sac.CasItem('鞋子'),
                    sac.CasItem('运动'),
                ]),
                sac.CasItem('男士', icon='node-plus-fill', children=[
                    sac.CasItem('保养'),
                    sac.CasItem('服装'),
                    sac.CasItem('鞋子'),
                    sac.CasItem('运动'),
                    sac.CasItem('电子产品'),
                ]),
                sac.CasItem('更多', icon='node-plus-fill', children=[
                    sac.CasItem('更多'),
                ]),
            ], placeholder='专业领域', search=True)
            if main_areas:
                generator_config["GENERATOR"]["main_areas"] = main_areas

        with st.expander("**营销需求**", expanded=True):
            needs = st.text_area("请输入你的营销需求", placeholder="给我写一份关于xxx产品的营销文案......")
            if needs:
                generator_config["GENERATOR"]["needs"] = needs

        with st.expander("**关键词**", expanded=True):
            key_words = st.text_input("请输入需要突出的关键词", placeholder="在这里输入关键词")
            if needs:
                generator_config["GENERATOR"]["key_words"] = key_words

        with st.expander("**人设风格**", expanded=True):
            character_style = sac.cascader(items=[
                sac.CasItem('女中学生'),
                sac.CasItem('男中学生'),
                sac.CasItem('女大学生'),
                sac.CasItem('男大学生'),
                sac.CasItem('职场女性'),
                sac.CasItem('职场男性'),
                sac.CasItem('运动员'),
                sac.CasItem('明星'),
                sac.CasItem('小女孩'),
                sac.CasItem('小男孩'),
                sac.CasItem('母亲'),
                sac.CasItem('父亲'),
                sac.CasItem('老年人'),
            ], placeholder='选择人设风格', search=True)
            if character_style:
                generator_config["GENERATOR"]["character_style"] = character_style

        with st.expander("**语言风格**", expanded=True):
            language_style = sac.cascader(items=[
                sac.CasItem('可爱'),
                sac.CasItem('活泼'),
                sac.CasItem('严肃'),
                sac.CasItem('专业'),
                sac.CasItem('有号召力'),
                sac.CasItem('平和'),
                sac.CasItem('温柔'),
                sac.CasItem('严厉'),
            ], placeholder='选择几个标签吧', multiple=True, search=True, clear=True)
            if language_style:
                generator_config["GENERATOR"]["language_style"] = language_style

        if st.button("保存所有参数", type="primary", use_container_width=True):
            with open(config_dir + '/generator.toml', 'w', encoding='utf-8') as file:
                toml.dump(generator_config, file)
                print(file)
            sac.alert(
                label='**参数设置已保存**',
                description='**未选择的部分将使用上一次的配置**',
                size='lg', radius=20, icon=True, closable=True, color='success')

    with col2:
        if st.button("开始生成", type="primary", use_container_width=True):
            print("开始生成")

            selected_models = generator_config["GENERATOR"]["generator_model"]
            tabs = st.tabs(selected_models)
            doc = utils.toml_to_txt()

            for i, model in enumerate(selected_models):
                with tabs[i]:
                    result = utils.generate_by_models(model, doc)
                    st.text_area("生成结果", value=result, height=400)



