from ex3.CardFactory import CardFactory
from ex0.CreatureCard import CreatureCard
from ex0.Card import Card
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from typing import Dict
import random


#  (*data) argument unpacking
class FantasyCardFactory(CardFactory):

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        creatures = {
            "dragon": ("Fire Dragon", 5, "Legendary", 7, 5),
            "goblin": ("Goblin Warrior", 2, "Common", 2, 2)
        }

        if isinstance(name_or_power, str) and\
                name_or_power.lower() in creatures:
            data = creatures[name_or_power.lower()]
            return CreatureCard(*data)

        data = random.choice(list(creatures.values()))
        return CreatureCard(*data)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        spells = {
            "fireball": ("Fireball", 3, "Rare", "damage"),
            "heal": ("Healing Light", 2, "Common", "heal"),
        }

        if isinstance(name_or_power, str) and name_or_power.lower() in spells:
            data = spells[name_or_power.lower()]
            return SpellCard(*data)

        data = random.choice(list(spells.values()))
        return SpellCard(*data)

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        artifacts = {
            "mana_ring": ("Mana Ring", 2, "Rare", 5,
                          "Permanent: +1 mana per turn"),
            "ancient_staff": ("Ancient Staff", 4, "Epic", 3,
                              "Permanent: +2 spell damage"),
        }

        if isinstance(name_or_power, str) and\
                name_or_power.lower() in artifacts:
            data = artifacts[name_or_power.lower()]
            return ArtifactCard(*data)

        data = random.choice(list(artifacts.values()))
        return ArtifactCard(*data)

    def create_themed_deck(self, size: int) -> Dict:
        deck = []
        for _ in range(size):
            choice = random.choice(["creature", "spell", "artifact"])

            if choice == "creature":
                deck.append(self.create_creature())
            elif choice == "spell":
                deck.append(self.create_spell())
            else:
                deck.append(self.create_artifact())

        return {
            "deck_size": size,
            "cards": deck
        }

    def get_supported_types(self) -> Dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
        }
