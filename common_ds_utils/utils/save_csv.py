import os
def create_dir(dir_path):
    """Generic method to check directory and create if doesn't exist

    Args:
        dir_path (str): directory
    """
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

def save_csv(data, dump_dir, file_name):
        """Function to save the csv files

        Args:
            data (pandas df): data
            dump_dir (str): directory to save files
            file_name (str): file name
        """
        try:
            create_dir(dump_dir)
            if ".csv" not in file_name:
                file_name = file_name + ".csv"
            path = dump_dir + file_name
            data.to_csv(path, index=False)
            print("Save csv complete ...")
        except Exception as e:
            print(str(e))
        return