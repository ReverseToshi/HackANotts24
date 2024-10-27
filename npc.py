from logic import current_game_day_of_week
class NPC:
    def __init__(self, name, dialogue):
        """Initialize NPC with a name and dialogue."""
        self.name = name
        self.dialogue = dialogue  # List of dialogue strings

    def talk(self, player):
        """Display the NPC's dialogue."""
        dialogue = self.dialogue_schedule.get(current_game_day_of_week, "No dialogue available today.")
        #print(f"{self.name}: {dialogue}")

    def interact(self, player):
        """Basic interaction method. Subclasses can override this."""
        self.talk(player)

class Viktor(NPC):
    def __init__(self):
        dialogue_schedule = {
            "Monday": "We start the week with a strong resolve, comrade.",
            "Tuesday": "Remember, your financial choices shape your future.",
            "Wednesday": "Midweek! How is your credit management going?",
            "Thursday": "Stay vigilant with your finances, comrade.",
            "Friday": "A strong end to the week is a sign of strength.",
            "Saturday": "Take some time to reflect on your financial goals.",
            "Sunday": "Prepare for the week ahead; Gosbank relies on you."
        }
        super().__init__("Comrade Viktor Kuznetsov", dialogue_schedule)

    def interact(self, player):
        """Unique interaction with Viktor, perhaps giving advice."""
        self.talk(player)


class Ivanov(NPC):
    def __init__(self):
        dialogue_schedule = {
            "Monday": "A good financial week starts with a solid plan.",
            "Tuesday": "Have you thought about the 50-30-20 rule?",
            "Wednesday": "Credit is a powerful tool; use it wisely.",
            "Thursday": "Every decision has a financial impact.",
            "Friday": "End the week by reviewing your expenses.",
            "Saturday": "The weekend is perfect for assessing your goals.",
            "Sunday": "Prepare yourself for a financially sound week ahead."
        }
        super().__init__("Professor Ivanov", dialogue_schedule)

    def interact(self, player):
        """Unique interaction with Ivanov, imparting financial wisdom."""
        self.talk(player)


class Nina(NPC):
    def __init__(self):
        dialogue_schedule = {
            "Monday": "Psst... need something off the record?",
            "Tuesday": "Deals are aplenty, but tread carefully.",
            "Wednesday": "I can get you what you need, for a price.",
            "Thursday": "Keep your reputation in check, comrade.",
            "Friday": "It's payday! Looking for something special?",
            "Saturday": "Just because it's not 'legal' doesn't mean it's wrong.",
            "Sunday": "A day to rest, but the deals keep coming!"
        }
        super().__init__("Nina 'The Squirrel'", dialogue_schedule)

    def interact(self, player):
        """Nina offers high-risk financial opportunities."""
        self.talk(player)


class Kolya(NPC):
    def __init__(self):
        dialogue_schedule = {
            "Monday": "Let's start the week responsibly, citizen.",
            "Tuesday": "High debt attracts attention; keep that in mind.",
            "Wednesday": "Today is a good day to lower your debts.",
            "Thursday": "You're being watched, make sure your finances are sound.",
            "Friday": "The end of the week is not a time to slack on responsibility.",
            "Saturday": "I advise against unnecessary spending this weekend.",
            "Sunday": "Prepare for the coming week with a sound mind."
        }
        super().__init__("Colonel Kolya Petrov", dialogue_schedule)

    def interact(self, player):
        """Kolya provides budgeting advice and monitors the player's financial behavior."""
        self.talk(player)

       
