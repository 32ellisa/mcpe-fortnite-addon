# battle:start
scoreboard objectives add battle_state dummy
scoreboard objectives add battle_health dummy
scoreboard objectives add battle_shield dummy
scoreboard objectives add battle_elims dummy
scoreboard players set @a battle_state 0
scoreboard players set @a battle_health 100
scoreboard players set @a battle_shield 0
scoreboard players set @a battle_elims 0
say Battle started. Find loot and survive the storm.
