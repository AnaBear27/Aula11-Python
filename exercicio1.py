notas_alunos = {
    'João': [8.5, 7.0, 9.2],
    'Maria': [9.0, 8.5, 7.5],
    'Pedro': [7.8, 6.5, 8.0]
}

medias_alunos = {}

for aluno, notas in notas_alunos.items():
    media = sum(notas) / len(notas)
    medias_alunos[aluno] = media

for aluno, media in medias_alunos.items():
    print(f"Aluno: {aluno} \n Média: {media:.2f}")