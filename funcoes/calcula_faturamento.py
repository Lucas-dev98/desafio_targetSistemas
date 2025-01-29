import json

def calcular_faturamento_diario():
    dados = '''[
        {"dia": 1, "faturamento": 1000.00},
        {"dia": 2, "faturamento": 1500.00},
        {"dia": 3, "faturamento": 0.00},
        {"dia": 4, "faturamento": 2000.00}
        # Adicione os demais dias
    ]'''

    faturamento_diario = json.loads(dados)
    faturamentos = [dia["faturamento"] for dia in faturamento_diario if dia["faturamento"] > 0]
    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)
    media_mensal = sum(faturamentos) / len(faturamentos)
    dias_acima_media = sum(1 for faturamento in faturamentos if faturamento > media_mensal)

    print(f"Menor faturamento: R$ {menor_faturamento}")
    print(f"Maior faturamento: R$ {maior_faturamento}")
    print(f"Dias com faturamento acima da média: {dias_acima_media}")
