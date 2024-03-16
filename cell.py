class Cell:
    def __init__(self, cell_size, cell_close_image):
        self.__cell_size = cell_size
        self.__is_bombed = False
        self.__is_opened = False
        self.__is_mine = False
        self.__is_flagged = False
        self.__cel_image = cell_close_image
        self.__cel_close_image = cell_close_image

    def get_cell_image(self):
        if self.__is_opened:
            return self.__cel_image
        else:
            return self.__cel_close_image

    def set_cell_image(self, cell_image):
        self.__cel_image = cell_image

    def set_is_mine(self, is_mine):
        self.__is_mine = is_mine

    def set_is_bombed(self, is_bombed):
        self.__is_bombed = is_bombed

    def set_is_opened(self, is_opened):
        self.__is_opened = is_opened

    def get_is_opened(self):
        return self.__is_opened

    def get_is_fagged(self):
        return self.__is_flagged
