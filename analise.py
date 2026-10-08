import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

# 1. Carregar os dados
print("--- LENDO OS ARQUIVOS CSV ---")
df1 = pd.read_csv('query_01.csv')
df2 = pd.read_csv('query_02.csv')

df1.columns = [col.upper() for col in df1.columns]
df2.columns = [col.upper() for col in df2.columns]

# 2. Estatísticas Descritivas
print("\n=== ESTATÍSTICAS SALARIAIS GERAIS (QUERY 1) ===")
media_salario = df1['SALARY'].mean()
mediana_salario = df1['SALARY'].median()
min_salario = df1['SALARY'].min()
max_salario = df1['SALARY'].max()

print(f"Média Salarial:   ${media_salario:.2f}")
print(f"Mediana Salarial: ${mediana_salario:.2f}")
print(f"Salário Mínimo:   ${min_salario:.2f}")
print(f"Salário Máximo:   ${max_salario:.2f}")

# 3. Resumo por Departamento
print("\n=== RESUMO POR DEPARTAMENTO ===")
dept_summary = df1.groupby('DEPARTMENT_NAME')['SALARY'].agg(['mean', 'median', 'count', 'min', 'max'])
dept_summary.columns = ['Média', 'Mediana', 'Qtd_Funcionários', 'Mínimo', 'Máximo']
print(dept_summary.round(2))

# 4. Resumo por Região
print("\n=== RESUMO POR REGIÃO ===")
region_summary = df2.groupby('REGION_NAME')['SALARY'].agg(['mean', 'median', 'count'])
region_summary.columns = ['Média', 'Mediana', 'Qtd_Funcionários']
print(region_summary.round(2))

# 5. Geração dos Gráficos
plt.figure(figsize=(12, 6))
sns.boxplot(x='DEPARTMENT_NAME', y='SALARY', data=df1, hue='DEPARTMENT_NAME', legend=False, palette='Set2')
plt.xticks(rotation=45, ha='right')
plt.title('Distribuição e Variação Salarial por Departamento', fontsize=14, fontweight='bold')
plt.xlabel('Departamento')
plt.ylabel('Salário ($)')
plt.tight_layout()
plt.savefig('boxplot_salarios_dept.png')
print("\n[✓] Gráfico 'boxplot_salarios_dept.png' gerado com sucesso!")

plt.figure(figsize=(9, 5))
sns.barplot(x='REGION_NAME', y='SALARY', data=df2, hue='REGION_NAME', legend=False, errorbar=None, palette='Blues_d')
plt.title('Média Salarial por Região Geográfica', fontsize=14, fontweight='bold')
plt.xlabel('Região')
plt.ylabel('Média Salarial ($)')
plt.tight_layout()
plt.savefig('media_salario_regiao.png')
print("[✓] Gráfico 'media_salario_regiao.png' gerado com sucesso!")

plt.show()