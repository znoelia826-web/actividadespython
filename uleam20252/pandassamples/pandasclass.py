import pandas as pd

print('********ok********')

setData = pd.Series(data=[10, 20, 30, 40], index=['carlos', 'jose', 'anita', 'luisa'])

print(setData)
print(setData.index)

# Esto causaba error porque 'lucas' no existe en el índice
# print(setData['lucas'])  # ❌
print('¿lucas está en setData?', 'lucas' in setData)

setData1 = setData * 2
print(setData1)

print('****************************** DATA FRAME *******************************************************')

dictionary = {
    'one': pd.Series(data=[1, 2, 3, 4, 5], index=['alex', 'jose', 'anita', 'luisa', 'carlos']),
    'two': pd.Series(data=[10, 20, 30, 40, 50], index=['alex', 'jose', 'anita', 'luisa', 'carlos'])
}

# ❌ era Dataframe → ✅ DataFrame
df = pd.DataFrame(dictionary)
print(df)
print(df.index)
print(df.columns)

df['three'] = df['one'] * df['two']
print(df)

df['filter'] = df['three'] > 45
print(df)

del df['filter']
print(df)

df.insert(1, 'copy of one', df['one'])
print(df)

print('/////////////////////////////////////////////// IMPORTING CSV FILES ///////////////////')
movies = pd.read_csv('movies.csv')
print(movies.columns)
print(movies.shape)

ratings = pd.read_csv('ratings.csv')
print(ratings.columns)
print(ratings.shape)

tags = pd.read_csv('tags.csv')
print(tags.columns)
print(tags.shape)

print(tags.tail(2))
del ratings['timestamp']
del tags['timestamp']
print('variables of tags:', tags.columns)
print('variables of ratings:', ratings.columns)

print('<--------------------------------------------------->')
print(tags.iloc[0])
print(tags.iloc[[0, 22, 500]])
print(tags.index)

print('*+++++++++++++++++ RATINGS +++++++++++++++++++++')
print(ratings.head(5))
print(ratings['rating'].describe())
print(ratings['rating'].mean())
print(ratings['rating'].min())
print(ratings['rating'].max())

is_highly_rated = ratings['rating'] >= 4
print(is_highly_rated.head(4))

print(ratings.shape)
print(ratings[is_highly_rated].shape)
print(movies.columns)
print(movies.head(2))

is_animation = movies['genres'].str.contains('Animation', na=False)
print(movies.shape)
print(movies[is_animation].shape)

print('movies')
print(movies.columns)
print('ratings')
print(ratings.columns)
