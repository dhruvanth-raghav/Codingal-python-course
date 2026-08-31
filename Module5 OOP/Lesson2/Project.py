class DailyMessage:
    def __init__(self):
        self.message = ""

    def get_message(self):
        self.message = input("Enter a message: ")

    def print_message(self):
        print(self.message.upper())

class HelperSession:
    def __init__(self):
        print("Session started✅")

    def __del__(self):
        print("Session ended❌")

def create_session():
    session = HelperSession()
    return session

class PairFinder:
    def find_pair(self, numbers, target):
        for i, number in enumerate(numbers):
            for j in range(i + 1, len(numbers)):
                if number + numbers[j] == target:
                    print("Index pair:", i, j)
                    return

daily_text = DailyMessage()
daily_text.get_message()
daily_text.print_message()

session = create_session()

numbers = [10, 20, 30, 40]
target = int(input("Enter target sum: "))

finder = PairFinder()
finder.find_pair(numbers, target)
