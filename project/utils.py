import os
import toml
import time
import datetime
from openai import OpenAI
from zhipuai import ZhipuAI


project_dir = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
config_dir = project_dir + "/config/"  # 配置文件
input_dir = project_dir + "/input/"    # 输入文件
output_dir = project_dir + "/output/"  # 输出文件

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
generator_model = generator_config["GENERATOR"]["generator_model"]
main_areas = generator_config["GENERATOR"]["main_areas"]
needs = generator_config["GENERATOR"]["needs"]
key_words = generator_config["GENERATOR"]["key_words"]
character_style = generator_config["GENERATOR"]["character_style"]
language_style = generator_config["GENERATOR"]["language_style"]

def toml_to_txt():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    os.makedirs(input_dir)
    input_file_dir = input_dir + current_time
    os.makedirs(input_file_dir)
    # 打开一个文件，如果文件不存在则创建它，并以写入模式打开
    with open(input_file_dir + '/' + 'input.txt', 'w', encoding='utf-8') as file:
        file.write(f"主要领域: {main_areas}\n")
        file.write(f"以{character_style}的口吻和角度\n")
        file.write(f"以及{language_style}的话语风格\n")
        file.write("写一篇营销文案")
        file.write(f"需求如下：{needs}\n")
        file.write(f"关键词：{key_words}\n")
    with open(input_file_dir + '/' + 'input.txt', 'r', encoding='utf-8') as file:
        doc = file.read()
    return doc

def generate_by_models(model, doc):
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
             "content": f"我的要求说明书如下：{doc},根据我的需求给我一份营销文案，仅仅给出文案，给出文案之后立即停止回答"}
        ])
    # 打印 response 的内容，用于调试
    print(response)
    if hasattr(response, 'choices') and response.choices:
        answer = response.choices[0].message.content
    else:
        answer = None
    return answer