# import dependencies
import csv
import os

# add a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initialize a total vote counter
total_votes = 0

# candidate options and candidate votes
candidate_options = []
candidate_votes = {}

# challenge county options and county votes
county_names = []
county_votes = {}

# track the winning candidate vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# challenges track the largest county voter turnout and its percentage
largest_county_turnout = ""
largest_county_votes = 0

# read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # read the header
    header = next(reader)

    # for each row in the csv file
    for row in reader:
        # add to the total votes count
        total_votes = total_votes + 1

        # get the candidate name from each row
        candidate_name = row[2]

        # extract the county name from each row
        county_name = row[1]

        # if the candidate does not match any existing candidate add
        # it into the list
        if candidate_name not in candidate_options:
            # add candidate name to candidate list
            candidate_options.append(candidate_name)
            # add begin tracking that candidate vote count
            candidate_votes[candidate_name] = 0
        # add a vote to that candidate count
        candidate_votes[candidate_name] += 1

        # challenge county
        if county_name not in county_names:

            # challenge add it to the list in the running
            county_names.append(county_name)

            # tracking that candidate voter count
            county_votes[county_name] = 0
        county_votes[county_name] += 1

    # save the result to text file
    with open(file_to_save, "w") as txt_file:
        # print the final vote count
        election_results = (
            f"\nElection Results\n"
            f'\n-----------------------\n'
            f"Total Votes: {total_votes:,}"
            f'\n-----------------------\n'
            f"\nCounty Votes:\n"
        )
        print(election_results, end = "")
        txt_file.write(election_results)

        # challenge save the final county vote count to the text file
        for county in county_votes:
            # retrieve vote count and percentage
            county_vote = county_votes[county]
            county_percent = int(county_vote) / int(total_votes) * 100
            county_results = (
                f"{county}: {county_percent:.1f}% ({county_vote:,})\n"
            )
            print(county_results, end = "")
            txt_file.write(county_results)

            # determine winning vote count and candidate
            if(county_vote > largest_county_votes):
                largest_county_votes = county_vote
                largest_county_turnout = county
        # print the county with the largest turnout
        largest_county_turnout = (
            f'\n-----------------------\n'
            f'Largest County Turnout: {largest_county_turnout}'
            f'\n-----------------------\n'
        )
        print(largest_county_turnout)
        txt_file.write(largest_county_turnout)

        for candidate in candidate_votes:
            # retrieve vote count and percentage
            votes = candidate_votes[candidate]
            vote_percentage = int(votes) / int(total_votes) * 100
            candidate_results = (
                f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n"
            )

            print(candidate_results)
            # save the candidate result to text file
            txt_file.write(candidate_results)

            # determine winning vote count winning percentage and candidate
            if(votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_candidate = candidate
                winning_percentage = vote_percentage
            
        winning_candidate_summary = (
            f'-----------------------\n'
            f'Winner: {winning_candidate}\n'
            f'Winning Vote Count: {winning_count:,}\n'
            f'Winning Percentage: {winning_percentage:.1f}%'
            f'\n-----------------------\n'
        )
        print(winning_candidate_summary)

        # save the winning candidate name to text file
        txt_file.write(winning_candidate_summary)