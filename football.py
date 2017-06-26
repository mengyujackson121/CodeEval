import sys

def get_list(each_country_and_team):
    team_set = set()
    for each_country in each_country_and_team:
        for team in each_country:
            team_set.add(int(team))
    every_team = sorted(team_set)
    return every_team

def get_list_value(every_team,each_country_and_team):
    final_result = []
    for each_team in every_team:
        team_something = []
        for i in range(len(each_country_and_team)):
            if str(each_team) in each_country_and_team[i]:
                team_something.append(str(i+1))
        final_result.append(str(each_team) + ':' +  ','.join(team_something))
    return final_result

def main():
    file = open(sys.argv[-1], 'r').readlines()
    for line in file:
        country = line.strip().split('| ')
        each_country_and_team = [team.strip().split(' ') for team in country]

        all_team = get_list(each_country_and_team)
        print '; '.join(get_list_value(all_team,each_country_and_team)) +';'


main()
