import json

class Player:
    def __init__(self, player_name: str, player_team: str, player_country: str, player_goals: int, player_assists: int, player_games: int):
        self.player_name = player_name
        self.player_team = player_team
        self.player_country = player_country #Seting each player parameter/value
        self.player_goals = player_goals
        self.player_assists = player_assists
        self.player_games = player_games
        self.player_score = self.player_goals + self.player_assists

    def __str__(self) -> str:
        return f"{self.player_name:20} {self.player_team:4} {self.player_goals:2} + {self.player_assists:2} = {self.player_score:3}" #Return string
    
class PlayerStatistics:
    def __init__(self):
        self.__players_statistic = [] #Here we save each player as object. Encapsulation
  
    def open_file(self, file: str): #Func to read and return the json file
        
        with open(file, "r") as my_file:
            data = my_file.read()

        players = json.loads(data)

        return players
    
    def add_players_to_list(self, file): #Func to set each player as object and add it to the players_statistic list
        players = file

        for player in players: #Iterating over all players

            player_name = player["name"] 
            player_team = player["team"]
            player_country = player["nationality"]
            player_goals = player["goals"]
            player_assists = player["assists"]
            player_games = player["games"]
            
            each_player = Player(player_name, player_team, player_country, player_goals, player_assists, player_games) #Create obj with this values
            self.__players_statistic.append(each_player) # add it to the list
    
    def find_player(self, player_name: str):
        player = list(filter(lambda x: x.player_name == player_name, self.__players_statistic)) #Search for a specific player if its in the list

        return player
    
    def find_all_teams(self):
        teams_total = sorted(list(set([line.player_team for line in self.__players_statistic]))) #Find all teams use set to eliminate repetition

        return teams_total
    
    def find_all_countryes(self):
        countries = sorted(list(set([line.player_country for line in self.__players_statistic]))) #Same as find_all_teams
        
        return countries
    
    def players_in_team(self, team: str):
        players_in_team = [player for player in self.__players_statistic if player.player_team == team] #Find all players in given team
        sorted_players = sorted(players_in_team, key=lambda x: x.player_score, reverse=True) #Sort them to their score top to bottom

        return sorted_players
    
    def players_in_country(self, country: str):
        players_in_country = [player for player in self.__players_statistic if player.player_country == country] #Same as players_in_team
        sorted_players = sorted(players_in_country, key=lambda x: x.player_score, reverse=True)

        return sorted_players
    
    def check_players_score(self): #Find players score, if score == score, who has more goals comes first
        def score_helper(player):
            return [player.player_score, player.player_goals]
        return sorted(self.__players_statistic, key=score_helper, reverse=True)
    
    def check_players_goals(self): #Find all players goals, if goals == goals, who has played lower num of games comes first
        def goals_helper(player):
            return [player.player_goals, (player.player_games)* -1]
        return sorted(self.__players_statistic, key=goals_helper, reverse=True) 
    
    def print_info(self, data: list): #Func to print players
        
        for player in data:
            print(player)
        
class StatisticApplication:
    def __init__(self):
         self.player_statistic = PlayerStatistics()

    def read_file(self): #Read file
        file_name = input("file name: ")
            
        json_file = self.player_statistic.open_file(file_name)
        self.player_statistic.add_players_to_list(json_file)
        total_players = len(json_file)
        print(f"read the data of {total_players} players\n")

    def menu(self): # help menu information
        print("commands:")
        print('0 quit\n'
            '1 search for player\n'
            '2 teams\n'
            '3 countries\n'
            '4 players in team\n'
            '5 players from country\n'
            '6 most points\n'
            '7 most goals')
    
    def execute(self): #execution of program
        
        while True:
            command = input("\ncommand: ")
            
            if command == '0':
                break

            elif command == '1':
                name = input("name: ")
                player = self.player_statistic.find_player(name)
                self.player_statistic.print_info(player)
                
            elif command == '2':
                teams = self.player_statistic.find_all_teams()
                self.player_statistic.print_info(teams)

            elif command == '3':
                countryes = self.player_statistic.find_all_countryes()
                self.player_statistic.print_info(countryes)
            
            elif command == '4':
                team = input("team: ")
                players_in_team = self.player_statistic.players_in_team(team)
                self.player_statistic.print_info(players_in_team)
            
            elif command == '5':
                country = input("country: ")
                players_in_country = self.player_statistic.players_in_country(country)
                self.player_statistic.print_info(players_in_country)

            elif command == '6':
                players_total = int(input("how many: "))
                score = self.player_statistic.check_players_score()

                for player in score[0:players_total]:
                    print(player)
            
            elif command == '7':
                players = int(input("how many: "))
                goals = self.player_statistic.check_players_goals()

                for player in goals[0:players]:
                    print(player)
            
application = StatisticApplication()
application.read_file()
application.menu()
application.execute()






