from openai import OpenAI
import tiktoken
import os
import pandas as pd
from CoT_1 import *
from CoT_qualification import theme_check
import time

client = OpenAI(api_key = "")

def valid_content_separator(content):
    seps = ['Article: ####', 'Article: \n####', 'Article:\n####', 'Article:####',
            '#### Article:', 'Article: ', '####Article:']
    flaga = content.lower().find('step 3:')
    flagb = content.lower().find('step 4:')
    for s in seps:
        pos = content.rfind(s)
        if pos > flaga and pos < flagb: # not -1 or found at the beginning of the reply
            return s
        # if pos >= 0:
        #     return s
    return None

def get_completion_from_messages(messages,
                                 model="gpt-3.5-turbo",
                                 temperature=0, top_p=0.7, top_k=5, max_tokens=2000):

    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            top_p=top_p,
            # top_k=top_k,
            max_tokens=max_tokens,
        )
        res = response.choices[0].message.content
        cnt = 0
        # while 'no' not in res.lower().split('step 5:')[-1] and cnt < top_k:
        #     response = client.chat.completions.create(
        #         model=model,
        #         messages=messages,
        #         temperature=temperature,
        #         top_p=top_p,
        #         # top_k=top_k,
        #         max_tokens=max_tokens,
        #     )
        #     res = response.choices[0].message.content
        #     cnt += 1
        sep = valid_content_separator(res)
        if sep is not None and 'no' in res.lower().split('step 5:')[-1]:
            # check_last = len(res.split('\n')[-1].split(' ')) > 10 # remove the last sentence indicating the generation of article
            # while not check_last:
            #     res = '\n'.join(res.split('\n')[:-1])
            #     check_last = len(res.split('\n')[-1].split(' ')) > 10
            print(sep, res)
            sep2 = res.lower().find('step 4:')
            res = res[:sep2]
            return res, sep
        else:
            print('Failed:----------------------------\n', res, '\n----------------------------')
            # print('Failed:----------------------------')
            return None, None
    except Exception as e:
        print('!!!!!!!!!!!!!!!!!!!!!', e)
        return None, None

def get_title(user_message,
              model="gpt-3.5-turbo",
              temperature=0, top_p=0.7, top_k=1, max_tokens=2000):
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


if __name__ == "__main__":
    news_filename = '../results/final/news_nodup1.csv'
    # fake_filename = '../results/final/news_nodup1_fake_CoT1.csv'
    save_name = '../results/final/news_nodup1_fake_CoT1_QA_v3.csv'
    start_modify, end_modify = 0, 500#501, 1000
    num_limit = 100 # number of articles to be generated
    df_true = pd.read_csv(news_filename, header=0)
    # df_fake = pd.read_csv(fake_filename, header=0).set_index(['Unnamed: 0', 'folder'])
    # df = df_true.loc[df_fake.index]
    df = df_true[df_true.folder.isin(['Nih', 'WebMD'])].set_index(['Unnamed: 0', 'folder'])

    print(df.shape)

    res, num, cnt = [], 0, 0
    for i, row in df.iloc[start_modify:].iterrows():
        num += 1
        source = 'QA'
        user_message = row['content']#[2:-2].split("', '")
        system_message = system_message1_bl_QA
        # if num < 100:
        #     system_message = system_message1_bl_QA_s
        #     source = 'QA_s'
        # elif num < 200:
        #     system_message = system_message1_bl_QA_m
        #     source = 'QA_m'
        # elif num < 300:
        #     system_message = system_message1_bl_QA
        #     source = 'QA'
        # else:
        #     system_message = system_message1_bl_QA_l
        #     source = 'QA_l'

        messages=[
            {
                "role": "system",
                "content": system_message},
            {
                "role": "user",
                "content": f"{delimiter}{user_message}{delimiter}"}
        ]
        response, sep = get_completion_from_messages(messages, temperature=0.7, top_p=1.0, top_k=5)

        if response is not None:

            user_message1, user_message2 = user_message, response
            user_message1, user_message2 = ' '.join(user_message1.split(' ')[:200]), ' '.join(
                user_message2.split(' ')[:200])
            chk = theme_check(user_message1, user_message2)
            if 'yes' in chk.lower():
                content = response.split(sep)[-1]
                title = get_title(content)
                row['content'] = '"'+content+'"'
                row['title'] = title
                row['source'] = source
                row['comment'] = chk
                res.append(row)
                cnt += 1

                print(f'finished checking news {num} generation news {cnt}')
        if cnt > num_limit:
            break
        # break
    # print(content)
    # save csv
    res = pd.DataFrame(res)
    if os.path.exists(save_name):
        res.to_csv(save_name, index=True, encoding="utf-8-sig", mode='a', header=False)
    else:
        res.to_csv(save_name, index=True, encoding="utf-8-sig")

    print(f'finished modification of {news_filename}', res.shape)