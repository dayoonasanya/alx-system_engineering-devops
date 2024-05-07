import requests

def number_of_subscribers(subreddit):
    # Reddit API endpoint for fetching subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Custom User-Agent to avoid rate-limiting issues
    headers = {'User-Agent': 'MyBot/0.0.1'}
    
    try:
        # Send GET request to the Reddit API
        response = requests.get(url, headers=headers)
        
        # Check if the response is successful
        if response.status_code == 200:
            # Parse JSON response
            data = response.json()
            
            # Extract the number of subscribers
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            # Invalid subreddit or other error
            return 0
    except Exception as e:
        print(f"Error: {e}")
        return 0

# Test the function
if __name__ == "__main__":
    subreddit = input("Enter subreddit name: ")
    num_subscribers = number_of_subscribers(subreddit)
    print(f"Number of subscribers in '{subreddit}': {num_subscribers}")
