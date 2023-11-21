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

            file_path(str): the file in which data should be entred

        """
        try:
            file = open(file_path, "ab")
        except FileNotFoundError:
            file = open(file_path, "wb")

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
            return "file not found"

        return data_set
