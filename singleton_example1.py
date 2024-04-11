from datetime import datetime
'''
Constructs an event logger class as a singleton to be used across the application
'''
class EventLogger:
    _instance = None  # Private class attribute
    _event_logs = []

    def __new__(cls, *args, **kwargs):
        if not cls._instance:  # Check if instance is created
            cls._instance = super(EventLogger, cls).__new__(cls) #If not created, creates a new instance of Eventlogger
        return cls._instance #Anycase returns the newly or the existing instance
    
    def log_event(self, event_message):
        timestamp = datetime.now().strftime( '%Y-%m-%d %H:%M:%S.%f UTC')
        self._event_logs.append(f"{timestamp}: {event_message}")

    def display_logs(self):
        for log in self._event_logs:
            print(log)
            
logger = EventLogger()
logger.log_event("Starting app")
logger.log_event("Executing task 1 ")

logger2 = EventLogger()
logger2.log_event("Finisihing app")
logger2.log_event("Ending task 1 ")

logger3 = EventLogger()
logger3.display_logs()