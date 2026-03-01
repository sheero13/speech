#train

# import os
# os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
# os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

# import numpy as np
# import pickle
# from tensorflow.keras.datasets import imdb
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Embedding, SimpleRNN, Dense

# print("Loading IMDB dataset...")

# vocab_size = 10000  

# (X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=vocab_size)

# print("Training samples:", len(X_train))
# print("Testing samples:", len(X_test))

# max_len = 200

# X_train = pad_sequences(X_train, maxlen=max_len)
# X_test = pad_sequences(X_test, maxlen=max_len)

# model = Sequential([
#     Embedding(vocab_size, 32, input_length=max_len),
#     SimpleRNN(32),
#     Dense(1, activation="sigmoid")
# ])

# model.compile(
#     loss="binary_crossentropy",
#     optimizer="adam",
#     metrics=["accuracy"]
# )

# model.summary()

# print("Training...")

# model.fit(
#     X_train,
#     y_train,
#     epochs=5,
#     batch_size=64,
#     validation_data=(X_test, y_test)
# )
# model.save("imdb_rnn_model.h5")

# print("Model saved successfully!")

#-----------------------------------------------------------------------------------------------------------

#test

# import os
# os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
# os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

# import numpy as np
# from tensorflow.keras.datasets import imdb
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# from tensorflow.keras.models import load_model

# model = load_model("imdb_rnn_model.h5")

# vocab_size = 10000
# max_len = 200

# word_index = imdb.get_word_index()

# reverse_word_index = {value: key for key, value in word_index.items()}

# def encode_review(text):
#     tokens = text.lower().split()
#     encoded = []
#     for word in tokens:
#         if word in word_index and word_index[word] < vocab_size:
#             encoded.append(word_index[word])
#         else:
#             encoded.append(2) 
#     return pad_sequences([encoded], maxlen=max_len)

# print("\nSentiment Analyzer Ready (type 'exit' to stop)\n")

# while True:
#     review = input("Enter review: ")
#     if review.lower() == "exit":
#         break

#     encoded = encode_review(review)
#     prediction = model.predict(encoded, verbose=0)[0][0]

#     if prediction > 0.5:
#         print("Sentiment: Positive")
#     else:
#         print("Sentiment: Negative")

#     print("Confidence:", float(prediction))
#     print("-" * 40)

#-----------------------------------------------------------------------------------------------------------

#comb

# import numpy as np
# import tensorflow as tf
# from tensorflow.keras.datasets import imdb
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Embedding, SimpleRNN, Dense, Dropout
# from sklearn.metrics import classification_report, confusion_matrix
# import matplotlib.pyplot as plt
# import seaborn as sns

# # 1. Load and Preprocess the Data
# # num_words=5000 limits the vocabulary to the top 5000 most frequent words
# (x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=5000)

# # pad_sequences ensures all reviews are exactly 100 words long
# x_train = pad_sequences(x_train, maxlen=100)
# x_test = pad_sequences(x_test, maxlen=100)

# # 2. Build the RNN Model
# model = Sequential([
#     Embedding(5000, 32),
#     SimpleRNN(32, dropout=0.2),
#     Dense(1, activation='sigmoid')
# ])

# model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# # 3. Train the Model
# model.fit(x_train, y_train, epochs=3, batch_size=64, validation_split=0.2)

# # 4. Save the Model
# model.save('imdb_rnn_model.keras')

# # 5. Prediction Function
# def predict_sentiment(text):
#     word_index = imdb.get_word_index()
#     words = text.lower().split()
#     # IMDB indices are offset by 3 (0: padding, 1: start, 2: unknown)
#     indices = [word_index.get(w, 2) + 3 for w in words]
#     padded = pad_sequences([indices], maxlen=100)

#     score = model.predict(padded, verbose=0)[0][0]
#     label = "Positive" if score > 0.5 else "Negative"

#     return label, f"{score:.4f}"

# # Example Usage:
# print(predict_sentiment("This movie was fantastic and I loved every minute"))
# print(predict_sentiment("The plot was boring and the acting was terrible"))

# # 6. Evaluation and Visualization
# # Basic Evaluation
# loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
# print(f"\nTest Accuracy: {accuracy:.4f}")

# # Detailed Class-wise Metrics
# y_pred_prob = model.predict(x_test)
# y_pred = (y_pred_prob > 0.5).astype("int32")

# print("\nDetailed Performance Report:")
# print(classification_report(y_test, y_pred, target_names=['Negative', 'Positive']))

# # Visualizing Errors with a Confusion Matrix
# cm = confusion_matrix(y_test, y_pred)
# plt.figure(figsize=(8, 6))
# sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Neg', 'Pos'], yticklabels=['Neg', 'Pos'])
# plt.xlabel('Predicted')
# plt.ylabel('Actual')
# plt.title('Confusion Matrix')
# plt.show()
