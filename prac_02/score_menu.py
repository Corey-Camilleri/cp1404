"""
CP1404/CP5632 - Practical
Menu-driven program that prints grade or stars.
"""

MENU = """(G)et a valid score
(P)rint grade
(S)how stars
(Q)uit"""


def main():
    """Menu-driven program that prints grade or stars based on score."""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'G':
            pass
        elif choice == 'P':
            pass
        elif choice == 'S':
            pass
        else:
            pass
        print(MENU)
        choice = input(">>> ").upper()


def determine_grade(score):
    """Determine the grade based on the score."""
    pass


def get_valid_score():
    """Get a score between 0 and 100."""
    pass


main()
