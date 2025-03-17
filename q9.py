import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('.\data\electronic.csv')

mask = (df['DateTime'] >= '2019-01-01') & (df['DateTime'] < '2019-01-02')
df_0101 = df[mask].copy()
print(df_0101)



plt.rc('figure', figsize=(10, 8))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(df_0101['DateTime'], df_0101['Consumption'], 'o-r')

ax.set_xticks([0, 6, 12, 18, 24])
ax.set_xticklabels(['00:00', '06:00', '12:00', '18:00', '24:00'], fontsize= 'small')

font_title = {'family':'batang','c':'b','size':30}
font_sub = {'family':'gulim','c':'k','size':15}

ax.set_title('19.01.01 시간당 전력소비량', fontdict=font_title)
ax.set_xlabel('시간', fontdict=font_sub)
ax.set_ylabel('전력 소비량', fontdict=font_sub)

ax.grid()

plt.show()




