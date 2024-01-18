class Singleton:
    __instance = None

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def __init__(self):
        if self.__class__.__instance is not None:
            raise Exception("This class is a singleton!")

try:
    s1 = Singleton.get_instance()
    print(s1)

    # Attempt to create a second instance
    s2 = Singleton()
    print(s2)  # This line should not be reached

except Exception as e:
    print(f"Error: {e}")