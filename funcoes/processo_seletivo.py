import pandas as pd
df = pd.read_csv('./data/workload.csv')
df.head()
def frequency_sort(items):
    """Sorts a list of items by number of occurrences"""

    df = pd.DataFrame(items, columns=['items'])
    df['count'] = df.groupby('items')['items'].transform('count')
    df = df.sort_values(['count', 'items'], ascending=[False, True])
    return df['items'].tolist()


def reverse_vowels(text):
    """Reverses the vowels in a string"""
    
    vowels = 'aeiou'
    text = list(text)
    i, j = 0, len(text) - 1
    while i < j:
        if text[i].lower() not in vowels:
            i += 1
        elif text[j].lower() not in vowels:
            j -= 1
        else:
            text[i], text[j] = text[j], text[i]
            i += 1
            j -= 1
    return ''.join(text)

def collapse_intervals(items):
    """Collapses a list of intervals into a list of non-overlapping intervals"""
    

    result = []
    start = items[0]
    end = items[0]
    for i in items:
        if i == end + 1:
            end = i
        else:
            if start == end:
                result.append(str(start))
            else:
                result.append(f'{start}-{end}')
            start = i
            end = i
    if start == end:
        result.append(str(start))
    else:
        result.append(f'{start}-{end}')
    return ','.join(result)

