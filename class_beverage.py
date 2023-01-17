from random import randint

user_list = []

class Beverage:
    def __init__(self, username : str) -> None:
        self.bev_list = ['water', 'wine', 'coffee', 'milk', 'bubble tea', 'tea', 'coca-cola', 'iced coffee', 'coconut juice']
        # generates a list of beverages
        self.user_dict = dict(user = username, 
                              bev_1 = self.bev_list[randint(0, len(self.bev_list) - 1)],
                              bev_2 = self.bev_list[randint(0, len(self.bev_list) - 1)],
                              bev_3 = self.bev_list[randint(0, len(self.bev_list) - 1)],
                              bev_4 = self.bev_list[randint(0, len(self.bev_list) - 1)])  
                              # generates the user's random beverages
        user_list.append(list(self.user_dict.values())) # appends the user's beverages as list
    
    def get_bev(self, a_enabled : bool, b_enabled : bool) -> str:
        """Returns the type of beverage preselected for the user"""
        if a_enabled: 
            bev = self.user_dict["bev_1"]
        elif a_enabled and not b_enabled:
            bev = self.user_dict["bev_2"]
        elif not a_enabled and b_enabled:
            bev = self.user_dict["bev_3"]
        else:
            bev = self.user_dict["bev_4"]  
        return bev
    
    def get_state(self, temp : int) -> str:
        """Takes as argument the temperature and it returns the state of the beverage"""
        if temp == 0:
            state = 'frozen'
        elif temp <= 15:
            state = 'cold'    
        elif temp <=41:
            state = 'warm' 
        elif temp <= 99:
            state = 'hot'
        else:
            state = 'boiling'  
        #  It compares the value the user chose and then it assigns a string to state variable
        return state
    
    def user_del(self, username : str)->None:
        """Deletes the user from the database"""
        for index in range(len(user_list)):
            if username in user_list[index]:
                user_list.remove(user_list[index])
        

