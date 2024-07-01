import os
import toml
import datetime
from openai import OpenAI
from zhipuai import ZhipuAI

def load_config():
    global project_dir
    project_dir = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
    global config_dir
    config_dir = project_dir + "/config/"  # 配置文件

    global api_config
    api_config = toml.load(config_dir + "api.toml")  # 加载API配置
    global kimi_key
    kimi_key = api_config["KIMI"]["kimi_key"]
    global kimi_base
    kimi_base = api_config["KIMI"]["kimi_base"]
    global deepseek_key
    deepseek_key = api_config["DEEPSEEK"]["deepseek_key"]
    global deepseek_base
    deepseek_base = api_config["DEEPSEEK"]["deepseek_base"]
    global chatglm_key
    chatglm_key = api_config["CHATGLM"]["chatglm_key"]
    global chatglm_base
    chatglm_base = api_config["CHATGLM"]["chatglm_base"]

    global generator_config
    generator_config = toml.load(config_dir + "generator.toml")
    global generator_model
    generator_model = generator_config["GENERATOR"]["generator_model"]
    global main_areas
    main_areas = generator_config["GENERATOR"]["main_areas"]
    global needs
    needs = generator_config["GENERATOR"]["needs"]
    global key_words
    key_words = generator_config["GENERATOR"]["key_words"]
    global character_style
    character_style = generator_config["GENERATOR"]["character_style"]
    global language_style
    language_style = generator_config["GENERATOR"]["language_style"]

def toml_to_str():
    str = f'主要领域：{main_areas},' + f'以{character_style}的口吻和角度,' + f'以及{language_style}的话语风格'+ '写一篇营销文案,' + f'需求如下: {needs},' + f'关键词：{key_words}'
    return str

def generate_by_models(model, str):
    result = None
    print("***正在生成***\n")
    if "moonshot-v1-8k" in model:
        client = OpenAI(api_key=kimi_key, base_url=kimi_base)
    elif "glm-4-flash" in model:
        client = ZhipuAI(api_key=chatglm_key)
    elif "deepseek-chat" in model:
        client = OpenAI(api_key=deepseek_key, base_url=deepseek_base)

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": f"你是一个优秀的营销文案作者"},
            {"role": "user",
             "content": f"我的需求说明如下：{str},根据我的需求给我一份营销文案，仅仅给出文案，给出文案之后立即停止回答"}
        ])
    # 打印 response 的内容，用于调试
    print(response)
    if hasattr(response, 'choices') and response.choices:
        answer = response.choices[0].message.content
    else:
        answer = None
    return answer