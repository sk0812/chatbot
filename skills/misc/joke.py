import random

jokes = ["i threw a boomerang a few years ago. I now live in constant fear", "My wife accused me of being to immature. I told her to get out of my fort",
         "you don't need a parachute to go skydiving. you need a parachute to go skydiving twice!", "Parallel lines have so much in common. It's a shame they will never meet",
         "Someone stole my mood ring. I don't know how i feel about that", "My grandfather told me not to rely on technology, so i plugged out his life support",
         "You're not completely useless, you can always serve as a bad exmaple", "Someone stole my microsoft office and, they are gonna pay. you have my Word",
         "I tried to catch fog yesterday. Mist", "Working in a mirror factory is something i can totally see myself doing", "What’s the best thing about Switzerland? I don’t know, but the flag is a big plus.",
         "I invented a new word! Plagiarism!", "Hear about the new restaurant called Karma? There’s no menu: You get what you deserve.", "Crime in multi-storey car parks. That is wrong on so many different levels.",
         "I have a lot of growing up to do. I realised that the other day inside my fort.", "If God had written the Bible, the first line should have been ‘It’s round.",
         "I bought myself some glasses. My observational comedy improved.", "A spa hotel? It’s like a normal hotel, only in reception there’s a picture of a pebble",
         "Life is like a box of chocolates. It doesn’t last long if you’re fat.", "I was in my car driving back from work. A police officer pulled me over and knocked on my window. I said, ‘One minute I’m on the phone.",
         "Do Transformers get car, or life insurance?", "I went down to my local supermarket and I said: “I want to make a complaint. This vinegar’s got lumps in it”. He said: “Those are pickled onions.",
         "Four fonts walk into a bar. The barman says: “Oi – get out. We don’t want your type in here.”", "A sandwich walks into a bar. The barman says: “Sorry, we don’t serve food in here.",
         "I went to buy camouflage trousers but I couldn’t find any", "I’m on a whisky diet. I’ve lost three days already.", "Which trees are the handiest. Palm trees",
         "Boy: The principal is so dumb! Girl: Do you know who I am? Boy: No... Girl: I am the principal's daughter! Boy: Do you know who I am? Girl: No... Boy: Good! * Walks away *"
         "What happens to a frog's car when it breaks down? It gets toad away.", "I can’t believe I got fired from the calendar factory: all I did was take a day off!",
         "You have two parts of the brain, “left” and “right” — in the left side, there’s nothing right and in the right side, there’s nothing left.", "Why do bees hum? They don’t remember the lyrics!",
         "Don’t spell part backwards. It’s a trap.", "Most people are shocked when they find out how bad I am as an electrician.", "Don’t trust atoms, they make up everything.",
         "Alcohol is a perfect solvent: It dissolves marriages, families and careers.", "Smoking will kill you… Bacon will kill you… And yet, smoking bacon will cure it.",
         "An optimist believes that we live in the best world. A pessimist is afraid that it might be true.", "Apparently I snore so loudly that it scares everyone in the car I'm driving.",
         "Today a man knocked on my door and asked for a small donation towards the local swimming pool. I gave him a glass of water.", "How did I escape Iraq? Iran.", "Moses had the first tablet that could connect to the cloud.",
         "I hate people who use big words just to make themselves look perspicacious.", "I'd tell you a chemistry joke but I know I wouldn't get a reaction.", "A clean house is the sign of a broken computer.",
         "I wasn't originally going to get a brain transplant, but then I changed my mind.", "It's better to let someone think you are an Idiot than to open your mouth and prove it.",
         "I think my neighbor is stalking me as she's been googling my name on her computer. I saw it through my telescope last night.", "What do you call the security outside of a Samsung Store? Guardians of the Galaxy.",
         "Just read that 4,153,237 people got married last year, not to cause any trouble but shouldn't that be an even number?", "I'm reading a book about anti-gravity. It's impossible to put down.",
         "I find it ironic that the colors red, white, and blue stand for freedom until they are flashing behind you.", "Plan ahead - It wasn't raining when Noah built the ark.", "I'm great at multitasking. I can waste time, be unproductive, and procrastinate all at once.",
         "I changed my password to 'incorrect'. So whenever I forget what it is the computer will say 'Your password is incorrect'.", "The older I get, the earlier it gets late.", "Aging gracefully is like the nice way of saying you're slowly looking worse.",
         "A man got hit hard in the head with a can of 7Up. He’s alright though, it was a soft drink.", "Light travels faster than sound. This is why some people appear bright until they open their mouths.",
         "I read recipes the same way I read science fiction. I get to the end and I think, 'Well, that's not going to happen.", "Just burned 2,000 calories. That’s the last time I leave brownies in the oven while I nap.",
         "The problem isn’t that obesity runs in your family. It’s that no one runs in your family.", " Before you criticize someone, walk a mile in their shoes. That way, when you do criticize them, you’re a mile away and you have their shoes.",
         "Blunt pencils are really pointless.", "Just got fired from my job as a set designer. I left without making a scene.", "What’s the difference between ignorance and apathy? I don’t know and I don’t care.",
         "The man who invented Velcro has died. RIP", "My friend was explaining electricity to me, but I was like, ‘Watt?’", "What if there were no hypothetical questions?"]

def joke():
    print(random.choice(jokes))
