class TodoApp (object):

    def __init__(self):
        self.commands = {"ny":self.new_task, "visa":self.show_tasks, "klar":self.mark_done,
                                                          "?":self.show_commands}
        self.task_list = TaskList()
        self.run()
        #kommando = kommando

    def run (self):
        while True:
            user_input = input("Ange kommando (q=avsluta ?=hjälp) ")
            if user_input == "q":
                break
            try:
                self.commands[user_input]()

            except KeyError:
                print("Inget kommando")

    def show_commands(self):
        print("Kommandon: ny, visa, klar, ?")

    def new_task(self):
        new_task = input("Beskriv uppgiften: ")
        self.task_list.create_task(new_task)

    def show_tasks(self):
        print ("Test show_tasks")
        self.task_list.__str__()

    def mark_done(self):
        self.task_list.mark_done()


class TaskList (object):

    def __init__(self):
        #self.task_counter = len(task_list)
        self.task_list = {}
        self.task_id = len(self.task_list)

    def create_task(self, new_task):
        #print("Test")
        self.task_list[new_task] = Task(new_task, self.task_id)

    def mark_done(self):
        self.__str__()
        finished_task_id = input("Vilken uppgift ska markeras som klar? ")
        for task in task_list.values():
            if task.task_id == finished_task_id:
                task.mark_done()

    def __str__(self):
        print("test str list")
        string = ""
        for task in self.task_list.values():
            string += task.__str__()
        return string

class Task(object):

    def __init__(self, task_description, task_id):
        self.task_id = task_id
        self.task_description = task_description
        self.done = False

    def mark_done(self):
        self.done = True

    def __str__(self):
        print("test str task")
        string = "{}. [{}] {} \n"
        if self.done == True:
            return string.format(self.task_id, "X", self.task_description)
        else:
            return string.format(self.task_id, " ", self.task_description)

if __name__ == "__main__":
    todo_app = TodoApp()
