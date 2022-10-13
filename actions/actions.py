# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
import math as m
import sqlite3 as sql


# class AddDatabase(Action):
#     def name(self) -> Text:
#         return "action_add_database"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         conn = sql.connect("D:/Works/RASAs/rasa0/Database/rasa.db")
#         conn.execute("delete from user where id = 2")
#         conn.execute("insert into USER(id, acc, password, balance) values (1, 'PQF', '132475', 3000)")
#         conn.commit()
#
#         dispatcher.utter_message(text="finished!")
#
#         return []

connect = sql.connect("D:/Works/RASAs/rasa0/Database/rasa.db")


def check_unique(name):
    cu = connect.cursor()
    cu.execute('select acc from USER')
    for back_name in cu.fetchall():
        if back_name[0] == name:
            return False
    return True


class EraseSlots(Action):
    def name(self) -> Text:
        return "action_erase_slots"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [AllSlotsReset()]


# class Wait(Action):
#     def name(self) -> Text:
#         return "action_wait"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         return[]


class OpenNewAccount(Action):
    def name(self) -> Text:
        return "action_open_new_account"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conn = sql.connect("D:/Works/RASAs/rasa0/Database/rasa.db")
        new_acc = tracker.get_slot("account")
        new_password = tracker.get_slot("password")

        if check_unique(new_acc):
            s = "insert into USER(acc, password, balance) values (?, ?, 0)"
            conn.execute(s, (new_acc, new_password, ))
            conn.commit()
            dispatcher.utter_message(text="Your account has been created!")
        else:
            dispatcher.utter_message(text=f"There is a user called {new_acc} already, please try another.")
        return []


class CheckBalance(Action):
    def name(self) -> Text:
        return "action_check_balance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conn = sql.connect("D:/Works/RASAs/rasa0/Database/rasa.db")
        cu = conn.cursor()
        acc = tracker.get_slot("account")
        password = tracker.get_slot("password")

        if not check_unique(acc):
            f = "select password from USER where acc = ?"
            compare_password = cu.execute(f, (acc, ))
            if password == compare_password.fetchone()[0]:
                s = "select balance from USER where acc = ?"
                res = cu.execute(s, (acc, ))
                result = res.fetchone()[0]

                dispatcher.utter_message(text=f"Your balance number is ${result}.")
            else:
                dispatcher.utter_message(text="You entered wrong password.")
        else:
            dispatcher.utter_message(text=f"It seems that there is no user named {acc}.")
        return []


class SaveMoney(Action):
    def name(self) -> Text:
        return "action_save_money"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conn = sql.connect("D:/Works/RASAs/rasa0/Database/rasa.db")
        cu = conn.cursor()
        acc = tracker.get_slot("account")
        password = tracker.get_slot("password")
        money_amount = tracker.get_slot("money_amount_save")

        if not check_unique(acc):
            f = "select password from USER where acc = ?"
            compare_password = cu.execute(f, (acc, ))
            if password == compare_password.fetchone()[0]:
                s = "select balance from USER where acc = ?"
                res = cu.execute(s, (acc, ))
                result = m.floor(res.fetchone()[0] + float(money_amount))

                u = "update USER set balance = ? where acc = ?"
                cu.execute(u, (result, acc, ))
                conn.commit()
                dispatcher.utter_message(text=f"You have saved money successfully and now your balance number is ${result}.")
            else:
                dispatcher.utter_message(text="You entered wrong password.")
        else:
            dispatcher.utter_message(text=f"It seems that there is no user named {acc}.")
        return []


class WithdrawMoney(Action):
    def name(self) -> Text:
        return "action_withdraw_money"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        conn = sql.connect("D:/Works/RASAs/rasa0/Database/rasa.db")
        cu = conn.cursor()
        acc = tracker.get_slot("account")
        password = tracker.get_slot("password")
        money_amount = tracker.get_slot("money_amount_withdraw")

        if not check_unique(acc):
            f = "select password from USER where acc = ?"
            compare_password = cu.execute(f, (acc, ))

            if password == compare_password.fetchone()[0]:
                s = "select balance from USER where acc = ?"
                res = cu.execute(s, (acc, ))
                balance_in_account = res.fetchone()[0]
                result = m.floor(balance_in_account - float(money_amount))

                if result >= 0:
                    u = "update USER set balance = ? where acc = ?"
                    cu.execute(u, (result, acc, ))
                    conn.commit()
                    dispatcher.utter_message(text=f"You have withdrawn money successfully and now your balance number is ${result}.")
                else:
                    dispatcher.utter_message(text="You don't have enough money in your account.")
            else:
                dispatcher.utter_message(text="You entered wrong password.")
        else:
            dispatcher.utter_message(text=f"It seems that there is no user named {acc}.")
        return []
