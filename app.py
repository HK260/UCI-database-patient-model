from flask import Flask, request, jsonify
from load_model import load_model
import pandas as pd

app = Flask(__name__)
model = load_model()

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = request.json  # Assuming JSON input
        
        # Check if input_data is a list (multiple rows) or a single dictionary (single row)
        if isinstance(input_data, list):
            input_df = pd.DataFrame(input_data)
        else:
            input_df = pd.DataFrame([input_data])
        
        # Drop the 'readmitted' column if it exists
        if 'readmitted' in input_df.columns:
            input_df = input_df.drop(columns=['readmitted'])
        
        # Make prediction
        prediction = model.predict(input_df)
        
        # Map predictions to user-friendly labels
        prediction_labels = ["Not readmitted" if pred == 0 else "Readmitted" for pred in prediction]
        
        return jsonify({'prediction': prediction_labels})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5001)

# In[15]:


get_ipython().run_line_magic('tb', '')


# In[ ]:




