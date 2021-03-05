limak_age, bob_age = list(map(int, input().split()))
no_of_years_needed = 0
while limak_age <= bob_age:
    limak_age = limak_age * 3
    bob_age = bob_age * 2
    no_of_years_needed = no_of_years_needed + 1

print(no_of_years_needed)
