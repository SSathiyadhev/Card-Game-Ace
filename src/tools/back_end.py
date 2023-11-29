import pickle


class BackEnd:
    """
    this class contains methods to access back end binary files

    """
    @staticmethod
    def add_data(data, file_path):
        """
        this method appends the given data to given file creats new file if 
        the given file is not found

        arg:
            data(any obj): the data which should be appanded in the file
                if multiple data pass as list

            file_path(str): the file in which data should be entred

        """
        try:
            file = open(file_path, "ab")
        except FileNotFoundError:
            file = open(file_path, "wb")

        if type(data) is list:

            for dat in data:
                pickle.dump(dat, file)

        else:
            pickle.dump(data, file)

        file.close()

    @staticmethod
    def get_all_data(file_path):
        """
        this method returns all the data in the file

        arg:
            file_path(str): path of file to read from

        returns:
            [list]: list containing data retrived from given file
                if unable to do then returns a string saying so

        """
        data_set = []
        try:
            file = open(file_path, "rb")

            while True:
                try:
                    data = pickle.load(file)
                    data_set.append(data)
                except EOFError:
                    file.close()
                    break

        except FileNotFoundError:
            return []

        return data_set

    @staticmethod
    def edit_data(field_search, search_data, field_change,
                  change_data,  file_path):
        """
        this function used to replaces old data with new data in file 
        in given path

        """
        data = BackEnd.get_all_data(file_path)
        found = False

        for dat in data:
            obj_attr_dict = vars(dat)
            for attr in obj_attr_dict:
                if attr == field_search and obj_attr_dict[attr] == search_data:
                    obj_attr_dict[field_change] = change_data
                    BackEnd.remove_all_data(file_path)
                    BackEnd.add_data(data, file_path)
                    found = True
            if found:
                break
        else:
            print("no data found matching your search")

    @staticmethod
    def remove_data(data, file_path):
        """
        this method removes given data

        arg:
            data(any obj): the data to be deleted

            file_path(str): the file in which data should be deleted
        """
        data_lst = BackEnd.get_all_data(file_path)

        for dat in list(data_lst): # itrating through copy of list
            print(vars(dat))
            print(vars(data))
            if dat == data:
                data_lst.remove(dat)
                break
        BackEnd.remove_all_data(file_path)
        BackEnd.add_data(data_lst, file_path)

    @staticmethod
    def remove_all_data(file_path):
        """
        remove all data from file

        arg:
            file_path(str): the file in which data should be deleted

        """
        file = open(file_path, "wb")
        file.close()
