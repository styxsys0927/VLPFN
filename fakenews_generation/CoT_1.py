delimiter = "####"
system_message1 = f"""
Follow these steps to analyze the news articles.
The contents of the article will be delimited with four hashtags,\
i.e. {delimiter}. 

Step 1:{delimiter} List the critical objects, events, relations, \
assumptions, and opinions provided by the article. \

You should reply the list with each item of the list starting with '*' and no additional words should be added except for the list. \

Step 2: {delimiter} Choose a role below who has motivations to modify the news article. \
The selection of role should be based on the degree of confidences you think the example scenario of the role aligns with the article. \

1. Financial Gain: This guy works for a hostile organization of interests. Criticizing the product/service mentioned in the article can make more customers turn to other product/service.
2. Political Agenda: This guy modifies articles supports a particular political ideology or candidate to make the public opinions turn against them and would not vote for them.
3. Social Media Attention: This guy rewrites articles by stressing the negative effects and ignoring positive aspects of things to get others' attention. 
4. Mischievous Intent: This guy writes to make celebrations look stupid to amuse others. For example, the president farts a lot during the meeting with the UN.
5. Promotion of Hate: This guy hates an agenda or ideology and wants the others hate it by claiming that the agenda/ideology having a history of lying or their intentions being hostile.
6. Competing with Legitimate Sources: This guy does not trust legitimate news sources and want to convince the others. He divertes attention away from accurate reporting.
7. Personal Vendettas: This guy hates someone interviewed in the article and tries to make his/her claim look wrong.
8. Ideological Manipulation: This guy believes in some gods and think everything he cannot explain are done by them. This guy may claim some shocking discovery or disaster are created by his gods.

Step 3: {delimiter} Consider that you are the selected role and you want to modify the critical factors to achieve your goal. \

There are some rules to follow during modifiction: \

1. The modifications have to change the meaning of the factors. 
2. You should not directly cite/question/negate the content of the original article. Rewrite the modified factor as if you are the first to report it.
3. All the modifications should serve the same conclusion. The conclusion should express a clear opinion which is different from the original article's conclustion.
4. The objectives of the modifications should be logically consist. 

Let's think step by step, what would you do to modify the article? \

Step 4: {delimiter} write an article with the modified factors in the writing style of the original article. \
The article should be of the similar length as the original article. \

Always start your answer with:
Article: {delimiter} \n

"""

system_message1_ab_all = f"""
Rewrite the news article below quoted by {delimiter}, so that the generated article holds different opinions against the original article.
Always start the content of the article with:
Article: {delimiter}\n

"""

system_message1_ab_role = f"""
Follow these steps to analyze the news articles.
The contents of the article will be delimited with four hashtags,\
i.e. {delimiter}. 

Step 1:{delimiter} List the critical objects, events, relations, \
assumptions, and opinions provided by the article. \

You should reply the list with each item of the list starting with '*' and no additional words should be added except for the list. \

Step 2: {delimiter} Consider that you want to modify the critical factors. \

There are some rules to follow during modifiction: \

1. The modifications have to change the meaning of the factors. 
2. You should not directly cite/question/negate the content of the original article. Rewrite the modified factor as if you are the first to report it.
3. All the modifications should serve the same conclusion. The conclusion should express a clear opinion which is different from the original article's conclustion.
4. The objectives of the modifications should be logically consist. 

Let's think step by step, what would you do to modify the article? \

Step 3: {delimiter} write an article with the modified factors in the writing style of the original article. \
The article should be of the similar length as the original article. \

Always start your answer with:
Article: {delimiter} \n

"""

system_message1_ab_sem = f"""
Follow these steps to analyze the news articles.
The contents of the article will be delimited with four hashtags,\
i.e. {delimiter}. 

Step 1:{delimiter} List the critical objects, events, relations, \
assumptions, and opinions provided by the article. \

You should reply the list with each item of the list starting with '*' and no additional words should be added except for the list. \

Step 2: {delimiter} Choose a role below who has motivations to modify the news article. \
The selection of role should be based on the degree of confidences you think the example scenario of the role aligns with the article. \

1. Financial Gain: This guy works for a hostile organization of interests. Criticizing the product/service mentioned in the article can make more customers turn to other product/service.
2. Political Agenda: This guy modifies articles supports a particular political ideology or candidate to make the public opinions turn against them and would not vote for them.
3. Social Media Attention: This guy rewrites articles by stressing the negative effects and ignoring positive aspects of things to get others' attention. 
4. Mischievous Intent: This guy writes to make celebrations look stupid to amuse others. For example, the president farts a lot during the meeting with the UN.
5. Promotion of Hate: This guy hates an agenda or ideology and wants the others hate it by claiming that the agenda/ideology having a history of lying or their intentions being hostile.
6. Competing with Legitimate Sources: This guy does not trust legitimate news sources and want to convince the others. He divertes attention away from accurate reporting.
7. Personal Vendettas: This guy hates someone interviewed in the article and tries to make his/her claim look wrong.
8. Ideological Manipulation: This guy believes in some gods and think everything he cannot explain are done by them. This guy may claim some shocking discovery or disaster are created by his gods.

Step 3: {delimiter} Consider that you are the selected role and you want to modify the critical factors to achieve your goal. \

There are some rules to follow during modifiction: \

1. The modifications have to change the meaning of the factors. 
2. You should not directly cite/question/negate the content of the original article. Rewrite the modified factor as if you are the first to report it.
3. All the modifications should serve the same conclusion. The conclusion should express a clear opinion which is different from the original article's conclustion.
4. The objectives of the modifications should be logically consist. 

Let's think step by step, what would you do to modify the article? \

Step 4: {delimiter} write an article with the modified factors. \

Always start your answer with:
Article: {delimiter} \n

"""

system_message1_bl_QA = f"""
Follow these steps to analyze the news articles.
The contents of the article will be delimited with four hashtags,\
i.e. {delimiter}. 

Step 1: Raise a question about the article, and answer the question based on your understanding of the article.
Step 2: Modify the answer, so that the modified answer describes a fact/opinion different from the original one. 
Step 3: Rewrite the article, modify as few details as possible to make it support the answer generated in the last step.

Start the content of the generated article in Step 3 with:
Article: {delimiter}\n

Step 4: What is the answer to the question in Step 1 based on the generated article?

Step 5: Is the answer in Step 1 the same as the answer in Step 4?

"""

system_message1_bl_QA_l = f"""
Follow these steps to analyze the news articles.
The contents of the article will be delimited with four hashtags,\
i.e. {delimiter}. 

Step 1: Raise a question about the theme of the article, and answer the question based on your understanding of the article.
Step 2: Modify the answer, so that the modified answer describes a fact/opinion different from the original one. 
Step 3: Rewrite the article, modify as few details as possible to make it support the answer generated in the last step.

Start the content of the generated article in Step 3 with:
Article: {delimiter}\n

Step 4: What is the answer to the question in Step 1 based on the generated article?

Step 5: Is the answer in Step 1 the same as the answer in Step 4?

"""

system_message1_bl_QA_m = f"""
Follow these steps to analyze the news articles.
The contents of the article will be delimited with four hashtags,\
i.e. {delimiter}. 

Step 1: Raise a question about a part of the article, and answer the question based on your understanding of the article.
Step 2: Modify the answer, so that the modified answer describes a fact/opinion different from the original one. 
Step 3: Rewrite the article, modify as few details as possible to make it support the answer generated in the last step.

Start the content of the generated article in Step 3 with:
Article: {delimiter}\n

Step 4: What is the answer to the question in Step 1 based on the generated article?

Step 5: Is the answer in Step 1 the same as the answer in Step 4?

"""

system_message1_bl_QA_s = f"""
Follow these steps to analyze the news articles.
The contents of the article will be delimited with four hashtags,\
i.e. {delimiter}. 

Step 1: Raise a question about a detail in the article, and answer the question based on your understanding of the article.
Step 2: Modify the answer, so that the modified answer is different from the original one. 
Step 3: Rewrite the article, modify as few details as possible to make it support the answer generated in the last step.

Start the content of the generated article in Step 3 with:
Article: {delimiter}\n

Step 4: What is the answer to the question in Step 1 based on the generated article?

Step 5: Is the answer in Step 1 the same as the answer in Step 4?

""" # (value, location, date, name, term, etc.)

# Step 3: {delimiter} Modify each of the critical factors from the perspective of the role you chose in the last step. \
# The modifications have to change the meaning of the factors. \
#
# Use the following format:
# {delimiter} the role you chose.
# 1.
# Original factor:{delimiter} a summary of the original factor chosen to be modified.
# Modified factor:{delimiter} a summary of the modified version of the chosen factor.
# Reason: why you choose the role and how your modification is related to the role.
# 2.
# Original factor:{delimiter} a summary of the original factor chosen to be modified.
# Modified factor:{delimiter} a summary of the modified version of the chosen factor.
# Reason: why you choose the role and how your modification is related to the role.
# ... (all the other factors with the same format as above) ...
# Make sure to include {delimiter} to separate every listed.
#
# Step 4: {delimiter} write an article with the modified factors in the writing style of the original article.

# Step 2:{delimiter} Check if any of the critical factors can be wrong. \
# Step 3:{delimiter} If there are factors that can be wrong, \
# list the factors that are identified suspicious in Step 2, \
# provide your reasons and how would you correct them. \
#
# Use the following format:
# 1. the first critical factor that can be wrong
# Reason:{delimiter} why do you think this factor is wrong
# Correction:{delimiter} the correct element to be used to replace the factor
# 2. the second critical factor that can be wrong
# Reason:{delimiter} why do you think this factor is wrong
# Correction:{delimiter} the correct element to be used to replace the factor
# ... (all the other factors with the same format as above) ...
# Make sure to include {delimiter} to separate every listed.

###### with generated fakenews writing method
# For each critical factor, check if you can use a method listed below to modify it. \
# The selection of methods should be based on the degree of confidences you are of to understand and utilized the method. \
# The more you are confident in using a method, the more often you should use it. \
# The method list is as follow:
# 1. Cherry-Picking Data: select specific data points that support the news' narrative while ignoring the broader context or contradictory information.
# 2. Misleading Headlines: craft sensational or misleading headlines so that the headline can grab attention and different from the actual content of the article.
# 3. Out-of-Context Quotes: quote statements out of context to give them a different meaning, misrepresenting the original intent.
# 4. Fabricating Sources: cite non-existent experts or sources to lend credibility to claims different from the original claim.
# 5. Creating False Equivalencies: equate unrelated or dissimilar events to create a false sense of comparison and establish a misleading narrative.
# 6. Selective Editing: manipulate quated documents, pictures, audio, or video clips through editing to alter the meaning of statements.
# 7. Emotional Language: use emotionally charged language to evoke strong reactions and bias readers' perceptions.
# 8. Conspiracy Theories: present unfounded conspiracy theories as if they were verified facts to create intrigue and mistrust.
# 9. Anonymous Sources: rely heavily on unnamed sources to make it difficult to verify the authenticity of the information.
# 10. Half-Truths: mix accurate information with false or misleading details to create a deceptive narrative.
# 11. Confirmation Bias: target specific audiences with content that aligns with their pre-existing beliefs, reinforcing their biases.
# 12. Satire Misinterpreted as Fact: share satirical content as if it were real news, leading to confusion.
# 13. Exaggeration: amplify minor incidents or events to make them seem more significant than they actually are.
# 14. Denying Reliable Sources: dismiss credible sources while promoting unverified or biased ones.

# Step 4: {delimiter} write an article with the modified factors in the writing style of the original article.
#
# Step 5: {delimiter} forget about step 1, step 2, and step 3. Point out what are the differences between the content generated in step 4 and the content of the original news article.