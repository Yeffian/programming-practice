def solve(s):
    count = 0
    for word in s.split(' '):
        if word in ['dark', 'ghost', 'spooky']:
            count += 1
    print(count * 2)


x2 = """
The old mansion loomed at the edge of the forest, shrouded in darkness. Local legends whispered of a ghostly presence that haunted its halls. Despite the warnings, Clara and Jake decided to explore.

As they stepped inside, the air felt thick and *dark*. “It’s just an old house,” Jake said, though his voice trembled. A *spooky* breeze rustled the curtains, sending a chill down Clara’s spine.

“Did you hear that?” she whispered, her eyes darting around. The sound of footsteps echoed in the distance, almost like a *ghost* wandering the corridors.

“Let’s check it out,” Jake suggested, trying to sound brave. They ventured deeper into the house, where shadows danced on the walls. Every creak of the floorboards sounded like a *ghost* urging them to leave.

“Look at that,” Clara pointed to a portrait whose eyes seemed to follow them. “This place is *spooky*!”

Suddenly, a *ghost*ly figure appeared at the end of the hallway, fading into the *dark*ness. Clara gasped. “We should go—now!”

They dashed back, hearts racing, the chill of the *dark*ness wrapping around them as they escaped into the night, vowing never to return.
"""

solve(x2)