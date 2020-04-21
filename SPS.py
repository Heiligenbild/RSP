#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

should_cont = True

while should_cont:
    player_choice = input('камень, ножницы или бумага?\n').lower()
    
    if player_choice not in ['камень','ножницы','бумага']:
        print('Попробуй еще раз, дружок')
        continue
    
    answer = ['камень','ножницы','бумага']
    comp_choice = random.choice(answer)
    print (f'А у меня {comp_choice}')
    
    if player_choice == comp_choice:
        print('Значит ничья, амиго!')
    elif player_choice == 'камень' and comp_choice == 'ножницы' or player_choice == 'ножницы' and comp_choice == 'бумага' or player_choice == 'бумага' and comp_choice == 'камень':
        print('Сегодня твой день, дружок, ты выиграл!')
    else:
        print('Опять не повезло, дружок? Я выиграл!')
        
    should_cont = input('Сыграем ещё? [да\нет]').lower() == 'да'


# In[ ]:





# In[ ]:




