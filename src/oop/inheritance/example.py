from abc import ABC, abstractmethod


# Multiple inheritance

class Action(ABC):
    def __init__(self,item):
        self._action_item = item

    @abstractmethod
    def take_action(self):
        print("Parent")
        pass

class ItemAction(Action,ABC):
    def __init__(self,item):
        super().__init__(item)
    @property
    def action(self):
        return self._action_item
    def take_action(self):
        print(f"Action is {self.action}")

class WearAction(ItemAction):
    def __init__(self):
        super().__init__("wear")

class EarAction(ItemAction):
    def __init__(self):
        super().__init__("ear")

class EyeAction(ItemAction):
    def __init__(self):
        super().__init__("eye")

if __name__ == '__main__':
    actions = [WearAction(), EyeAction(), EarAction()]
    for act in actions:
        act.take_action()