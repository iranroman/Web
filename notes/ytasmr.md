
Original paper: [Telling Left from Right: Learning Spatial Correspondence of Sight and Sound](https://arxiv.org/abs/2006.06175)

## Obtaining the data

- The [official data repository](https://zenodo.org/record/3889168#.YH86O-2YUbA) contains csv files with urls and timestamps for each youtube video in this dataset.

- Authors first used `beautiful soup` to scrape YouTube for the urls based on search terms.

- To download the data, authors used `youtube-dl`.

## Data processing

- The videos were randomly split by name into training, validation, and test sets.

- The 10-second clips were randomly selected from each video based on total the length.
 
- The audio was resampled to 16kHz using librosa. The original sampling rate may vary depending on the video.

- The 3-second inputs that were passed to the model were randomly selected from the 10-second clips.

### Source

private email conversation with the first author Karren Yang
