import os
import toml
import time
import datetime

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
local_key = api_config["LOCAL"]["api_key"]
local_base = api_config["LOCAL"]["base_url"]
local_model = api_config["LOCAL"]["model_name"]

generator_config = toml.load(config_dir + "generator.toml")
main_areas = generator_config["GENERATOR"]["main_areas"]
needs = generator_config["GENERATOR"]["needs"]
key_words = generator_config["GENERATOR"]["key_words"]
character_style = generator_config["GENERATOR"]["character_style"]
language_style = generator_config["GENERATOR"]["language_style"]

def toml_to_txt(toml_file_dir):
    print(toml_file_dir)
def read_txt(txt_dir):
    with open(txt_dir, "r", encoding='utf-8') as file:
        doc = file.read()
    return doc

def generate_by_models(selected_models, ):

    print("generate by models")