from class_beverage import Beverage

usr_bev = Beverage("dgonz348") # define your MRU username here


def get_temperature_desc(slider_value: int) -> str:
    """
    Returns the temperature description defined by the slider value.
    Assume the value is always an integer between 0 and 100 (inclusive).
    """
    # this block checks if the value of the slider is in the range 0-100, 
    # and prevents users to keep going until the input is an interger
    while slider_value != int or slider_value < 0 or slider_value > 100:
        try:
            temp_value = int(slider_value)
            if temp_value < 0 or temp_value > 100:
                print("Invalid input, try again")
                temp_value = input("Invalid entry, please use an interger from 0-100: ")
            else:
                break
        except ValueError:
            print("Invalid input, try again")
            temp_value = input("Please use an interger from 0-100: ") 
    
    return usr_bev.get_state(temp_value)
    


def get_switch_value(switch_name: str) -> bool:
    """
    Prompts the user for the state of the specified switch.
    Returns true if the specified switch is enabled and false otherwise.
    """
    is_switch_name = input(f"Is switch {switch_name} enabled?(y/n): ").lower()
    # sets the variable to the parameter's value 
    if is_switch_name != 'y' or is_switch_name != 'n':
        while is_switch_name != 'y' and is_switch_name != 'n':
            is_switch_name = input("Invalid entry, please use y or n: ").lower()
        # Checks for user's input to see if it complies with the program
    if is_switch_name == 'y':
        return True
    else:
        return False
    # It compares the value and depending on the string it sets switch_name to either True or False




def main() -> None:
    """
    Prompts the user for the state of switches A and B and
    the value of the numeric slider. Using the various provided
    function headers, duplicate the functionality of the
    abandoned replicator at https://mru-replicator.fly.dev.
    """
    
    switch_a = get_switch_value("A")
    # it sets the argument to what the user input and then calls in the function 
    # to then set the variable to what the function returned
    
    switch_b = get_switch_value("B")
    # it sets the argument to what the user input and then calls in the function 
    # to then set the variable to what the function returned

    slider_value = input("What's the value of the slider?(0-100): ")
    #set the variable to what the user input, the value is a integer
    

    print(f'result: {usr_bev.get_bev(switch_a, switch_b)}, {get_temperature_desc(slider_value)}')
    # calls in the functions "get_beverage_type" and "get_temperature_desc" using 
    # the values from the previous variables as arguments and then it prints the result  


main() # calls in main to execute program