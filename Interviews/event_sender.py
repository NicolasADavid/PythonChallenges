"""
Design an SDK:

https://amplitude.com/docs/apis/analytics/http-api-quickstart

The task is to build an Amplitude SDK to send event data to a server. 

The SDK is initialized with 3 parameters:
- API Key: this allows the app to authenticate with Amplitude 
- flushQueueSize: Only send data to Amplitude once these many events have been accumulated.
- flushIntervalMillis - Only send data to Amplitude after the configured interval. (Counted from when an event is tracked)

The Amplitude client should be able to track an event with the field event type. Eg: amplitude.track(“button click”).

"""


import requests
import json
import threading

headers = {
    'Content-Type': 'application/json',
    'Accept': '*/*'
}

# data = {
#     "api_key": "xxxxxxx",
#     "events": [{
#         "user_id": "203201202",
#         "device_id": "C8F9E604-F01A-4BD9-95C6-8E5357DF265D",
#         "event_type": "watch_tutorial"
#     }]
# }

# response = requests.post('https://api2.amplitude.com/2/httpapi',
#                         headers=headers, data=json.dumps(data))

HTTP_API = "https://api2.amplitude.com/2/httpapi"
API_KEY = "xxxxxxx"  # Replace with your actual API key
FLUSH_TIME = 5  # seconds
EVENT_LIMIT = 5 # events

class Event(object):
    
    def __init__(self, event_type, user_id, device_id):
        self.event_type = event_type
        self.user_id = user_id
        self.device_id = device_id

    def to_dict(self):
        return {
            "event_type": self.event_type,
            "user_id": self.user_id,
            "device_id": self.device_id
        }
    
class AmplitudeClient(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.events = []
        self.scheduled_flush_handle = None

    def get_events(self):

      return self.events
    
      # return [
      #     {
      #         "user_id": "203201202",
      #         "device_id": "C8F9E604-F01A-4BD9-95C6-8E5357DF265D",
      #         "event_type": "watch_tuatorial"
      #     },
      #     {
      #         "user_id": "203201203",
      #         "device_id": "C8F9E604-F01A-4BD9-95C6-8E5357DF266D",
      #         "event_type": "click_button"
      #     }
      # ]

    def schedule_flush(self):
        if not self.scheduled_flush_handle:
          self.scheduled_flush_handle = threading.Timer(FLUSH_TIME, self.flush_events)
          self.scheduled_flush_handle.start()
          print("Flush scheduled in", FLUSH_TIME, "seconds")

    def cancel_flush(self):
        
        if self.scheduled_flush_handle:
            self.scheduled_flush_handle.cancel()
            self.scheduled_flush_handle = None
            print("Flush cancelled")
        else:
            print("No flush scheduled")
        
    def flush_events(self):
        
        events = self.get_events()

        if not events:
            print("No events to flush")
            return
        
        success = self.send_amplitude_event_batch(events)

        if success:
          # TODO: Is there a concurrency issue here?
          print("Flushed events successfully")
          self.events = []
          self.cancel_flush()

    def write_event_to_db(self, event):
        self.events.append(event)

    def collect_event(self, event_type, user_id, device_id):
        
        event = Event(event_type, user_id, device_id)
        self.write_event_to_db(event)

        if len(self.events) >= EVENT_LIMIT:
            # If the event limit is reached, flush immediately
            self.flush_events()
        else:
            # Schedule a flush if not already scheduled
            if not self.scheduled_flush_handle:
              print("Scheduling flush")
              self.schedule_flush()

        return event

    def send_amplitude_event_batch(self, events) -> bool:
        
        if not events:
          return

        data = json.dumps({
          "api_key": self.api_key,
          "events": [event.to_dict() for event in events]
        })

        response = requests.post(HTTP_API, headers=headers, data=data)

        if response.status_code == 200:
            print("Success:", response.json())
            return True
        elif response.status_code == 400:
            print("Bad Request:", response.text)
            return False
        else:
            print("Error:", response.text)
            return False

# import time

if __name__ == "__main__":
    # Example
    ac = AmplitudeClient(API_KEY)

    # Collect an event
    ac.collect_event("watch_tutorial", "203201202", "C8F9E604-F01A-4BD9-95C6-8E5357DF265D")
    ac.collect_event("watch_tutorial", "203201202", "C8F9E604-F01A-4BD9-95C6-8E5357DF265D")
    ac.collect_event("watch_tutorial", "203201202", "C8F9E604-F01A-4BD9-95C6-8E5357DF265D")
    ac.collect_event("watch_tutorial", "203201202", "C8F9E604-F01A-4BD9-95C6-8E5357DF265D")
    ac.collect_event("watch_tutorial", "203201202", "C8F9E604-F01A-4BD9-95C6-8E5357DF265D")
    ac.collect_event("watch_tutorial", "203201202", "C8F9E604-F01A-4BD9-95C6-8E5357DF265D")
    ac.collect_event("watch_tutorial", "203201202", "C8F9E604-F01A-4BD9-95C6-8E5357DF265D")
    ac.collect_event("watch_tutorial", "203201202", "C8F9E604-F01A-4BD9-95C6-8E5357DF265D")

    # def new_event():
    #     # Collect a new event
    #     ac.collect_event("click_button", "203201203", "C8F9E604-F01A-4BD9-95C6-8E5357DF266D")

    # while True:
    #   time.sleep(2)
    #   new_event()
