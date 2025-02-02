from openai import OpenAI
import tiktoken
import os
import pandas as pd
from CoT_1 import delimiter
import time
import re

client = OpenAI(api_key = "")

def theme_check(user_message1, user_message2,
              model="gpt-3.5-turbo",
              temperature=0, top_p=0.7, top_k=1, max_tokens=2000):
    messages = [
        {
            "role": "system",
            "content": f"""
                Given two articles, are there any differences between the two articles, despite the expression, wording or structure? 
                Reply "yes" if there are any differences between the articles and "no" if the two articles are exectly the same.
                You should also explain the reason for your answer.
                
                The contents of the articles will be delimited with four hashtags,\
                i.e. {delimiter}. """
        },
        {
            "role": "user",
            "content": f"{delimiter}{user_message1}{delimiter}{user_message2}{delimiter}"}
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
    except Exception as e:
        print(e)
        res = ''
    print(res)
    return res


if __name__ == "__main__":
    data_dir = '../results/final/'
    save_name = 'pair_check_loose_'
    df = pd.read_csv(os.path.join(data_dir, 'pair_check_same.csv'), header=0) # 'Unnamed: 0.1', 'Unnamed: 0', 'folder', 'source', 'content_real', 'content_fake', 'comment'
    df = df[df.folder.isin(['Nih', 'WebMD'])]
    print(df.shape)
    df_same, df_notsame = [], []
    cnt = 0
    for i, row in df.iterrows():
        print(f"---------------------- {row['source']} ----------------------")
        user_message1, user_message2 = row['content_real'], row['content_fake']
        user_message1, user_message2 = ' '.join(user_message1.split(' ')[:200]), ' '.join(user_message2.split(' ')[:200])
        res = theme_check(user_message1, user_message2)
        newrow = {'Unnamed: 0': row['Unnamed: 0'], 'folder': row['folder'], 'source': row['source'],
                  'content_real': row['content_real'], 'content_fake': row['content_fake'], 'comment': '"'+res+'"'}
        if 'yes' in res.lower():
            df_notsame.append(newrow)
        else:
            df_same.append(newrow)
        cnt += 1
        print(f'finished comparing {cnt}/{df.shape[0]}')
        # break

    # save csv
    df_same, df_notsame = pd.DataFrame(df_same), pd.DataFrame(df_notsame)
    print(f'Find {df_notsame.shape[0]} qualified articles and {df_same.shape[0]} unqualified articles.')
    print('---------------------- Qualified ----------------------')
    print(df_notsame.groupby(by='source').count())
    print('---------------------- Not Qualified ----------------------')
    print(df_same.groupby(by='source').count())
    save_same, save_notsame = os.path.join(data_dir, save_name+'same.csv'), os.path.join(data_dir, save_name+'notsame.csv')

    if os.path.exists(save_same):
        df_same.to_csv(save_same, index=True, encoding="utf-8-sig", mode='a', header=False)
    else:
        df_same.to_csv(save_same, index=True, encoding="utf-8-sig")

    if os.path.exists(save_notsame):
        df_notsame.to_csv(save_notsame, index=True, encoding="utf-8-sig", mode='a', header=False)
    else:
        df_notsame.to_csv(save_notsame, index=True, encoding="utf-8-sig")
