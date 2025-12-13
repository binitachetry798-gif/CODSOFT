# Simple Movie Recommendation System

A minimal Python script that recommends movies based on genre using an in-memory dataset.

**Features**
- Recommend up to 3 movies sharing the same genre as a user-provided title.
- Case-insensitive matching for movie titles.

**Requirements**
- Python 3.7+
- pandas

**Installation**
```bash
pip install pandas
```

**Run**
```bash
python "recommendation system/RECOMMENDATION_SYSTEM"
```

**Usage**
- When prompted, enter a movie title (case-insensitive).
- Example:
```
Enter a movie title: Inception

Movies similar to 'Inception':
• Interstellar
• The Martian
• Gravity
```

**How it works**
- The script constructs a small pandas DataFrame of movies and genres.
- Movie titles are normalized to lowercase for matching.
- `recommend_similar_movies(movie_title, num_recommendations=3)` returns other movies in the same genre.

**Files**
- [RECOMMENDATION_SYSTEM](recommendation system/RECOMMENDATION_SYSTEM): main script and dataset.

**Next steps / Ideas**
- Move the dataset to `data/movies.csv` and load via `pd.read_csv`.
- Expand similarity metrics (tags, actors, ratings).
- Add CLI flags or a small web UI.

**Author & License**
Please provide the project author name and preferred license to include here.
