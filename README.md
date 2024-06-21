# Google-Flights-Ranking-Analyzer

This Python script analyzes the top Google Flights results for a one way trip from NYC to LA on January 1, 2025 for one adult flying Economy.

Uses Selenium and Beautiful Soup to parse and scrape prices from this URL: https://www.google.com/travel/flights/search?tfs=CBwQAhorEgoyMDI1LTAxLTAxag0IAhIJL20vMDJfMjg2cg4IAxIKL20vMDMwcWIzdEABSAFwAYIBCwj___________8BmAEC&tfu=EgYIABABGAA&hl=en-US&gl=US

Through testing I found that Google Flight's “best flights” are identified by the "jLMuyc" token. Results with this token are "ranked based on the best trade-off between price and convenience factors such as duration, number of stops, and airport changes during layovers" and results without this token "are ranked by price" by Google's own algorithm.

