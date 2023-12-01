def count_words(text):
    # Zerlegt den Text in einzelne Wörter
    words = text.split()
    return len(words)

def calculate_word_frequency(text):
    # Erstellt ein Wörterbuch zur Zählung der Häufigkeit jedes Wortes
    words = text.split()
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency

def analyze_text(text):
    # Funktionen aufrufen, um Anzahl der Wörter und Wortfrequenz zu berechnen
    word_count = count_words(text)
    word_frequency = calculate_word_frequency(text)

    # Findet das am häufigsten vorkommende Wort
    most_frequent_word = max(word_frequency, key=word_frequency.get)

    # Berechnet die durchschnittliche Wortlänge
    total_characters = sum(len(word) for word in text.split())
    average_word_length = total_characters / word_count

    return word_count, most_frequent_word, average_word_length

# Test des refaktorisierten Codes
result = analyze_text("Beispieltext mit einigen Wörtern. Einige Wörter wiederholen sich.")
print("Anzahl der Wörter:", result[0])
print("Häufigstes Wort:", result[1])
print("Durchschnittliche Wortlänge:", result[2])
