## Code generating fake news.

[CoT_1.py](https://github.com/styxsys0927/VLPFN/blob/main/fakenews_generation/CoT_1.py) includes fake news generation prompts mentioned in the paper.

[CoT_qualification.py](https://github.com/styxsys0927/VLPFN/blob/main/fakenews_generation/CoT_qualification.py) contains functions used for the qualification step in the paper.

Since VLPrompt and SUMMARY generate the fake news article in the last step while QA generates the article in the third step out of five, the articles require different processes to be pulled out. Therefore, to get clean articles, we use [CoT_generation_VLP_SUMMARY.py](https://github.com/styxsys0927/VLPFN/blob/main/fakenews_generation/CoT_generation_VLP_SUMMARY.py) to separate the articles from the VLPrompt/SUMMARY's outputs and [CoT_generation_QA.py](https://github.com/styxsys0927/VLPFN/blob/main/fakenews_generation/CoT_generation_QA.py) to get the articles of QA's outputs. Note that different LLMs may also format their answers differently. You may need to change the string processing functions to deal with your model's outputs.
