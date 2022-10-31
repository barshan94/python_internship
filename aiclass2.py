
# Class 2



#Numpy Library

import numpy as np
a=np.array(["Dress","Saree","Churi"])
print(a)
print(a.ndim)
print(a.size)
b=np.array([["Chicken","Butter","Mutton"],["1 plate","1 piece","1 kg"],["Birthday","Random","Anniversary"]])
print(b)
print(b.ndim)
print(b.size)


# MAtplot Library
import matplotlib.pyplot as plt
a=[1,2,3,4]
b=[1,8,27,64]
plt.plot(a,b,color="black",marker="*",linewidth="2")
plt.title("Simple Graph")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")


# Line graph using numpy & matplotlib
import numpy as np
import matplotlib.pyplot as plt
c=np.array([1,4,9,16,25])
d=np.array([1,2,3,4,5])
plt.plot(c,d,color="blue",linewidth="1",marker="*")
plt.title("Sample Graph")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.xticks(range(-5,30,5))
plt.yticks(range(0,6,1))



# Scatter graph using numpy & matplotlib
import numpy as np
import matplotlib.pyplot as plt
c=np.array([1,4,9,16,25])
d=np.array([1,2,3,4,5])
plt.scatter(c,d,color="gold")
plt.plot(c,d,color="blue",linewidth="1")
plt.title("Sample Graph")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.xticks(range(-5,30,5))
plt.yticks(range(0,6,1))



# Bar graph using numpy & matplotlib
import numpy as np
import matplotlib.pyplot as plt
c=np.array(["BGB","Tony","Amit","Ranok","Susmoy"])
d=np.array([120,90,60,69,96])
plt.bar(c,d,color=["blue","red","orange","pink","yellow"])
# for hot=rizontal=  plt.barh(c,d,color=["blue","red","orange","pink","yellow"]) 
plt.title("Bar Graph")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")



# Pandas
# DataFrame & Series
# DataFrame
import pandas as pd
mydata={"food":["Grill","Roast","Biriyani"],"quantity":["Full","4 piece","Full"]}
df=pd.DataFrame(mydata)
df



# Pandas
# Series
import pandas as pd
mydata=[1,4,8,12,16,20]
df=pd.Series(mydata)
df


#Dataset -> "https://storage.googleapis.com/kagglesdsdata/datasets/9590/13660/fruit_data_with_colors.txt?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20221031%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20221031T082950Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=438cfbb521fe20d043bd5eeebd3e21507ba0457af63f6f77d09a6f1c7205d8d4df8aa12f8c917c6f86ed6fc15f4abcf87a1f5055bef756f95c08f3553f4bf0b8aa11efffe9a7b5182976f32cf549262d0d5e281bac63697422a7bb3c7b4e877626a03795afe1d000f0176cf91de26cc8bee8897aa2665d1ae0f084fe939bd8ff2b51d218cad05f3dc4c36267db5d0f5d4b726047c404d5ea0bb40be08d5e3165fe9c19b43fb1bc401a512c522a17d1340986c4b8b487f829c92ca82350df31826bf78cef4e4d8bb8449361470001cd9a3130b7afdddbe7140cff68d3f4a0a7fb43f8ecbb61a7c2a0a16da35eb3c73d88b9a5af70a1b475df29b81f83608732be"
# External Data set analysis using Pandas
import pandas as pd
df=pd.read_csv("https://storage.googleapis.com/kagglesdsdata/datasets/9590/13660/fruit_data_with_colors.txt?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20221031%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20221031T082950Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=438cfbb521fe20d043bd5eeebd3e21507ba0457af63f6f77d09a6f1c7205d8d4df8aa12f8c917c6f86ed6fc15f4abcf87a1f5055bef756f95c08f3553f4bf0b8aa11efffe9a7b5182976f32cf549262d0d5e281bac63697422a7bb3c7b4e877626a03795afe1d000f0176cf91de26cc8bee8897aa2665d1ae0f084fe939bd8ff2b51d218cad05f3dc4c36267db5d0f5d4b726047c404d5ea0bb40be08d5e3165fe9c19b43fb1bc401a512c522a17d1340986c4b8b487f829c92ca82350df31826bf78cef4e4d8bb8449361470001cd9a3130b7afdddbe7140cff68d3f4a0a7fb43f8ecbb61a7c2a0a16da35eb3c73d88b9a5af70a1b475df29b81f83608732be",sep="\t")
#read_csv working for reading a csv file
#sep="\t" working to seperate all collumn
df


df.info()
#for knowing all details descriptively


df.shape
#for exactly knowing rows and collumns



df.size
# for the total of all rows and collumn multiplication


#slicing from 25 to upto 43
df[25:44]

df.iloc[25:44,0:2]
#iloc is used for both row and collumn slicing

df.fruit_name.nunique()
# to count the number of unique foods


df.fruit_name.unique()
# to find the fruit name also


df.groupby("fruit_name").size()
# count of individual fruits total

