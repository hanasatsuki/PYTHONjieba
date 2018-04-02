
# coding: utf-8

# In[1]:


pip install jieba


# In[8]:


#encoding=utf-8
import jieba

sentence = "獨立音樂需要大家一起來推廣，歡迎加入我們的行列！"
print ("Input：", sentence)
words = jieba.cut(sentence, cut_all=False)
print ("Output 精確模式 Full Mode：")
for word in words:
    print (word)

sentence = "独立音乐需要大家一起来推广，欢迎加入我们的行列！"
print ("Input：", sentence)
words = jieba.cut(sentence, cut_all=False)
print ("Output 精確模式 Full Mode：")
for word in words:
    print (word)


# In[18]:


#encoding=utf-8
import jieba

jieba.set_dictionary('dict.txt.big')

content = open('lyric.txt', 'rb').read()

print ("Input：", content)

words = jieba.cut(content, cut_all=False)

print ("Output 精確模式 Full Mode：")
for word in words:
    print (word)


# In[20]:


# encoding=utf-8
import jieba

jieba.set_dictionary('dict.txt.big')

seg_list = jieba.cut("塵世中一個迷途小書僮")
print(" / ".join(seg_list))

seg_list = jieba.cut("我們在野生動物園玩")
print(" / ".join(seg_list)) # 歧異詞辨識

seg_list = jieba.cut("林志傑是結巴PHP的作者")
print(" / ".join(seg_list)) # 新詞辨識


# In[22]:


# encoding=utf-8
import jieba

jieba.set_dictionary('dict.txt.big')

seg_list = jieba.cut("下雨天留客天留我不留")
print(" / ".join(seg_list))

seg_list = jieba.cut("海水朝朝朝朝朝朝朝落；浮雲長長長長長長長消。")
print(" / ".join(seg_list))

seg_list = jieba.cut("海水潮，朝朝潮，朝潮朝落；浮雲長，常常長，常長常消。")
print(" / ".join(seg_list))

