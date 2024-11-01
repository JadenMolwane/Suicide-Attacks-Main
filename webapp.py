from flask import Flask, request, render_template, flash, request
from markupsafe import Markup

import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('index2.html')

@app.route("/p1")
def render_page1():
    return render_template('index3.html')

@app.route("/p2")
def render_page2():
    return render_template('index4.html')

with open('suicide_attacks.json') as f:
    data = json.load(f)
    
@app.route("/response")
def render_response():
    year = int(request.args['year'])  # Extract the year from the submitted value
   
    # Count the number of suicide attacks for the specified year
    count = sum(1 for test in data if test['date']['year'] == year)
    return render_template('index2.html', Year2 = count, year = year)
 
@app.route('/showGameFact')
def render_fact():
     with open('suicide_attacks.json') as suicideAttack_data:
        suicideAttacks = json.load(suicideAttacks_data)
        if "attack" in request.args:
       
            attack = request.args.get('attack')
            for attack in suicideAttacks:
                if attack["group"] == attack:
                    wounded_low = attack["statistics"]["#wounded_low"]
                    wounded_high = attack["statistics"][ "# wounded_high"]
                    killed_low = attack["statistics"]["# killed_low"]
                    killed_high = attack["statistics"]["# killed_high"]
                    killed_low_civilian = attack["statistics"]["# killed_low_civilian"]
                    killed_high_civilian = attack["statistics"]["# killed_high_civilian"]
                    killed_low_political = attack["statistics"]["# killed_low_political"]
                    killed_high_political = attack["statistics"]["# killed_high_political"]
                    killed_low_security = attack["statistics"]["# killed_low_security"]
                    killed_high_security = attack["statistics"]["# killed_high_security"]
                    belt_bomb = attack["statistics"]["# belt_bomb"]
                    truck_bomb = attack["statistics"]["# truck_bomb"]
                    weapon_oth = attack["statistics"]["# weapon_oth"]
                    weapon_unk = attack["statistics"]["# weapon_unk"]
                    attackers = attack["statistics"]["# attackers"]
                    female_attackers = attack["statistics"]["# female_attackers"]
                    male_attackers = attack["statistics"]["# male_attackers"]
                    unknown_attackers = attack["statistics"]["# unknown_attackers"]
                    year = attack["date"]["year"]
                    month = attack["date"]["month"]
                    day = attack["date"]["day"]
                    weapon = attack["target"]["weapon"]
                    region = attack["target"]["region"]
                    subregion = attack["target"]["subregion"]
                    country = attack["target"]["country"]
                    province = attack["target"]["province"]
                    city = attack["target"]["city"]
                    location = attack["target"]["location"]
                    latitude = attack["target"]["latitude"]
                    longtitude = attack["target"]["longtitude"]
                    desc = attack["target"]["desc"]
                    Type = attack["target"]["type"]
                    nationality = attack["target"]["nationality"]
                    gender = attack["attacker"]["gender"]
                  
            return render_template('index2extended.html', ishandheld=ishandheld, maxPlayers=maxPlayers, Multiplat=Multiplat, online=online, genre=genre, licen=licen, publish=publish, sequel=sequel, review=review, sale=sale, used=used, console=console, rating=rating, re_release=re_release, year=year, average=average, leisure=leisure, median=median, polled=polled, rushed=rushed, average2=average2, leisure2=leisure2, median2=median2, polled2=polled2, rushed2=rushed2, average3=average3, leisure3=leisure3, median3=median3, polled3=polled3, rushed3=rushed3, average4=average4, leisure4=leisure4, median4=median4, polled4=polled4, rushed4=rushed4)
        attack = get_game_options()
        return render_template('index2.html', ishandheld=ishandheld, maxPlayers=maxPlayers, Multiplat=Multiplat, online=online, genre=genre, licen=licen, publish=publish, sequel=sequel, review=review, sale=sale, used=used, console=console, rating=rating, re_release=re_release, year=year, average=average, leisure=leisure, median=median, polled=polled, rushed=rushed, average2=average2, leisure2=leisure2, median2=median2, polled2=polled2, rushed2=rushed2, average3=average3, leisure3=leisure3, median3=median3, polled3=polled3, rushed3=rushed3, average4=average4, leisure4=leisure4, median4=median4, polled4=polled4, rushed4=rushed4)

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
if __name__=="__main__":
    app.run(debug=True)
    
    