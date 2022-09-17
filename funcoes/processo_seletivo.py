import pandas as pd

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
    
    try:
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
    except IndexError:
        return ''

def calc_employee_dist(filepath):
    """Calculates the distribution of employees by time zone"""

    def convert(hora):
        """Converts a string in the format 'HH:MM' to integer in minutes"""
        hora = hora.split(':')
        minuto = int(hora[0])*60 + int(hora[1])
        return int(minuto/10)

    df = pd.read_csv(filepath)
    aux_df = df.copy()
    aux_df = aux_df.values.tolist()

    flow = []
    escala = [0] * 144
    for employ in aux_df:
        lista = list(map(convert, employ))
        flow.append(lista)
    for hour in flow:
        for c in range(hour[0],hour[1]):
            escala[c] += 1
        for c in range(hour[2],hour[3]):
            escala[c]+=1
    return escala