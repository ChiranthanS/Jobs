# Python script to fetch job postings from specified RSS feeds
import feedparser

# Define the RSS feed URLs
rss_feeds = {
    "Apple": "https://jobs.apple.com/en-us/rss",
    "Cisco": "https://jobs.cisco.com/jobs/SearchJobs/rss",
    "Microsoft": "https://jobs.careers.microsoft.com/us/en-us/rss"
}

def fetch_job_postings(company):
    try:
        # Parse the RSS feed
        feed = feedparser.parse(rss_feeds.get(company))

        # Print the job postings
        print(f"Job Postings for {company}:\n")
        for entry in feed.entries:
            print(f"Title: {entry.title}")
            print(f"Link: {entry.link}")
            print(f"Published Date: {entry.published}\n")
    except Exception as e:
        print(f"Error fetching {company} jobs: {e}")

if __name__ == "__main__":
    # Fetch job postings for each company
    for company in rss_feeds:
        fetch_job_postings(company)
