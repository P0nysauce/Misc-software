from __future__ import print_function
from random import choice
import hexchat

__module_name__ = 'Ralph'
__module_version__ = '2.0'
__module_description__ = 'Ralph Wiggum Quotes'
__author__ = 'PonySauce + Gallows'

ralph = [
    'Lies are like stars, they always come out. I have five face holes.',
    'Me, fail English? That’s unpossible.',
    'The doctor said I wouldn’t have so many nosebleeds if I kept my finger outta there.',
    'Miss Hoover, I glued my head to my shoulder.',
    'This is my swing set. This is my sandbox. I’m not allowed to go in the deep end.',
    'Hi, Lisa! Hi, Super Nintendo Chalmers. I’m learneding.',
    'That’s where I saw the Leprechaun. He tells me to burn things.',
    'Slow down, Bart! My legs don’t know how to be as long as yours.',
    'Dear Miss Hoover, you have Lyme disease. We miss you. Kevin is biting me. Come back soon. Here’s a drawing of a spirochete. Love, Ralph.',
    'Martin Luther King had a dream. Dreams are where Elmo and Toy Story had a party, and I was invited. Yay! My turn is over!',
    'My Grandma had hair like that when she went to sleep in her forever box.',
    'All my friends have birthdays this year!',
    'When I grow up, I wanna be a principal or a caterpillar.',
    'If Mommy’s purse didn’t belong in the microwave, why did it fit?',
    'I cheated wrong. I copied the Lisa name and used the Ralph answers.',
    'Plant it, and you’ll grow a new Ralph.',
    'Lisa’s bad dancing makes my feet sad.',
    'And when the doctor said I didn’t have worms anymore, that was the happiest day of my life.',
    'I wet my arm pants.',
    'My knob tastes funny.',
    'Your eyes need diapers.',
    'I’m a crayon, and I’m the best color.',
    'I was done before we came in.',
    'Do alligators alligate?',
]

def ralph(word, word_eol, userdata):
    quote = choice(ralph)  # Select a random quote
    hexchat.command("say {}".format(quote))  # Print the quote to the channel

# Register the command in HexChat
hexchat.hook_command("ralph", ralph, help="Usage: /ralph - Outputs a random Ralph Wiggum quote")

# Notify that the plugin is loaded
hexchat.prnt(__module_name__ + ' version ' + __module_version__ + ' loaded.')