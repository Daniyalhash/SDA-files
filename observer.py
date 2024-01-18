from abc import ABC, abstractmethod

# Observer Interface
class NewsChannel(ABC):
    @abstractmethod
    def update(self, news):
        pass

# Concrete Observer
class SportsNewsChannel(NewsChannel):
    def update(self, news):
        print(f"Sports News Channel: {news}")

# Concrete Observer
class FinanceNewsChannel(NewsChannel):
    def update(self, news):
        print(f"Finance News Channel: {news}")

# Subject
class NewsAgency:
    def __init__(self):
        self.subscribers = []
        self.news = None

    def attach(self, subscriber):
        self.subscribers.append(subscriber)

    def detach(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify_subscribers(self):
        for subscriber in self.subscribers:
            subscriber.update(self.news)

    def set_news(self, news):
        self.news = news
        self.notify_subscribers()

# Client Code
if __name__ == "__main__":
    # Create subjects and observers
    news_agency = NewsAgency()
    sports_channel = SportsNewsChannel()
    finance_channel = FinanceNewsChannel()

    # Attach observers to the subject
    news_agency.attach(sports_channel)
    news_agency.attach(finance_channel)

    # Set and notify news
    news_agency.set_news("New sports season starts!")
    print("")

    # Detach an observer
    news_agency.detach(sports_channel)

    # Set and notify news again
    news_agency.set_news("Stock market update!")
