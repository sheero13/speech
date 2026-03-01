#train
# import os
# os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
# os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

# import numpy as np
# import pickle
# import json
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Embedding, LSTM, Dense
# from tensorflow.keras.utils import to_categorical

# print("Reading doc.txt...")
# with open(r"Next_Word_Prediction\doc.txt", "r", encoding="utf-8") as f:
#     text = f.read().lower()

# tokenizer = Tokenizer()
# tokenizer.fit_on_texts([text])

# total_words = len(tokenizer.word_index) + 1

# input_sequences = []

# for line in text.split("\n"):
#     token_list = tokenizer.texts_to_sequences([line])[0]
#     for i in range(1, len(token_list)):
#         input_sequences.append(token_list[:i+1])

# max_len = max(len(seq) for seq in input_sequences)

# input_sequences = pad_sequences(input_sequences, maxlen=max_len, padding="pre")

# X = input_sequences[:, :-1]
# y = input_sequences[:, -1]

# y = to_categorical(y, num_classes=total_words)

# print("Training model...")

# model = Sequential([
#     Embedding(total_words, 32, input_length=max_len-1),
#     LSTM(64),
#     Dense(total_words, activation="softmax")
# ])

# model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# model.fit(X, y, epochs=200, verbose=0)

# print("Training complete!")

# model.save("next_word_model.h5")

# with open("tokenizer.pkl", "wb") as f:
#     pickle.dump(tokenizer, f)

# with open("config.json", "w") as f:
#     json.dump({"max_len": max_len}, f)

# print("Model and tokenizer saved")

#---------------------------------------------------------------------------------------------------------------------------------

#test.py

# import os
# os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
# os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

# import numpy as np
# import pickle
# import json
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing.sequence import pad_sequences

# model = load_model(r"Next_Word_Prediction\next_word_model.h5")

# with open(r"Next_Word_Prediction\tokenizer.pkl", "rb") as f:
#     tokenizer = pickle.load(f)

# with open(r"Next_Word_Prediction\config.json", "r") as f:
#     config = json.load(f)

# max_len = config["max_len"]

# print("Model loaded successfully!\n")

# def predict_next_word(seed_text):
#     token_list = tokenizer.texts_to_sequences([seed_text])[0]
#     token_list = pad_sequences([token_list], maxlen=max_len-1, padding="pre")

#     predicted = np.argmax(model.predict(token_list, verbose=0), axis=-1)[0]

#     for word, index in tokenizer.word_index.items():
#         if index == predicted:
#             return word
#     return ""


# while True:
#     seed = input("Enter text: ").lower()

#     if seed == "exit":
#         break

#     next_word = predict_next_word(seed)
#     print("Next word:", next_word)
#     print("-" * 40)

#------------------------------------------------------------------------------------------------------------------
#comb

# import numpy as np
# import tensorflow as tf
# from datasets import load_dataset
# from tensorflow.keras.preprocessing.text import Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# import pickle


# dataset = load_dataset("wikitext", "wikitext-2-v1", split='train')

# # Filter lines longer than 100 characters and take the first 1000 for training
# raw_text = [line for line in dataset['text'] if len(line) > 100][:1000]
# corpus = " ".join(raw_text).lower()


# vocab_size = 5000
# tokenizer = Tokenizer(num_words=vocab_size, oov_token="<OOV>")
# tokenizer.fit_on_texts([corpus])
# total_words = len(tokenizer.word_index) + 1

# token_list = tokenizer.texts_to_sequences([corpus])[0]

# #Trigram Sequences (2 words as input X, 1 word as target y)
# X = []
# y = []

# for i in range(2, len(token_list)):
#     trigram = token_list[i-2:i+1]
#     X.append(trigram[:2])  
#     y.append(trigram[2])   

# X = np.array(X)
# y = np.array(y)

# print(f"Total training sequences: {len(X)}")


# model = tf.keras.Sequential([
#     # Embedding layer: vocab_size × 100-dimensional vectors
#     tf.keras.layers.Embedding(
#         input_dim=vocab_size,   
#         output_dim=100,         
#         input_shape=(2,)        
#     ),
#     # LSTM layer: 150 units
#     tf.keras.layers.LSTM(150),
#     # Dense output: predict next word via softmax
#     tf.keras.layers.Dense(vocab_size, activation='softmax')
# ])


# model.compile(
#     loss='sparse_categorical_crossentropy',
#     optimizer='adam',
#     metrics=['accuracy']
# )

# model.summary()

# model.fit(X, y, epochs=10, batch_size=32)


# def predict_next_word(seed_text):
    
#     token_list = tokenizer.texts_to_sequences([seed_text.lower()])[0]
    
#     token_list = token_list[-2:]
#     token_list = np.array([token_list])
    
    
#     predictions = model.predict(token_list, verbose=0)
#     predicted_index = np.argmax(predictions, axis=-1)[0]

    
#     output_word = ""
#     for word, index in tokenizer.word_index.items():
#         if index == predicted_index:
#             output_word = word
#             break
#     return output_word


# seed_text = "The university"
# next_words = 5

# for _ in range(next_words):
#     predicted_word = predict_next_word(seed_text)
#     seed_text += " " + predicted_word

# print(f"Final Generation: {seed_text}")

# model.save('trigram_lstm_model.h5')
# with open('tokenizer.pkl', 'wb') as f:
#     pickle.dump(tokenizer, f)

# print("Model and Tokenizer saved successfully.")
