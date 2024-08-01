def return_questions():
    QUESTIONS = [
    {"label": "A1a", "text": "Were you ever depressed or down, or felt sad, empty or hopeless most of the day, nearly every day, for two weeks?", "type": 0},

    {"label": "A1b", "text": "For the past two weeks, were you depressed or down, or felt sad, empty or hopeless most of the day, nearly every day??", "type": 0},

    {"label": "A2a", "text": "Were you ever much less interested in most things or much less able to enjoy the things you used to enjoy most of the time, for two weeks?", "type": 0},

    {"label": "A2b", "text": "In the past two weeks, were you much less interested in most things or much less able to enjoy the things you used to enjoy, most of the time?", "type": 0},

    {"label": "Check", "text": "IS A1a OR A2a CODED YES?", "type": 0},

    {"label": "A3a", "text": "IF A1b OR A2b = YES: EXPLORE THE CURRENT AND THE MOST SYMPTOMATIC PAST EPISODE, OTHERWISE\n IF A1b AND A2b = NO: EXPLORE ONLY THE MOST SYMPTOMATIC PAST EPISODE. \nOver that two week period, when you felt depressed or uninterested:\n A3a. Was your appetite decreased or increased nearly every day? Did your weight decrease or increase without trying intentionally (i.e., by ±5% of body weight or ±8 lb or ± 3.5 kg, for a 160 lb/70 kg person in a month)? IF YES TO EITHER, CODE YES.", "type": 1},

    {"label": "A3b", "text": "Did you have trouble sleeping nearly every night (difficulty falling asleep, waking up in the middle of the night, early morning wakening or sleeping excessively)?", "type": 1},

    {"label": "A3c", "text": "Did you talk or move more slowly than normal or were you fidgety, restless or having trouble sitting still almost every day? Did anyone notice this?", "type": 1},

    {"label": "A3d", "text": "Did you feel tired or without energy almost every day?", "type": 1},

    {"label": "A3e", "text": "Did you feel worthless or guilty almost every day?", "type": 1},
    
    {"label": "A3e_follow_up", "text": "IF YES TO A3e, ASK FOR EXAMPLES. LOOK FOR DELUSIONS OF FAILURE, OF INADEQUACY, OF RUIN OR OF GUILT, OR OF NEEDING PUNISHMENT OR DELUSIONS OF DISEASE OR DEATH OR NIHILISTIC OR SOMATIC DELUSIONS. THE EXAMPLES ARE CONSISTENT WITH A DELUSIONAL IDEA.", "type": 1},

    {"label": "A3f", "text": "Did you have difficulty concentrating, thinking or making decisions almost every day?", "type": 1},
    
    {"label": "A3g", "text": "Did you repeatedly think about death (FEAR OF DYING DOES NOT COUNT HERE), or have any thoughts of killing yourself, or have any intent or plan to kill yourself? Did you attempt suicide? IF YES TO EITHER, CODE YES.", "type": 1},
    
    {"label": "A4", "text": "Did these symptoms cause significant distress or problems at home, at work, at school, socially, in your relationships, or in some other important way, and are they a change from your previous functioning?", "type": 1},
    
    {"label": "A5", "text": "In between 2 episodes of depression, did you ever have an interval of at least 2 months, without any significant depression or any significant loss of interest?", "type": 0},
 
    {"label": "A6a", "text": "How many episodes of depression did you have in your lifetime?Between each episode there must be at least 2 months without any significant depression.", "type": 2}
    ]

    return QUESTIONS