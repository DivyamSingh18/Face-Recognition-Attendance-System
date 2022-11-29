from keras.models import load_model    # experimental code
from keras.utils import pad_sequences

import pickle
# Load model
model = load_model('best_model.h5')

def predict_class(text):
    '''Function to predict sentiment class of the passed text'''
    
    sentiment_classes = ['Negative', 'Neutral', 'Positive']
    max_len=50
    flag =0
    lst = text[0].split(" ")
    
    for i in lst:
        if i.lower() == "not":
            flag = 1
            print('Neutral')
            string = 'Neutral'
            return string
            
    if flag== 1:
        pass
    else:
        # Transforms text to a sequence of integers using a tokenizer object
        with open('saved_tokenizer.pickle', 'rb') as handle:
            tokenizer = pickle.load(handle)
        xt = tokenizer.texts_to_sequences(text)
        # print(xt)
        
        # Pad sequences to the same length
        xt = pad_sequences(xt, padding='post', maxlen=max_len)
        # print(xt)
        
        # Do the prediction using the loaded model
        yt = model.predict(xt).argmax(axis=1)
        # print(yt)
        
        # Print the predicted sentiment
        # print(sentiment_classes[yt[0]])
        string = sentiment_classes[yt[0]]

        return string
        