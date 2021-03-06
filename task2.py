# Implement 2 classes, the first one is the Boss and the second one is the Worker.
#
# Worker has a property 'boss', and its value must be an instance of Boss.
#
# You can reassign this value, but you should check whether the new value is Boss.
# Each Boss has a list of his own workers. You should implement a method that allows you to add workers to a Boss.
# You're not allowed to add instances of Boss class to workers list directly via access to attribute,
# use getters and setters instead!
# id_ - is just a random unique integer

class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_

        self.name = name

        self.company = company

        self.__workers = []

    def add_new_worker(self, worker: 'Worker'):
        if isinstance(worker, Worker):
            self.__workers.append(worker)
        else:
            raise ValueError('Value must be an instance of Worker')


class Worker:

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, value):
        if isinstance(value, Boss):
            self._boss = value
        else:
            raise ValueError("Value must be an instance of Boss")

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_

        self.name = name

        self.company = company

        self._boss = boss
