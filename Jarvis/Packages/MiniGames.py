import random

class RPS:
    def jarvisChoice(self):
        random.choice("⛰","📰","✂")

    def gameResult(self,userChoice,jarvisChoice):
        if userChoice == "⛰" and jarvisChoice == "✂" or userChoice == "📰" and jarvisChoice == "⛰" or userChoice == "✂" and jarvisChoice == "📰":
            return "You won!"
        elif userChoice == jarvisChoice:
            return "It's a tie!"