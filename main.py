from pyscript import document

def candidate_checker(e):
    club_members = ['micaiah robles', 'athena silva', 'luis solis', 'becca vinco', 'rj magno','pio serdena', 'sophie gamban', 'nathan bernaldez,' 'jacob opillia', 'max calata'] 
    f_name = document.getElementById('first_name').value
    l_name = document.getElementById('last_name').value
    candidate = f_name + '' + l_name
    member_checker = candidate.lower() in club_members

    messages = (f'Sorry {candidate}, your name is not on the list!', 
                f'Congratulations,{candidate}! You are now part of the OBMC Glee Club.)

    document.getElementById('result').innerHTML=messages[member_checker]