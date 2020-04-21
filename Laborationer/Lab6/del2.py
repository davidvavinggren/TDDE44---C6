class TodoApp (object):

    def __init__(self):
        pass
        #kommando = kommando

    def show_commands():
        pass
    def new_task():
        pass
    def show_tasks():
        pass
    def mark_done():
        pass
    def main ():
        todo_app = TodoApp()
        while True:
            kommando = input("Ange kommando (q=avsluta ?=hjälp) ")
            if kommando == "q":
                break
            elif kommando == "?":
                todo_app.show_commands()

    main()

#class TaskList (object):
    #def

#class Task(object):
    #def

todo_app = TodoApp()
