import pandas as pd

segundo_periodo= {'cursos' : ['ciência, Tecnologia e Sociedade','Álgebra Linear', 'Fenômenos Mecânicos', 'Raciocínio Computacional','Projeto Integrador I', 'Cálculo 2'  ],
                  'Créditos': [3, 4, 5, 4, 4, 5]}

df = pd.DataFrame(segundo_periodo)
print(df)