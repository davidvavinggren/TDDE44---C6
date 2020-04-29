"""TDDE44, Labb 6, Del 2."""


class TodoApp (object):
    """Klassen TodoApp."""

    def __init__(self):
        """Initiera instansen med tillhörande instansvariabler."""
        self.commands = {"ny": self.new_task, "visa": self.show_tasks,
                         "klar": self.mark_done, "?": self.show_commands}
        self.task_list = TaskList()
        self.run()

    def run(self):
        """Kör enligt nedanstående anvisning."""
        # kör loopen alltid såvida inte if-satsen uppfylls
        while True:
            user_input = input("Ange kommando (q=avsluta ?=hjälp): ")
            # stäng ner om man skriver q
            if user_input == "q":
                break
            # pröva om ett kommando finns i kommandolistan
            try:
                self.commands[user_input]()
            # skriv ut om try misslyckas
            except KeyError:
                print("Inget kommando.")

    def show_commands(self):
        """Printa de olika kommandon som finns."""
        print("Kommandon: ny, visa, klar, ?")

    def new_task(self):
        """Gör ett nytt taskobjekt."""
        new_task = input("Beskriv uppgiften: ")
        confirmation = input("Du skrev {}, är det OK? [j/n]: ".format(new_task))
        if confirmation == "j":
            self.task_list.create_task(new_task)

    def show_tasks(self):
        """Visa de tasks som lagts till."""
        print(self.task_list)

    def mark_done(self):
        """Skriv ut de som finns och kör mark_done på den utpekade."""
        print(self.task_list)
        finished_task_id = input("Vilken uppgift ska markeras som klar? ")
        try:
            self.task_list.mark_done(int(finished_task_id))
        except ValueError:
            print("Icke giltigt index.")


class TaskList (object):
    """Klassen TaskList."""

    def __init__(self):
        """Initiera instansten med tillhörande instansvariabler."""
        self.task_list = {}
        self.task_counter = 0

    def create_task(self, new_task):
        """Lägg till i dictet och skapa ett task samt räkna upp antalet."""
        self.task_list[new_task] = Task(new_task, self.task_counter)
        self.task_counter += 1

    def mark_done(self, finished_task_id):
        """Gå igenom uppgifterna och kör mark_done på rätt."""
        # loopa genom uppgifterna för att hitta rätt
        for task in self.task_list.values():
            # hitta rätt uppgift och kör mark_done på den
            if task.task_id == finished_task_id:
                task.mark_done()
            else:
                print("Icke giltigt index.")

    def __str__(self):
        """Printa enligt taskobjektens __str__."""
        # skriv ut om listan är tom
        if self.task_list == {}:
            print("Listan är tom")
            return ""
        string = ""
        # loopa genom uppgiftobjekten och skriv ut deras prints
        for task in self.task_list.values():
            string += task.__str__()
        return string[:-1]


class Task(object):
    """Klassen Task."""

    def __init__(self, task_description, task_id):
        """Initiera taskklassen och skicka in namnet samt siffran."""
        self.task_id = task_id
        self.task_description = task_description
        self.done = False

    def mark_done(self):
        """Ändra instansvariabeln done till True."""
        self.done = True

    def __str__(self):
        """Printa enligt anvisning."""
        string = "{}. [{}] {} \n"
        if self.done:
            # skriv ut med kryss om uppgiften är klar annars utan
            return string.format(self.task_id, "X", self.task_description)
        return string.format(self.task_id, " ", self.task_description)

if __name__ == "__main__":
    """Huvudfunktion där man kör."""
    todo_app = TodoApp()
