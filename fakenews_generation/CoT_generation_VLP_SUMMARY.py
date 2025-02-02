# import tiktoken
import os
import pandas as pd
from CoT_1 import *
import transformers
from transformers import AutoTokenizer
from CoT_qualification import theme_check
import torch
import time

model = "lmsys/vicuna-13b-v1.5-16k"#'gaurangavimk/text-davinci-003' #"lmsys/vicuna-13b-v1.5-16k" #"meta-llama/Llama-2-13b-chat-hf"
token = ''
tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    # "chat-completion",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
)

def valid_content_separator(content):
    seps = ['Article: ####', 'Article: \n####', 'Article:\n####', 'Article:####',
            '#### Article:', 'Article: ', '####Article:']
    for s in seps:
        if content.find(s) != -1:
            return s
    return None

def get_title(user_message,
              model="gpt-3.5-turbo",
              temperature=0, top_p=0.7, top_k=1, max_tokens=4096):
    messages = [
        {
            "role": "system",
            "content": f"""
                Generate a title for the article.
                The contents of the article will be delimited with four hashtags,\
                i.e. {delimiter}. """
        },
        {
            "role": "user",
            "content": f"{delimiter}{user_message}{delimiter}"}
    ]
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            top_p = top_p,
            # top_k = top_k,
            max_tokens=max_tokens,
        )

        res = response.choices[0].message.content
    except:
        res = ''
    return res

def get_completion_from_messages(messages,
                                 model="gpt-3.5-turbo",
                                 temperature=0, max_tokens=4096):
    try:
        sequences = pipeline(
            messages,
            do_sample=True,
            top_k=3,
            num_return_sequences=1,
            eos_token_id=tokenizer.eos_token_id,
            max_length=max_tokens,
        )

        res = sequences[0]['generated_text']
        sep = valid_content_separator(res)
        if sep is not None:
            # check_last = len(res.split('\n')[-1].split(' ')) > 10 # remove the last sentence indicating the generation of article
            # while not check_last:
            #     res = '\n'.join(res.split('\n')[:-1])
            #     check_last = len(res.split('\n')[-1].split(' ')) > 10
            print(sep, res)
            return res[sep:], sep
        else:
            print('Failed:----------------------------\n', res, '\n----------------------------')
            return None, None
    except Exception as e:
        print(e)
        print(res)
        return None, None


if __name__ == "__main__":
    cur_filename = './data/news_nodup1.csv'
    save_name = './data/news_nodup1_fake_CoT1_Vicuna13b.csv'
    num_modify = 90
    df = pd.read_csv(cur_filename, header=0)
    df = df[df.folder.isin(['Nih', 'WebMD'])].set_index(['Unnamed: 0', 'folder'])

    print(df.shape)

    res, cnt, num = [], 0, 0
    for i, row in df.iterrows():
        num += 1
        if cnt > num_modify:
            break

        user_message = row['content']#[2:-2].split("', '")

        chat = [
            {
                "role": "system",
                "content": system_message1},
            {
                "role": "user",
                "content": f"{delimiter}{user_message}{delimiter}"}
        ]
        tokenizer.use_default_system_prompt = False
        messages = tokenizer.apply_chat_template(chat, tokenize=False)
        response, sep = get_completion_from_messages(messages, temperature=1)

        if response is not None:

            user_message1, user_message2 = user_message, response
            user_message1, user_message2 = ' '.join(user_message1.split(' ')[:200]), ' '.join(
                user_message2.split(' ')[:200])
            chk = theme_check(user_message1, user_message2)
            if 'yes' in chk.lower():
                content = response.split(sep)[-1]
                title = get_title(content)
                row['content'] = '"' + content + '"'
                row['title'] = title
                row['source'] = 'vicuna'
                res.append(row)
                cnt += 1

                print(f'finished checking news {num} generation news {cnt}')
        # break
    # print(content)
    # save csv
    res = pd.DataFrame(res)
    if os.path.exists(save_name):
        res.to_csv(save_name, index=True, encoding="utf-8-sig", mode='a', header=False)
    else:
        res.to_csv(save_name, index=True, encoding="utf-8-sig")

    print(f'finished modification of {cur_filename}', res.shape)