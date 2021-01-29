#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## funcion que recibe nombre de archivo excel y de hoja a leer
def open_excel(file, sheet):
	import pandas as pd
	return pd.read_excel(file, sheet_name = sheet)


# In[ ]:


## FUNCION GRAFICO BARRA CON BINS
def barplot_bins(x_axis, title='', x_label='',y_label='', x_max=10, x_min=-10, y_max=10, y_min=-10):
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    min_diff = x_axis.min()
    max_diff = x_axis.max()
    diff = abs(int(np.diff([ max_diff, min_diff ])[0]*10)) ## se extrae diferencia en puntos (1 pto = 10 decimas) y se multiplica por 10 para obtener decimas

    bins = pd.cut(x_axis, bins=diff) ## se crean valores para hacer agrupacion por rango
    y = x_axis.groupby(bins).count()  ## se agrupan diferencias de notas por rango de diferencia
    x = range(int(min_diff*10)+1,int(max_diff*10)+1,1) ## se crea una lista de valores para eje X, y asi evitar exceso de texto (para no mostrar como rangos)
    plt.bar(x, y)

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)


    ## SETEA RANGOS EN EJES X, Y
    plt.xlim(x_min,x_max)
    plt.ylim(y_min,y_max)

    plt.show()

# In[ ]:


## SCATTER PLOT SIN CATEGORIZAR
def scatterplot(x_axis, y_axis, title='', x_label='', y_label='', color='black', label='', alpha=0.15):
    import matplotlib.pyplot as plt
    import pandas as pd
    
    plt.plot(x_axis, y_axis, marker='o', markersize=2, linestyle='None', color=color, label=label, alpha=alpha)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(color='navy', linewidth=0.5, alpha=0.3)

    ## SETEA RANGOS EN EJES X, Y
    plt.xlim(0,7)
    plt.ylim(0,7)
    plt.legend()
    
    plt.show()


# In[ ]:


## SCATTER PLOT CATEGORIZADO
def hue_scatterplot(data, x_axis_name, y_axis_name, hue, size, x_label='', y_label='', color='black', label='', alpha=0.15):
    import matplotlib.pyplot as plt
    import seaborn as sns
    import pandas as pd
    
    sns.scatterplot(data=data, x=x_axis_name, y=y_axis_name, hue=hue, s=size, alpha=alpha, palette='hls')

    ## SETEA RANGOS EN EJES X, Y

    plt.show()


# In[ ]:


## FILTRO ESTUDIANTE Y CURSO
def check_student_by_course(user_id, course_id):
	import pandas as pd
	if(user_id != '' and course_id != ''):
		caso = notas[ (notas['course_id'] == course_id) & (notas['user_id'] == user_id) ][['course_id','RUT','user_id','NOTA_PRESENTACION_BANNER','NOTA_PRESENTACION_BB','NOTA_FINAL_BANNER','NOTA_FINAL_REAL_BB']]
		caso


# In[ ]:


## GRAFICO DE CORRELACION CON MAPA DE CALOR
def corr_heatmap_plot(array):
    import matplotlib.pyplot as plt
    import seaborn as sns
    import pandas as pd

    corr_array = array.corr()

    sns.heatmap(corr_array, square=True,cmap='RdYlGn' )
    
    plt.plot()


# In[ ]:


## GRAFICO DE CORRELACION CON TENDENCIA Y SCATTERPLOT
def corr_trend_scatter_plot(array, category=''):
    import matplotlib.pyplot as plt
    import seaborn as sns
    import pandas as pd
    
    sns.pairplot(array, kind="scatter", hue=category, markers=".", palette="hls")
    
    plt.show()


# In[ ]:




