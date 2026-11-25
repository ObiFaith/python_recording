def intro():
    print(
        f"\nWelcome to The Yellow Bus Odyssey: Escape from Third Mainland Bridge!\n",
        f"\nYou are a commuter inside a legendary Lagos Danfo (yellow commercial bus). It is 5:30 PM, the sun is blazing, and you are trapped in the mother of all gridlocks. Your mission? Survive the traffic, keep your sanity, and make it home.\n",
        f"\nCopy and paste the game text below into your favorite document or shared space to play with friends, or just read through and choose your path!\n"
    )
    print("-" * 80 + "\n")

scenes = {
    "the_stationary_danfo": {
        "stay": {
            "the_chicken_uprising": ""
        }
    }
}

def main():
    intro()


if __name__ == "__main__":
    main()