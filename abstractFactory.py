class Door:
    def getDescription(self):
        pass

class WoodenDoor(Door):
    def getDescription(self):
        print('I am a wooden door')

class IronDoor(Door):
    def getDescription(self):
        print('I am an iron door')

class DoorFittingExpert:
    def getDescription(self):
        pass

class Welder(DoorFittingExpert):
    def getDescription(self):
        print('I can only fit iron doors')

class Carpenter(DoorFittingExpert):
    def getDescription(self):
        print('I can only fit wooden doors')

class DoorFactory:
    def makeDoor(self):
        pass

    def makeFittingExpert(self):
        pass

class WoodenDoorFactory(DoorFactory):
    def makeDoor(self):
        return WoodenDoor()

    def makeFittingExpert(self):
        return Carpenter()

class IronDoorFactory(DoorFactory):
    def makeDoor(self):
        return IronDoor()

    def makeFittingExpert(self):
        return Welder()

if __name__ == '__main__':
    # Creating instances of concrete factories
    woodenFactory = WoodenDoorFactory()
    ironFactory = IronDoorFactory()

    # Creating wooden door and fitting expert
    wooden_door = woodenFactory.makeDoor()
    wooden_expert = woodenFactory.makeFittingExpert()

    # Displaying descriptions
    wooden_door.getDescription()
    wooden_expert.getDescription()

    # Creating iron door and fitting expert
    iron_door = ironFactory.makeDoor()
    iron_expert = ironFactory.makeFittingExpert()

    # Displaying descriptions
    iron_door.getDescription()
    iron_expert.getDescription()
