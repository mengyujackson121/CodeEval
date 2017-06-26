import sys
f = open(sys.argv[-1],'r').readlines()

def get_total_distance(home,friend_list):
    distance_list = []
    for friend in friend_list:
        distance = abs(home - friend)
        distance_list.append(distance)
    return sum(distance_list)

for line in f:
    a = line.strip().split(' ')
    friend_list = sorted(int(s) for s in a[1:])
    best_home = friend_list[len(friend_list)/2]
    print get_total_distance(best_home,friend_list)
    # home_list = range(min(friend_list)+1, max(friend_list)+1)
    # total_distance_list = []
    #
    # for home in home_list:
    #     total_distance_list.append(get_total_distance(home,friend_list))
    # print min(total_distance_list)