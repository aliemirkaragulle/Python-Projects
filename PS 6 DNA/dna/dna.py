import csv
import sys


def main():

    # Check for command-line usage
    if len(sys.argv) != 3:
        print("There Should be Given 3 Command-Line Arguments.")
        sys.exit(1)

    # First argument is the database, second argument is the sequence (of DNA)
    database = sys.argv[1]
    sequence = sys.argv[2]

    # Read database file into a variable
    persons = []
    keys = []
    with open(database) as databases:
        reader = csv.DictReader(databases)
        for row in reader:
            #print(row["name"], row["AGATC"], row["AATG"], row["TATC"])
            persons.append(row)
    #print(f"Persons: {persons}")

    keys = list(persons[0])[1:]
    #print(f"Keys: {keys}")

    # Read DNA sequence file into a variable
    f = open(sequence)
    sequences = str(f.read())
    #print(f"Sequence: {sequences}")

    # Find longest match of each STR in DNA sequence
    matches = dict()
    for i in range(len(keys)):
        matches[keys[i]] = longest_match(sequences, keys[i])
    #print(f"Matches: {matches}")

    # Check database for matching profiles
    # for i in range(len(keys)):
        # print(matches[keys[i]])
    # print()

    for i in range(len(persons)):
        count = 0
        curr_person = persons[i]
        #print(f"Current Person: {curr_person}")
        for j in range(len(keys)):
            # print(curr_person[keys[j]])
            # print(matches[keys[j]])
            #print(int(curr_person[keys[j]]) == int(matches[keys[j]]))
            if int(curr_person[keys[j]]) == int(matches[keys[j]]):
                count += 1
        #print(f"Count: {count}")

        if count == len(keys):
            print(curr_person["name"])
            return
    print("No Match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
