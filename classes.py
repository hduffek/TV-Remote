class Television:
    '''
    Class to represent Television objects
    '''
    MIN_CHANNEL = 0  # Minimum TV channel
    MAX_CHANNEL = 3  # Maximum TV channel

    MIN_VOLUME = 0  # Minimum TV volume
    MAX_VOLUME = 2  # Maximum TV volume

    def __init__(self) -> None:
        '''
        Method to set default state of the TV
        '''
        self.__channel: int = Television.MIN_CHANNEL
        self.__volume: int = Television.MIN_VOLUME
        self.__status: str = "False"

    def power(self) -> None:
        '''
        Method to turn TV On/Off
        :return: True if TV is Off, False if TV is On
        '''
        if self.__status == "False":
            self.__status: str = "True"
        else:
            self.__status: str = "False"

    def channel_up(self) -> None:
        '''
        Method to turn TV Channel Up
        :return: Sets TV Channel to MIN if current channel is at MAX, otherwise adds 1 to Channel
        '''
        if self.__status == "True":
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel: int = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        '''
        Method to turn TV Channel Down
        :return: Sets TV Channel to MAX if current channel is at MIN, otherwise subtracts 1 from Channel
        '''
        if self.__status == "True":
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel: int = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        '''
        Method to turn TV Volume Up
        :return: Sets TV Volume to MAX if it already is MAX, otherwise adds 1 to Volume
        '''
        if self.__status == "True":
            if self.__volume == Television.MAX_VOLUME:
                pass
            else:
                self.__volume += 1

    def volume_down(self) -> None:
        '''
        Method to Turn TV Volume Down
        :return: Sets TV Volume to MIN if it already is MIN, otherwise subtracts 1 from Volume
        '''
        if self.__status == "True":
            if self.__volume == Television.MIN_VOLUME:
                pass
            else:
                self.__volume -= 1

    def __str__(self):
        '''
        Sting Method that reports TV Status after each Television class call
        :return: Statement on TV Status (On/Off), current Channel, and current Volume
        '''
        return f'TV Status: Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
