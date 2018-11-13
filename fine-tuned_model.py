# -*- coding: utf-8 -*-

def get_lstm_finetuned(X_train, y_train, X_val, y_val, X_test, y_test):
    
    model = Sequential()
    model.add(Embedding(vocab_size, embedding_size, input_length=55, weights=[pretrained_weights]))
    model.add(Bidirectional(LSTM(units=embedding_size)))
    model.add(Dense(vocab_size, activation='softmax'))

    model.load_weights('my_model_fin22.h5', by_name=True)
    model.layers.pop()
    model.outputs = [model.layers[-1].output]
    model.layers[-1].outbound_nodes = []
    model.add(Dense(vocab_size, activation='softmax'))
    
    for layer in model.layers[:1]:
         layer.trainable = False
         
    model.compile(loss='categorical_crossentropy',
              optimizer = RMSprop(lr=0.001),
              metrics=['accuracy'])
    
    model.fit(np.array(X_train), np.array(y_train), epochs=1, validation_data=(np.array(X_val), np.array(y_val)))
    score = model.evaluate(x=np.array(X_test), y=np.array(y_test), batch_size=32)
    prediction = model.predict(np.array(X_test), batch_size=32)
    
    return prediction, model, score

