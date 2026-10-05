from typing import Callable

# ==========================================
# Higher-Order Magic Functions
# ==========================================

def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """
    Returns a new function that casts both spells simultaneously
    and returns a tuple of their results.
    """
    def combined(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """
    Returns a new function that casts the original spell but
    multiplies the power level before casting.
    """
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """
    Returns a new function that evaluates a condition before casting.
    If the condition is True, it casts the spell. Otherwise, it fizzles.
    """
    def conditionally_cast(target: str, power: int) -> str:
        # Evaluate the condition using the same target and power
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    
    return conditionally_cast


def spell_sequence(spells: list[Callable]) -> Callable:
    """
    Returns a new function that iterates over a list of spells,
    casting them all in order with the same arguments.
    """
    def sequenced(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    
    return sequenced


# ==========================================
# Demonstration / Testing Block
# ==========================================
if __name__ == "__main__":
    
    # 1. Define some base spells that follow the contract
    def fireball(target: str, power: int) -> str:
        return f"Fireball hits {target} for {power} damage"

    def heal(target: str, power: int) -> str:
        return f"Heal restores {target} for {power} HP"

    def shield(target: str, power: int) -> str:
        return f"Shield protects {target} blocking {power} damage"


    # --- Test: spell_combiner ---
    print("Testing spell combiner...")
    # Combines fireball and heal into a single callable
    combat_medic_spell = spell_combiner(fireball, heal)
    res1, res2 = combat_medic_spell("Dragon", 50)
    print(f"Combined spell result: {res1}, {res2}\n")


    # --- Test: power_amplifier ---
    print("Testing power amplifier...")
    # Creates a new spell that is 3x as powerful as the base fireball
    mega_fireball = power_amplifier(fireball, 3)
    print(f"Original: {fireball('Goblin', 10)}")
    print(f"Amplified: {mega_fireball('Goblin', 10)}\n")


    # --- Test: conditional_caster ---
    print("Testing conditional caster...")
    # Define a condition that requires at least 20 power to cast
    def requires_high_focus(target: str, power: int) -> bool:
        return power >= 20

    unstable_fireball = conditional_caster(requires_high_focus, fireball)
    print(f"Low power (10): {unstable_fireball('Orc', 10)}")
    print(f"High power (25): {unstable_fireball('Orc', 25)}\n")


    # --- Test: spell_sequence ---
    print("Testing spell sequence...")
    # Creates a macro-spell that casts shield, heal, and fireball in order
    defend_and_counter = spell_sequence([shield, heal, fireball])
    sequence_results = defend_and_counter("Hero", 30)
    for result in sequence_results:
        print(f"- {result}")
