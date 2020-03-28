#!/usr/bin/env python
# coding: utf-8

import random


class RPS():
    def __init__(self):
        self.wins = {'p': 'r', 'r': 's', 's': 'p'}
        self.choices = {'p': 'Paper', 'r': 'Rock', 's': 'Scissors'}

    def run(self):
        x, y, z = self.play()
        print('You: {}, Computer: {} => {}'.format(self.choices[x], self.choices[y], z))

    def play(self):
        player = self.select()
        computer = self.rand()
        result = self.resolve(player, computer)

        return player, computer, result

    def rand(self):
        return random.choice(list(self.wins.keys()))

    def select(self):
        choice = input('Select r-rock, p-paper, s-scissors: ').lower()
        if choice == 'q':
            print('Bye!')
            exit()

        if choice not in self.wins:
            print('Wrong choice, select again')
            return self.select()
        
        return choice

    def resolve(self, player, computer):
        if player == computer:
            return 'Tie'
        
        if self.wins[player] == computer:
            return 'You won!'
            
        return 'You lost!'

if __name__ == '__main__':
    RPS().run()
