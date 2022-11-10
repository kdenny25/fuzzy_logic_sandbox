import rapidfuzz as rf
import pandas as pd
import rapidfuzz.string_metric

# upload a sample of data into a dataframe
df = pd.read_csv('./data/sample.csv')

pd.set_option('display.max_colwidth', None)
# sample phrase to compare
phrase = df.text.iloc[1]


print('RATIO')

# empty dataframe to add values to
ratio_list = []
text_list = []

# Ratio method calculates a normalized distance between two texts
for idx, value in enumerate(df.text):
    ratio = rf.fuzz.ratio(phrase, value)
    if(ratio > 50):
        ratio_list.append(ratio)
        text_list.append(value)

new_df = pd.DataFrame(list(zip(ratio_list, text_list)),
                      columns=['ratio', 'text'])
display(new_df)

print('PARTIAL RATIO')

#clear the lists
ratio_list.clear()
text_list.clear()

# Partial Ratio method
for idx, value in enumerate(df.text):
    pratio = rf.fuzz.partial_ratio(phrase, value)
    if(pratio > 50):
        ratio_list.append(pratio)
        text_list.append(value)

new_df = pd.DataFrame(list(zip(ratio_list, text_list)),
                      columns=['ratio', 'text'])
display(new_df)

print('TOKEN SET RATIO')

#clear the lists
ratio_list.clear()
text_list.clear()

# Token Set Ratio compares the words in the strings based on unique
# common words between them.
for idx, value in enumerate(df.text):
    tratio = rf.fuzz.token_set_ratio(phrase, value)
    if(tratio > 50):
        ratio_list.append(tratio)
        text_list.append(value)

new_df = pd.DataFrame(list(zip(ratio_list, text_list)),
                      columns=['ratio', 'text'])
display(new_df)

print('TOKEN SORT RATIO')

#clear the lists
ratio_list.clear()
text_list.clear()

# Token Sort Ratio sorts the words in the strings based and calculates the fuzz.ratio between them
# common words between them.
for idx, value in enumerate(df.text):
    tratio = rf.fuzz.token_sort_ratio(phrase, value)
    if(tratio > 50):
        ratio_list.append(tratio)
        text_list.append(value)

new_df = pd.DataFrame(list(zip(ratio_list, text_list)),
                      columns=['ratio', 'text'])
display(new_df)

print('W RATIO')

#clear the lists
ratio_list.clear()
text_list.clear()

# W Ratio calculated the weighted ratio based on other ratio algorithms.
for idx, value in enumerate(df.text):
    tratio = rf.fuzz.WRatio(phrase, value)
    if(tratio > 50):
        ratio_list.append(tratio)
        text_list.append(value)

new_df = pd.DataFrame(list(zip(ratio_list, text_list)),
                      columns=['ratio', 'text'])
display(new_df)

print('Q RATIO')

#clear the lists
ratio_list.clear()
text_list.clear()

# W Ratio calculated the weighted ratio based on other ratio algorithms.
for idx, value in enumerate(df.text):
    tratio = rf.fuzz.QRatio(phrase, value)
    if(tratio > 50):
        ratio_list.append(tratio)
        text_list.append(value)

new_df = pd.DataFrame(list(zip(ratio_list, text_list)),
                      columns=['ratio', 'text'])
display(new_df)

# Jaro Similarity
print('JARO SIMILARITY')
print(rf.distance.Jaro.similarity('hey there', 'hey thereyou'))


# Jaro-Winkler Similarity - has a scaling factor p, making it more accurate
print('JARO-WINKLER SIMILARITY')
print(rf.distance.JaroWinkler.similarity('hey there', 'hey thereyou'))

# Hamming Distance - The minimum amount of substitutions required to transform
# s1 into s2. Both strings need to be of the same length
print('HAMMING DISTNACE')
print(rf.distance.Hamming.similarity('awesomeee', 'aweeesome'))