# mock_data_process

## Intro

Behold the latest version of our state-of-the-art transaction processing process. This is the first step in helping our users find tax write-offs.

This process is run in a cronjob once per day. If it runs into an error it will just restart. It doesn't have to restart every day.

The data science team spent most of their time perfecting the model that takes a raw merchant description and cleans it up so that it's intelligible to users (for this mock process it's just title casing) and haven't fully optimized anything else.

Please explore the code and take note of any improvements you could make or questions you would need answered before making said improvements.

## Organization

The cronjob calls `main.py` which contains the highest abstraction of the process. All helper functions are in `helpers.py`. You can assume most of these are mocked up versions of a real function that handles interation with an API, database, local processing, etc.

## Run

```
python main.py
```

## Testing
TODO


