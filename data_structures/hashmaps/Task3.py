from Task2 import LinearProbing
from Task1_A import get_hashcode, div_compression


class StorePasswords(LinearProbing):
    def __init__(self, capacity):
        self.password_table = LinearProbing(capacity)
        self.all_users = {}

    def store_password(self, username, password_tuple):
        """
        Arguments:
        username: String e.g. "Ali"
        password_tuple: Tuple e.g. ("honeyword1", "true_password", "honeyword2", 1)
                       where last index will indicate the index of the true password.

        Returns: Nothing
        """
        pass

    def find_password(self, password):
        """
        Arguments:
        password: String

        Returns: Tuple
        If the password is not found: (“login_failed”)
        If the password is the true password: (username, “successful_login”)
        If the password is a honeyword: (username, “hack_alert”)
        """
        pass

    def update_password(self, old_password, new_password):
        """
        Arguments:
        old_password: String
        new_password: String

        Returns: Tuple
        If the password is not found: (“login_failed”)
        If the password is the true password: (username, “successful_password_update”)
        If the password is a honeyword: (username, “hack_alert”)
        """
        pass
