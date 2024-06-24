import random
from colorama import Fore


def generate():
    words = input(f"{Fore.GREEN}[*] Enter key words: {Fore.WHITE}").split(" ")

    def random_generator(size,words):
        return ''.join(random.choice(words) for _ in range(size))

    lower_words = [word.lower() for word in words]
    upper_words = [word.upper() for word in words]
    capitalized_words = [word.capitalize() for word in words]
    random_words = []

    for x in range(20):
        random_words.append(random_generator(size=2,words=words))
        random_words.append(random_generator(size=2,words=lower_words))
        random_words.append(random_generator(size=2,words=upper_words))
        random_words.append(random_generator(size=2,words=capitalized_words))



    united_words = lower_words+upper_words+capitalized_words+random_words+words
    with open("wlist.txt","w") as f:
        for word in united_words:
            f.write(f"{word}\n")

    print(f"{Fore.RED}Generated and saved to {Fore.BLUE}wlist.txt{Fore.WHITE}")
