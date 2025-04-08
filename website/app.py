from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    # Load all CSVs
    rankings_df = pd.read_csv('player_rankings_2024.csv')
    final_levels_df = pd.read_csv('cricket_levels_final.csv')
    dream_11_df = pd.read_csv('dream_11_team_final.csv')
    confidence_intervals_df = pd.read_csv('confidence_intervals_final.csv')

    # Replace NaN values in Dream 11 team with an empty string
    dream_11_df = dream_11_df.fillna('')

    # Limit the number of rows for each DataFrame (except Dream 11)
    rankings_df = rankings_df.head(10)
    final_levels_df = final_levels_df.head(10)
    confidence_intervals_df = confidence_intervals_df.head(10)

    # Define a uniform Bootstrap table class for styling
    table_class = 'table table-striped table-bordered table-hover'

    return render_template('index.html',
                           rankings=rankings_df.to_html(classes=table_class, index=False),
                           final_levels=final_levels_df.to_html(classes=table_class, index=False),
                           confidence_intervals=confidence_intervals_df.to_html(classes=table_class, index=False),
                           dream_11=dream_11_df.to_html(classes=table_class, index=False))

if __name__ == '__main__':
    app.run(debug=True)



