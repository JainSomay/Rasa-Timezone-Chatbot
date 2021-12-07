# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

timezones = {"mumbai":"GMT+5:30",
             "tokyo":"GMT+9",
             "luxembourg":"GMT+2",
             "seoul":"GMT+9",
             "sydney":"GMT+10"
}

class ActionShowTimeZone(Action):

    def name(self) -> Text:
        return "action_show_time_zone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city = tracker.get_slot("city")
        timezone = timezones.get(city)

        if timezone is None:
            output = "could not find th timezone of {}".format(city)
        else:
            output =  "Time zone of a {} is {}".format(city)
        dispatcher.utter_message(text=output)

        return []
