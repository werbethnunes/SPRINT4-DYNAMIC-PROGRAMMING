import random
from functools import lru_cache

dias = 30
estoque_inicial = 20
estoque_max = 100
pedido_max = 40
custo_pedido = 2
custo_estoque = 1
custo_falta = 5

insumos = ["Luva", "Seringa", "Reagente", "Mascara", "Alcool"]

random.seed(12)

# gera demanda diaria para cada insumo
demanda_insumos = {item: [random.randint(1, 12) for _ in range(dias)] for item in insumos}

def custo_dia(estoque, pedido, demanda_dia):
    disponivel = estoque + pedido
    falta = max(0, demanda_dia - disponivel)
    usado = min(disponivel, demanda_dia)
    fim = disponivel - usado
    custo = custo_pedido * pedido + custo_estoque * fim + custo_falta * falta
    return custo, fim

def acoes_possiveis(estoque):
    limite = min(pedido_max, estoque_max - estoque)
    return range(0, limite + 1)

# recursiva
def dp_recursiva(dia, estoque, demanda):
    if dia == dias:
        return 0
    melhor = float("inf")
    for pedido in acoes_possiveis(estoque):
        c, prox = custo_dia(estoque, pedido, demanda[dia])
        val = c + dp_recursiva(dia + 1, prox, demanda)
        if val < melhor:
            melhor = val
    return melhor

# memo
@lru_cache(maxsize=None)
def dp_memo(dia, estoque, idx_insumo):
    if dia == dias:
        return 0
    nome = insumos[idx_insumo]
    demanda = demanda_insumos[nome]
    melhor = float("inf")
    for pedido in acoes_possiveis(estoque):
        c, prox = custo_dia(estoque, pedido, demanda[dia])
        val = c + dp_memo(dia + 1, prox, idx_insumo)
        if val < melhor:
            melhor = val
    return melhor

def politica_memo(estoque_inicial, idx_insumo):
    nome = insumos[idx_insumo]
    demanda = demanda_insumos[nome]
    politica = []
    e = estoque_inicial
    for d in range(dias):
        melhor = float("inf")
        melhor_p = 0
        for p in acoes_possiveis(e):
            c, prox = custo_dia(e, p, demanda[d])
            val = c + dp_memo(d + 1, prox, idx_insumo)
            if val < melhor:
                melhor = val
                melhor_p = p
                prox_estoque = prox
        politica.append(melhor_p)
        e = prox_estoque
    return politica

# bottom-up
def dp_bottom_up(demanda):
    dp = [[0]*(estoque_max + 1) for _ in range(dias + 1)]
    for d in range(dias - 1, -1, -1):
        for e in range(estoque_max + 1):
            melhor = float("inf")
            for p in acoes_possiveis(e):
                c, prox = custo_dia(e, p, demanda[d])
                val = c + dp[d + 1][prox]
                if val < melhor:
                    melhor = val
            dp[d][e] = melhor
    return dp

def politica_bottom_up(dp, demanda):
    politica = []
    e = estoque_inicial
    for d in range(dias):
        alvo = dp[d][e]
        for p in acoes_possiveis(e):
            c, prox = custo_dia(e, p, demanda[d])
            val = c + dp[d + 1][prox]
            if abs(val - alvo) < 1e-9:
                politica.append(p)
                e = prox
                break
    return politica

# execucao
if __name__ == "__main__":
    print("Simulacao de reposicao de insumos\n")
    for nome in insumos:
        print(nome, ":", demanda_insumos[nome])

    print("\nResultados:\n")

    for idx, nome in enumerate(insumos):
        dem = demanda_insumos[nome]
        custo_memo = dp_memo(0, estoque_inicial, idx)
        dp_tab = dp_bottom_up(dem)
        custo_iter = dp_tab[0][estoque_inicial]
        poli_memo = politica_memo(estoque_inicial, idx)
        poli_iter = politica_bottom_up(dp_tab, dem)

        print(f"Insumo: {nome}")
        print("Custo total (memo):", round(custo_memo, 2))
        print("Custo total (iterativo):", round(custo_iter, 2))
        print("Politica (primeiros 10 dias, memo):", poli_memo[:10])
        print("Politica (primeiros 10 dias, iter):", poli_iter[:10])
        print("-----------------------------------")
