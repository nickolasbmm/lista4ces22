from tkinter import *
from abc import *
import ast

class ICommand(metaclass=ABCMeta):
    """The command interface, which all commands will implement"""

    @abstractstaticmethod
    def execute():
        """The required execute method which all command obejcts will use"""


class AddFundsCommand(ICommand):
    """A Command object, which implemets the ICommand interface"""

    def __init__(self, user):
        self.user = user

    def execute(self,args):
        deposit = args[0]
        return self.user.add_funds(deposit)


class ShowHistoryCommand(ICommand):
    """A Command object, which implemets the ICommand interface"""

    def __init__(self, user):
        self.user = user

    def execute(self,args):
        return self.user.show_history()

class SessionHistoryCommand(ICommand):
    """A Command object, which implemets the ICommand interface"""

    def __init__(self, user):
        self.user = user

    def execute(self,args):
        return self.user.session_history()

class TransferFundsCommand(ICommand):
    """A Command object, which implemets the ICommand interface"""

    def __init__(self, user):
        self.user = user

    def execute(self,args):
        transfer = args[0]
        destination = args[1]
        return self.user.transfer_funds(transfer,destination)


class Switch:

    """The Invoker Class"""

    def __init__(self):
        self._commands = {}



    @property
    def history(self):
        return self._history


    def register(self, command_name, command):
        self._commands[command_name] = command


    def execute(self, command_name,*args):
        if command_name in self._commands.keys():
            return self._commands[command_name].execute(args)
        else:
            print(f"Command [{command_name}] not recognised")


class User:

    def __init__(self,funds,history):
        self.funds = funds
        self.history = history
        self.currentsessionhistory = "--- Current Session History ---\n"
        if self.history == None or self.history == "":
            self.history = "--- Account Statement ---\n"

    def add_funds(self,deposit):
        deposit = float(deposit)
        self.funds = self.funds + deposit
        self.history = self.history + "Deposit: $ " + str(deposit) + "\n"
        self.currentsessionhistory = self.currentsessionhistory + "Deposit: $ " + str(deposit) + "\n"
        self.save_data()
        return "Deposit: $ " + str(deposit) + "\n"

    def show_history(self):
        self.currentsessionhistory = self.currentsessionhistory + "Printed Account Statement\n"
        return self.history

    def session_history(self):
        return self.currentsessionhistory

    def transfer_funds(self,transfer,destination):
        transfer = float(transfer)
        if(transfer > self.funds):
            return "You can't transfer more than your funds\n"
        else:
            self.funds = self.funds - transfer
            self.history = self.history + "Transfer to " + str(destination) + ": $ " + str(transfer) + "\n"
            self.currentsessionhistory = self.currentsessionhistory + "Transfer to " + str(destination) + ": $ " + str(transfer) + "\n"
            self.save_data()
            return "Transfer to " + str(destination) + ": $ " + str(transfer) + "\n"

    def save_data(self):
        #Write funds and history on data file
        data = {"funds":user.funds,"history":user.history}
        f = open('userdata.txt', 'w')
        f.write(str(data))
        f.close()



if __name__ == "__main__":

    def labelmessage(message):
        l["text"] = message
    
    def deposit_button():
        value = e.get()
        if value != "Insert value":
            message = SWITCH.execute("Deposit",value)
            e.delete(0,"end")
            e.insert(0,"Insert value")
            labelmessage(message)
            account_funds["text"] = "Funds: $" + str(user.funds)
    
    def transfer_button():
        destination = d.get()
        value = e.get()
        if destination != "Insert destination" and value != "Insert value":
            message = SWITCH.execute("Transfer",value,destination)
            e.delete(0,"end")
            e.insert(0,"Insert value")
            d.delete(0,"end")
            d.insert(0,"Insert destination")
            account_funds["text"] = "Funds: $" + str(user.funds)
            labelmessage(message)

    def statement_button():
        message = SWITCH.execute("History")

        labelmessage(message)

    def currenthistory_button():
        message = SWITCH.execute("Session History")

        labelmessage(message)

    try: 
        f = open('userdata.txt', 'r')
        data = f.read()
        data = ast.literal_eval(data)
        f.close()
    except:
        f = open('userdata.txt', 'w')
        data = {"funds" : 0, "history" : None}
        f.close()

    user = User(data["funds"],data["history"])


    #Create Commands

    ADD_FUNDS = AddFundsCommand(user)
    SHOW_HISTORY = ShowHistoryCommand(user)
    TRANSFER_FUNDS = TransferFundsCommand(user)
    SESSION_HISTORY = SessionHistoryCommand(user)

    # Register the commands with the invoker (Switch)
    SWITCH = Switch()
    SWITCH.register("Deposit", ADD_FUNDS)
    SWITCH.register("History", SHOW_HISTORY)  
    SWITCH.register("Transfer", TRANSFER_FUNDS) 
    SWITCH.register("Session History", SESSION_HISTORY)



    app = Tk()
    app.title("Banco Cliente")
    app.geometry("800x600")
    app.resizable(0,0)

    e = Entry(app)
    e.insert(0,"Insert value")
    e.pack()

    d = Entry(app)
    d.insert(0,"Insert destination")
    d.pack()

    account_funds = Label(app,text = "Funds: $" + str(user.funds))
    account_funds.pack()


    deposit = Button(app,text = "Deposit Funds",command = deposit_button)
    deposit.pack()

    transfer = Button(app,text = "Transfer Funds",command = transfer_button)
    transfer.pack()

    statement = Button(app,text = "Account Statement",command = statement_button)
    statement.pack()

    currenthistory = Button(app,text = "Session History",command = currenthistory_button)
    currenthistory.pack()

    l = Label(app,text=None)
    l.pack()




    app.mainloop()