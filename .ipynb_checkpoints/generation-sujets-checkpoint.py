#!/usr/bin/env python
# coding: utf-8

# # Génération des exercices

# In[ ]:


import pandas as pd


# In[ ]:


get_ipython().run_line_magic('cd', '/home/hathout/Developpements/2022-Demonext/Generation-exercices/Demonext/')


# In[ ]:


people = pd.read_csv('names.csv')
people = people.sort_values('last')
people = people['first'] + '_' + people['last']
people = list(people.drop_duplicates())


# In[ ]:


sem = pd.read_csv('Data/sem.csv', delimiter=',')
specif = {}
ex = {}


# In[ ]:


data1 = pd.read_csv('Data/data-iser.csv')

specif['exun'] = {'type':'exlex+class', 'nbex':5, 'nbclass':2}

ex['exun'] = {}
ex['exun']['adj'] = data1['verbe'][(data1['cat_base']=='adj')]
ex['exun']['noun'] = data1['verbe'][(data1['cat_base']=='noun')]
ex['exun']['prefix'] = data1['verbe'][(data1['cat_base']=='prefix')]
ex['exun']['simplex'] = data1['verbe'][(data1['cat_base']=='simplex')]


# In[ ]:


data2 = pd.read_csv('Data/data-ite.csv')

specif['exdeux'] = {'type':'exlex+class', 'nbex':4, 'nbclass':2}

ex['exdeux'] = {}
ex['exdeux']['absurdite'] = data2['dérivé'][(data2['procédé']=='ité') & (data2['allomorphie?']=='0') & (data2['m=f']==1)]
ex['exdeux']['adaptabilite'] = data2['dérivé'][(data2['procédé']=='ité') & (data2['allomorphie?'].isin(['able~abil'])) & (data2['m=f']==1)]
ex['exdeux']['biodiversite'] = data2['dérivé'][data2['procédé']=='pfx']
ex['exdeux']['bonte'] = data2['dérivé'][(data2['procédé']=='té') & (data2['allomorphie?']=='0') & (data2['m=f']==1)]
ex['exdeux']['parite'] = data2['dérivé'][(data2['procédé']=='ité') & (data2['allomorphie?'].isin(['el~al','aire~ar'])) & (data2['m=f']==1)]


# In[ ]:


data3 = pd.read_csv('Data/data-denominaux.csv', delimiter=',')
data3['couple'] = data3['graph_1'] + ' -- ' + data3['graph_2']
data3 = data3.join(sem.set_index('graphie'), on='graph_2')

specif['extrois'] = {'type':'exlex', 'nbex':2}

ex['extrois'] = {}
ex['extrois']['panifier'] = data3['couple'][(data3['cstr_1'].isin(['Xifier', 'Xiser'])) & (data3['Artifact']==1)]
ex['extrois']['embrasser'] =  data3['couple'][(data3['cstr_1'] == 'enX') & (data3['Body']==1)]
ex['extrois']['vampiriser'] = data3['couple'][(data3['cstr_1'].isin(['Xifier', 'Xiser'])) & (data3['Person']==1)]

specif['extroisbis'] = {'type':'exlex', 'nbex':5}
ex['extroisbis'] = {}
ex['extroisbis']['pain'] = sem['graphie'][(sem['Artifact'] == 1)]
ex['extroisbis']['bras'] = sem['graphie'][(sem['Body'] == 1)]
ex['extroisbis']['vampire'] = sem['graphie'][(sem['Person'] == 1)]


# In[ ]:


data4 = pd.read_csv('Data/data-conversion.csv', delimiter=',')
data4['couple'] = data4['graph_1'] + ' -- ' + data4['graph_2']
data4 = data4.join(sem.set_index('graphie'), on='graph_2')

specif['exquatre'] = {'type':'exlex', 'nbex':2}

ex['exquatre'] = {}
ex['exquatre']['zigzaguer'] = data4['couple'][(data4['cat_1'] == 'V') & (data4['Act']==1)]
ex['exquatre']['vitrioler'] = data4['couple'][(data4['cat_1'] == 'V') & (data4['Substance']==1)]
ex['exquatre']['ventriloquer'] = data4['couple'][(data4['cat_1'] == 'V') & (data4['Person']==1)]

specif['exquatrebis'] = {'type':'exlex', 'nbex':5}

ex['exquatrebis'] = {}
ex['exquatrebis']['zigzag'] = sem['graphie'][(sem['Act'] == 1)]
ex['exquatrebis']['vitriol'] = sem['graphie'][(sem['Substance'] == 1)]
ex['exquatrebis']['ventriloque'] = sem['graphie'][(sem['Person'] == 1)]


# In[ ]:


data5 = pd.read_csv('Data/data-histoire.csv', delimiter=',')
data5['couple'] = data5['graph_1'] + ' -- ' + data5['graph_2']

specif['excinq'] = {'type':'exlex', 'nbex':5}

ex['excinq'] = {}
ex['excinq']['cogestionnaire'] = data5['couple'][(data5['cat_1'] == 'Adj') & (data5['cat_2']== 'V') & (data5['complexite'] == 'complexe') & (data5['orientation'] == 'des2as')]
ex['excinq']['poulailler'] = data5['couple'][(data5['cat_1'].isin(['Nm', 'Nf', 'Npx'])) & (data5['cat_2'].isin(['Nm', 'Nf', 'Npx'])) & (data5['complexite'] == 'complexe') & (data5['orientation'] == 'des2as')]
ex['excinq']['langagier'] = data5['couple'][(data5['cat_1'] == 'Adj') & (data5['cat_2'].isin(['Nm', 'Nf', 'Npx'])) & (data5['complexite'] == 'complexe') & (data5['orientation'] == 'des2as')]
ex['excinq']['bitumisation'] = data5['couple'][(data5['cat_1'].isin(['Nm', 'Nf', 'Npx'])) & (data5['cat_2'] == 'V')]


# In[ ]:


data6 = pd.read_csv('Data/data-nouvelle-histoire.csv', delimiter=',')
data6['couple'] = data6['graph_1'] + ' -- ' + data6['graph_2']

specif['exsix'] = {'type':'exlex', 'nbex':1}

ex['exsix'] = {}
ex['exsix']['antigrippal'] = data6['couple'][(data6['cat_1'] == 'Adj') & (data6['cat_2'].isin(['Nm', 'Nf', 'Npx'])) & (data6['type_cstr_1'] == 'pre-suf') & (data6['cstr_2'] == 'X')]
ex['exsix']['postglaciaire'] = data6['couple'][(data6['cat_1'] == 'Adj') & (data6['cat_2'].isin(['Nm', 'Nf', 'Npx'])) & (data6['type_cstr_1'] == 'pre-suf') & (data6['orientation'] == 'indirect')]


# In[ ]:


data7 = pd.read_csv('Data/data-indirect-simple.csv', delimiter=',')
data7['couple'] = data7['graph_1'] + ' -- ' + data7['graph_2']

specif['exsept'] = {'type':'exlex', 'nbex':1}

ex['exsept'] = {}
ex['exsept']['applicateur'] = data7['couple'][(data7['cat_1'].isin(['Nm', 'Nf', 'Npx'])) & (data7['cat_2'].isin(['Nm', 'Nf', 'Npx'])) & (data7['type_cstr_1'] == 'suf') & (data7['type_cstr_2'] == 'suf') & (data7['orientation'] == 'indirect') & (data7['complexite'] == 'simple')]
ex['exsept']['contestataire'] =  data7['couple'][(data7['cat_1'] == 'Adj') & (data7['cat_2'].isin(['Nm', 'Nf', 'Npx'])) & (data7['type_cstr_1'] == 'suf') & (data7['type_cstr_2'] == 'suf') & (data7['orientation'] == 'indirect') & (data7['complexite'] == 'simple')]


# In[ ]:


data8 = pd.read_csv('Data/data-variation.csv', delimiter=',')

specif['exhuit'] = {'type':'exlist', 'nbex':1}

data8 = data8[data8['cat_2']  == 'Nm']
data8['duplic'] = data8.graph_2.duplicated(keep='last')
data8x = data8[['graph_1', 'graph_2']][data8['duplic'] == True].copy()
data8x['graph_1'] = data8x['graph_2']
data8y = pd.concat([data8[['graph_1', 'graph_2']], data8x]).drop_duplicates()
masky = data8y.graph_2.duplicated(keep=False)
data8z = data8y[masky].groupby(['graph_2']).graph_1.apply(list).reset_index(name='variantes')

ex['exhuit'] = {}
ex['exhuit'] = data8z


# In[ ]:


data9 = pd.read_csv('Data/data-decalages.csv', delimiter=',')
data9['couple'] = data9['graph_1'] + ' -- ' + data9['graph_2']

specif['exneuf'] = {'type':'exlex', 'nbex':1}

ex['exneuf'] = {}
ex['exneuf']['cartesianisme'] = data9['couple'][(data9['cstr_1'] == 'Xianisme') & (data9['cstr_2'] == 'X') & (data9['complexite'] == 'motiv-sem')]
ex['exneuf']['urbanisme'] = data9['couple'][(data9['cstr_1'] == 'Xanisme') & (data9['cstr_2'] == 'X') & (data9['complexite'] == 'motiv-sem')]
ex['exneuf']['historicisme'] = data9['couple'][(data9['cstr_1'] == 'Xicisme') & (data9['cstr_2'] == 'X') & (data9['complexite'] == 'motiv-sem')]
ex['exneuf']['cellularisme'] = data9['couple'][(data9['cstr_1'] == 'Xarisme') & (data9['cstr_2'] == 'X') & (data9['complexite'] == 'motiv-sem')]


# In[ ]:


for etudiant in people:
    enonce = ''
    enonce += '\\newcommand{{\\student}}{{{0}}}\n'.format(' '.join(etudiant.split('_')))
    
    for exo in ex:
        match specif[exo]['type']:
            case 'exlex':
                for extype in sorted(ex[exo].keys()):
                    exlex = list(ex[exo][extype].sample(specif[exo]['nbex']))
                    enonce += '\\newcommand{{\\{0}}}{{\\label{{{0}}} {1}}}\n'.format(extype + exo, ', '.join(sorted(exlex))) 
            case 'exlex+class':
                exa_classer = []
                for extype in sorted(ex[exo].keys()):
                    exemples = list(ex[exo][extype].sample(specif[exo]['nbex'] + specif[exo]['nbclass']))
                    exlex = exemples[:specif[exo]['nbex']]
                    exa_classer  += exemples[specif[exo]['nbex']:]
                    enonce += '\\newcommand{{\\{0}}}{{\\label{{{0}}} {1}}}\n'.format(extype + exo, ', '.join(sorted(exlex)))
                enonce += '\\newcommand{{\\aclasser{0}}}{{{1}}}\n'.format(exo, ', '.join(sorted(exa_classer)))    
            case 'exlist':
                exlist = sorted(set(ex[exo].sample(specif[exo]['nbex']).iloc[0]['variantes']))
                enonce += '\\newcommand{{\\{0}}}{{\\label{{{0}}} {1}}}\n'.format(exo, ', '.join(exlist))         

    file = open('latexvars','w')
    file.write(enonce)
    file.close()
    get_ipython().system("cat enonces-preamble.tex latexvars enonces-body.tex > {'enonces_' + etudiant + '.tex'}")
    get_ipython().system("xelatex {'enonces_'+ etudiant +'.tex'}")
    get_ipython().system("xelatex {'enonces_'+ etudiant +'.tex'}")
    get_ipython().system("mv {'enonces_' + etudiant + '.pdf'} {'sujets/'}")
    get_ipython().system("rm {'*' + etudiant + '*'}")
    get_ipython().system('rm latexvars')

