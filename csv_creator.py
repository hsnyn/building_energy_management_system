# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 14:44:27 2020

@author: user
"""

import pandas as pd
data = pd.read_csv('AI-1_235.csv')
data = data[['Date','Time','AI Chiller Cost','AI Chiller Energy(MJ)','Legacy Chiller Cost','Legacy Chiller Energy(MJ)','Visitors','Otemp','OHum','Legacy AHU RT','AI AHU RT','AI_AC-1','AI_AC-2','AI_AC-3','AI_AC-4','AI_ AC-5','AI_ AC-6','AI_LTC-1','AI_LTC-2','AI_LTC-3','AI_STC-1','AI_STC-2','AC-1','AC-2','AC-3','AC-4','AC-5','AC-6','LTC-1','LTC-2','LTC-3','STC-1','STC-2','AH-101A-RT','AH-101B-RT','AH-102A-RT','AH-102B-RT','AH-201A-RT','AH-201B-RT','AH-202A-RT','AH-202B-RT','AH-301-RT_X','AH-302-RT_X','AH-303A-RT','AH-303B-RT','AH-401A-RT','AH-401B-RT','AH-402A-RT','AH-402B-RT','AH-501A-RT','AH-501B-RT','AH-502A-RT','AH-502B-RT','AH-503A-RT','AH-503B-RT','AH-504A-RT','AH-504B-RT','AH-505A-RT','AH-505B-RT','AH-506-RT_X','AH-601A-RT','AH-601B-RT','AH-602A-RT','AH-602B-RT','AH-603A-RT','AH-603B-RT','AH-604A-RT','AH-604B-RT','AH-605A-RT','AH-605B-RT','AH-606-RT_X','AH-701A-RT','AH-701B-RT','AH-702A-RT','AH-702B-RT','AH-703A-RT','AH-703B-RT','AH-704A-RT','AH-704B-RT','AH-705A-RT','AH-705B-RT','AH-706-RT_X','AH-801A-RT','AH-801B-RT','AH-802A-RT','AH-802B-RT','AH-803A-RT','AH-803B-RT','AH-804-RT_X','AH-805-RT_X','AH-806-RT_X','AH-901-RT_X','AH-902-RT_X','AH-B01A--RT','AH-B01B--RT','AH-B02A--RT','AH-B02B--RT','AH-B03A--RT','AH-B03B--RT','AH-B04A--RT','AH-B04B--RT']]
data['temp'] = data['Date'].str.split('/').str[2]
data = data.loc[data['temp'] == '2019']
del data['temp']
data = data.reset_index(drop=True)
data['Date'] = data['Date'].str.split('/').str[2]+'.'+data['Date'].str.split('/').str[0]+'.'+data['Date'].str.split('/').str[1]
data.to_csv('Data_2019.csv', index=0)