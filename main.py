from League import League

league = League.from_json("../практика/Bundesliga.json")

print(league[0])  
print(league["FC Bayern München"])

for team in league:
    print(team)

print("\nТаблица лиги:")
for i, team in enumerate(league.get_standings(), 1):
    print(f"{i}. {team.name} — {team.points} очков, разница: {team.goals_scored - team.goals_conceded}")

league.play_match("RB Leipzig", "VfB Stuttgart", 2, 1)

league.to_json("../практика/Bundesliga_updated.json")
