# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    },
    "Bellatrix": {
        "RA": "05h 25m 07.9s",
        "Dec": "+06° 20′ 59″",
        "Magnitude": 1.64,
        "Spectral Type": "B2III"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
def print_names(thingy):
    for i in thingy:
        print(i)


# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def print_name_and_spectral(thingy):
    for i in thingy:
        print(i, " ", thingy[i]["Spectral Type"])


# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def find_mags(thingy):
    for i in thingy:
        if thingy[i]["Magnitude"] > 0.1:
            print(i + " " + str(thingy[i]["Magnitude"]))

print_names(targets)
print_name_and_spectral(targets)
find_mags(targets)
# 4) Look up another target, add all the necessary information to the targets list. 



# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
# I do not understand what this question is asking us to do.


# 6) What is your favorite constellation?
# My favorite constellation is Orion. Though I definitely like the Pleiades Cluster, though I dunno if that's a constellation