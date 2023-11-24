from src.tools.general_functions import GenFunc


class Menu:
    """
    a class used to create menu

    atributes:
        name(str): name of the menu

        label(str): question to be asked or text to be displayed

        option_lst(list): a nested list contianing lists of options and
            functions in formate-
            [[opt1_no(str), opt1_text(str), opt1_func(fuc), "exit"]....]
            last option is optional to make the option kill the menu ones the
            function given to the option is completed option function can also
            be replaced with "exit" to make the function just to kill the menu

        inv_opt_text(str): text to show when invalid option enterd

        running(bool): running status of menu

    """
    def __init__(self,
                 name,
                 label,
                 option_lst,inv_opt_text = "please enter valid input..."
                ):
        self.name = name
        self.label = label
        self.option_lst = option_lst
        self.inv_opt_text = inv_opt_text
        self.running = False

    def get_response(self):
        """
        this function shows the menu items and then get response from user

        returns:
            resp(str): response given by user

        """
        print(self.name)
        print(self.label)

        for arg in self.option_lst: # printing options
            print(arg[0]+")", arg[1])

        resp = input("enter option number:") # getting response from user
        print() # for space
        return resp

    def exicute_response(self, resp):
        """
        this function exicutes the function connected with the response

        arg:
            resp(str): this is the response given by user usually given by
            the get_response function

        """
        for arg in self.option_lst:
            if resp == arg[0]: # matching resp to the option
                if len(arg) == 4: # checking if it has both function and exit
                    arg[2]()
                    self.kill()
                else: # has eaither function ot exit
                    if arg[-1] == "exit": # checking if only exit
                        self.kill()
                    else: # only function
                        arg[2]()
                break
        else: # if no option matched
            GenFunc.clear_terminal()
            print(self.inv_opt_text)

    def show(self):
        """
        this method shows the menu in the screen

        """
        GenFunc.clear_terminal()
        self.running = True
        while self.running:
            resp = self.get_response()
            self.exicute_response(resp)

    def kill(self):
        """
        this method stops the menu loop

        """
        self.running = False
        GenFunc.clear_terminal()

    def add_option(self, new_option_lst):
        """
        this method used to update option list

        arg:
            new_opt_lis(list): list of new option  in formate
            [opt_no(str), opt_text(str), opt_func(fuc), "exit"]
            last element optional

        """
        self.option_lst = new_option_lst

    def change_label(self, new_label_text):
        """
        this function changes the label text

        arg:
            new_label_text(str): new label text

        """
        self.label = new_label_text
