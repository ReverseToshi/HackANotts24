class logic:
    def __init__(self, name):
        """Initialize player with default stats and financial status."""
        self.name = name
        self.reputation = 500  # Starting credit score
        self.credit_limit = 1000  # Credit card maximum limit
        self.card_balance = 0  # Credit card balance
        self.current_account_balance = 500  # Debit card balance (cash in hand)
        self.strikes = 0  # Strike count for missed payments
        self.weekly_interest_rate = 1.15  # Weekly interest rate (e.g., 15%)
        self.reputation_status="Proletarii Kredit"
        self.cur=0

    def __str__(self):
        """Return a string representation of the player's stats."""
        return (f"Player: {self.name}\n"
                f"Reputation (Credit Score): {self.reputation}\n"
                f"Credit Limit: {self.credit_limit}\n"
                f"Credit Card Balance: {self.card_balance}\n"
                f"Current Account Balance: {self.current_account_balance}\n"
                f"Strikes: {self.strikes}\n")

    def get_payed(self):
        self.current_account_balance+=100

    def purchase(self, amount, payment_method):
        """Make a purchase using either the debit or credit card."""
        if payment_method == "debit":
            self.use_debit(amount)
        elif payment_method == "credit":
            self.use_credit(amount)
        #else:
            #print("Invalid payment method. Please choose 'debit' or 'credit'.")

    def use_debit(self, amount):
        """Attempt to make a purchase using the debit card balance."""
        if amount <= self.current_account_balance:
            self.current_account_balance -= amount
            #print(f"Purchase of {amount} made with debit card. Remaining balance: {self.current_account_balance}.")
        #else:
            #print("Insufficient funds on debit card.")

    def use_credit(self, amount):
        """Attempt to make a purchase using the credit card."""
        if amount + self.card_balance <= self.credit_limit:
            self.card_balance += amount
            self.cur=self.card_balance/self.credit_limit
        else:
            self.reputation-=20
            self.check_status()

            #print("Purchase exceeds credit limit on credit card.")

    def make_payment(self, amount):
        """Make a payment toward the credit card balance."""
        if amount < self.card_balance * 0.1:
            print("Minimum payment required is 10% of the balance.")
            return
        elif amount > self.card_balance:
            amount = self.card_balance  # Avoid overpaying

        if amount <= self.current_account_balance:
            self.current_account_balance -= amount
            self.card_balance -= amount
            if 0 < self.cur <= 0.3:
                self.reputation+=50
            else:
                self.reputation+= round((-71*self.cur)+71)
            print(f"Payment of {amount} made. Remaining credit card balance: {self.card_balance}.")
        else:
            self.reputation-=50
            self.issue_strike()
            print("Insufficient funds for payment! Strike issued.")
        
        self.check_status()
        
        
    def check_status(self):
        """Return the reputation status based on the current score."""
        if self.reputation < 480:
            return "Krov"
        elif 480 <= self.reputation <= 519:
            return "ProLetarii"
        elif 520 <= self.reputation <= 619:
            return "Komsomolov"
        elif 620 <= self.reputation <= 719:
            return "Rabochii"
        elif 720 <= self.reputation <= 999:
            return "Patriotov"
        else:
            return "Unknown"

    def apply_interest(self):
        """Apply weekly interest to any remaining credit card balance."""
        if self.card_balance > 0:
            self.card_balance *= self.weekly_interest_rate
            #print(f"Interest applied. New credit card balance: {self.card_balance:.2f}")

    def issue_strike(self):
        """Issue a strike for missed payments or insufficient funds."""
        self.strikes += 1
        print(f"Strike {self.strikes} issued.")
        if self.strikes >= 3:
            print("Game over! You've reached the maximum number of strikes.")
            # Add game-over logic here if needed

    def monday_payment_option(self):
        """Prompt player to pay full balance, minimum, or custom amount on credit card."""
        #print("It's Monday! Time to pay your credit card balance.")
        #print(f"Your balance is {self.card_balance}. Options: ")
        #print("1. Pay in full")
        #print("2. Pay minimum (10%)")
        #print("3. Pay custom amount (10% or above)")

        choice = input("Choose an option (1, 2, or 3): ")

        if choice == "1":
            self.make_payment(self.card_balance)
        elif choice == "2":
            minimum_payment = self.card_balance * 0.1  # Minimum 10% or a set threshold
            self.make_payment(minimum_payment)
        elif choice == "3":
            custom_payment = float(input("Enter the amount you want to pay: "))
            if custom_payment >= self.card_balance * 0.1:
                self.make_payment(custom_payment)
            else:
                print("Custom amount must be at least 10% of the balance.")
                self.issue_strike()
        else:
            print("Invalid choice. You missed the payment.")
            self.issue_strike()

    def weekly_update(self):
        """Perform weekly updates: prompt for payment and apply interest."""
        self.get_payed()
        self.monday_payment_option()
        self.apply_interest()



#this is the current day in the game. rolls over 
current_game_day = 0
days_of_week = ["Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
                "Sunday"]
current_game_day_of_week = None
def calculate_day_of_week():
    current_game_day_of_week = days_of_week[current_game_day % 7]