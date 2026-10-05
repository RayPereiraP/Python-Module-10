def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """
    Ordena os artefatos mágicos pelo nível de 'power' em ordem decrescente.
    """
    return sorted(artifacts, key=lambda artifact: artifact['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """
    Filtra a lista de magos, retornando apenas aqueles com poder >= min_power.
    """
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """
    Transforma os nomes dos feitiços adicionando "* " no início e " *" no final.
    """
    return list(map(lambda spell: f"* {spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    """
    Calcula as estatísticas de poder dos magos (máximo, mínimo e média).
    """
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}

    # Encontra o mago mais forte e o mais fraco usando lambda como chave (key)
    max_power = max(mages, key=lambda mage: mage['power'])['power']
    min_power = min(mages, key=lambda mage: mage['power'])['power']
    
    # Extrai todos os poderes usando map + lambda para calcular a média
    total_power = sum(map(lambda mage: mage['power'], mages))
    avg_power = round(total_power / len(mages), 2)

    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg_power
    }

# ==========================================
# Bloco de testes (Opcional, para você rodar e verificar)
# ==========================================
if __name__ == "__main__":
    test_artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'Orb'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'Staff'},
        {'name': 'Wooden Wand', 'power': 30, 'type': 'Wand'}
    ]
    
    test_mages = [
        {'name': 'Gandalf', 'power': 95, 'element': 'Light'},
        {'name': 'Merlin', 'power': 88, 'element': 'Arcane'},
        {'name': 'Apprentice', 'power': 15, 'element': 'Water'}
    ]
    
    test_spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(test_artifacts)
    for a in sorted_artifacts:
        print(f"{a['name']} ({a['power']} power)")

    print("\nTesting power filter (min 80)...")
    powerful_mages = power_filter(test_mages, 80)
    print([m['name'] for m in powerful_mages])

    print("\nTesting spell transformer...")
    print(" ".join(spell_transformer(test_spells)))

    print("\nTesting mage stats...")
    print(mage_stats(test_mages))