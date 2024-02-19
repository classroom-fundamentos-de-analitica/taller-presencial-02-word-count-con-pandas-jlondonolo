"""Taller evaluable"""

import glob

import pandas as pd


def load_input(input_directory):
    """Load text files in 'input_directory/'"""
    #
    # Lea los archivos de texto en la carpeta input/ y almacene el contenido en
    # un DataFrame de Pandas. Cada línea del archivo de texto debe ser una
    # entrada en el DataFrame.
    #
    # Get a list of all input files
    input_files = glob.glob(input_directory + '/*.txt')
    
    # Read all input files into a single DataFrame
    df = pd.concat((pd.read_csv(f, sep='\t', header=None, names=['text']) for f in input_files), ignore_index=True)
    
    return df


def clean_text(dataframe):
    """Text cleaning"""
    #
    # Elimine la puntuación y convierta el texto a minúsculas.
    #
    dataframe['clean_text'] = dataframe['text'].apply(lambda x: x.translate(str.maketrans('', '', string.punctuation)).lower())
    return dataframe


def count_words(dataframe):
    """Word count"""
    # Split the text into words
    words = dataframe['clean_text'].str.split(expand=True).stack()
    
    # Count the words
    word_counts = words.value_counts().reset_index()
    word_counts.columns = ['word', 'count']
    
    return word_counts

def save_output(dataframe, output_filename):
    """Save output to a file."""

    dataframe.to_csv(output_filename, sep='\t', index=False, header=False)


#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def run(input_directory, output_filename):
    """Call all functions."""
    # Load input files into a DataFrame
    input_df = load_input(input_directory)

    # Clean text
    clean_df = clean_text(input_df)

    # Count words
    word_count_df = count_words(clean_df)

    # Save output
    save_output(word_count_df, output_filename)

if __name__ == "__main__":
    run(
        "input",
        "output.txt",
    )
