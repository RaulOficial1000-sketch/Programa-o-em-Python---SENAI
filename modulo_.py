import statistics as st

def calcular_notas(lista_notas):




    media = st.mean(lista_notas)
    mediana = st.median(lista_notas)
    desvio = st.stdev(lista_notas)


    print(f'Média: {media}')
    print(f'Mediana: {mediana}')
    print(f'Desvio padrão: {desvio}')
