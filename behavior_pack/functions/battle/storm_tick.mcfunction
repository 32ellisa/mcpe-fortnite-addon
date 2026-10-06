# battle:storm_tick
execute as @a[scores={battle_state=0}] run effect @s weakness 1 0 true
execute as @a[scores={battle_health=..0}] run scoreboard players set @s battle_state 1
execute as @a[scores={battle_state=0}] run say Storm is closing. Stay inside the safe zone.
