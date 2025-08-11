#Created with Jupyter cells
# Cell 1: Imports
	import time
	import pyttsx3
	import os
	import platform

# Cell 2: Voice package
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')

	for i, voice in enumerate(voices):
	    print(f"{i}: {voice.name} ({voice.gender}) - {voice.id}")

# Cell 3: macOS-compatible "beep", a prompt used in between each stretch
	def beep(is_first=False):
	    if platform.system() == "Darwin":  # macOS
	        if not is_first:
	            os.system('say -v Karen "prepare for next stretch"')
	    else:
	        if not is_first:
	            print('\a')  # Fallback beep

# Cell 4: List of stretches with duration for each stretch
	stretches = [
	    ("Feet shoulder width apart, touch toes", 22),
	    ("Cherry pickers", 43),
	    ("Feet together, touch toes", 22),
	    ("Cross leg, touch toes", 43),
	    ("Donkey kicks", 33),
	    ("Inside of the ankle pull", 22),
	    ("Frankenstein", 22),
	    ("Hug Knee", 22),
	    ("Calfs", 22),
	    ("Inch worm", 16),
	    ("Sumo Squat", 22),
	    ("Butterfly", 43),
	    ("Both legs out straight", 22),
	    ("Both legs out wide", 43),
	    ("Right in, left out", 16),
	    ("Left in, right out", 16),
	    ("Thread the needle, right", 22),
	    ("Thread the needle, left", 22),
	    ("Hug leg, right", 33),
	    ("Hug leg, left", 33),
	    ("Trunk twist, right", 22),
	    ("Trunk twist, left", 22),
	    ("Pornstar, right", 33),
	    ("Pornstar, left", 33),
	    ("Rollypolly", 22),
	    ("Teddy bear roll", 43),
	    ("Pigeon, right", 22),
	    ("Pigeon, left", 22),
	    ("Karate kid, hamstring", 43),
	    ("Karate kid, groin", 43),
	    ("Ankle rolls", 33),
	    ("Hulk jump", 22),
	    ("Arms over head", 33),
	    ("Arms across chest", 33),
	    ("McGregors", 33),
	    ("Small arm circles, forward", 22),
	    ("Small arm circles, back", 22),
	    ("Big arm circles, forward", 22),
	    ("Big arm circles, back", 22),
	    ("Push ups", 33)
	]

# Cell 5: Initialize text-to-speech engine
	engine = pyttsx3.init()
	engine.setProperty('rate', 150)  # Set speech speed

# Cell 6: Main prompt for warmup/stretch routine output
	# Intro before first stretch
	print("Get ready")
	os.system('say -v Karen "Get ready."')
	time.sleep(1)

	# Loop through each stretch with its custom duration
	for i, (stretch_name, duration) in enumerate(stretches):
	    # Beep (skip "prepare" cue on first stretch)
	    beep(is_first=(i == 0))
	    time.sleep(1)

	    # First stretch announcement
	    if i == 0:
	        print("First stretch")
	        os.system('say -v Karen "First stretch."')
	        time.sleep(.69)

	    # Announce stretch
	    print(stretch_name)
	    os.system(f'say -v Karen "{stretch_name}"')
	    time.sleep(1.3)
	    
	    # "Ready. Go." prompt
	    print("Ready")
	    os.system('say -v Karen "Ready."')
	    time.sleep(0.69)
	    print("Go")
	    os.system('say -v Karen "Go."')

	    # Wait for stretch duration minus 3 seconds
	    if duration > 5:
	        time.sleep(duration - 3)
	        # Countdown last 5 seconds
	        for t in range(3, 0, -1):
	            print(t)
	            os.system(f'say -v Karen "{t}"')
	            time.sleep(.69)
	    else:
	        time.sleep(duration)

	# End of routine
	print("Warmup complete")
	os.system('say -v Karen "Warmup complete!"')
