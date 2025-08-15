from abc import ABC, abstractmethod


class WorkBreakable(ABC):

    @abstractmethod
    def take_break(self):
        pass


class Workable(ABC):

    @abstractmethod
    def work(self):
        pass


class Manageable(ABC):

    @abstractmethod
    def manage(self):
        pass


class HumanWorker(WorkBreakable, Workable):

    def work(self):
        print('Human is working')

    def take_break(self):
        print('Human is taking break')


class RobotWorker(Workable):

    def work(self):
        print('Robot is working')


class ManagerWorker(Manageable):

    def manage(self):
        print('Manager is Managing')


class WorkProgressChecker:

    def check_work(self, worker: Workable):
        return worker.work()


human_worker = HumanWorker()
robot_worker = RobotWorker()
manager_worker = ManagerWorker()


WorkProgressChecker().check_work(human_worker)
WorkProgressChecker().check_work(robot_worker)
# This line will correctly fail, proving your design is robust!
WorkProgressChecker().check_work(manager_worker)
# AttributeError: 'ManagerWorker' object has no attribute 'work'
