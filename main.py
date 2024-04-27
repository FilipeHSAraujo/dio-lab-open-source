import random
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def total_damage(damage, defence_points, toughness, is_critical):
    total_damage = damage * (1 - min(20, max(defence_points / 5, defence_points - (damage / (2 * toughness + 6)))) / 25)
    if is_critical:
        total_damage *= 1.5
    return total_damage

def main():
    while True:
        clear_console()
        print("=== Simulador de Dano do Minecraft ===")
        print("1. Calcular Dano")
        print("2. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            damage = float(input("Digite o dano de sua arma: "))
            defence_points = float(input("Digite o total de armadura do inimigo: "))
            toughness = float(input("Digite o nível de resistência da armadura do inimigo: "))
            hp = float(input("Digite o HP do inimigo: "))

            while hp > 0:
                is_critical = random.random() <= 0.25
                armor = total_damage(damage, defence_points, toughness, is_critical)

                
                print("=== Resultado ===")
                if is_critical:
                    print("Ataque crítico! Inimigo sofreu", round(armor, 1), "de dano")
                else:
                    print("Inimigo sofreu", round(armor, 1), "de dano")

                hp -= armor  # Reduz a vida do inimigo pelo dano aplicado
                hp = max(0, hp)  # Se a vida do inimigo for negativa após o dano, ajusta para zero

                input("Pressione Enter para continuar...")
        elif choice == '2':
            clear_console()
            print("Obrigado por usar o simulador! Até mais!")
            break
        else:
            input("Opção inválida! Pressione Enter para continuar...")

if __name__ == "__main__":
    main()
