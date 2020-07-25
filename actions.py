from rasa_core.actions import Action
from rasa_core.events import SlotSet
import requests
import random
import sqlite3
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

def action():
    class ActionCriteria(Action):
        def name(self):
            return 'action_criteria'

        def run(self, dispatcher, tracker, domain):

            criteria = tracker.get_slot('CRITERIA')
            company_name = tracker.get_slot('COMPANY')
               #here we can pass db path and sql query to fetch data what we want
    #         print(criteria)
    #         print(company_name)
            msg = 60

    #         cuisine = tracker.get_slot('cuisine')
    #         q = "select * from restaurants where cuisine='{0}' limit 1".format(cuisine)
    #         result = db.query(q)


            if msg:
                print("Criteria for {} company is that it needed {}% in Btech ". format(company_name,msg))
    #             dispatcher.utter_message(response)
            else:
                dispatcher.utter_message("Criteria not found ")

    # class ActionApplication()

    # class ActionMovie(Action):
    #     def name(self):
    #         return 'action_top_movie'

    #     def run(self, dispatcher, tracker, domain):
    #         top = tracker.get_slot('VALUE')
    #         movie = tracker.get_slot('MOVIE')
    #         conn = sqlite3.connect('./Db-IMDB.db')

    #         query = "SELECT title FROM {} limit {}".format(movie,top)
    #         result = pd.read_sql_query(query,conn)

    #         #result
    #         res_list = list(result['title'])
    # #         cuisine = tracker.get_slot('cuisine')
    # #         q = "select * from restaurants where cuisine='{0}' limit 1".format(cuisine)
    # #         result = db.query(q)
    #         if result:
    #             response = "Is this fine". format(print(*res_list, sep = " , "))
    #             dispatcher.utter_message(response)
    #         else:
    #             dispatcher.utter_message("Movie not found ")

    class ActionRestarted(Action):
        """ This is for restarting the chat"""

        def name(self):
            return "action_restart"

        def run(self, dispatcher, tracker, domain):
            return [Restarted()]
