from event import Event

class MyRequests:
    def __init__(self):
        pass

    def login(self, user_id, password):
        pass

    def logout(self):
        pass

    def keep_session(self):
        pass

    def scan_events(self, user_id):
        pass

    def construct_event(self, event_id):
        _id = event_id
        title = 'Title'
        description = 'Description'
        download_path = 'Download Path'
        return Event(_id, title, description, download_path)

    def comment(self, event_id):
        pass

    def assign(self):
        pass

    def resolve(self):
        pass
