#!/usr/bin/env python

import time
import os
import re
from contextlib import suppress
from dataclasses import dataclass
'''

WANT: 
    Who is a threat (combination of bed breaks, kills, final kills, sweaty name, -deaths, -accidents, #players, stars, has a bed, been to mid)
    speak bed breaks and eliminations


'''
@dataclass
class Team:
    players: set = set
    kills: int = 0
    finals: int = 0
    deaths: int = 0
    accidents: int = 0
    bedBreaks: int = 0
    hasBed: bool = True

    #not implemented
    beenToMid: bool = False
    
    #bookkeeping stuff
    membersFinalKilled: set = set

    def registerPlayer(self, name):
        #team members who have been final killed can not be re-added to a team
        if name not in self.membersFinalKilled:
            self.players.add(name)

    def playerKilled(self):
        self.deaths += 1

    def accident(self):
        self.accidents += 1

    def playerFinalKilled(self, name):
        self.deaths += 1
        self.players.remove(name)

    def lostBed(self):
        self.hasBed = False

    def gotKill(self):
        self.kills += 1

    def gotFinal(self):
        self.finals += 1

    def goneMid(self):
        self.beenToMid = True

    def brokeBed(self):
        self.bedBreaks += 1

    @property
    def numPlayers(self):
        return len(self.players)

    @property
    def threatLevel(self):#TODO: make better formula
        if self.numPlayers == 0:
            return 0

        return self.kills + 2 * self.finals +  5 * self.bedBreaks - self.deaths - self.accidents

class BedWars:
    
    def __init__(self):
        self.teamColors = ["RED","BLUE","GREEN","YELLOW","AQUA","WHITE","PINK","GRAY"]
        self.teams = {color: Team() for color in self.teamColors}
        
        self.nameToColor = dict()
        self.unhandledEvents = []
        self.lastFinalKilled = ""

    def newGame(self):
        print("New Game")

    def bedDestroyed(self, color, player):
        print(f"{color} bed Destroyed by {player}")

def main():
    #filePath = os.getenv("APPDATA") + "/.minecraft/logs/latest.log"
    #filePath = os.getenv("APPDATA") + "/.minecraft/logs/blclient/minecraft/latest.log"
    filePath = "C:/Users/Samue/Desktop/code/temp/temp.log"

    game = BedWars()

    for line in follow(filePath):
        processLine(line, game)

def processLine(line, game):

    isChat = f"\[Client thread/INFO\]: \[CHAT\] (.*)"

    match = re.search(isChat, line)

    if not match:
        return

    text = match.group(1)

    events = [
        #format (eventCondition, eventHandler)
        (r"Protect your bed and destroy the enemy beds", game.newGame),
        (r"BED DESTRUCTION > (.*?) Bed was .*? by (.*?)!", game.bedDestroyed),
    ]


    for eventCondition, eventHandler in events:
        match = re.search(eventCondition, text, flags=re.IGNORECASE)

        if match:
            eventHandler(*match.groups())
            return
  
def follow(filePath):

    with open(filePath, "r") as thefile:
        #thefile.seek(0,2) #TODO: uncomment this
        while True:
            line = thefile.readline()
            if not line:
                time.sleep(0.1)
                continue
            yield line

if __name__ == "__main__":
    main()
