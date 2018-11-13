# -*- coding: utf-8 -*-

def get_baseline_model(X_train, y_train, X_val, y_val):
 
    model = Sequential()
    model.add(Embedding(vocab_size, embedding_size, input_length=55)) 
    model.add(Bidirectional(LSTM(units=embedding_size)))
    model.add(Dense(vocab_size, activation='softmax'))

# uncomment the lines below to have an overview of the parameters and weights
#    for e in zip(model.layers[-1].trainable_weights, model.layers[-1].get_weights()):
#        print('Param %s:\n%s' % (e[0],e[1]))
#    print(np.array(model.layers[-1].get_weights()[0]).shape)

    model.compile(loss='categorical_crossentropy',
              optimizer = RMSprop(lr=0.0005),
              metrics=['accuracy'])

    model.fit(np.array(X_train), np.array(y_train), epochs=1, validation_data=(np.array(X_val), np.array(y_val)))
    model.evaluate(x=np.array(X_test_poetry), y=np.array(y_test_poetry), batch_size=32)    
    return model

# we save the model because we want to use it to fine-tune another network
model.save('my_model.h5')  # creates a HDF5 file 'my_model.h5'
#del model  # deletes the existing model

#returns a compiled model
#identical to the previous one
#model = load_model('my_model2.h5') uncomment here to reload the model



