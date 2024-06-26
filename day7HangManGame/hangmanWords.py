word_list = [
'abyss', 
'awkward', 
'beekeeper', 
'bikini', 
'blitz', 
'blizzard',
'bookworm',
'buffalo', 
'buzzard', 
'buzzing', 
'buzzwords', 
'cockiness', 
'croquet', 
'cycle', 
'dizzying', 
'duplex',  
'equip', 
'faking', 
'fishhook', 
'fixable', 
'flapjack', 
'flopping', 
'fluffiness',  
'foxglove', 
'frizzled', 
'funny', 
'galaxy', 
'galvanize', 
'gazebo', 
'glowworm', 
'glyph',
'gossip', 
'grogginess',  
'icebox', 
'injury', 
'jackpot', 
'jelly', 
'jinx', 
'jogging', 
'joking', 
'joyful', 
'juicy', 
'jukebox', 
'jumbo', 
'keyhole', 
'kilobyte', 
'kiosk', 
'kitsch', 
'kiwifruit',
'lengths', 
'lucky', 
'luxury', 
'matrix', 
'microwave',  
'nightclub', 
'nowadays', 
'oxidize', 
'oxygen', 
'pajama', 
'peekaboo', 
'pixel', 
'pizazz', 
'pneumonia', 
'puppy', 
'puzzling', 
'quartz', 
'queue', 
'quiz', 
'rhythm', 
'rickshaw', 
'scratch',  
'snazzy', 
'sphinx',  
'squawk', 
'staff', 
'strength', 
'strengths', 
'stretch', 
'stronghold', 
'subway', 
'swivel', 
'syndrome', 
'thriftless', 
'thumbscrew', 
'topaz', 
'transcript', 
'transgress', 
'transplant', 
'twelfth', 
'twelfths', 
'unknown', 
'unworthy', 
'unzip', 
'uptown', 
'vaporize', 
'vixen', 
'vodka', 
'voodoo', 
'vortex', 
'voyeurism', 
'walkway', 
'wave', 
'wavy', 
'waxy', 
'wellspring', 
'wheezy', 
'whiskey', 
'whizzing', 
'whomever', 
'wimpy', 
'witchcraft', 
'wizard', 
'woozy', 
'wristwatch', 
'yachtsman', 
'yippee', 
'youthful', 
'yummy', 
'zephyr',
'zigzag',
'zipper', 
'zodiac', 
'zombie', 
]
hints_list = [
    "A deep or seemingly bottomless chasm.",
    "Lacking grace or skill in manner or movement.",
    "Someone who maintains and manages hives of bees.",
    "A two-piece swimsuit for women.",
    "An intense military campaign or a sudden energetic effort.",
    "A severe snowstorm with high winds and low visibility.",
    "A person devoted to reading.",
    "A large animal of the cattle family, native to North America.",
    "A large bird of prey.",
    "Making a continuous, low, humming sound.",
    "Trendy words or phrases often used in business or politics.",
    "Overconfidence or arrogance.",
    "A game played on a lawn, where players hit balls through hoops.",
    "A series of events that are regularly repeated in the same order.",
    "Causing a sensation of spinning around and losing balance.",
    "A house divided into two apartments.",
    "To supply with necessary items for a particular purpose.",
    "Pretending something that is not true.",
    "A hook used for catching fish.",
    "Capable of being repaired.",
    "A sweet pancake or a type of bar made with oats.",
    "Falling, hanging, or moving in a loose and ungainly way.",
    "The quality of being light and soft.",
    "A tall plant with tubular flowers, often pink or purple.",
    "Fried until crisp or curled tightly.",
    "Causing laughter or amusement.",
    "A system of millions or billions of stars, together with gas and dust.",
    "To shock or excite someone into taking action.",
    "A freestanding, open-sided structure with a roof.",
    "A beetle or larva that emits light.",
    "A carved or inscribed symbol.",
    "Casual or unconstrained conversation about others.",
    "The state of being sleepy or not fully alert.",
    "An old-fashioned refrigerator.",
    "Harm or damage to the body.",
    "A large cash prize in a game or lottery.",
    "A sweet, clear, and gelatinous spread made from fruit.",
    "A person or thing that brings bad luck.",
    "Running at a steady, gentle pace.",
    "Making jokes or saying things in a playful manner.",
    "Feeling or expressing great happiness.",
    "Full of juice; succulent.",
    "A machine that plays selected music from records.",
    "Very large.",
    "The hole in a lock into which a key fits.",
    "A unit of memory or data equal to 1,024 bytes.",
    "A small, open-fronted hut or cubicle.",
    "Art or objects considered to be in poor taste but appreciated in an ironic or knowing way.",
    "A small, fuzzy, brown fruit with green flesh.",
    "The measurement or extent of something from end to end.",
    "Having good fortune.",
    "The state of great comfort and extravagant living.",
    "An environment or material in which something develops.",
    "A type of oven that cooks food by electromagnetic radiation.",
    "A place for late-night entertainment with music and dancing.",
    "At the present time.",
    "To combine or become combined chemically with oxygen.",
    "A chemical element essential for life.",
    "Loose-fitting clothes worn for sleeping.",
    "A game played with babies where you hide your face and then suddenly reveal it.",
    "The smallest unit of a digital image.",
    "An attractive combination of vitality and glamour.",
    "A lung infection causing inflammation and fluid buildup.",
    "A young dog.",
    "Confusing or baffling.",
    "A hard, crystalline mineral composed of silicon and oxygen.",
    "A line of people or vehicles awaiting their turn.",
    "A test of knowledge.",
    "A strong, regular, repeated pattern of movement or sound.",
    "A light, two-wheeled hooded vehicle pulled by one or more people.",
    "To make a mark or wound with a sharp object.",
    "Stylish and attractive.",
    "A mythical creature with a lion's body and a human head.",
    "A loud, harsh noise made by a bird.",
    "A group of people employed in an organization.",
    "The quality of being strong.",
    "Plural of strength; multiple strong points or abilities.",
    "To extend or lengthen.",
    "A place that has been fortified to protect against attack.",
    "An underground railway system.",
    "To turn around a central point.",
    "A group of symptoms that consistently occur together.",
    "Lacking the ability to save money.",
    "A device for torture; a small screw used to bind the thumb.",
    "A precious stone typically colorless, yellow, or pale blue.",
    "A written or printed version of material originally presented in another medium.",
    "To infringe or go beyond the bounds of a moral principle or other established standard.",
    "To move something from one place to another.",
    "The position after eleventh.",
    "Plural of twelfth.",
    "Not known or familiar.",
    "Not deserving effort, attention, or respect.",
    "To open the zipper of.",
    "In, relating to, or characteristic of the residential area of a city.",
    "To convert into vapor.",
    "A female fox or a spiteful woman.",
    "A clear distilled alcoholic beverage.",
    "A religion practiced chiefly in the Caribbean and southern U.S., combining elements of Roman Catholic ritual with traditional African magical and religious rites.",
    "A whirling mass of fluid or air.",
    "The practice of gaining sexual pleasure from watching others when they are naked or engaged in sexual activity.",
    "A passage or path for walking.",
    "A long body of water curling into an arched form and breaking on the shore.",
    "Having a form or edge that smoothly curves in and out.",
    "Having the texture or appearance of wax.",
    "An abundant source of something.",
    "Making a high-pitched, whistling sound while breathing.",
    "A distilled alcoholic beverage made from fermented grain mash.",
    "Moving quickly through the air with a whistling or whooshing sound.",
    "The objective case of whoever.",
    "Weak and cowardly or feeble.",
    "The practice of magical skills and abilities.",
    "A person who practices magic or sorcery.",
    "Unsteady, dizzy, or dazed.",
    "A small timepiece worn on the wrist.",
    "A person who owns or sails a yacht.",
    "An exclamation of delight.",
    "Young or seeming young.",
    "Delicious or tasty.",
    "A gentle, mild breeze.",
    "A line or course having abrupt alternate right and left turns.",
    "A fastening device consisting of two parallel rows of metal or plastic teeth.",
    "A belt of the heavens divided into twelve signs.",
    "A person who is undead and feeds on human flesh."
]
