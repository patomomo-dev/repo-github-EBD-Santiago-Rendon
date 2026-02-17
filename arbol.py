import hashlib

def hash_data(data):
    """Genera el hash SHA-256 de un string"""
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def build_merkle_tree(leaves):
    """
    Construye el árbol de Merkle y devuelve todos los niveles.
    leaves: lista de strings (datos originales)
    """
    # Nivel 0: hashes de las hojas
    current_level = [hash_data(leaf) for leaf in leaves]
    tree = [current_level]

    # Construcción hacia arriba hasta llegar a la raíz
    while len(current_level) > 1:
        next_level = []

        # Si hay número impar de nodos, duplicar el último
        if len(current_level) % 2 != 0:
            current_level.append(current_level[-1])

        # Combinar pares
        for i in range(0, len(current_level), 2):
            combined = current_level[i] + current_level[i + 1]
            parent_hash = hash_data(combined)
            next_level.append(parent_hash)

        tree.append(next_level)
        current_level = next_level

    return tree

def print_merkle_tree(tree):
    """Imprime el árbol por niveles"""
    for level_index, level in enumerate(tree):
        print(f"Nivel {level_index}:")
        for node in level:
            print(f"  {node}")
        print()

# ---------------------------
# Ejemplo de uso
# ---------------------------

data_blocks = ["hola", "Hola", "chao", "Chao"]

merkle_tree = build_merkle_tree(data_blocks)

print("Árbol de Merkle:\n")
print_merkle_tree(merkle_tree)

print("Raíz de Merkle:")
print(merkle_tree[-1][0])

