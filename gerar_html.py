from jinja2 import Environment, FileSystemLoader

# Dados dos treinos
treinos = {
    "A": ["Supino Articulado","Voador/Peck Deck","Crucifixo","Desenvolvimento Articulado","Elevação Lateral","Tríceps Puley","Tríceps no Aparelho"],
    "B": ["Agachamento","Leg Press","Cadeira Extensora","Stiff","Panturrilha"],
    "C": ["Puxada Frontal","Remada Baixa","Rosca Direta","Rosca Martelo","Encolhimento"],
    "Bíceps":["Rosca scott","Rosca direta com W","Rosca inclinada com halteres", "Rosca martelo"]
}

env = Environment(loader=FileSystemLoader('templates'))

# index.html
index_template = env.get_template('index_template.html')
with open('index.html','w',encoding='utf-8') as f:
    f.write(index_template.render(treinos=treinos.keys()))

# treinos
treino_template = env.get_template('treino_template.html')
for treino_id, exercicios in treinos.items():
    with open(f'treino{treino_id}.html','w',encoding='utf-8') as f:
        f.write(treino_template.render(treino_id=treino_id, exercicios=exercicios))
