class WorldFrequencyCounter:
    def __init__(self):
        self.word_count = {}

    def process_text(self, sentence):
        for string in sentence.lower().split():
            string = string.strip(',.";:[]{}()')

            if string:
                self.word_count[string] = self.word_count.get(string, 0) + 1

    def display_values(self):
        if not self.word_count:
            return "\nNo Sentence to display"

        return "\n".join(
            [f"{word} : {count}" for word, count in self.word_count.items()]
        )


counter = WorldFrequencyCounter()

from time import sleep


# menu
def menu():

    while True:
        sleep(1)

        print(
            """
        \nWelcome to Word Frequency Counter:\n

        1.Process text
        2.Display value
        3.Quit the program\n
        
        """
        )

        try:
            choice = int(input("Enter your choice: "))

        except ValueError:
            print("\nEnter a numeric value!")
            continue

        if choice == 1:
            sentence = input("\nEnter a sentence: ").strip()
            counter.process_text(sentence)

        elif choice == 2:
            print("\n" + counter.display_values())

        elif choice == 3:
            print("\nExiting the program\n")
            break

        else:
            print("\nInvalid operator! Choose from the given options")