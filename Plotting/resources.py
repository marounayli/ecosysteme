def get_probe_country_map():
    probe_country_map = dict()
    with open("../log_active_probes.txt", 'r') as f:
        for line in f:
            segment = line.rstrip().split("-")
            probe_country_map[int(segment[0])] = segment[1]
    return probe_country_map


def get_countries():
    countries = set()
    with open("../log_active_probes.txt", 'r') as f:
        for line in f:
            segment = line.rstrip().split("-")
            countries.add(segment[1])
    return countries


def get_games_ips():
    GamesIPS = dict()
    with open("../log_creation_successes.txt", 'r') as f:
        for line in f:
            line = line.rstrip().split("##")
            (ip, game) = (line[0], line[1])
            GamesIPS[ip] = game
    return GamesIPS


print(get_games_ips()["103.10.125.1"])
